"""Classes 010-013 — OOP, pathlib, logging, type hints."""
from __future__ import annotations
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from build_parte0_classes import ClassSpec, Cell, write_class  # type: ignore

SPECS: list[ClassSpec] = []


SPECS.append(ClassSpec(
    folder="010-oop-basico-dataclasses-herencia",
    number="010",
    title="OOP básico, dataclasses, herencia",
    duration="90 min",
    source="Ramalho, *Fluent Python* 2e — caps. 5 (Data Class Builders) y 14 (Inheritance) · *Python Tutorial* cap. 9.",
    objetivo=(
        "Que el alumno escriba clases cuando aportan (no por hábito Java), use `@dataclass` para "
        "records sin boilerplate, entienda herencia con criterio (preferir composición), y conozca "
        "los métodos dunder más usados (`__repr__`, `__eq__`, `__lt__`, `__len__`)."
    ),
    resultados=[
        "**Definir clases** con `__init__`, atributos de instancia y métodos.",
        "**Usar `@dataclass`** para records inmutables/mutables sin escribir `__init__`/`__repr__`/`__eq__`.",
        "**Heredar** y sobreescribir métodos con `super()`.",
        "**Implementar dunders esenciales**: `__repr__`, `__str__`, `__eq__`, `__lt__`, `__len__`, `__iter__`.",
        "**Decidir** entre clase, dataclass o NamedTuple según el caso.",
    ],
    temas=[
        ("Clase mínima: `__init__` + atributos + métodos", "El bloque básico."),
        ("`@dataclass(frozen=True)`", "Records inmutables sin boilerplate."),
        ("Herencia + `super()`", "Reutilizar implementación de la clase base."),
        ("Composición > herencia", "\"Has-a\" generalmente mejor que \"is-a\"."),
        ("Métodos dunder", "Integran tu clase con `len()`, `==`, `repr()`, `sorted()`."),
        ("`dataclass` vs `NamedTuple` vs `TypedDict`", "Elegir según necesidad de mutabilidad/comportamiento."),
    ],
    dataset="Sintético: lista de objetos `Punto` y `Estudiante`. Sin descarga.",
    ejercicios=[
        "**Clase Punto.** Define `Punto(x, y)` con `__repr__`, `__eq__`, distancia al origen y `__add__` para sumar puntos.",
        "**Dataclass Estudiante.** `@dataclass` con `nombre`, `notas: list[float]`, método `promedio()`. Crea 3 instancias, ordena por promedio.",
        "**Frozen Vector.** `@dataclass(frozen=True)` para un vector 2D inmutable. Intenta modificar un atributo y observa la excepción.",
        "**Herencia.** `Animal` con `hablar()` → `'genérico'`. `Perro(Animal)` que sobreescribe a `'guau'`. `Gato(Animal)` a `'miau'`.",
        "**Composición.** `Coche` que tiene un `Motor` (composición) en vez de heredar de `Motor`. Justifica por qué.",
    ],
    homework=(
        "Notebook con: (a) `Punto` con 4 dunders y tests; (b) `@dataclass Estudiante` con sort por promedio; "
        "(c) `@dataclass(frozen=True) Vector` que demuestra inmutabilidad lanzando excepción; "
        "(d) jerarquía `Animal → Perro/Gato` con polimorfismo (lista mixta llamando `hablar()`)."
    ),
    homework_criterio="Las 4 clases pasan tests; `frozen=True` lanza `FrozenInstanceError` al asignar.",
    referencias=[
        "Ramalho, *Fluent Python* 2e — caps. 5, 11, 14.",
        "[`dataclasses` docs](https://docs.python.org/3/library/dataclasses.html)",
        "[Python Tutorial — Classes](https://docs.python.org/3/tutorial/classes.html)",
    ],
    siguiente=("011-pathlib-lectura-y-escritura-de-archivos", "pathlib, lectura y escritura de archivos"),
    cells=[
        Cell("md", "# Clase 010 — OOP básico, dataclasses, herencia\n\n**Parte 0** · Ramalho caps. 5 y 14.\n\n> 🎯 Clases cuando aportan, `@dataclass` para records, herencia con criterio, dunders esenciales.\n\n> ⏱️ ~90 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "from dataclasses import dataclass, field, FrozenInstanceError\nfrom math import sqrt\nfrom typing import NamedTuple"),
        Cell("md", "## 1️⃣ Clase mínima\n\n```python\nclass Punto:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def distancia_origen(self):\n        return (self.x**2 + self.y**2) ** 0.5\n```\n\nProblema: sin `__repr__` ni `__eq__`, debugar es horrible (`<__main__.Punto object at 0x7f...>`)."),
        Cell("code", "class Punto:\n    def __init__(self, x, y):\n        self.x = x\n        self.y = y\n    def __repr__(self):\n        return f'Punto(x={self.x}, y={self.y})'\n    def __eq__(self, other):\n        return isinstance(other, Punto) and (self.x, self.y) == (other.x, other.y)\n    def __add__(self, other):\n        return Punto(self.x + other.x, self.y + other.y)\n    def distancia_origen(self):\n        return sqrt(self.x**2 + self.y**2)\n\np1 = Punto(3, 4)\np2 = Punto(3, 4)\nprint(p1)            # Punto(x=3, y=4)\nprint(p1 == p2)      # True\nprint(p1 + Punto(1, 1))   # Punto(x=4, y=5)\nprint(f'distancia: {p1.distancia_origen()}')"),
        Cell("md", "## 2️⃣ `@dataclass` — el atajo\n\nEscribir `__init__`/`__repr__`/`__eq__` a mano para 10 atributos = error humano. `@dataclass` los genera."),
        Cell("code", "@dataclass\nclass Estudiante:\n    nombre: str\n    notas: list[float] = field(default_factory=list)\n\n    def promedio(self) -> float:\n        return sum(self.notas) / len(self.notas) if self.notas else 0.0\n\nestudiantes = [\n    Estudiante('Ana', [6.5, 7.0, 5.8]),\n    Estudiante('Bob', [4.2, 5.5]),\n    Estudiante('Cris', [7.0, 6.8, 7.2, 6.5]),\n]\n\nfor e in sorted(estudiantes, key=lambda x: x.promedio(), reverse=True):\n    print(f'{e.nombre}: {e.promedio():.2f}')"),
        Cell("md", "**Nota**: `default_factory=list` evita el [bug del default mutable de la clase 006](../006-python-tipos-estructuras-control-de-flujo/README.md)."),
        Cell("md", "## 3️⃣ `frozen=True` — inmutabilidad\n\nIdeal para records que viajan como datos puros (eventos, configs, coordenadas):"),
        Cell("code", "@dataclass(frozen=True)\nclass Vector:\n    x: float\n    y: float\n\nv = Vector(3.0, 4.0)\nprint(v)\n\ntry:\n    v.x = 99.0\nexcept FrozenInstanceError as e:\n    print(f'Bien — no se puede mutar: {e}')\n\n# Como bonus: frozen=True lo hace hashable, sirve como key de dict\norigenes = {Vector(0, 0): 'origen', Vector(1, 0): 'eje x'}\nprint(origenes[Vector(0, 0)])"),
        Cell("md", "## 4️⃣ Herencia + `super()`\n\n```python\nclass Animal:\n    def __init__(self, nombre):\n        self.nombre = nombre\n    def hablar(self):\n        return 'sonido genérico'\n\nclass Perro(Animal):\n    def hablar(self):\n        return 'guau'\n```\n\n`super()` invoca al método de la clase base — útil para extender, no reemplazar:"),
        Cell("code", "class Animal:\n    def __init__(self, nombre):\n        self.nombre = nombre\n    def hablar(self):\n        return 'sonido genérico'\n    def __repr__(self):\n        return f'{type(self).__name__}({self.nombre!r})'\n\nclass Perro(Animal):\n    def __init__(self, nombre, raza):\n        super().__init__(nombre)\n        self.raza = raza\n    def hablar(self):\n        return f'guau (soy {self.raza})'\n\nclass Gato(Animal):\n    def hablar(self):\n        return 'miau'\n\nanimales = [Perro('Rex', 'pastor'), Gato('Mishi'), Animal('???')]\nfor a in animales:\n    print(f'{a}: {a.hablar()}')"),
        Cell("md", "## 5️⃣ Composición > herencia\n\nLa regla **\"is-a vs has-a\"**:\n\n- `Perro` **is-a** `Animal` → herencia OK.\n- `Coche` **has-a** `Motor` → composición (el coche tiene un motor, no es un motor).\n\nHerencia mal usada acopla y crea jerarquías frágiles (\"problema del diamante\")."),
        Cell("code", "# Composición: Coche contiene Motor\n@dataclass\nclass Motor:\n    potencia_hp: int\n    def arrancar(self):\n        return f'rrrrr ({self.potencia_hp} HP)'\n\n@dataclass\nclass Coche:\n    marca: str\n    motor: Motor   # has-a, no is-a\n    def arrancar(self):\n        return f'{self.marca}: {self.motor.arrancar()}'\n\nc = Coche('Toyota', Motor(180))\nprint(c.arrancar())"),
        Cell("md", "## 6️⃣ ¿Cuándo cada herramienta?\n\n| Necesito… | Usa |\n|---|---|\n| Record inmutable, hashable, sin métodos | `NamedTuple` o `@dataclass(frozen=True)` |\n| Record mutable con algunos métodos | `@dataclass` |\n| Validación, computed fields, lifecycle | `pydantic.BaseModel` (verás en MLOps) |\n| Estructura mutable sin comportamiento | `dict` o `TypedDict` |\n| Lógica compleja, estado, polimorfismo | Clase normal con `__init__` |"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé escribir una clase con `__init__` y dunders\n- [ ] Uso `@dataclass` en vez de boilerplate manual\n- [ ] Entiendo cuándo `frozen=True` aporta\n- [ ] Sé heredar y usar `super()`\n- [ ] Prefiero composición salvo cuando is-a es genuino"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. `Punto`, `Estudiante`, `Vector` frozen, jerarquía `Animal`."),
        Cell("md", "## 🔗 Referencias\n\n- Ramalho, *Fluent Python* 2e, caps. 5, 11, 14\n- [`dataclasses` docs](https://docs.python.org/3/library/dataclasses.html)\n\n➡️ **Siguiente:** [011 — pathlib](../011-pathlib-lectura-y-escritura-de-archivos/README.md)"),
    ],
    definiciones=[
        ("Clase / instancia", "Una **clase** es una plantilla (`class Punto:`); una **instancia** es un objeto concreto (`p = Punto(3, 4)`). `__init__` se llama al crear la instancia. `self` es la convención para referirse a la instancia dentro de los métodos."),
        ("Método dunder (\"magic method\")", "Método con doble underscore (`__init__`, `__repr__`, `__eq__`, `__lt__`, `__len__`, `__iter__`, `__add__`). Python los invoca implícitamente con sintaxis especial (`len(obj)` → `obj.__len__()`)."),
        ("`@dataclass`", "Decorador que genera `__init__`, `__repr__`, `__eq__` automáticamente desde las anotaciones de tipo de la clase. Reduce boilerplate. Con `frozen=True` la hace inmutable y hashable."),
        ("Herencia", "`class B(A)` — B hereda atributos y métodos de A; puede sobreescribirlos. `super()` invoca al método de la clase padre. Múltiple herencia existe pero se complica (MRO)."),
        ("Composición", "\"B *tiene un* A\" (atributo) en vez de \"B *es un* A\" (herencia). Generalmente preferible: menos acoplamiento, sin problemas de herencia múltiple/diamante."),
        ("Polimorfismo", "Distintas clases responden al mismo método con comportamiento distinto (`Animal.hablar()` → 'guau' o 'miau' según la subclase). Permite tratar instancias heterogéneas uniformemente."),
        ("NamedTuple vs dataclass vs TypedDict", "**NamedTuple**: tupla con nombres, inmutable, hashable, sin métodos custom. **dataclass**: clase con boilerplate auto, mutable por default (mejor con métodos). **TypedDict**: dict con esquema (estructural, no nominal)."),
    ],
    errores_comunes=[
        ("Olvidé `self` en un método y el error es confuso", "Cualquier método de instancia recibe `self` automáticamente. Sin él, Python lo confunde con otra cosa. **Fix**: siempre `def metodo(self, ...)`."),
        ("`@dataclass` con field mutable default rompe", "`@dataclass class X: items: list = []` lanza `ValueError: mutable default ...`. **Fix**: `items: list = field(default_factory=list)`."),
        ("`__eq__` definido pero `__hash__` rompe", "Definir `__eq__` sin `__hash__` hace la clase no-hashable automáticamente. **Fix**: define ambos, o usa `@dataclass(frozen=True)` (lo hace por ti)."),
        ("`super().__init__(...)` olvidado en subclase", "Atributos del padre quedan sin inicializar. **Fix**: si la subclase override `__init__`, llama `super().__init__(...)` explícitamente."),
        ("Modifico atributo y otra instancia también cambió", "Asignaste un mutable como class attribute, no instance: `class X: items = []` — todas las instancias comparten esa lista. **Fix**: inicializa en `__init__` (`self.items = []`)."),
    ],
    faq=[
        ("¿Cuándo necesito OOP en data science?",
         "Menos de lo que crees. Para análisis exploratorio, funciones + dicts/dataclasses bastan. Necesitas clases cuando hay: estado mutable complejo (modelos sklearn), polimorfismo (varios algoritmos misma interfaz), o frameworks que lo exigen (PyTorch nn.Module)."),
        ("¿`@dataclass` o NamedTuple o pydantic?",
         "NamedTuple: record inmutable simple, sin validación. dataclass: record con métodos opcionales. **pydantic** (no en stdlib): cuando además quieres validación de tipos en runtime, parsing desde JSON, etc. (lo verás en MLOps)."),
        ("¿Composición > herencia siempre?",
         "Como regla. Usa herencia solo cuando *is-a* sea genuino (`PerroLabrador` is-a `Perro` is-a `Animal`). Para *has-a* (`Coche` tiene un `Motor`), composición. Para reutilizar comportamiento sin jerarquía, considera mixins o protocols."),
        ("¿`property` y getters/setters Java-style?",
         "En Python no escribes `getNombre()/setNombre()`. Usa atributo público (`self.nombre = ...`). Si después necesitas lógica, conviertes a `@property` sin cambiar el caller. Es la magia."),
        ("¿Cuándo `__slots__`?",
         "Optimización: define los atributos permitidos y ahorra memoria (~50%) al no usar `__dict__` por instancia. Útil solo en clases con millones de instancias. Costo: pierde herencia múltiple y dinamismo."),
    ],
))


SPECS.append(ClassSpec(
    folder="011-pathlib-lectura-y-escritura-de-archivos",
    number="011",
    title="pathlib, lectura y escritura de archivos",
    duration="60 min",
    source="*Python Tutorial* cap. 10 · `pathlib` docs · *Effective Python* (Slatkin) ítem 38.",
    objetivo=(
        "Que el alumno deje de usar `os.path.join` + strings y adopte `pathlib.Path` — API orientada "
        "a objetos, multiplataforma (Windows/Unix), con métodos legibles para todas las operaciones "
        "de filesystem que hace todo el tiempo en DS (leer CSV, listar archivos, crear carpetas)."
    ),
    resultados=[
        "**Construir paths** con `Path(...) / 'subdir' / 'file.csv'` (operador `/`).",
        "**Leer/escribir** archivos texto y binarios con métodos de `Path` (`read_text`, `write_bytes`).",
        "**Listar y filtrar** archivos con `iterdir`, `glob`, `rglob` (recursivo).",
        "**Crear/eliminar** estructuras de directorios sin pelear con `os.makedirs(exist_ok=True)`.",
        "**Manejar rutas relativas vs absolutas** y entender `__file__`.",
    ],
    temas=[
        ("`Path` vs strings", "Objetos con métodos > concatenación manual."),
        ("Operador `/` para componer", "Legible y multiplataforma."),
        ("`read_text` / `write_text` / `read_bytes`", "One-liners para operaciones simples."),
        ("`glob` y `rglob`", "Patrones tipo shell: `*.csv`, `**/*.py`."),
        ("`mkdir(parents=True, exist_ok=True)`", "Crea árbol completo idempotente."),
        ("`Path(__file__).parent` y `resolve()`", "Localizar recursos relativos al script."),
    ],
    dataset="Carpeta temporal creada en el notebook con archivos sintéticos. Sin descarga.",
    ejercicios=[
        "**Construye una ruta multiplataforma.** Dado `Path.home() / 'datos' / '2026' / 'enero.csv'`, imprime cómo se ve en Windows vs Unix.",
        "**Lista CSVs.** En una carpeta con archivos mixtos (.csv, .txt, .py), lista solo los `.csv` ordenados por tamaño.",
        "**Búsqueda recursiva.** En un árbol de carpetas, encuentra todos los `.py` que contengan la palabra `TODO` en su contenido.",
        "**Escribe + lee.** Genera 3 archivos `txt` con `write_text`, léelos con `read_text`, concaténalos en uno solo.",
        "**Ruta del script.** Escribe un script que cargue un dataset que vive *al lado* del script (no del cwd), usando `Path(__file__).parent / 'data.csv'`.",
    ],
    homework=(
        "Script `inventario.py` que recibe un directorio y produce un reporte CSV con: nombre, "
        "tamaño_bytes, extensión, última_modificación para cada archivo recursivamente, usando "
        "solo `pathlib` (no `os`)."
    ),
    homework_criterio="El script corre tanto en Windows como en Linux/macOS sin cambios.",
    referencias=[
        "[`pathlib` docs](https://docs.python.org/3/library/pathlib.html)",
        "[PEP 428 — Object-oriented filesystem paths](https://peps.python.org/pep-0428/)",
        "Slatkin, *Effective Python* 2e — ítem 38 *Use Pathlib instead of os.path*.",
    ],
    siguiente=("012-logging", "Logging"),
    cells=[
        Cell("md", "# Clase 011 — pathlib\n\n**Parte 0** · `pathlib` docs + PEP 428.\n\n> 🎯 API moderna y multiplataforma para todo lo de filesystem. Adiós a `os.path.join`.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import tempfile\nfrom pathlib import Path\nimport time\n\n# Carpeta de trabajo temporal\nbase = Path(tempfile.mkdtemp(prefix='lab011_'))\nprint(f'trabajo en: {base}')"),
        Cell("md", "## 1️⃣ `Path` vs string\n\n```python\n# ❌ Vieja escuela\nimport os\npath = os.path.join(os.path.expanduser('~'), 'datos', '2026', 'enero.csv')\n\n# ✅ pathlib\nfrom pathlib import Path\npath = Path.home() / 'datos' / '2026' / 'enero.csv'\n```\n\nEl operador `/` se sobreescribe en `Path` para componer rutas. **Es multiplataforma**: en Windows se renderiza con `\\`, en Unix con `/`."),
        Cell("code", "p = Path.home() / 'datos' / '2026' / 'enero.csv'\nprint(f'path: {p}')\nprint(f'parent: {p.parent}')\nprint(f'name: {p.name}')\nprint(f'stem: {p.stem}')\nprint(f'suffix: {p.suffix}')\nprint(f'parts: {p.parts}')"),
        Cell("md", "## 2️⃣ Crear, leer, escribir\n\nOne-liners cubren el 90% de los casos:"),
        Cell("code", "# Crear estructura\n(base / 'subdir').mkdir(parents=True, exist_ok=True)\n\n# Escribir texto\n(base / 'hola.txt').write_text('hola mundo\\nsegunda línea\\n', encoding='utf-8')\n\n# Leer texto\ncontenido = (base / 'hola.txt').read_text(encoding='utf-8')\nprint('contenido:')\nprint(contenido)\n\n# Binario\n(base / 'datos.bin').write_bytes(b'\\x00\\x01\\x02\\x03')\nprint('bytes:', (base / 'datos.bin').read_bytes())"),
        Cell("md", "## 3️⃣ Listar archivos\n\n- `path.iterdir()` — listado simple (no recursivo)\n- `path.glob('*.csv')` — patrón en un nivel\n- `path.rglob('*.py')` — recursivo (todo el árbol)"),
        Cell("code", "# Genera archivos de muestra\nfor ext in ['csv', 'csv', 'txt', 'py', 'csv']:\n    nombre = f'archivo_{ext}_{int(time.time()*1000)%10000}.{ext}'\n    (base / nombre).write_text(f'demo {ext}')\n\n# Solo CSVs, ordenados por tamaño\ncsvs = sorted(base.glob('*.csv'), key=lambda p: p.stat().st_size, reverse=True)\nfor p in csvs:\n    print(f'  {p.name:35s} {p.stat().st_size} bytes')"),
        Cell("md", "## 4️⃣ Operaciones útiles\n\n```python\np.exists()         # bool\np.is_file()        # bool\np.is_dir()         # bool\np.absolute()       # ruta absoluta (sin resolver symlinks)\np.resolve()        # ruta absoluta + resuelve symlinks\np.unlink()         # borra archivo\np.rmdir()          # borra dir vacío\np.rename(nuevo)    # renombra/mueve\np.stat().st_size   # info filesystem (tamaño, mtime, etc.)\np.with_suffix('.json')   # cambia extensión\n```"),
        Cell("code", "# Demostración\np = base / 'hola.txt'\nprint(f'absolute      : {p.absolute()}')\nprint(f'with_suffix   : {p.with_suffix(\".md\")}')\nprint(f'with_name     : {p.with_name(\"otro.txt\")}')\nprint(f'mtime         : {p.stat().st_mtime:.0f}')\nprint(f'size          : {p.stat().st_size} bytes')"),
        Cell("md", "## 5️⃣ Rutas relativas al script — `__file__`\n\n**Problema clásico**: tu script carga `data.csv` con `pd.read_csv('data.csv')` y funciona desde el directorio del proyecto, pero falla cuando lo ejecutan desde otro lado.\n\n**Solución**: rutas relativas al script, no al cwd:\n\n```python\nfrom pathlib import Path\n\nROOT = Path(__file__).parent\ndf = pd.read_csv(ROOT / 'data' / 'penguins.csv')\n```\n\n`__file__` apunta al archivo Python actual. `.parent` da su carpeta. `.resolve()` lo convierte en absoluto."),
        Cell("md", "## ✅ Checklist\n\n- [ ] Uso `Path(...) / 'sub' / 'file'` en vez de strings\n- [ ] Conozco `read_text` / `write_text` / `read_bytes`\n- [ ] Uso `glob` y `rglob` según el alcance\n- [ ] `mkdir(parents=True, exist_ok=True)` es mi default\n- [ ] Rutas relativas a `__file__`, no al cwd"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Script `inventario.py` que recorre un directorio y produce CSV con metadata."),
        Cell("md", "## 🔗 Referencias\n\n- [`pathlib` docs](https://docs.python.org/3/library/pathlib.html)\n- [PEP 428](https://peps.python.org/pep-0428/)\n\n➡️ **Siguiente:** [012 — Logging](../012-logging/README.md)"),
    ],
    definiciones=[
        ("`Path`", "Objeto que representa una ruta de filesystem orientada a objetos (`pathlib.Path`). Sobreescribe `/` para componer rutas, multiplataforma (Windows usa `\\`, Unix `/`, transparente). Tiene métodos para casi todo: leer, escribir, listar, mover, borrar."),
        ("Ruta absoluta vs relativa", "**Absoluta**: empieza desde la raíz (`C:\\dev\\proyecto\\data.csv` o `/home/user/data.csv`). **Relativa**: parte del cwd (`data.csv`). Las rutas relativas dependen de dónde se ejecuta — fuente de bugs."),
        ("`Path.cwd()` vs `Path(__file__).parent`", "`cwd()` es el directorio donde se ejecutó el script (cambia según el invocante). `__file__` es la ruta al archivo Python actual; `.parent` su carpeta. **Usa `__file__`** para recursos que viven junto al script."),
        ("`glob` vs `rglob`", "Patrones tipo shell. `glob('*.csv')` busca en el directorio actual (1 nivel). `rglob('*.csv')` busca recursivo (todo el árbol). `**` significa 'cualquier número de directorios'."),
        ("`read_text` / `write_text`", "One-liners para texto: `Path('x.txt').write_text(contenido, encoding='utf-8')`. Para binario: `read_bytes` / `write_bytes`. Para JSON/CSV usa librerías especializadas."),
    ],
    errores_comunes=[
        ("`FileNotFoundError` aunque el archivo existe", "Estás usando ruta relativa y el cwd no es el que crees. **Fix**: `print(Path.cwd())` para diagnosticar; usa rutas relativas a `__file__` para archivos del proyecto."),
        ("`PermissionError` al escribir", "Carpeta read-only, OneDrive sincronizando, antivirus bloqueando. **Fix**: chequea permisos con `p.stat()`, escribe a `tempfile.gettempdir()` para tests."),
        ("`mkdir()` falla si el directorio ya existe", "Default es `exist_ok=False`. **Fix**: `p.mkdir(parents=True, exist_ok=True)` — crea árbol completo idempotente."),
        ("Mezclo `os.path` y `pathlib`", "Algunos funciones esperan strings (`open()`, `pd.read_csv()`). Path soporta el protocolo `os.PathLike` y la mayoría las acepta directo; si no, `str(p)` lo convierte."),
        ("`glob('*.CSV')` no encuentra `archivo.csv`", "Case-sensitive en Linux, insensible en Windows. **Fix**: filtra explícito con `[p for p in path.iterdir() if p.suffix.lower() == '.csv']`."),
    ],
    faq=[
        ("¿`pathlib` o `os.path`?",
         "**`pathlib`** para código nuevo. `os.path` es la API funcional vieja (strings + funciones); pathlib es OO y mucho más legible. Solo usa `os.path` para compatibilidad con código viejo."),
        ("¿Cómo evito el típico `'C:/Users/...'` vs `'/home/...'` cross-platform?",
         "**No hardcodees rutas absolutas.** Usa `Path.home()`, `Path(__file__).parent`, `tempfile.gettempdir()`. Y siempre `Path` + `/`, nunca strings concatenados."),
        ("¿Cómo leo un CSV grande con pathlib?",
         "Pathlib es para *paths*, no parsing. Combina: `pd.read_csv(Path('data') / 'big.csv')`. El Path se convierte a string automáticamente."),
        ("¿`Path('a') / 'b/c'` o `Path('a') / 'b' / 'c'`?",
         "Ambas funcionan: `Path` parsea separadores. Pero la primera es menos explícita; prefiere la segunda."),
        ("¿`shutil` o `pathlib` para mover/copiar?",
         "**`shutil`** para operaciones recursivas (copytree, rmtree, move) — pathlib solo cubre operaciones simples. Combinable: `shutil.copy(src_path, dst_path)` acepta Path directo."),
    ],
))


SPECS.append(ClassSpec(
    folder="012-logging",
    number="012",
    title="Logging",
    duration="60 min",
    source="*Python Tutorial* logging HOWTO · *The Pragmatic Programmer* — \"Programming by Coincidence\".",
    objetivo=(
        "Que el alumno **deje de usar `print` para debug** y aprenda el módulo `logging` estándar: "
        "niveles (DEBUG/INFO/WARNING/ERROR/CRITICAL), handlers (consola, archivo), formatters, y "
        "configuración por módulo. Es la diferencia entre código que se debuggea reiniciando el "
        "notebook y código que se debuggea leyendo logs."
    ),
    resultados=[
        "**Diferenciar** los 5 niveles de logging y cuándo usar cada uno.",
        "**Configurar** un logger con `logging.basicConfig` y entender por qué `basicConfig` solo funciona una vez.",
        "**Crear loggers por módulo** con `logging.getLogger(__name__)`.",
        "**Agregar handlers**: uno a consola (INFO+), otro a archivo (DEBUG+).",
        "**Formatear** logs con timestamp, módulo y nivel.",
    ],
    temas=[
        ("`print` vs `logging`", "print() es output; logging es observabilidad."),
        ("Niveles: DEBUG/INFO/WARNING/ERROR/CRITICAL", "Filtran qué se ve sin tocar código."),
        ("Logger jerárquico por módulo", "`getLogger(__name__)` para herencia natural."),
        ("Handlers: consola, archivo, rotating", "Mismo log → múltiples destinos."),
        ("Formatters", "Timestamp + nivel + módulo + mensaje."),
        ("`logging.basicConfig` y sus límites", "Solo afecta el primero; preferir config explícita."),
    ],
    dataset="Genera un log file de demo. Sin descarga.",
    ejercicios=[
        "**Reemplaza prints.** Toma una función con 5 prints y conviértelos a logger con niveles apropiados.",
        "**Logger por módulo.** Crea 2 archivos `.py` que cada uno usa `getLogger(__name__)`. Configura el root logger una vez; verifica que ambos heredan.",
        "**Handler doble.** Configura: consola = INFO+, archivo `app.log` = DEBUG+. Genera 5 logs de niveles distintos y verifica qué aparece en cada destino.",
        "**Formato con timestamp.** Cambia el formato a `'%(asctime)s [%(levelname)s] %(name)s: %(message)s'`. Inspecciona output.",
        "**Logger en notebook.** Pelea con `basicConfig` no recordando estado entre reinicios — usa `dictConfig` o `force=True`.",
    ],
    homework=(
        "Notebook + 2 módulos `.py` que importan y loguean. Un `logging_config.py` con `dictConfig` "
        "que define: consola (INFO+, formato corto) y `app.log` (DEBUG+, formato verbose con "
        "timestamp). El notebook ejecuta funciones que generan logs de distintos niveles desde "
        "ambos módulos. Adjunta el `app.log` resultante."
    ),
    homework_criterio="`app.log` contiene timestamp y módulo correcto en cada línea; consola filtra DEBUG.",
    referencias=[
        "[Logging HOWTO](https://docs.python.org/3/howto/logging.html)",
        "[Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)",
        "[`logging.config` — dictConfig](https://docs.python.org/3/library/logging.config.html)",
    ],
    siguiente=("013-type-hints-y-mypy", "Type hints y mypy"),
    cells=[
        Cell("md", "# Clase 012 — Logging\n\n**Parte 0** · Logging HOWTO.\n\n> 🎯 Dejar `print` para debug y usar `logging` con niveles, handlers, formatters. La diferencia entre código observable y código que adivinas.\n\n> ⏱️ ~60 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "import logging\nimport tempfile\nfrom pathlib import Path\nfrom logging.config import dictConfig"),
        Cell("md", "## 1️⃣ Por qué `logging` y no `print`\n\n| `print` | `logging` |\n|---|---|\n| stdout fijo | múltiples destinos |\n| sin nivel | DEBUG/INFO/WARNING/ERROR/CRITICAL |\n| sin contexto | módulo, función, timestamp automáticos |\n| no se silencia sin tocar código | filtras por nivel |\n| no estructurado | parseable, integrable con observabilidad |"),
        Cell("md", "## 2️⃣ Niveles\n\n| Nivel | Uso |\n|---|---|\n| `DEBUG` | detalles para diagnóstico (variables, flujo) |\n| `INFO` | progreso normal (\"cargados 1000 registros\") |\n| `WARNING` | algo raro pero no fatal (\"valor por defecto usado\") |\n| `ERROR` | la operación falló (\"no se pudo cargar el CSV\") |\n| `CRITICAL` | sistema no puede continuar |\n\nFiltro: si configuras nivel `INFO`, solo se muestran INFO/WARNING/ERROR/CRITICAL."),
        Cell("md", "## 3️⃣ Setup mínimo con `basicConfig`\n\n```python\nimport logging\nlogging.basicConfig(\n    level=logging.INFO,\n    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',\n)\nlog = logging.getLogger(__name__)\nlog.info('arrancando...')\nlog.warning('cuidado')\n```\n\n⚠️ **Gotcha**: `basicConfig` solo aplica si **no había handlers** en root. En Jupyter (kernel reusado) puede no tener efecto — usa `force=True`."),
        Cell("code", "# Reset y configuración explícita para notebook\nfor h in logging.root.handlers[:]:\n    logging.root.removeHandler(h)\n\nlogging.basicConfig(\n    level=logging.DEBUG,\n    format='%(asctime)s [%(levelname)s] %(name)s: %(message)s',\n    datefmt='%H:%M:%S',\n    force=True,\n)\n\nlog = logging.getLogger(__name__)\nlog.debug('detalle interno')\nlog.info('todo OK')\nlog.warning('algo raro')\nlog.error('fallo manejable')"),
        Cell("md", "## 4️⃣ Logger por módulo — la práctica correcta\n\n```python\n# loader.py\nimport logging\nlog = logging.getLogger(__name__)   # 'loader' o 'mi_pkg.loader'\n\ndef cargar(path):\n    log.info(f'cargando {path}')\n    ...\n```\n\nVentaja: el root logger configurado **una vez** propaga a todos los módulos. Puedes silenciar uno solo con `logging.getLogger('loader').setLevel(WARNING)`."),
        Cell("code", "# Simula 2 módulos\nlog_app = logging.getLogger('mi_app')\nlog_db  = logging.getLogger('mi_app.db')\n\nlog_app.info('arrancando app')\nlog_db.info('conectando a db')\nlog_db.warning('latencia alta')\n\n# Silencia un módulo específico\nlog_db.setLevel(logging.ERROR)\nlog_db.info('esto NO se ve')\nlog_db.error('esto sí se ve')"),
        Cell("md", "## 5️⃣ Handler doble — consola + archivo\n\nPara producción típicamente queremos:\n- Consola: INFO+ (lo que el operador ve)\n- Archivo: DEBUG+ (todo para post-mortem)"),
        Cell("code", "log_file = Path(tempfile.gettempdir()) / 'demo_app.log'\n\nconfig = {\n    'version': 1,\n    'disable_existing_loggers': False,\n    'formatters': {\n        'verbose': {'format': '%(asctime)s [%(levelname)s] %(name)s: %(message)s'},\n        'corto':   {'format': '[%(levelname)s] %(message)s'},\n    },\n    'handlers': {\n        'consola': {\n            'class': 'logging.StreamHandler',\n            'level': 'INFO',\n            'formatter': 'corto',\n        },\n        'archivo': {\n            'class': 'logging.FileHandler',\n            'filename': str(log_file),\n            'level': 'DEBUG',\n            'formatter': 'verbose',\n            'mode': 'w',\n        },\n    },\n    'root': {\n        'level': 'DEBUG',\n        'handlers': ['consola', 'archivo'],\n    },\n}\ndictConfig(config)\n\nlog = logging.getLogger('demo')\nlog.debug('DEBUG: solo va al archivo')\nlog.info('INFO: va a ambos')\nlog.warning('WARN: va a ambos')\nlog.error('ERROR: va a ambos')\n\nprint(f'\\n--- contenido de {log_file} ---')\nprint(log_file.read_text())"),
        Cell("md", "## 6️⃣ Buenas prácticas\n\n- **No hagas `f'{var}'` en el mensaje** si vas a filtrar por nivel: pasa args separados, `log.debug('valor: %s', var)`. Así no se formatea si el nivel no aplica.\n- **No loguees datos sensibles**: PII, tokens, contraseñas. Filtra antes.\n- **`exc_info=True`** en `log.error` para capturar el traceback completo.\n- **Logger por módulo**, configuración por aplicación. No mezcles."),
        Cell("code", "# exc_info=True para capturar traceback\ntry:\n    1 / 0\nexcept ZeroDivisionError:\n    log.error('división falló', exc_info=True)"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Sé los 5 niveles y cuándo usar cada uno\n- [ ] Uso `getLogger(__name__)` en cada módulo\n- [ ] Configuro logging UNA vez en el entrypoint\n- [ ] Tengo handler consola (INFO+) y archivo (DEBUG+)\n- [ ] Uso `exc_info=True` para errores con stacktrace"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Notebook + 2 módulos + `logging_config.py` con `dictConfig`; entrega `app.log`."),
        Cell("md", "## 🔗 Referencias\n\n- [Logging HOWTO](https://docs.python.org/3/howto/logging.html)\n- [Logging Cookbook](https://docs.python.org/3/howto/logging-cookbook.html)\n\n➡️ **Siguiente:** [013 — Type hints y mypy](../013-type-hints-y-mypy/README.md)"),
    ],
    definiciones=[
        ("Logger", "Punto de entrada para emitir logs. Se obtiene con `logging.getLogger(__name__)` — esto crea un logger nombrado por el módulo. Característica clave: los loggers son **jerárquicos** (separados por `.`); la config de root propaga a hijos."),
        ("Handler", "Define **a dónde** van los logs (consola, archivo, syslog, sentry…). Un logger puede tener N handlers. Cada handler tiene su propio nivel y formatter."),
        ("Formatter", "Define **cómo** se renderiza el log: `'%(asctime)s [%(levelname)s] %(name)s: %(message)s'`. Campos comunes: `asctime`, `levelname`, `name` (logger), `message`, `funcName`, `lineno`, `pathname`."),
        ("Nivel (DEBUG/INFO/WARNING/ERROR/CRITICAL)", "Severidad ascendente. Filtran qué se emite. **DEBUG**: detalle interno; **INFO**: progreso normal; **WARNING**: algo raro pero no fatal; **ERROR**: operación falló; **CRITICAL**: sistema no puede continuar."),
        ("`dictConfig`", "Forma declarativa de configurar logging desde un dict (o YAML/JSON). Más mantenible que llamadas `basicConfig`/`addHandler` dispersas. Convención: una sola llamada en el entrypoint."),
    ],
    errores_comunes=[
        ("`logging.basicConfig(...)` no tiene efecto", "`basicConfig` solo aplica si root no tiene handlers ya. **Fix**: `basicConfig(..., force=True)` o limpia handlers (`for h in logging.root.handlers[:]: logging.root.removeHandler(h)`)."),
        ("Logs duplicados (cada mensaje aparece 2 veces)", "Configuraste el mismo handler dos veces (común al recargar módulos en Jupyter). **Fix**: limpia handlers antes de añadir, o usa `dictConfig` con `disable_existing_loggers=False` cuidadosamente."),
        ("`log.debug(f'valor: {expensive_call()}')` siempre evalúa", "El f-string se construye **antes** de pasar a `debug` — el filtro de nivel no ayuda. **Fix**: usa lazy: `log.debug('valor: %s', expensive_call)` (sin paréntesis ⇒ solo se llama si pasa el filtro)."),
        ("Mi logger emite en INFO pero quiero ver DEBUG", "El nivel está en handler o logger raíz. **Fix**: `logging.getLogger().setLevel(logging.DEBUG)` Y `handler.setLevel(logging.DEBUG)` (ambos deben permitirlo)."),
        ("`logging` rompe en multiprocessing", "Handlers no son fork-safe. **Fix**: en cada proceso, configura logging de nuevo; o usa `QueueHandler` + `QueueListener` del cookbook oficial."),
    ],
    faq=[
        ("¿`print` o `logging`?",
         "**`logging` siempre en código que vivirá >1 día.** `print` solo para REPL/scripts one-shot. Logging te da niveles, timestamps, módulo origen, múltiples destinos, integración con observabilidad."),
        ("¿Dónde configuro logging?",
         "**Una sola vez** en el entrypoint (`__main__`, `app.py`, `cli.py`). Cada módulo solo hace `log = logging.getLogger(__name__)`; nunca llama a `basicConfig`/`addHandler` desde un módulo importable."),
        ("¿Por qué `getLogger(__name__)`?",
         "Crea un logger jerárquico nombrado por el módulo. Permite silenciar uno específico (`logging.getLogger('mi_app.db').setLevel(WARNING)`) sin tocar el resto. Pattern estándar."),
        ("¿Cómo formato un dict/object en el mensaje?",
         "`log.info('user=%s data=%s', user_id, data)` (mejor que f-string por el lazy). Para JSON estructurado, usa `python-json-logger` o stdlib con custom formatter."),
        ("¿`logging` propaga al root logger?",
         "Por default, sí — cada logger propaga al padre hasta root. Si configuras handlers en root y en hijos, verás el mensaje dos veces. **Fix**: `logger.propagate = False` en el hijo, o solo configura root."),
    ],
))


SPECS.append(ClassSpec(
    folder="013-type-hints-y-mypy",
    number="013",
    title="Type hints y mypy",
    duration="75 min",
    source="*Fluent Python* 2e cap. 8 (Type Hints in Functions) · *typing* docs · mypy docs.",
    objetivo=(
        "Que el alumno anote tipos en sus funciones y dataclasses — no por dogma, sino porque "
        "permiten que el IDE autocomplete bien, que `mypy` detecte bugs antes de runtime, y que "
        "el lector entienda la intención. Tipos como **documentación verificable**."
    ),
    resultados=[
        "**Anotar** funciones con tipos en parámetros y retorno (`def f(x: int) -> str`).",
        "**Usar tipos compuestos**: `list[int]`, `dict[str, float]`, `tuple[int, str]`, `Optional[X]`, `X | None`.",
        "**Definir tipos personalizados** con `TypeAlias` y `Protocol` (structural typing).",
        "**Ejecutar mypy** sobre código y interpretar sus errores.",
        "**Reconocer** cuándo type hints aportan (APIs públicas, data classes) y cuándo no (notebooks exploratorios).",
    ],
    temas=[
        ("Sintaxis básica: `x: int`, `-> bool`", "Solo anotaciones — no afectan runtime."),
        ("Tipos compuestos modernos (3.9+): `list[int]`", "Sin `from typing import List`."),
        ("`Optional[X]` y `X | None` (3.10+)", "Cuando algo puede ser None."),
        ("`Literal`, `TypedDict`, `Protocol`", "Tipos avanzados útiles."),
        ("`mypy`: instalar y correr", "Static type checker."),
        ("`reveal_type(x)` y `# type: ignore`", "Diagnóstico y escape hatch."),
        ("Cuándo SÍ y cuándo NO", "API pública sí; notebook exploratorio quizá no."),
    ],
    dataset="Funciones de ejemplo en el notebook. Sin descarga.",
    ejercicios=[
        "**Anota una función.** Toma una función de los ejercicios de clase 008 (sin tipos) y anótala completa.",
        "**Optional vs default.** Distingue `def f(x: int = 0)` (default 0) de `def f(x: int | None = None)` (puede no haber valor).",
        "**TypedDict.** Define `class PersonaDict(TypedDict)` con `nombre: str`, `edad: int`. Úsala como tipo de un parámetro.",
        "**Corre mypy.** Instala mypy, créate un archivo con un bug de tipo intencional (`def f(x: int) -> str: return x + 1`) y corre `mypy archivo.py`. Lee y explica el error.",
        "**Protocol.** Define `class TienePromedio(Protocol)` con método `promedio() -> float`. Acepta cualquier clase que lo implemente (duck typing tipado).",
    ],
    homework=(
        "Repo con un módulo `analytics.py` (5+ funciones completamente anotadas), `pyproject.toml` "
        "que incluye mypy en `[tool.mypy]` con `strict = true`, y screenshot/log de `mypy analytics.py` "
        "sin errores."
    ),
    homework_criterio="`mypy --strict` corre sin errores ni warnings. Tipos consistentes y precisos.",
    referencias=[
        "Ramalho, *Fluent Python* 2e — cap. 8.",
        "[`typing` docs](https://docs.python.org/3/library/typing.html)",
        "[mypy docs](https://mypy.readthedocs.io/)",
        "[PEP 484 — Type Hints](https://peps.python.org/pep-0484/)",
        "[PEP 604 — `X | Y` syntax](https://peps.python.org/pep-0604/)",
    ],
    siguiente=("014-numpy-tipos-creacion-atributos", "NumPy: tipos, creación, atributos"),
    cells=[
        Cell("md", "# Clase 013 — Type hints y mypy\n\n**Parte 0** · Ramalho cap. 8 + PEP 484.\n\n> 🎯 Tipos como documentación verificable. mypy detecta bugs antes de runtime.\n\n> ⏱️ ~75 min"),
        Cell("md", "## ⚙️ Setup"),
        Cell("code", "from typing import Optional, Literal, TypedDict, Protocol, TypeAlias\nfrom dataclasses import dataclass"),
        Cell("md", "## 1️⃣ Sintaxis básica\n\n```python\ndef saludar(nombre: str, formal: bool = False) -> str:\n    return f'Buenos días, {nombre}' if formal else f'Hola {nombre}'\n```\n\n**Importante**: los tipos son **anotaciones** — Python NO los verifica en runtime. Son para tooling (IDE, mypy, IA)."),
        Cell("code", "def saludar(nombre: str, formal: bool = False) -> str:\n    return f'Buenos días, {nombre}' if formal else f'Hola {nombre}'\n\nprint(saludar('Ana'))\nprint(saludar('Bob', formal=True))\n\n# Esto NO falla en runtime (Python no verifica), pero mypy lo detectaría:\nprint(saludar(123))  # type hint dice str, le pasamos int"),
        Cell("md", "## 2️⃣ Tipos compuestos modernos\n\nDesde Python 3.9+, usa **lowercase** built-ins:\n\n```python\n# ✅ moderno (3.9+)\ndef f(xs: list[int], lookup: dict[str, float]) -> tuple[int, str]:\n    ...\n\n# ❌ viejo (pre-3.9)\nfrom typing import List, Dict, Tuple\ndef f(xs: List[int], lookup: Dict[str, float]) -> Tuple[int, str]:\n    ...\n```\n\nDesde 3.10+, usa `|` para uniones:\n\n```python\n# ✅ moderno (3.10+)\ndef parse(x: str | int) -> float | None:\n    ...\n\n# ❌ viejo\nfrom typing import Union, Optional\ndef parse(x: Union[str, int]) -> Optional[float]:\n    ...\n```"),
        Cell("code", "# Demo: tipos compuestos\ndef promedios_por_grupo(\n    datos: list[dict[str, float]],\n    grupo_key: str = 'grupo',\n    valor_key: str = 'valor',\n) -> dict[str, float]:\n    sumas: dict[str, float] = {}\n    conteos: dict[str, int] = {}\n    for d in datos:\n        g = d[grupo_key]\n        sumas[g] = sumas.get(g, 0.0) + d[valor_key]\n        conteos[g] = conteos.get(g, 0) + 1\n    return {g: sumas[g] / conteos[g] for g in sumas}\n\ndatos = [\n    {'grupo': 'A', 'valor': 10.0},\n    {'grupo': 'A', 'valor': 20.0},\n    {'grupo': 'B', 'valor': 5.0},\n]\nprint(promedios_por_grupo(datos))"),
        Cell("md", "## 3️⃣ `Optional` vs default\n\nDistinción importante:\n\n```python\ndef f(x: int = 0):           # x es int; default 0 si no se pasa\ndef f(x: int | None = None): # x puede ser None — el caller debe decidir\n```\n\nEl segundo caso obliga al cuerpo a manejar `None`:"),
        Cell("code", "def buscar(nombre: str, default: int | None = None) -> int:\n    db = {'Ana': 30, 'Bob': 25}\n    if nombre in db:\n        return db[nombre]\n    if default is None:\n        raise KeyError(nombre)\n    return default\n\nprint(buscar('Ana'))\nprint(buscar('Cris', default=0))\ntry:\n    buscar('Cris')\nexcept KeyError as e:\n    print(f'KeyError: {e}')"),
        Cell("md", "## 4️⃣ `TypedDict` — diccionarios con esquema\n\nÚtil cuando recibes JSON o configs:"),
        Cell("code", "class PersonaDict(TypedDict):\n    nombre: str\n    edad: int\n    activo: bool\n\ndef saludar_persona(p: PersonaDict) -> str:\n    return f'{p[\"nombre\"]} ({p[\"edad\"]}) está {\"activo\" if p[\"activo\"] else \"inactivo\"}'\n\np: PersonaDict = {'nombre': 'Ana', 'edad': 30, 'activo': True}\nprint(saludar_persona(p))"),
        Cell("md", "## 5️⃣ `Literal` — valores concretos como tipo\n\nÚtil para parámetros que solo aceptan ciertos strings:"),
        Cell("code", "def ordenar(items: list[int], orden: Literal['asc', 'desc'] = 'asc') -> list[int]:\n    return sorted(items, reverse=(orden == 'desc'))\n\nprint(ordenar([3, 1, 4, 1, 5]))\nprint(ordenar([3, 1, 4, 1, 5], orden='desc'))\n# mypy detectaría: ordenar([1,2], orden='upward')  # 'upward' no es 'asc'|'desc'"),
        Cell("md", "## 6️⃣ `Protocol` — duck typing tipado\n\n\"Cualquier cosa que tenga estos métodos\":"),
        Cell("code", "class TienePromedio(Protocol):\n    def promedio(self) -> float: ...\n\n@dataclass\nclass Curso:\n    notas: list[float]\n    def promedio(self) -> float:\n        return sum(self.notas) / len(self.notas)\n\n@dataclass\nclass Atleta:\n    tiempos: list[float]\n    def promedio(self) -> float:\n        return sum(self.tiempos) / len(self.tiempos)\n\ndef reportar(items: list[TienePromedio]) -> None:\n    for it in items:\n        print(f'{type(it).__name__}: {it.promedio():.2f}')\n\nreportar([Curso([6.5, 7.0]), Atleta([10.1, 9.8])])"),
        Cell("md", "## 7️⃣ Correr mypy\n\n```bash\npip install mypy\nmypy archivo.py            # modo permisivo\nmypy --strict archivo.py   # modo estricto (recomendado para libs)\n```\n\nConfig en `pyproject.toml`:\n\n```toml\n[tool.mypy]\npython_version = \"3.12\"\nstrict = true\nignore_missing_imports = true   # libs sin stubs\n```\n\n**`# type: ignore`** al final de una línea silencia mypy en esa línea — escape hatch para casos legítimos (libs sin stubs, hacks intencionales)."),
        Cell("md", "## 8️⃣ ¿Cuándo SÍ, cuándo NO?\n\n**Sí**:\n- APIs públicas (funciones que importan otros)\n- Data classes / records\n- Lógica de dominio compleja\n- Tipos que mejoran autocompletado\n\n**Quizá no**:\n- Notebooks puramente exploratorios\n- Scripts one-shot\n- Cuando el tipo es obvio y agregar ruido (`x = 5  # int` no aporta)"),
        Cell("md", "## ✅ Checklist\n\n- [ ] Anoto funciones públicas con tipos en params y retorno\n- [ ] Uso `list[int]` (3.9+) en vez de `List[int]`\n- [ ] Uso `X | None` (3.10+) en vez de `Optional[X]`\n- [ ] Sé correr mypy y leer sus errores\n- [ ] Conozco `TypedDict`, `Literal`, `Protocol`"),
        Cell("md", "## 📝 Homework\n\nVer `README.md`. Módulo `analytics.py` con 5+ funciones anotadas, `pyproject.toml` con `[tool.mypy] strict=true`, log de mypy sin errores."),
        Cell("md", "## 🔗 Referencias\n\n- Ramalho, *Fluent Python* 2e, cap. 8\n- [typing docs](https://docs.python.org/3/library/typing.html)\n- [mypy docs](https://mypy.readthedocs.io/)\n\n➡️ **Siguiente:** [014 — NumPy: tipos, creación, atributos](../014-numpy-tipos-creacion-atributos/README.md)"),
    ],
    definiciones=[
        ("Type hint (annotation)", "Anotación de tipo en signature o variable: `def f(x: int) -> str`. **Python NO verifica en runtime** — son metadata leída por IDE/linter/mypy. Disponibles en `f.__annotations__`."),
        ("`Optional[X]` / `X | None`", "Indica que el valor puede ser `X` o `None`. `Optional[X]` ≡ `Union[X, None]` ≡ `X | None` (PEP 604, 3.10+). Usa la sintaxis con `|` en código nuevo."),
        ("`TypedDict`", "Esquema para diccionarios: `class PersonaDict(TypedDict): nombre: str; edad: int`. Permite tipear dicts que vienen de JSON/API sin convertirlos a dataclass."),
        ("`Literal`", "Restringe a un conjunto de valores: `Literal['asc', 'desc']` solo acepta esas 2 strings. Útil para flags, modos, enums simples."),
        ("`Protocol` (structural typing)", "Define interfaz por **estructura** (duck typing tipado): `class TienePromedio(Protocol): def promedio(self) -> float: ...`. Cualquier clase con `.promedio()` la satisface, sin heredarla."),
        ("mypy", "Static type checker oficial. Lee tu código, sigue las anotaciones, reporta inconsistencias antes de ejecutar. Modo `--strict` lo hace exigente; recomendado para librerías."),
    ],
    errores_comunes=[
        ("`from typing import List` da deprecation warning en mypy", "Python 3.9+ usa lowercase: `list[int]` en vez de `List[int]`. **Fix**: actualiza imports + sintaxis."),
        ("`Optional[int] = 0` confunde", "`Optional[int]` admite `None`. Si tu default es `0`, no necesitas Optional. **Fix**: `x: int = 0` (no admite None) vs `x: int | None = None` (admite None)."),
        ("mypy se queja \"Cannot find module 'libreria'\"", "Lib sin type stubs publicados. **Fix**: `pip install types-libreria` si existe (PEP 561), o `[tool.mypy] ignore_missing_imports = true` en pyproject."),
        ("Anoté pero mypy no encuentra errores", "mypy no se llamó. **Fix**: `mypy archivo.py`. No es automático — debe estar en CI o pre-commit."),
        ("`reveal_type(x)` no existe en runtime", "Es exclusivo de mypy: lo lees como output del check, NO ejecutas. Si lo dejas en código que corre, lanza NameError."),
    ],
    faq=[
        ("¿Tipo hints son obligatorios?",
         "**No** — Python no los verifica. Pero son fuertemente recomendados en: APIs públicas (funciones que importan otros), librerías, código compartido. En notebooks exploratorios, casi nunca aportan."),
        ("¿Slow my code los type hints?",
         "**No** — son metadata, no impactan runtime. `from __future__ import annotations` además las hace lazy (strings, evaluadas solo si introspeccionas)."),
        ("¿mypy en CI: estricto o permisivo?",
         "Empieza permisivo (sin `--strict`), arregla lo obvio, luego activa `--strict` gradualmente. Si arrancas estricto en un repo viejo, te ahogas en errores y termina ignorado."),
        ("¿Y si no sé qué tipo poner?",
         "`Any` (de `typing`) es válido — desactiva el check para ese caso. Mejor que mentir con un tipo incorrecto. Convención: comentario `# TODO: tipo correcto` para revisión futura."),
        ("¿Pydantic vs dataclass + type hints?",
         "**dataclass + hints**: tipos solo a nivel mypy, no en runtime. **Pydantic**: valida en runtime (parsing de JSON con coerción y errores legibles). Para input externo (API, config) → Pydantic. Para internal record → dataclass."),
    ],
))


def main() -> int:
    print(f"Generating {len(SPECS)} classes")
    for s in SPECS:
        write_class(s)
    print("Done.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
