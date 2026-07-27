"""Utilidades para (re)construir y verificar notebook.ipynb del currículo v3.

- ``write_notebook(path, cells)`` escribe un notebook canónico nbformat 4.5,
  SIN outputs (igual que los 120 notebooks ya completos del repo). ``cells`` es
  una lista de tuplas ``("md", texto)`` o ``("code", texto)``.

- ``run_notebook(path, timeout)`` ejecuta el notebook headless con nbclient
  usando el kernel del entorno actual y devuelve ``(ok, error_str)``. NO
  persiste outputs: es solo verificación de que el código corre limpio.

- ``strip_outputs(path)`` deja el notebook sin outputs ni execution_count
  (idempotente) para que el commit quede como el resto del repo.

Uso CLI:
    python scripts/nbbuild.py --run classes/parte-1-.../NNN-.../notebook.ipynb
    python scripts/nbbuild.py --strip <path>
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

import nbformat as nbf

KERNELSPEC = {"display_name": "Python 3", "language": "python", "name": "python3"}
LANGUAGE_INFO = {"name": "python", "version": "3.12"}


def write_notebook(path: str | Path, cells: list[tuple[str, str]]) -> Path:
    """Escribe un notebook canónico (sin outputs) a ``path``."""
    nb = nbf.v4.new_notebook()
    nb.metadata = {"kernelspec": dict(KERNELSPEC), "language_info": dict(LANGUAGE_INFO)}
    built = []
    for typ, src in cells:
        src = src.rstrip("\n")
        if typ in ("md", "markdown"):
            built.append(nbf.v4.new_markdown_cell(src))
        elif typ in ("code", "py"):
            built.append(nbf.v4.new_code_cell(src))
        else:
            raise ValueError(f"tipo de celda desconocido: {typ!r}")
    nb.cells = built
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    nbf.write(nb, str(path))
    return path


def strip_outputs(path: str | Path) -> None:
    """Elimina outputs y execution_count de todas las celdas de código."""
    path = Path(path)
    nb = nbf.read(str(path), as_version=4)
    for cell in nb.cells:
        if cell.get("cell_type") == "code":
            cell["outputs"] = []
            cell["execution_count"] = None
    nbf.write(nb, str(path))


def run_notebook(path: str | Path, timeout: int = 300) -> tuple[bool, str]:
    """Ejecuta el notebook headless. Devuelve (ok, mensaje_de_error).

    No persiste el notebook ejecutado: solo verifica que corra sin excepción.
    """
    from nbclient import NotebookClient
    from nbclient.exceptions import CellExecutionError

    path = Path(path)
    nb = nbf.read(str(path), as_version=4)
    client = NotebookClient(
        nb,
        timeout=timeout,
        kernel_name="python3",
        resources={"metadata": {"path": str(path.parent)}},
    )
    try:
        client.execute()
        return True, ""
    except CellExecutionError as exc:
        return False, str(exc)[:4000]
    except Exception as exc:  # noqa: BLE001
        return False, f"{type(exc).__name__}: {exc}"[:4000]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--run", metavar="NB", help="ejecuta y reporta ok/err")
    ap.add_argument("--strip", metavar="NB", help="limpia outputs")
    ap.add_argument("--timeout", type=int, default=300)
    args = ap.parse_args()
    if args.strip:
        strip_outputs(args.strip)
        print(f"stripped: {args.strip}")
        return 0
    if args.run:
        ok, err = run_notebook(args.run, timeout=args.timeout)
        if ok:
            print(f"OK  {args.run}")
            return 0
        print(f"FAIL {args.run}\n{err}")
        return 1
    ap.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
