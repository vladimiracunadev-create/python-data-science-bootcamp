# 📚 Registro de fuentes

Este directorio es el aparato que hace comprobable lo que enseñan las 232 clases.

Las clases citaban obras reales desde el principio —232 bloques de fuentes
distintos, uno por clase— pero no existía ningún sitio donde comprobar qué obra
hay detrás de cada cita. Una bibliografía sin localizadores es una lista de
títulos: se lee bien y no se puede verificar.

## Qué hay aquí

| Archivo | Qué es |
|---|---|
| [`bibliography.json`](bibliography.json) | El registro. Una entrada por obra o enlace citado, con su localizador. |
| [`library_versions.json`](library_versions.json) | A qué versión de cada librería apunta la documentación enlazada, y con qué versión se comprobó. |

Ambos son **generados y comprobados por script**. No se editan a mano salvo para
curar la identificación de una obra (autoría, título, tipo); el resto —
`used_in`, `locator`, `accessed`, `status`— lo produce la herramienta.

## La regla

> Toda afirmación del programa se apoya en una entrada de este registro.
> Ninguna entrada se acepta sin localizador verificable.

Se admiten exactamente tres formas de localizador:

| Tipo | Localizador | Forma canónica |
|---|---|---|
| `book` | ISBN-13 con dígito de control válido | `https://openlibrary.org/isbn/{isbn13}` |
| `paper` | DOI | `https://doi.org/{doi}` |
| `standard`, `reference`, `dataset` | URL https de la fuente primaria | la URL, con `accessed` |

Lo que no resuelve se marca `"status": "pendiente"` con su `pending_reason` y **se
conserva**. Un hueco declarado es información; un hueco rellenado por intuición
es una invención con formato de bibliografía.

## Las dos capas de comprobación

Están separadas a propósito. Si la red entra en el CI, el CI se vuelve inestable
y se acaba ignorando — y con él se ignora todo lo demás.

### `scripts/verify-sources` — offline, determinista, bloquea en CI

```bash
python scripts/verify-sources
```

Comprueba que el registro parsea y cumple el esquema; que cada `book` tiene un
ISBN-13 con dígito de control válido y cada `paper` un DOI; que el `locator` está
en la forma canónica de su tipo; que toda obra citada en una clase existe en el
registro y que ninguna entrada del registro quedó sin usar; que ningún bloque de
fuentes se repite entre clases; que ningún enlace apunta a `/stable/` cuando esa
librería publica documentación por versión; y que las cifras del README coinciden
con el recuento real.

Las cifras del README las escribe este mismo verificador:

```bash
python scripts/verify-sources --write-readme
```

### `scripts/refresh-sources` — con red, manual, no bloquea

```bash
python scripts/refresh-sources --all
```

Resuelve ISBN contra `openlibrary.org`, DOI contra `api.crossref.org` y
`api.datacite.org`, y hace GET a cada URL de norma o documentación comparando
título y autoría antes de dar nada por bueno. Actualiza `verified_on` y
`accessed`, y **reporta lo que dejó de resolver sin borrarlo**.

Fases sueltas:

```bash
python scripts/refresh-sources --versions       # a qué versión anclar cada doc
python scripts/refresh-sources --anchor-links   # reescribe /stable/ en las clases
python scripts/refresh-sources --seed           # alta de citas nuevas (sin red)
python scripts/refresh-sources --resolve        # ISBN / DOI / URL
```

## Por qué los enlaces no apuntan a `/stable/`

`scikit-learn.org/stable/modules/tree.html` no es una fuente: es una redirección
a lo que sea que scikit-learn publique hoy. La misma URL describía otra API hace
dos versiones y describirá otra dentro de un año, sin que la cita cambie ni una
letra. Por eso el material enlaza `scikit-learn.org/1.8/modules/tree.html`, y
`library_versions.json` guarda con qué versión se comprobó y con cuál se ejecutó.

La versión no se elige a ojo: `refresh-sources --versions` pide a PyPI la lista
real de releases y prueba, de la más nueva hacia atrás, **las rutas concretas que
el material enlaza**. Se queda con la primera versión en la que responden todas.
