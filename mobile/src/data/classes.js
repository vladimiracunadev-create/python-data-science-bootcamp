// GENERADO AUTOMÁTICAMENTE — no editar a mano.
//
// Fuente: classes/parte-*/NNN-*/README.md (las 232 clases del currículo v3).
// Regenerar con:  python scripts/generate_mobile_curriculum.py
//
// El contenido va embebido en el bundle JS para que el programa se pueda leer
// sin conexión; solo los enlaces a Colab requieren internet.

export const CURRICULUM_VERSION = "v3.9.0";

export const PARTS = [
  {
    "id": "parte-0-prerrequisitos",
    "number": 0,
    "title": "Prerrequisitos",
    "subtitle": "Python, NumPy, pandas, viz, SQL, NoSQL, APIs",
    "level": "Basico",
    "classCount": 49,
    "firstClass": 1,
    "lastClass": 49
  },
  {
    "id": "parte-1-machine-learning-clasico",
    "number": 1,
    "title": "ML clásico",
    "subtitle": "Regresión, clasificación, ensembles, no supervisado",
    "level": "Intermedio",
    "classCount": 50,
    "firstClass": 50,
    "lastClass": 99
  },
  {
    "id": "parte-2-deep-learning",
    "number": 2,
    "title": "Deep Learning",
    "subtitle": "Keras, TF, CNN, RNN, Transformers, RL, despliegue",
    "level": "Avanzado",
    "classCount": 75,
    "firstClass": 100,
    "lastClass": 174
  },
  {
    "id": "parte-3-estadistica-inferencial",
    "number": 3,
    "title": "Estadística inferencial",
    "subtitle": "Hipótesis, A/B testing, inferencia causal, Bayes",
    "level": "Intermedio-Avanzado",
    "classCount": 19,
    "firstClass": 175,
    "lastClass": 193
  },
  {
    "id": "parte-4-mlops",
    "number": 4,
    "title": "MLOps",
    "subtitle": "Docker, CI/CD, MLflow, monitoreo, interpretabilidad",
    "level": "Avanzado",
    "classCount": 14,
    "firstClass": 194,
    "lastClass": 207
  },
  {
    "id": "parte-5-ingenieria-de-datos",
    "number": 5,
    "title": "Ingeniería de datos",
    "subtitle": "Spark, Airflow, lakehouses, streaming",
    "level": "Avanzado",
    "classCount": 8,
    "firstClass": 208,
    "lastClass": 215
  },
  {
    "id": "parte-6-sistemas-de-recomendacion",
    "number": 6,
    "title": "Recomendadores",
    "subtitle": "Filtrado colaborativo, factorización, secuenciales",
    "level": "Intermedio-Avanzado",
    "classCount": 7,
    "firstClass": 216,
    "lastClass": 222
  },
  {
    "id": "parte-7-etica-fairness-privacidad",
    "number": 7,
    "title": "Ética, fairness, privacidad",
    "subtitle": "Sesgo, explicabilidad, marcos normativos",
    "level": "Intermedio",
    "classCount": 6,
    "firstClass": 223,
    "lastClass": 228
  },
  {
    "id": "parte-8-capstones",
    "number": 8,
    "title": "Capstones",
    "subtitle": "Proyectos integradores end-to-end",
    "level": "Integrador",
    "classCount": 4,
    "firstClass": 229,
    "lastClass": 232
  }
];

export const CLASSES = [
  {
    "id": "parte-0-prerrequisitos/001-instalacion-de-python-3-12-y-entornos-virtuales-venv-uv-conda",
    "number": 1,
    "slug": "001-instalacion-de-python-3-12-y-entornos-virtuales-venv-uv-conda",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Instalación de Python 3.12+ y entornos virtuales (venv, uv, conda)",
    "description": "Que el alumno deje su máquina lista para trabajar en data science: con Python 3.12+ instalado correctamente, con al menos dos gestores de entornos virtuales funcionando (venv nativo + uv o conda), y con la disciplina de…",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno deje su máquina lista para trabajar en data science: con Python 3.12+ instalado correctamente, con al menos dos gestores de entornos virtuales funcionando (venv nativo + uv o conda), y con la disciplina de nunca instalar paquetes en el Python del sistema. Al final de la clase, deberá poder crear un entorno limpio, activarlo, instalar dependencias declaradas, y reproducirlo exactamente en otra máquina.",
    "outcomes": [
      "Verificar qué versión de Python tiene su máquina y desde qué ruta se ejecuta (python -V, which python / where python, sys.executable).",
      "Crear, activar y destruir entornos virtuales con venv, uv venv y conda create — y explicar cuándo conviene cada uno.",
      "Instalar dependencias desde requirements.txt y desde pyproject.toml, y congelar versiones reproducibles (pip freeze, uv pip compile, conda env export).",
      "Diagnosticar el error más frecuente del principiante: \"instalé un paquete pero el import falla\" (causa: pip instaló en un Python distinto del que ejecuta el notebook).",
      "Justificar por qué un entorno virtual por proyecto es no-negociable en data science (reproducibilidad, conflictos de versiones, aislamiento de experimentos)."
    ],
    "topics": [
      "Qué es Python \"del sistema\" y por qué no tocarlo",
      "Instaladores oficiales vs. pyenv / mise",
      "venv (stdlib)",
      "uv (Astral)",
      "conda / mamba",
      "requirements.txt vs pyproject.toml vs environment.yml",
      "El bug más común: \"pip install funciona pero import falla\""
    ],
    "materials": [
      "Python.org downloads — instalador oficial.",
      "uv docs — gestor moderno de Astral.",
      "Miniconda — instalación mínima de conda (evita Anaconda completo, pesa 3 GB)."
    ],
    "exercises": [
      "Diagnóstico inicial. Abre una terminal y reporta: versión de Python (python -V), ruta absoluta (where python en Windows, which python en Unix) y el contenido de sys.path ejecutando un script. Anótalo — lo usarás de baseline.",
      "Crea un entorno venv llamado .venv en un directorio nuevo, actívalo, instala numpy==2.1.0 y pandas==2.2.3, y verifica con pip list. Luego desactívalo y comprueba que numpy ya no se importa desde el Python global.",
      "Replica el mismo entorno con uv. Instala uv (pipx install uv o el instalador oficial), corre uv venv, uv pip install numpy pandas, y compara la velocidad contra el paso anterior.",
      "Genera requirements.txt congelando versiones exactas con pip freeze > requirements.txt. Borra el entorno, recréalo desde cero y reinstala con pip install -r requirements.txt. Verifica que las versiones coinciden.",
      "Provoca y resuelve el bug clásico. Desde Jupyter (ejecutando con un Python distinto al del venv activo), corre !pip install seaborn y luego import seaborn. Diagnostica por qué falla (o por qué se instaló en el lugar equivocado) usando import sys; sys.executable en una celda."
    ],
    "codeExamples": [
      {
        "id": "parte-0-prerrequisitos/001-instalacion-de-python-3-12-y-entornos-virtuales-venv-uv-conda-code-1",
        "title": "Bloque 1",
        "explanation": "Código incluido en el material de la clase.",
        "schema": "bash · 4 líneas",
        "language": "bash",
        "code": "python -m venv .venv\nsource .venv/bin/activate    # o .venv\\Scripts\\activate en Windows\npip install -r requirements.txt\npython verify.py"
      }
    ],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/001-instalacion-de-python-3-12-y-entornos-virtuales-venv-uv-conda/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/002-jupyter-y-jupyterlab-kernels-magics-debugging-profiling",
    "number": 2,
    "slug": "002-jupyter-y-jupyterlab-kernels-magics-debugging-profiling",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Jupyter y JupyterLab — kernels, magics, debugging, profiling",
    "description": "Que el alumno deje de usar Jupyter como un editor de texto con botón \"play\" y empiece a usarlo como un entorno exploratorio profesional: con magics que ahorran horas, debugger interactivo (%debug), y profiling real (%ti…",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno deje de usar Jupyter como un editor de texto con botón \"play\" y empiece a usarlo como un entorno exploratorio profesional: con magics que ahorran horas, debugger interactivo (%debug), y profiling real (%timeit, %prun). Al final debe poder diagnosticar por qué un notebook es lento sin adivinar.",
    "outcomes": [
      "Diferenciar kernel, frontend (Notebook vs JupyterLab vs VS Code) y servidor — y saber qué pasa cuando uno se cuelga.",
      "Usar magics esenciales: %timeit, %%time, %run, %load, %matplotlib inline, %debug, %who, %xmode.",
      "Conectar un kernel específico a un notebook (ipykernel install --user --name <env>) sin pelearse con el venv equivocado.",
      "Debuggear una excepción con %debug y pdb (n, s, c, q, p, l).",
      "Profilar código lento con %timeit (microbenchmark) y %prun (line profiler) para decidir dónde optimizar."
    ],
    "topics": [
      "Kernel ↔ frontend ↔ servidor",
      "Modo comando vs modo edición + atajos",
      "Magics line (%) vs cell (%%)",
      "%timeit y %%time",
      "%debug + pdb",
      "%prun y %lprun",
      "Registro de kernels por venv"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Atajos sin mouse. Crea 5 celdas, navega solo con teclado: convierte 2 a markdown, ejecuta todo en orden, borra una, deshaz. Cronométrate.",
      "Registra tu kernel. Desde un venv recién creado: python -m ipykernel install --user --name ds-lab-001 --display-name 'DS Lab 001'. Abre Jupyter, selecciona ese kernel, verifica con import sys; sys.executable.",
      "Benchmark vectorización. Con %timeit, compara sumar range(10_000) con un for vs np.arange(10_000).sum(). Anota cuántas veces más rápido es NumPy.",
      "Post-mortem. Provoca un ZeroDivisionError, luego ejecuta %debug en la siguiente celda y navega el stack con u/d, inspecciona variables con p.",
      "Profila una función. Escribe una función que ordene una lista 1000 veces con sort burbuja. Ejecuta %prun -s cumulative tu_func(). Identifica la línea más cara."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/002-jupyter-y-jupyterlab-kernels-magics-debugging-profiling/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/003-git-y-github-para-data-scientists",
    "number": 3,
    "slug": "003-git-y-github-para-data-scientists",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Git y GitHub para data scientists",
    "description": "Que el alumno use git no como \"botón save\" sino como un sistema serio de versionado: commits atómicos con mensajes útiles, branches por feature, PRs con review, y resolución de conflictos sin pánico.",
    "level": "Basico",
    "duration": "120 min",
    "theory": "Que el alumno use git no como \"botón save\" sino como un sistema serio de versionado: commits atómicos con mensajes útiles, branches por feature, PRs con review, y resolución de conflictos sin pánico. Adicionalmente: ignorar correctamente los archivos típicos de DS (datos pesados, notebooks con output, secrets).",
    "outcomes": [
      "Inicializar un repo, hacer commits atómicos con mensajes en formato convencional.",
      "Trabajar con branches: crear, cambiar, mergear y resolver un conflicto sin perder código.",
      "Configurar .gitignore para un proyecto de DS (datos, .venv, secrets, outputs de notebooks).",
      "Abrir y revisar un PR en GitHub desde la línea de comandos con gh.",
      "Recuperar trabajo perdido con git reflog (la red de seguridad invisible)."
    ],
    "topics": [
      "Modelo de git: working tree → staging → repo → remote",
      "Commits atómicos + mensajes convencionales",
      "Branches y merge vs rebase",
      ".gitignore para data science",
      "Conflictos: anatomía y resolución",
      "Pull Requests + review en GitHub",
      "git reflog — la red de seguridad"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Repo desde cero. git init, crea 3 archivos (README.md, data.csv, notebook.ipynb), haz 3 commits con mensajes en formato tipo: descripción (feat/fix/docs/chore).",
      "Branch + conflicto. Crea rama feature/x, modifica una línea en README.md. Vuelve a main, modifica la misma línea distinto. Mergea, resuelve el conflicto a mano.",
      ".gitignore profesional. Genera uno que ignore: .venv/, __pycache__/, .ipynb_checkpoints/, .csv en data/raw/, .env, models/.pkl. Verifica con git status que no aparecen.",
      "PR desde la CLI. Crea repo en GitHub (con gh repo create), push, crea PR con gh pr create y descripción no trivial.",
      "Recuperación. Borra una rama con commits. Recupera el HEAD con git reflog + git checkout <sha> + git switch -c rescate."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/003-git-y-github-para-data-scientists/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/004-estructura-reproducible-de-proyecto-cookiecutter-data-science",
    "number": 4,
    "slug": "004-estructura-reproducible-de-proyecto-cookiecutter-data-science",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Estructura reproducible de proyecto (cookiecutter-data-science)",
    "description": "Que el alumno deje de crear proyectos como \"una carpeta con notebooks\" y empiece a usar una estructura estándar que separa código, datos, modelos, notebooks de exploración y documentación.",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno deje de crear proyectos como \"una carpeta con notebooks\" y empiece a usar una estructura estándar que separa código, datos, modelos, notebooks de exploración y documentación. Esto no es estética — es lo que permite que un compañero entienda el proyecto en 5 minutos y que el código viva más allá del notebook donde nació.",
    "outcomes": [
      "Generar un proyecto con la plantilla cookiecutter-data-science (CCDS v2).",
      "Justificar la separación data/raw (inmutable) ↔ data/interim ↔ data/processed.",
      "Mover código de un notebook a src/ cuando deja de ser exploratorio.",
      "Documentar dependencias en pyproject.toml (no en requirements.txt suelto).",
      "Reconocer los olores de un proyecto mal estructurado (notebooks con números 01/02/03, código duplicado, datos en git)."
    ],
    "topics": [
      "Estructura CCDS v2",
      "data/raw es sagrado",
      "notebooks/ vs src/",
      "pyproject.toml como fuente de verdad de deps",
      "Makefile como interfaz",
      "Olores típicos"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Genera un proyecto CCDS. pipx run cookiecutter https://github.com/drivendataorg/cookiecutter-data-science con nombre ds-lab-004. Explora la estructura.",
      "Mueve código a src/. Toma una función de un notebook tuyo previo y muévela a src/<proyecto>/features.py. Importa desde el notebook con from <proyecto>.features import ….",
      "Convierte requirements.txt a pyproject.toml (sección [project.dependencies]).",
      "Refactoriza un notebook caótico. Toma uno con bloques copy-paste y extrae 2 funciones a src/.",
      "Lista 5 olores en un repo público que conozcas y propón cómo arreglarlos."
    ],
    "codeExamples": [
      {
        "id": "parte-0-prerrequisitos/004-estructura-reproducible-de-proyecto-cookiecutter-data-science-code-1",
        "title": "Bloque 1",
        "explanation": "Código incluido en el material de la clase.",
        "schema": "python · 2 líneas",
        "language": "python",
        "code": "def normalize(x):\n    return (x - x.mean()) / x.std()"
      },
      {
        "id": "parte-0-prerrequisitos/004-estructura-reproducible-de-proyecto-cookiecutter-data-science-code-2",
        "title": "Bloque 2",
        "explanation": "Código incluido en el material de la clase.",
        "schema": "python · 9 líneas",
        "language": "python",
        "code": "import numpy as np\nimport pandas as pd\nfrom mi_proyecto.features import normalize\n\ndef test_normalize_media_cero():\n    s = pd.Series([1.0, 2.0, 3.0, 4.0, 5.0])\n    result = normalize(s)\n    assert np.isclose(result.mean(), 0.0)\n    assert np.isclose(result.std(), 1.0)"
      }
    ],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/004-estructura-reproducible-de-proyecto-cookiecutter-data-science/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/005-vs-code-cursor-para-python-y-jupyter",
    "number": 5,
    "slug": "005-vs-code-cursor-para-python-y-jupyter",
    "partSlug": "parte-0-prerrequisitos",
    "title": "VS Code / Cursor para Python y Jupyter",
    "description": "Que el alumno deje de usar VS Code como Notepad y lo configure como un IDE serio para Python + Jupyter: selector de intérprete, debugger gráfico, linter (ruff), formatter (ruff format), tests integrados y notebooks edit…",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno deje de usar VS Code como Notepad y lo configure como un IDE serio para Python + Jupyter: selector de intérprete, debugger gráfico, linter (ruff), formatter (ruff format), tests integrados y notebooks editables. Bonus: cuándo conviene Cursor (VS Code + IA integrada).",
    "outcomes": [
      "Configurar VS Code con la extensión Python + Jupyter, seleccionando el intérprete del venv del proyecto.",
      "Debuggear un script Python paso a paso desde el panel gráfico (breakpoints, watch, call stack).",
      "Editar y ejecutar notebooks sin Jupyter web — con autocompletado, type hints y debug de celda.",
      "Configurar ruff como linter + formatter (reemplaza black + isort + flake8 en un solo tool).",
      "Decidir cuándo usar Cursor (idéntico a VS Code + IA integrada con autorización por chat)."
    ],
    "topics": [
      "Selección de intérprete por workspace",
      "Debugger gráfico vs print",
      "Notebooks nativos en VS Code",
      "ruff = linter + formatter en uno",
      "Tests integrados (pytest)",
      "Extensiones esenciales",
      "Cursor: cuándo sí"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Selecciona intérprete. En VS Code: Ctrl+Shift+P → \"Python: Select Interpreter\" → elige el del .venv del proyecto. Verifica con print(sys.executable) en una celda.",
      "Debug paso a paso. Toma un script con un bug, pon breakpoint (F9), ejecuta con F5, navega con F10 (next), F11 (step in), Shift+F11 (step out). Inspecciona variables en panel.",
      "Configura ruff. En pyproject.toml: [tool.ruff] con line-length = 100, [tool.ruff.lint] con select = [\"E\", \"F\", \"I\", \"UP\"]. Habilita format on save.",
      "Edita un notebook. Abre notebook.ipynb en VS Code, ejecuta una celda, comprueba que el autocompletado funciona con type hints de pandas.",
      "Tests con un click. Instala pytest, crea tests/test_simple.py con 2 tests (uno OK, uno FAIL). Usa el panel \"Testing\" para correr/debuggear."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/005-vs-code-cursor-para-python-y-jupyter/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo",
    "number": 6,
    "slug": "006-python-tipos-estructuras-control-de-flujo",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Python: tipos, estructuras, control de flujo",
    "description": "Refrescar (o instalar) los cimientos de Python que el resto del programa asume: tipos primitivos, las 4 estructuras built-in (list, tuple, set, dict), control de flujo (if/for/while), unpacking, truthiness y la diferenc…",
    "level": "Basico",
    "duration": "120 min",
    "theory": "Refrescar (o instalar) los cimientos de Python que el resto del programa asume: tipos primitivos, las 4 estructuras built-in (list, tuple, set, dict), control de flujo (if/for/while), unpacking, truthiness y la diferencia entre mutables e inmutables — la fuente del 90% de bugs sutiles.",
    "outcomes": [
      "Diferenciar tipos mutables (list, dict, set) vs inmutables (tuple, str, int, frozenset) y predecir el efecto en asignaciones.",
      "Usar las 4 estructuras eligiendo bien: list (orden + duplicados), tuple (inmutable, rápida), set (unicidad), dict (lookup O(1)).",
      "Aplicar unpacking en for, returns múltiples y *args/**kwargs.",
      "Evaluar truthiness correctamente ([], {}, 0, '', None son falsy; el resto es truthy).",
      "Identificar el bug del default mutable en funciones (def f(x, lst=[])) y por qué es trampa."
    ],
    "topics": [
      "Mutables vs inmutables",
      "list, tuple, set, dict — cuándo cada uno",
      "Iteración: for, enumerate, zip",
      "Unpacking y starred expressions",
      "Truthiness y operadores and/or",
      "Default mutables: el clásico"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Cuenta palabras. Dado un texto, devuelve un dict[str, int] con frecuencias. Sin usar Counter.",
      "Unique con orden. Recibe list[int], devuelve la lista de únicos manteniendo el orden de primera aparición.",
      "Reproduce el bug del default mutable. Escribe def add(item, target=[]), llámala 3 veces con add('x'). Observa. Explica por qué y arregla.",
      "Top-K palabras. Mismo texto del ejercicio 1, devuelve las 5 más frecuentes ordenadas por frecuencia descendente.",
      "Grupos por inicial. Dado list[str], devuelve dict[str, list[str]] agrupando por primera letra (case-insensitive)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/007-comprehensions-y-generadores",
    "number": 7,
    "slug": "007-comprehensions-y-generadores",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Comprehensions y generadores",
    "description": "Que el alumno escriba código Python idiomático: list/dict/set comprehensions en vez de for+append, generadores cuando el dataset no cabe en memoria, y entienda la diferencia fundamental entre construir una lista y produ…",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno escriba código Python idiomático: list/dict/set comprehensions en vez de for+append, generadores cuando el dataset no cabe en memoria, y entienda la diferencia fundamental entre construir una lista y producir un iterable perezoso.",
    "outcomes": [
      "Convertir loops for+append a list/dict/set comprehensions sin perder legibilidad.",
      "Usar generadores (yield y generator expressions) para procesar datos que no caben en RAM.",
      "Distinguir [x for x in xs] (lista) vs (x for x in xs) (generador): memoria y consumo.",
      "Encadenar generadores con itertools (chain, islice, takewhile, groupby).",
      "Identificar cuándo NO usar comprehension (lógica compleja, side effects, debug difícil)."
    ],
    "topics": [
      "List comprehension: [expr for x in xs if cond]",
      "Dict/set comprehensions",
      "Generator expressions: (expr for x in xs)",
      "Funciones generadoras con yield",
      "itertools — la caja de herramientas",
      "Comprehension vs loop: cuándo NO"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "De for a comprehension. Toma 3 loops for+append (cuadrados, filtra pares, mapea a strings) y conviértelos.",
      "Generador de Fibonacci infinito. Función con yield que produce Fibonacci. Úsala con itertools.islice para tomar los primeros 20.",
      "Memoria: lista vs generador. Mide RAM (con tracemalloc) de sum([ii for i in range(10_000_000)]) vs sum(ii for i in range(10_000_000)). Reporta la diferencia.",
      "Procesa CSV línea por línea. Lee un archivo grande con yield línea por línea, filtra por una condición, cuenta sin cargar todo en memoria.",
      "Pivot con dict comprehension. Dada list[tuple[str, int]] (nombre, puntaje), construye dict[str, list[int]] agrupando puntajes por nombre."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/007-comprehensions-y-generadores/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/008-funciones-args-kwargs-lambdas-closures",
    "number": 8,
    "slug": "008-funciones-args-kwargs-lambdas-closures",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Funciones: args, kwargs, lambdas, closures",
    "description": "Que el alumno use funciones como ciudadanos de primera clase: pasarlas como argumento, retornarlas, escribir lambdas cuando aportan, y entender closures — la base de los decoradores que verán más adelante.",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno use funciones como ciudadanos de primera clase: pasarlas como argumento, retornarlas, escribir lambdas cuando aportan, y entender closures — la base de los decoradores que verán más adelante. Sin esto, el código pandas/sklearn parece magia.",
    "outcomes": [
      "Definir funciones con argumentos posicionales, keyword-only, *args y **kwargs.",
      "Pasar funciones como argumento (callbacks: sorted(xs, key=fn), df.apply(fn)).",
      "Usar lambdas donde son legibles (callbacks cortos) y evitarlas donde no (lógica).",
      "Explicar y escribir closures (función que captura variables del scope exterior).",
      "Anticipar la diferencia entre args y , args (keyword-only marker)."
    ],
    "topics": [
      "Argumentos: posicional, keyword, default",
      "*args y **kwargs",
      "Keyword-only con * separador",
      "Funciones como objetos",
      "Lambdas: dónde sí y dónde no",
      "Closures: capturando scope"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Función con todo. Define f(a, b=10, *args, c, **kwargs). Llámala de 3 formas distintas que sean válidas. Identifica qué llamadas son inválidas y por qué.",
      "sorted con key. Dada list[dict] de personas, ordena por edad (asc) y por nombre alfabético. Usa lambda primero, luego operator.itemgetter.",
      "Closure contador. Escribe make_counter() que retorna una función que cada vez que se llama incrementa y retorna un contador interno. ¿Por qué funciona?",
      "Memoización manual. Implementa un decorador @memoize usando closure + dict. Aplícalo a Fibonacci recursivo y mide el speedup con %timeit.",
      "Compose. Escribe compose(f, g, h) que retorna una función equivalente a lambda x: f(g(h(x)))."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/008-funciones-args-kwargs-lambdas-closures/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/009-manejo-de-excepciones-y-context-managers",
    "number": 9,
    "slug": "009-manejo-de-excepciones-y-context-managers",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Manejo de excepciones y context managers",
    "description": "Que el alumno maneje excepciones con criterio (sin except: pass), construya jerarquías de excepciones propias cuando aporta, y use context managers (with) — tanto los built-in como propios con @contextmanager — para gar…",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno maneje excepciones con criterio (sin except: pass), construya jerarquías de excepciones propias cuando aporta, y use context managers (with) — tanto los built-in como propios con @contextmanager — para garantizar limpieza de recursos. Sin esto, el código de carga de datos es una bomba de relojería.",
    "outcomes": [
      "Diferenciar los 3 tipos de errores (Syntax, runtime exceptions, logical) y dónde se manejan.",
      "Capturar excepciones específicas (except ValueError, no except:) y propagar las que no sabes manejar.",
      "Crear una excepción propia heredando de la jerarquía estándar (class DatasetCorruptoError(Exception)).",
      "Usar with para archivos, sesiones HTTP, transacciones DB.",
      "Escribir un context manager propio con @contextmanager (timer, supress, change_dir)."
    ],
    "topics": [
      "Jerarquía de excepciones built-in",
      "try/except/else/finally",
      "Capturar específico, no genérico",
      "Excepciones propias",
      "Context managers: protocolo __enter__/__exit__",
      "@contextmanager de contextlib"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Captura específica. Escribe una función parse_int_safe(s, default=0) que use try/except solo para ValueError. Demuestra que no esconde otros errores (ej. TypeError si pasas un dict).",
      "Excepción propia. Define class DatasetCorruptoError(Exception) con un atributo linea. Lanzala desde una función cargar_csv cuando una línea no tenga el número correcto de columnas.",
      "with para archivo. Lee un archivo línea por línea contando palabras. Compara con la versión sin with (manual open/close) y muestra qué pasa si hay excepción a mitad.",
      "Context manager propio: timer. Con @contextmanager, escribe with timer(\"carga\"): que imprima cuánto duró el bloque.",
      "Context manager: change_dir. with cd(\"/tmp\"): cambia de directorio al entrar y vuelve al salir — incluso si hay excepción."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/009-manejo-de-excepciones-y-context-managers/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/010-oop-basico-dataclasses-herencia",
    "number": 10,
    "slug": "010-oop-basico-dataclasses-herencia",
    "partSlug": "parte-0-prerrequisitos",
    "title": "OOP básico, dataclasses, herencia",
    "description": "Que el alumno escriba clases cuando aportan (no por hábito Java), use @dataclass para records sin boilerplate, entienda herencia con criterio (preferir composición), y conozca los métodos dunder más usados (__repr__, __…",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno escriba clases cuando aportan (no por hábito Java), use @dataclass para records sin boilerplate, entienda herencia con criterio (preferir composición), y conozca los métodos dunder más usados (__repr__, __eq__, __lt__, __len__).",
    "outcomes": [
      "Definir clases con __init__, atributos de instancia y métodos.",
      "Usar @dataclass para records inmutables/mutables sin escribir __init__/__repr__/__eq__.",
      "Heredar y sobreescribir métodos con super().",
      "Implementar dunders esenciales: __repr__, __str__, __eq__, __lt__, __len__, __iter__.",
      "Decidir entre clase, dataclass o NamedTuple según el caso."
    ],
    "topics": [
      "Clase mínima: __init__ + atributos + métodos",
      "@dataclass(frozen=True)",
      "Herencia + super()",
      "Composición > herencia",
      "Métodos dunder",
      "dataclass vs NamedTuple vs TypedDict"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Clase Punto. Define Punto(x, y) con __repr__, __eq__, distancia al origen y __add__ para sumar puntos.",
      "Dataclass Estudiante. @dataclass con nombre, notas: list[float], método promedio(). Crea 3 instancias, ordena por promedio.",
      "Frozen Vector. @dataclass(frozen=True) para un vector 2D inmutable. Intenta modificar un atributo y observa la excepción.",
      "Herencia. Animal con hablar() → 'genérico'. Perro(Animal) que sobreescribe a 'guau'. Gato(Animal) a 'miau'.",
      "Composición. Coche que tiene un Motor (composición) en vez de heredar de Motor. Justifica por qué."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/010-oop-basico-dataclasses-herencia/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/011-pathlib-lectura-y-escritura-de-archivos",
    "number": 11,
    "slug": "011-pathlib-lectura-y-escritura-de-archivos",
    "partSlug": "parte-0-prerrequisitos",
    "title": "pathlib, lectura y escritura de archivos",
    "description": "Que el alumno deje de usar os.path.join + strings y adopte pathlib.Path — API orientada a objetos, multiplataforma (Windows/Unix), con métodos legibles para todas las operaciones de filesystem que hace todo el tiempo en…",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno deje de usar os.path.join + strings y adopte pathlib.Path — API orientada a objetos, multiplataforma (Windows/Unix), con métodos legibles para todas las operaciones de filesystem que hace todo el tiempo en DS (leer CSV, listar archivos, crear carpetas).",
    "outcomes": [
      "Construir paths con Path(...) / 'subdir' / 'file.csv' (operador /).",
      "Leer/escribir archivos texto y binarios con métodos de Path (read_text, write_bytes).",
      "Listar y filtrar archivos con iterdir, glob, rglob (recursivo).",
      "Crear/eliminar estructuras de directorios sin pelear con os.makedirs(exist_ok=True).",
      "Manejar rutas relativas vs absolutas y entender __file__."
    ],
    "topics": [
      "Path vs strings",
      "Operador / para componer",
      "read_text / write_text / read_bytes",
      "glob y rglob",
      "mkdir(parents=True, exist_ok=True)",
      "Path(__file__).parent y resolve()"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Construye una ruta multiplataforma. Dado Path.home() / 'datos' / '2026' / 'enero.csv', imprime cómo se ve en Windows vs Unix.",
      "Lista CSVs. En una carpeta con archivos mixtos (.csv, .txt, .py), lista solo los .csv ordenados por tamaño.",
      "Búsqueda recursiva. En un árbol de carpetas, encuentra todos los .py que contengan la palabra TODO en su contenido.",
      "Escribe + lee. Genera 3 archivos txt con write_text, léelos con read_text, concaténalos en uno solo.",
      "Ruta del script. Escribe un script que cargue un dataset que vive al lado del script (no del cwd), usando Path(__file__).parent / 'data.csv'."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/011-pathlib-lectura-y-escritura-de-archivos/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/012-logging",
    "number": 12,
    "slug": "012-logging",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Logging",
    "description": "Que el alumno deje de usar print para debug y aprenda el módulo logging estándar: niveles (DEBUG/INFO/WARNING/ERROR/CRITICAL), handlers (consola, archivo), formatters, y configuración por módulo.",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno deje de usar print para debug y aprenda el módulo logging estándar: niveles (DEBUG/INFO/WARNING/ERROR/CRITICAL), handlers (consola, archivo), formatters, y configuración por módulo. Es la diferencia entre código que se debuggea reiniciando el notebook y código que se debuggea leyendo logs.",
    "outcomes": [
      "Diferenciar los 5 niveles de logging y cuándo usar cada uno.",
      "Configurar un logger con logging.basicConfig y entender por qué basicConfig solo funciona una vez.",
      "Crear loggers por módulo con logging.getLogger(__name__).",
      "Agregar handlers: uno a consola (INFO+), otro a archivo (DEBUG+).",
      "Formatear logs con timestamp, módulo y nivel."
    ],
    "topics": [
      "print vs logging",
      "Niveles: DEBUG/INFO/WARNING/ERROR/CRITICAL",
      "Logger jerárquico por módulo",
      "Handlers: consola, archivo, rotating",
      "Formatters",
      "logging.basicConfig y sus límites"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Reemplaza prints. Toma una función con 5 prints y conviértelos a logger con niveles apropiados.",
      "Logger por módulo. Crea 2 archivos .py que cada uno usa getLogger(__name__). Configura el root logger una vez; verifica que ambos heredan.",
      "Handler doble. Configura: consola = INFO+, archivo app.log = DEBUG+. Genera 5 logs de niveles distintos y verifica qué aparece en cada destino.",
      "Formato con timestamp. Cambia el formato a '%(asctime)s [%(levelname)s] %(name)s: %(message)s'. Inspecciona output.",
      "Logger en notebook. Pelea con basicConfig no recordando estado entre reinicios — usa dictConfig o force=True."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/012-logging/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/013-type-hints-y-mypy",
    "number": 13,
    "slug": "013-type-hints-y-mypy",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Type hints y mypy",
    "description": "Que el alumno anote tipos en sus funciones y dataclasses — no por dogma, sino porque permiten que el IDE autocomplete bien, que mypy detecte bugs antes de runtime, y que el lector entienda la intención.",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno anote tipos en sus funciones y dataclasses — no por dogma, sino porque permiten que el IDE autocomplete bien, que mypy detecte bugs antes de runtime, y que el lector entienda la intención. Tipos como documentación verificable.",
    "outcomes": [
      "Anotar funciones con tipos en parámetros y retorno (def f(x: int) -> str).",
      "Usar tipos compuestos: list[int], dict[str, float], tuple[int, str], Optional[X], X | None.",
      "Definir tipos personalizados con TypeAlias y Protocol (structural typing).",
      "Ejecutar mypy sobre código y interpretar sus errores.",
      "Reconocer cuándo type hints aportan (APIs públicas, data classes) y cuándo no (notebooks exploratorios)."
    ],
    "topics": [
      "Sintaxis básica: x: int, -> bool",
      "Tipos compuestos modernos (3.9+): list[int]",
      "Optional[X] y `X",
      "Literal, TypedDict, Protocol",
      "mypy: instalar y correr",
      "reveal_type(x) y # type: ignore",
      "Cuándo SÍ y cuándo NO"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Anota una función. Toma una función de los ejercicios de clase 008 (sin tipos) y anótala completa.",
      "Optional vs default. Distingue def f(x: int = 0) (default 0) de def f(x: int | None = None) (puede no haber valor).",
      "TypedDict. Define class PersonaDict(TypedDict) con nombre: str, edad: int. Úsala como tipo de un parámetro.",
      "Corre mypy. Instala mypy, créate un archivo con un bug de tipo intencional (def f(x: int) -> str: return x + 1) y corre mypy archivo.py. Lee y explica el error.",
      "Protocol. Define class TienePromedio(Protocol) con método promedio() -> float. Acepta cualquier clase que lo implemente (duck typing tipado)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/013-type-hints-y-mypy/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/014-numpy-tipos-creacion-atributos",
    "number": 14,
    "slug": "014-numpy-tipos-creacion-atributos",
    "partSlug": "parte-0-prerrequisitos",
    "title": "NumPy: tipos, creación, atributos",
    "description": "Que el alumno entienda el modelo mental de un ndarray — bloque contiguo de memoria con shape, dtype y strides — y sepa crear arrays de las 6 formas más útiles (array, zeros, arange, linspace, random, desde lista).",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno entienda el modelo mental de un ndarray — bloque contiguo de memoria con shape, dtype y strides — y sepa crear arrays de las 6 formas más útiles (array, zeros, arange, linspace, random, desde lista). Sin este modelo, todo el rendimiento de NumPy parece magia.",
    "outcomes": [
      "Explicar por qué ndarray es 50–100× más rápido que list (memoria contigua + dtype fijo + sin overhead Python).",
      "Crear arrays con np.array, np.zeros, np.ones, np.full, np.arange, np.linspace.",
      "Inspeccionar un array con shape, dtype, ndim, size, nbytes, itemsize.",
      "Cambiar dtype explícitamente con astype y entender promociones implícitas (int + float = float).",
      "Generar arrays aleatorios reproducibles con np.random.default_rng(seed)."
    ],
    "topics": [
      "ndarray: memoria contigua + dtype fijo",
      "Creación: array, zeros, arange, linspace",
      "dtype: int8/16/32/64, float32/64, bool",
      "Atributos: shape, dtype, ndim, size, nbytes",
      "astype y promoción de tipos",
      "random moderno: default_rng(seed)"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Memoria. Crea list(range(1_000_000)) y np.arange(1_000_000). Compara sys.getsizeof y arr.nbytes. Calcula el ratio.",
      "Las 6 formas. Crea: vector 100 ceros, matriz 5×5 unos, vector 0..1 con 50 puntos equiespaciados, matriz 3×3 de 7s, vector de 100 aleatorios uniformes [0,1).",
      "Bug de dtype. Crea np.array([100, 200, 50], dtype=np.int8) y suma 200 a cada elemento. Observa el resultado y explica.",
      "Diagnóstico. Dado un array, escribe una función que imprima shape, dtype, ndim, size, nbytes y memoria humana (KB/MB).",
      "Random reproducible. Genera 1000 normales N(0,1) con seed=42. Calcula media y std. Repite — debe dar exactamente lo mismo."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/014-numpy-tipos-creacion-atributos/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/015-numpy-ufuncs-y-vectorizacion",
    "number": 15,
    "slug": "015-numpy-ufuncs-y-vectorizacion",
    "partSlug": "parte-0-prerrequisitos",
    "title": "NumPy: ufuncs y vectorización",
    "description": "Que el alumno abandone los for loops sobre arrays NumPy y use ufuncs (universal functions) para operaciones elementwise — la fuente real del speedup.",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno abandone los for loops sobre arrays NumPy y use ufuncs (universal functions) para operaciones elementwise — la fuente real del speedup. Ufuncs son C compilado vectorizado; un for Python sobre array es lo peor de ambos mundos.",
    "outcomes": [
      "Identificar una ufunc (np.add, np.multiply, np.sin, np.exp, np.log, comparadores).",
      "Reemplazar un for+append por una expresión vectorizada y medir el speedup.",
      "Usar el parámetro out= para escribir el resultado in-place (evita allocar memoria extra).",
      "Combinar ufuncs con operadores aritméticos (+, -, *, /, **).",
      "Reconocer las trampas de la vectorización (overflow, NaN propagación, división por cero)."
    ],
    "topics": [
      "¿Qué es una ufunc?",
      "Ufuncs unarias y binarias",
      "Operadores → ufuncs",
      "out= para in-place",
      "Trampas: overflow, NaN, inf, división por cero",
      "np.where(cond, a, b)"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Benchmark. Calcula [xx + 2x + 1 for x in range(1_000_000)] vs arrarr + 2arr + 1. Mide con %timeit.",
      "Logaritmo y exponencial. Con np.exp y np.log, verifica que log(exp(x)) ≈ x para 1000 valores. Reporta el error máximo.",
      "In-place vs alloc. arr = arr * 2 + 1 vs np.multiply(arr, 2, out=arr); np.add(arr, 1, out=arr). Compara tracemalloc.",
      "np.where ternario. Dado un array de notas, crea otro array con 'aprobado' si nota >= 4, 'reprobado' si no.",
      "Trampa NaN. Crea np.array([1, 2, np.nan, 4]).sum() y .mean(). Compara con np.nansum y np.nanmean."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/015-numpy-ufuncs-y-vectorizacion/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/016-numpy-agregaciones",
    "number": 16,
    "slug": "016-numpy-agregaciones",
    "partSlug": "parte-0-prerrequisitos",
    "title": "NumPy: agregaciones",
    "description": "Que el alumno reduzca arrays a estadísticos (sum, mean, std, percentile, min, max) controlando el axis correcto — la fuente del 50% de los bugs de pandas/sklearn cuando alguien se confunde de eje.",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno reduzca arrays a estadísticos (sum, mean, std, percentile, min, max) controlando el axis correcto — la fuente del 50% de los bugs de pandas/sklearn cuando alguien se confunde de eje. También: variantes nan* y reducciones acumulativas.",
    "outcomes": [
      "Calcular sum, mean, std, var, median, percentile sobre arrays.",
      "Controlar el eje con axis=0 (a lo largo de filas, da resultado por columna) y axis=1 (a lo largo de columnas, da por fila).",
      "Usar variantes nan* (nansum, nanmean, etc.) cuando hay datos faltantes.",
      "Reducciones acumulativas con cumsum y cumprod.",
      "Encontrar índice del min/max con argmin/argmax."
    ],
    "topics": [
      "Reducciones básicas",
      "Eje: el bug más común",
      "Variantes NaN-aware",
      "Acumulativas",
      "argmin/argmax",
      "all y any"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Promedio por columna. Dada matriz 100×4 de ventas (filas=día, cols=tienda), calcula la media por tienda y por día.",
      "Estadísticos completos. Para un array de 1000 normales, reporta mean, std, median, p25, p75, min, max.",
      "Con NaN. Inserta 50 NaN aleatorios en el array anterior. Compara mean (propaga) vs nanmean.",
      "Cumsum. Genera array de retornos diarios aleatorios. Calcula el precio acumulado con cumprod(1+r).",
      "Mejor tienda. Con la matriz del ejercicio 1, usa argmax(axis=0) para encontrar el día de mayor venta de cada tienda."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/016-numpy-agregaciones/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/017-numpy-broadcasting",
    "number": 17,
    "slug": "017-numpy-broadcasting",
    "partSlug": "parte-0-prerrequisitos",
    "title": "NumPy: broadcasting",
    "description": "Que el alumno internalice las reglas de broadcasting — el mecanismo por el que NumPy operó arrays de shapes distintos sin copiar datos.",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno internalice las reglas de broadcasting — el mecanismo por el que NumPy operó arrays de shapes distintos sin copiar datos. Es lo que hace que M - M.mean(axis=0) centrado por columna sea una línea, no un bucle anidado.",
    "outcomes": [
      "Recitar las 3 reglas de broadcasting (alinea por la derecha, dim 1 estira, falla si no es 1 ni igual).",
      "Predecir la shape del resultado de una operación entre arrays de shapes distintos.",
      "Centrar y escalar matrices por fila/columna sin loops.",
      "Usar np.newaxis (o None) para promover un vector a matriz fila/columna.",
      "Diagnosticar un ValueError: operands could not be broadcast together leyendo las shapes."
    ],
    "topics": [
      "Las 3 reglas",
      "Vector + matriz",
      "np.newaxis / None",
      "Caso canónico: centrar/escalar",
      "Outer product sin loop",
      "ValueError común: \"operands could not be broadcast together\""
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Predice antes de ejecutar. Para shapes (3,), (3,1), (1,3), (2,3,4) × (4,), predice la shape del resultado. Verifica.",
      "Estandariza features. Matriz 100×5 aleatoria. Resta media por columna y divide por std por columna en una línea.",
      "Outer product. Vectores a=[1,2,3], b=[10,20,30,40]. Calcula la matriz outer (3×4) sin np.outer, solo broadcasting.",
      "Distance matrix. Dados 5 puntos 2D, construye matriz 5×5 de distancias euclídeas entre pares — sin cdist, solo broadcasting.",
      "Diagnostica error. Intenta np.ones((3,4)) + np.ones((4,3)). Lee el ValueError y explica."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/017-numpy-broadcasting/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/018-numpy-boolean-masks-y-fancy-indexing",
    "number": 18,
    "slug": "018-numpy-boolean-masks-y-fancy-indexing",
    "partSlug": "parte-0-prerrequisitos",
    "title": "NumPy: boolean masks y fancy indexing",
    "description": "Que el alumno seleccione, filtre y modifique sub-arrays de tres formas: slicing (visto), máscaras booleanas (arr[arr > 0]) y fancy indexing (arr[[0, 3, 5]]).",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno seleccione, filtre y modifique sub-arrays de tres formas: slicing (visto), máscaras booleanas (arr[arr > 0]) y fancy indexing (arr[[0, 3, 5]]). Saber cuál devuelve vista vs copia y cuándo cada uno es la herramienta correcta.",
    "outcomes": [
      "Filtrar elementos con máscaras booleanas: arr[arr > 0], arr[(a > 0) & (a < 10)].",
      "Combinar máscaras con &, |, ~ — NO con and/or (no vectorizan).",
      "Seleccionar por índices con fancy indexing: arr[[0, 3, 5]] o arr[idx_array].",
      "Modificar in-place con máscara: arr[arr < 0] = 0 (clipping).",
      "Diferenciar vista vs copia: slicing es vista; fancy indexing y máscara son copia."
    ],
    "topics": [
      "Comparaciones elementwise → arrays bool",
      "np.count_nonzero, np.sum sobre bool",
      "Combinar máscaras con &, `",
      "Fancy indexing con array de índices",
      "Vista vs copia",
      "np.where(cond) (sin alternativas)"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Cuenta días lluviosos. Dado array de 365 días con precipitación (mm), cuenta cuántos tuvieron >5mm.",
      "Estadísticos por máscara. Calcula precipitación media solo en días lluviosos (>0mm).",
      "AND/OR combinados. Días entre 1 y 10 mm. Días <1 o >50 mm.",
      "Clipping. Reemplaza valores negativos por 0 in-place (arr[arr < 0] = 0).",
      "Vista vs copia. Demuestra con un experimento que arr[:5] modifica el original pero arr[arr > 0] no."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/018-numpy-boolean-masks-y-fancy-indexing/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/019-numpy-ordenamiento-y-busqueda",
    "number": 19,
    "slug": "019-numpy-ordenamiento-y-busqueda",
    "partSlug": "parte-0-prerrequisitos",
    "title": "NumPy: ordenamiento y búsqueda",
    "description": "Que el alumno ordene arrays con criterio: sort vs argsort, ordenamiento por eje, partial sort con partition, y búsqueda binaria con searchsorted.",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno ordene arrays con criterio: sort vs argsort, ordenamiento por eje, partial sort con partition, y búsqueda binaria con searchsorted. Útil para top-K, rankings, alineación de series.",
    "outcomes": [
      "Ordenar con np.sort(arr) (devuelve copia) y arr.sort() (in-place).",
      "Obtener índices del orden con argsort — base de top-K y rankings.",
      "Ordenar por eje en matrices con axis=0 o axis=1.",
      "Top-K eficiente con np.partition (no ordena completo, solo separa).",
      "Búsqueda binaria con np.searchsorted en arrays ordenados (O(log n))."
    ],
    "topics": [
      "np.sort vs arr.sort()",
      "argsort: el truco del top-K",
      "Ordenamiento por eje",
      "np.partition para top-K",
      "np.searchsorted — binaria O(log n)",
      "np.unique"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Top-10. Dado array de 1M puntajes, obtén los 10 más altos. Compara np.sort()[-10:] vs np.partition.",
      "Ranking. Con argsort, asigna a cada estudiante su ranking (1 = mejor).",
      "Ordena matriz por columna. Matriz 10×5; ordena cada columna por su valor.",
      "Mediana por bisect. Implementa una función que dado un valor v y un array ordenado, devuelve su posición percentil usando searchsorted.",
      "np.unique con cuentas. Dado array de categorías, obtén valores únicos y sus frecuencias."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/019-numpy-ordenamiento-y-busqueda/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/020-numpy-algebra-lineal-con-numpy-linalg",
    "number": 20,
    "slug": "020-numpy-algebra-lineal-con-numpy-linalg",
    "partSlug": "parte-0-prerrequisitos",
    "title": "NumPy: álgebra lineal con numpy.linalg",
    "description": "Que el alumno opere con vectores y matrices al nivel necesario para entender ML: producto punto, multiplicación matricial, inversa, sistema de ecuaciones (solve), descomposiciones (SVD, eigen).",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno opere con vectores y matrices al nivel necesario para entender ML: producto punto, multiplicación matricial, inversa, sistema de ecuaciones (solve), descomposiciones (SVD, eigen). Saber cuándo no usar la inversa (lentitud + inestabilidad numérica).",
    "outcomes": [
      "Multiplicar vectores y matrices con @ (operador moderno) y np.dot.",
      "Resolver sistemas Ax = b con np.linalg.solve (NO con inv(A) @ b).",
      "Calcular norma, determinante, rango, traza.",
      "Computar SVD con np.linalg.svd y entender qué retorna.",
      "Calcular eigenvalores/eigenvectores con np.linalg.eig / eigh (simétrica)."
    ],
    "topics": [
      "@ operador (PEP 465): multiplicación matricial",
      "Producto punto vs producto matricial",
      "Resolver sistemas: solve vs inv",
      "Norma, det, rank, trace",
      "SVD — la factorización universal",
      "Eigen"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Producto punto. Dados dos vectores 100-dim aleatorios, calcula np.dot(a, b) y verifica que coincide con sum(a*b).",
      "Multiplicación matricial. (50, 30) @ (30, 20) → (50, 20). Verifica shapes y un elemento manualmente.",
      "Resuelve sistema. Genera A = (5,5) aleatoria, b = (5,), resuelve Ax = b con solve. Verifica A @ x ≈ b.",
      "Inv vs solve benchmark. Para A (1000,1000) y b (1000,), mide tiempo de inv(A) @ b vs solve(A, b). Reporta speedup.",
      "SVD de matriz baja rank. Crea M = u @ v.T (rank 1). Calcula SVD y observa que solo el primer valor singular es no-cero."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/020-numpy-algebra-lineal-con-numpy-linalg/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/021-numpy-aleatoriedad-y-semillas",
    "number": 21,
    "slug": "021-numpy-aleatoriedad-y-semillas",
    "partSlug": "parte-0-prerrequisitos",
    "title": "NumPy: aleatoriedad y semillas",
    "description": "Que el alumno genere números aleatorios reproduciblemente con el API moderno (np.random.default_rng(seed)), use las distribuciones más comunes (uniforme, normal, Bernoulli, Poisson, exponencial), y entienda por qué la r…",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno genere números aleatorios reproduciblemente con el API moderno (np.random.default_rng(seed)), use las distribuciones más comunes (uniforme, normal, Bernoulli, Poisson, exponencial), y entienda por qué la reproducibilidad es no-negociable en ciencia de datos.",
    "outcomes": [
      "Crear un Generator con np.random.default_rng(seed) y usarlo para reproducibilidad.",
      "Generar muestras de uniforme, normal, integers, binomial, Poisson, exponencial.",
      "Permutar y muestrear sin/con reemplazo con permutation y choice.",
      "Reproducir un experimento exactamente con el mismo seed.",
      "Saber por qué np.random.seed() (API legacy) es deprecated en favor de Generator."
    ],
    "topics": [
      "np.random.default_rng(seed)",
      "Distribuciones continuas: uniform, normal, exponential, gamma, beta",
      "Distribuciones discretas: integers, binomial, poisson",
      "permutation y choice",
      "Reproducibilidad: por qué importa",
      "Múltiples generadores independientes"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Reproducibilidad. Crea 2 rngs con seed=42, genera 1000 normales con cada uno. Verifica que son idénticos.",
      "Distribuciones. Genera 10000 muestras de: uniforme [0,1], normal(5,2), exponential(λ=1/3), poisson(λ=4). Calcula media y std empírica y compara con teórica.",
      "Monte Carlo de π. Estima π lanzando puntos en un cuadrado 2×2 y contando cuántos caen dentro del círculo unitario. Compara con π real.",
      "Bootstrap. Dado un sample de 30 valores, estima la distribución de la media por bootstrap (1000 resamples con reemplazo).",
      "Permutación. Mezcla un array de 100 elementos con permutation. Verifica que es la misma cuando usas el mismo seed."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/021-numpy-aleatoriedad-y-semillas/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/022-pandas-series-y-dataframe",
    "number": 22,
    "slug": "022-pandas-series-y-dataframe",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: Series y DataFrame",
    "description": "Que el alumno entienda qué es una Series (ndarray + index) y un DataFrame (dict de Series alineadas por index), cómo se construyen desde 5 fuentes distintas, y por qué el index es el rasgo que distingue pandas de NumPy.",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno entienda qué es una Series (ndarray + index) y un DataFrame (dict de Series alineadas por index), cómo se construyen desde 5 fuentes distintas, y por qué el index es el rasgo que distingue pandas de NumPy.",
    "outcomes": [
      "Crear Series y DataFrames desde dict, lista de tuplas, arrays NumPy, CSV y desde otro DataFrame.",
      "Inspeccionar un DataFrame con head, tail, info, describe, dtypes, shape.",
      "Acceder a columnas como atributo (df.col) y como key (df['col']) — y saber cuándo cada uno falla.",
      "Modificar el index con set_index, reset_index, rename.",
      "Convertir Series ↔ DataFrame ↔ ndarray cuando sea necesario."
    ],
    "topics": [
      "Series = ndarray + index",
      "DataFrame = dict de Series alineadas",
      "Construcción desde 5 fuentes",
      ".loc vs .iloc vs []",
      "Index labels vs posición",
      "info y describe como first-look"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Series desde dict. Crea Series con población de 5 ciudades. Accede por label y por posición.",
      "DataFrame desde dict de listas. Construye DataFrame de 5 estudiantes (nombre, edad, nota). Inspecciona con info() y describe().",
      "Lee Palmer Penguins. pd.read_csv desde URL pública. Reporta shape, dtypes, % de NaN por columna.",
      "Index labeled. Setea species como index. Compara df.loc['Adelie'] vs df.iloc[0].",
      "Alineación automática. Crea 2 Series con index parcialmente solapado. Súmalas. Observa los NaN."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/022-pandas-series-y-dataframe/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/023-pandas-indexacion-loc-iloc-at-iat",
    "number": 23,
    "slug": "023-pandas-indexacion-loc-iloc-at-iat",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: indexación (loc, iloc, at, iat)",
    "description": "Que el alumno domine los 4 indexers de pandas y elija el correcto según el caso.",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno domine los 4 indexers de pandas y elija el correcto según el caso. El bug \"SettingWithCopyWarning\" y el bug del slicing por label inclusivo nacen aquí — saber qué indexer usar evita ambos.",
    "outcomes": [
      "Usar .loc[row_label, col_label] para acceso por etiqueta (inclusivo en slicing).",
      "Usar .iloc[row_pos, col_pos] para acceso por posición entera (exclusivo, como Python).",
      "Usar .at / .iat para acceso a un único valor (más rápido que loc/iloc).",
      "Evitar SettingWithCopyWarning usando .loc para asignar en una vista.",
      "Filtrar filas con boolean mask dentro de .loc: df.loc[df['edad'] > 30, 'nombre']."
    ],
    "topics": [
      "[] directo: shortcut con quirks",
      ".loc: por label, slicing inclusivo",
      ".iloc: por posición, slicing exclusivo (como Python)",
      ".at / .iat: single value",
      "Mask + loc para filtros con asignación",
      "SettingWithCopyWarning: qué es y cómo evitarlo"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Acceso simple. Carga penguins. Obtén la columna species con los 3 métodos: df.species, df['species'], df.loc[:, 'species'].",
      "loc inclusivo vs iloc exclusivo. Con index 0..N por default, compara df.loc[0:5] vs df.iloc[0:5]. ¿Cuántas filas devuelve cada uno?",
      "Filtro + columnas seleccionadas. Pingüinos Adelie machos con bill_length > 40: df.loc[(df.species=='Adelie') & (df.sex=='male') & (df.bill_length_mm > 40), ['species', 'island', 'bill_length_mm']].",
      "Asignación segura. Crea una columna is_big que sea True si body_mass_g > 4500, usando .loc.",
      "Provoca y arregla SettingWithCopyWarning. Slicea con df[df.x > 0] y modifica → ve warning. Hazlo con .loc → sin warning."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/023-pandas-indexacion-loc-iloc-at-iat/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/024-pandas-operaciones-y-alineacion",
    "number": 24,
    "slug": "024-pandas-operaciones-y-alineacion",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: operaciones y alineación",
    "description": "Que el alumno entienda cómo pandas alinea automáticamente por index en operaciones entre Series/DataFrames, cómo manejar NaN resultantes, y use apply/map para transformaciones custom (con consciencia de cuándo es lento).",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno entienda cómo pandas alinea automáticamente por index en operaciones entre Series/DataFrames, cómo manejar NaN resultantes, y use apply/map para transformaciones custom (con consciencia de cuándo es lento).",
    "outcomes": [
      "Predecir el resultado de operar dos Series/DataFrames con indexes parcialmente distintos.",
      "Usar fill_value en operaciones para no propagar NaN: s1.add(s2, fill_value=0).",
      "Aplicar funciones con apply (lento, flexible), map (Series), applymap / df.map (elementwise).",
      "Vectorizar transformaciones cuando se puede en vez de apply (10–100× más rápido).",
      "Usar ufuncs NumPy sobre Series — pandas las soporta directamente y preserva el index."
    ],
    "topics": [
      "Alineación automática por index",
      "fill_value para operaciones",
      "apply axis=0 vs axis=1",
      "map para Series con dict",
      "df.map (era applymap) — elementwise",
      "Vectorización > apply"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Suma con alineación. Dos Series con index parcialmente solapado. Súmalas (default) y con fill_value=0.",
      "apply por fila. Define una función que reciba una fila de penguins y devuelva BMI = body_mass / bill_length². Aplica con axis=1.",
      "Mismo cálculo vectorizado. Implementa BMI con operaciones vectorizadas. Mide ambos con %timeit.",
      "map con dict. Mapea species a códigos: {'Adelie': 0, 'Chinstrap': 1, 'Gentoo': 2}.",
      "ufunc NumPy preserva index. Aplica np.log a una columna; verifica que el index sigue intacto."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/024-pandas-operaciones-y-alineacion/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/025-pandas-datos-faltantes",
    "number": 25,
    "slug": "025-pandas-datos-faltantes",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: datos faltantes",
    "description": "Que el alumno detecte, cuantifique y maneje datos faltantes con criterio.",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno detecte, cuantifique y maneje datos faltantes con criterio. Eliminar es la opción fácil pero suele ser incorrecta: cuándo eliminar, cuándo imputar (media, mediana, forward-fill), y cuándo el faltante es señal que merece su propia columna.",
    "outcomes": [
      "Detectar NaN con isna(), notna() y cuantificar por columna/fila.",
      "Eliminar filas/columnas con NaN usando dropna con how/thresh/subset.",
      "Imputar con fillna: valor escalar, media/mediana, forward/backward fill, interpolación.",
      "Distinguir NaN vs None vs pd.NA y por qué importan los dtypes nullable (Int64, boolean).",
      "Decidir entre eliminar/imputar/dejar — y crear columna was_missing cuando el faltante es informativo."
    ],
    "topics": [
      "Tipos de missing en pandas: NaN, None, NaT, pd.NA",
      "Detección: isna, notna, isna().sum()",
      "dropna: how='any'/'all', thresh, subset",
      "fillna: escalar, dict, ffill, bfill, interpolate",
      "Dtypes nullable: Int64, Float64, boolean",
      "was_missing como feature"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Cuantifica. Carga penguins, reporta % de NaN por columna y por fila.",
      "Eliminar filas con cualquier NaN. df.dropna(how='any'). Compara shape antes/después.",
      "Eliminar solo filas con NaN en sex. df.dropna(subset=['sex']). Más selectivo.",
      "Imputar. Rellena bill_length_mm con la mediana por especie (groupby + transform). Justifica por qué la mediana es mejor que la media aquí.",
      "Forward fill en series temporales. Crea una Series con NaN intercalados. Aplica ffill, bfill, interpolate. Compara."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/025-pandas-datos-faltantes/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/026-pandas-multiindex",
    "number": 26,
    "slug": "026-pandas-multiindex",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: MultiIndex",
    "description": "Que el alumno use índices jerárquicos (MultiIndex) cuando hay estructura natural en los datos (país × ciudad, año × mes, sector × empresa).",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno use índices jerárquicos (MultiIndex) cuando hay estructura natural en los datos (país × ciudad, año × mes, sector × empresa). Saber cuándo aporta vs cuándo complica — el 80% del tiempo en data science aplanado es mejor.",
    "outcomes": [
      "Crear MultiIndex desde tuplas, arrays, producto cartesiano (from_product).",
      "Indexar con .loc[(nivel1, nivel2)] y .loc[:, ('grupo', 'col')].",
      "Aplanar y reconstruir con unstack(), stack(), reset_index().",
      "Decidir cuándo MultiIndex aporta (groupby con múltiples claves devuelve uno automáticamente) y cuándo es más legible aplanar.",
      "Renombrar niveles con rename(level=...) y reordenarlos con swaplevel."
    ],
    "topics": [
      "MultiIndex: motivación",
      "Construcción: tuples, arrays, from_product",
      "Indexación: tuple selector",
      "stack / unstack — pivot rápido",
      "groupby + multiindex resultado",
      "Cuándo aplanar"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Construye desde tuplas. Crea DataFrame con index [(España, 2023), (España, 2024), (Chile, 2023), (Chile, 2024)] y 2 cols ventas/clientes.",
      "from_product. Mismo con pd.MultiIndex.from_product([paises, años]).",
      "Acceso jerárquico. df.loc['España'], df.loc[('España', 2024)]. Compara con df.xs(2024, level=1) para slice por nivel.",
      "unstack y stack. Convierte tu MultiIndex en wide (años como columnas) y de vuelta.",
      "groupby produce MultiIndex. Carga penguins, agrupa por (species, sex) y agrega mean(). Aplana con reset_index()."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/026-pandas-multiindex/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/027-pandas-concat-merge-join",
    "number": 27,
    "slug": "027-pandas-concat-merge-join",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: concat, merge, join",
    "description": "Que el alumno junte datasets correctamente: concat (apilado simple), merge (SQL-style joins) y join (atajo por index).",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno junte datasets correctamente: concat (apilado simple), merge (SQL-style joins) y join (atajo por index). El error más común es usar el join equivocado y obtener duplicados o filas perdidas — saber qué tipo (inner/left/right/outer) evita semanas de bugs.",
    "outcomes": [
      "Apilar DataFrames con pd.concat por filas (axis=0) o columnas (axis=1).",
      "Hacer joins SQL-style con pd.merge: inner, left, right, outer, cross.",
      "Diagnosticar duplicados generados por merge con validate='one_to_one' | 'many_to_one' | ….",
      "Joinear por index con df1.join(df2) (atajo para merge por index).",
      "Usar indicator=True para saber qué filas vienen de cada lado del merge."
    ],
    "topics": [
      "concat axis=0 (filas) vs axis=1 (columnas)",
      "merge how='inner'/'left'/'right'/'outer'",
      "on vs left_on/right_on",
      "validate para evitar duplicación",
      "indicator=True para auditar",
      "df.join por index"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Concat por filas. 3 DataFrames mensuales con mismas columnas → uno anual. ignore_index=True.",
      "Inner join. Clientes + órdenes por cliente_id. Verifica que solo aparecen clientes con al menos 1 orden.",
      "Left join. Clientes + órdenes, conservando clientes sin órdenes (NaN en cols de orden).",
      "Detectar duplicados. Provoca un merge muchos-a-muchos no intencional. Usa validate='one_to_many' para que falle si hay duplicación oculta.",
      "indicator=True. Auditar cuántas filas son left_only / right_only / both."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/027-pandas-concat-merge-join/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/028-pandas-groupby-split-apply-combine",
    "number": 28,
    "slug": "028-pandas-groupby-split-apply-combine",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: groupby (split-apply-combine)",
    "description": "Que el alumno aplique el patrón split-apply-combine que es el patrón fundamental de análisis tabular: dividir por grupo, aplicar función, recombinar.",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno aplique el patrón split-apply-combine que es el patrón fundamental de análisis tabular: dividir por grupo, aplicar función, recombinar. Saber elegir entre agg, transform, filter y apply — cada uno tiene su rol.",
    "outcomes": [
      "Agrupar por una o más columnas con groupby y aplicar agregaciones (sum, mean, count).",
      "Usar agg con dict para distintas funciones por columna: agg({'a': 'sum', 'b': 'mean'}).",
      "transform para preservar la shape original (broadcasting del estadístico de grupo).",
      "filter para filtrar grupos enteros según condición.",
      "Diferenciar los 4 métodos del groupby y elegir el correcto."
    ],
    "topics": [
      "Split-apply-combine: el patrón",
      "agg (= aggregate)",
      "transform",
      "filter",
      "apply: el más flexible, el más lento",
      "Múltiples columnas de agrupación"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Agg básico. Penguins agrupado por species: media de cada feature numérica.",
      "Agg con dict. Por species: mean de bill_length, max de body_mass, count de filas.",
      "Transform: z-score por grupo. Crea columna mass_z = z-score de body_mass dentro de su species.",
      "Filter: solo grupos grandes. Conserva solo species con >100 individuos.",
      "Apply custom. Por species, devuelve el pingüino con mayor body_mass (un DataFrame por grupo)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/028-pandas-groupby-split-apply-combine/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/029-pandas-pivot-tables-y-crosstab",
    "number": 29,
    "slug": "029-pandas-pivot-tables-y-crosstab",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: pivot tables y crosstab",
    "description": "Que el alumno construya tablas pivot (estilo Excel) con pivot_table y tablas de contingencia con crosstab.",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno construya tablas pivot (estilo Excel) con pivot_table y tablas de contingencia con crosstab. Son atajos sobre groupby pensados para resumen×visualización rápida.",
    "outcomes": [
      "Usar pivot_table con index, columns, values, aggfunc.",
      "Añadir totales con margins=True.",
      "Construir tablas de contingencia con pd.crosstab y normalizar (normalize='all'/'index'/'columns').",
      "Diferenciar pivot (sin agregar) vs pivot_table (con aggfunc, agrega duplicados).",
      "Visualizar una pivot como heatmap básico para confirmar patrones."
    ],
    "topics": [
      "pivot vs pivot_table",
      "Parámetros: index, columns, values, aggfunc",
      "margins=True: totales",
      "crosstab: tabla de contingencia",
      "normalize en crosstab",
      "Pivot → heatmap"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Pivot básico. Penguins: índice species, columnas sex, valores body_mass mean.",
      "Pivot con totales. Mismo con margins=True.",
      "Crosstab counts. Counts species × island.",
      "Crosstab normalizado. Mismo con normalize='index' (% por fila).",
      "Pivot → heatmap. Toma un pivot table y plotéala con matplotlib imshow."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/029-pandas-pivot-tables-y-crosstab/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/030-pandas-operaciones-vectorizadas-sobre-strings",
    "number": 30,
    "slug": "030-pandas-operaciones-vectorizadas-sobre-strings",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: operaciones vectorizadas sobre strings",
    "description": "Que el alumno limpie y transforme columnas de texto sin caer en apply(lambda x: ...), usando el accessor .str de pandas — vectorizado, NaN-aware, con métodos análogos a los de Python (lower, strip, replace, split, conta…",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno limpie y transforme columnas de texto sin caer en apply(lambda x: ...), usando el accessor .str de pandas — vectorizado, NaN-aware, con métodos análogos a los de Python (lower, strip, replace, split, contains, regex).",
    "outcomes": [
      "Usar .str para aplicar operaciones de string vectorizadamente a una Series.",
      "Manejar NaN automáticamente (los métodos .str propagan NaN sin error).",
      "Aplicar regex con .str.contains(patron), .str.extract(...), .str.replace(...).",
      "Dividir y unir con .str.split(sep, expand=True) que produce un DataFrame.",
      "Trabajar con categorical cuando el cardinalidad es baja (memoria y speedup)."
    ],
    "topics": [
      "Accessor .str",
      "Casos típicos: lower, strip, replace, contains",
      "Regex con .str.extract y grupos nombrados",
      ".str.split(expand=True) → DataFrame",
      "dtype='string' (nullable) vs object",
      "Categorical para baja cardinalidad"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Lower + strip. Lista de emails con mayúsculas y espacios. Normaliza con .str.lower().str.strip().",
      "Extract dominio. De una columna de emails, extrae el dominio con regex (@(.+)$).",
      "Split nombre completo. Columna 'Ana García' → nombre, apellido en columnas separadas.",
      "Filtro por contains. Filas donde la columna descripcion contiene la palabra (case-insensitive) 'urgente'.",
      "Categorical. Convierte una columna con 5 valores únicos en 100k filas a Categorical. Compara memoria."
    ],
    "codeExamples": [
      {
        "id": "parte-0-prerrequisitos/030-pandas-operaciones-vectorizadas-sobre-strings-code-1",
        "title": "Bloque 1",
        "explanation": "Código incluido en el material de la clase.",
        "schema": "python · 7 líneas",
        "language": "python",
        "code": "import re\n\nemail = \"vladimir.acuna@gmail.com\"\npat = re.compile(r\"(?P<usuario>[\\w.]+)@(?P<dominio>[\\w.]+)\")\nm = pat.search(email)\nprint(m.group(\"usuario\"))  # vladimir.acuna\nprint(m.group(\"dominio\"))  # gmail.com"
      }
    ],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/030-pandas-operaciones-vectorizadas-sobre-strings/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/031-pandas-series-de-tiempo-resampling-rolling",
    "number": 31,
    "slug": "031-pandas-series-de-tiempo-resampling-rolling",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: series de tiempo, resampling, rolling",
    "description": "Que el alumno trabaje con datos temporales correctamente: parsear fechas, indexar por DatetimeIndex, hacer resampling (cambiar la frecuencia) y rolling (ventanas móviles para tendencias).",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno trabaje con datos temporales correctamente: parsear fechas, indexar por DatetimeIndex, hacer resampling (cambiar la frecuencia) y rolling (ventanas móviles para tendencias).",
    "outcomes": [
      "Parsear strings de fecha con pd.to_datetime(..., format=..., errors=...).",
      "Indexar por DatetimeIndex y slicear con strings de fecha (df.loc['2024-01':'2024-03']).",
      "Resamplear a otra frecuencia: df.resample('M').sum(), 'W', 'D', 'H'.",
      "Aplicar ventanas móviles con rolling(window).mean() para suavizar tendencias.",
      "Manejar zonas horarias con tz_localize y tz_convert."
    ],
    "topics": [
      "pd.to_datetime con errors='coerce'",
      "DatetimeIndex y slicing por fecha",
      "Resampling: 'D', 'W', 'M', 'Q', 'Y', 'H'",
      "Rolling windows",
      "shift y diff",
      "Timezones: localize → convert"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Parseo robusto. Lista de fechas con formatos mixtos ('2024-01-15', '15/02/2024', 'foo'). Parsea con errors='coerce'. Reporta NaT.",
      "Slice por fecha. Con índice datetime, selecciona Q1 2024 con df.loc['2024-01':'2024-03'].",
      "Resample diaria → mensual. Suma ventas por mes con df.resample('M').sum().",
      "Rolling 7-day mean. Calcula media móvil de 7 días sobre ventas diarias. Plotea junto a la serie original.",
      "shift para lag feature. Crea columna ventas_lag_1 con shift(1). Útil para features de ML."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/031-pandas-series-de-tiempo-resampling-rolling/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/032-pandas-eval-y-query",
    "number": 32,
    "slug": "032-pandas-eval-y-query",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Pandas: eval y query",
    "description": "Que el alumno conozca df.eval y df.query — herramientas para expresar operaciones y filtros con sintaxis tipo SQL en strings.",
    "level": "Basico",
    "duration": "45 min",
    "theory": "Que el alumno conozca df.eval y df.query — herramientas para expresar operaciones y filtros con sintaxis tipo SQL en strings. Útiles para legibilidad en cadenas largas y, en datasets muy grandes, también más rápidos (usan numexpr).",
    "outcomes": [
      "Filtrar con df.query(\"col > 10 and other == 'X'\").",
      "Calcular columnas nuevas con df.eval('z = x + y') o df.eval('x * 2').",
      "Referenciar variables locales en query/eval con prefijo @: df.query('x > @threshold').",
      "Decidir cuándo usar query (legibilidad en cadenas largas) vs filtro tradicional (mejor autocompletado IDE).",
      "Saber que el speedup real solo aparece con datasets >10k filas y expresiones complejas."
    ],
    "topics": [
      "df.query — sintaxis tipo SQL",
      "df.eval — expresiones aritméticas",
      "Variables locales con @",
      "numexpr para speedup",
      "Trade-off: legibilidad vs introspección IDE"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Filter tradicional vs query. df[(df.a > 10) & (df.b < 5) & (df.c == 'x')] vs df.query('a > 10 and b < 5 and c == \"x\"'). Compara legibilidad.",
      "Variable local. threshold = 100; filtra con df.query('precio > @threshold').",
      "eval para nueva columna. df.eval('total = precio * cantidad', inplace=True).",
      "Benchmark. Genera df 1M filas. Compara filter tradicional vs query con %timeit.",
      "eval con inplace=False vs cálculo tradicional df['total'] = df['precio'] * df['cantidad'] — verifica resultados idénticos."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/032-pandas-eval-y-query/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/033-polars-dataframes-modernos",
    "number": 33,
    "slug": "033-polars-dataframes-modernos",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Polars: DataFrames modernos",
    "description": "Conocer Polars — la librería de DataFrames moderna (Rust + Arrow) que está reemplazando a pandas en proyectos donde performance importa.",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Conocer Polars — la librería de DataFrames moderna (Rust + Arrow) que está reemplazando a pandas en proyectos donde performance importa. Aprender su API (similar a pandas pero con expresiones lazy y paralelismo automático) y entender cuándo conviene Polars sobre pandas (datasets > 1 GB, pipelines con muchas transformaciones, multi-core).",
    "outcomes": [
      "Instalar Polars (pip install polars) y leer datos con pl.read_csv, pl.read_parquet, pl.scan_csv (lazy).",
      "Aplicar la API de expresiones: df.select(pl.col('precio').sum()), pl.col('x').filter(pl.col('y') > 0).mean().",
      "Diferenciar eager (DataFrame) de lazy (LazyFrame) — y por qué lazy permite optimizaciones del query planner.",
      "Hacer groupby, join, pivot, unpivot con sintaxis Polars y comparar con pandas.",
      "Reconocer el speedup típico: 5-30× sobre pandas en operaciones comunes (single-machine, multi-core)."
    ],
    "topics": [
      "Polars vs pandas vs DuckDB: el panorama 2026.",
      "Arrow como formato columnar in-memory.",
      "Eager (DataFrame) vs Lazy (LazyFrame).",
      "Expresiones encadenables: pl.col(...).operation().",
      "Query optimization automática: predicate pushdown, projection pushdown.",
      "Multi-threading automático."
    ],
    "materials": [
      "NYC Taxi (~100 MB Parquet) o cualquier CSV > 100 MB.",
      "Librerías: polars, pandas (para comparar), pyarrow."
    ],
    "exercises": [
      "Eager básico: df = pl.read_csv('archivo.csv'); df.head(); df.describe(). Comparar con pandas.",
      "Expresiones: df.filter(pl.col('precio') > 100).group_by('categoria').agg(pl.col('precio').mean().alias('precio_medio')).",
      "Lazy + collect: lf = pl.scan_csv('big.csv').filter(...).group_by(...).agg(...); result = lf.collect(). Comparar tiempo vs eager.",
      "Query plan: lf.explain() muestra el plan optimizado. Identificar predicate pushdown.",
      "Pandas ↔ Polars: df.to_pandas() y pl.from_pandas(pd_df). Útil para mantener compatibilidad gradual."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/033-polars-dataframes-modernos/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/034-parquet-arrow-pyarrow-duckdb",
    "number": 34,
    "slug": "034-parquet-arrow-pyarrow-duckdb",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Parquet, Arrow, PyArrow, DuckDB",
    "description": "Conocer el stack columnar moderno que reemplaza al CSV para datos serios: Parquet (formato en disco), Arrow (formato in-memory), PyArrow (la implementación Python), y DuckDB (SQL embebido sobre Parquet/Arrow).",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Conocer el stack columnar moderno que reemplaza al CSV para datos serios: Parquet (formato en disco), Arrow (formato in-memory), PyArrow (la implementación Python), y DuckDB (SQL embebido sobre Parquet/Arrow). Saber por qué el ecosistema entero (Polars, pandas 2.x, Spark, BigQuery, DataFusion) convergió a este stack.",
    "outcomes": [
      "Leer y escribir Parquet con pandas, polars y pyarrow.",
      "Aplicar column pruning (leer solo columnas necesarias) y predicate pushdown (leer solo filas necesarias).",
      "Manejar particionado por columna (year=2024/month=03/) para queries eficientes.",
      "Hacer queries SQL con DuckDB directamente sobre Parquet sin cargarlo a RAM.",
      "Reconocer ventajas de Arrow: zero-copy entre librerías (Polars ↔ pandas ↔ Spark)."
    ],
    "topics": [
      "CSV: limitaciones (sin tipos, fila por fila, sin compresión).",
      "Parquet: columnar, comprimido (snappy/zstd), tipos preservados, metadata por chunk.",
      "Arrow: formato in-memory zero-copy.",
      "PyArrow: API Python para ambos.",
      "DuckDB: \"SQLite para analytics\", consulta Parquet directo.",
      "Particionado tipo Hive."
    ],
    "materials": [
      "NYC Taxi Parquet (Cloudfront público).",
      "Librerías: pyarrow, duckdb, polars, pandas."
    ],
    "exercises": [
      "CSV → Parquet: leer un CSV grande con pandas, escribir Parquet con df.to_parquet('file.parquet', compression='zstd'). Comparar tamaño en disco (típicamente 3-10× menor).",
      "Column pruning: leer SOLO 2 columnas de un Parquet de 50 columnas con pq.read_table('f.parquet', columns=['a', 'b']). Comparar tiempo vs leer todo.",
      "DuckDB sobre Parquet: duckdb.sql(\"SELECT date, AVG(amount) FROM 'taxi/*.parquet' WHERE amount > 10 GROUP BY date\").df(). Sin cargar nada explícitamente.",
      "Particionado: escribir df.to_parquet('out/', partition_cols=['year', 'month']). Inspeccionar estructura de directorios.",
      "Arrow zero-copy: arrow_table = polars_df.to_arrow(); pandas_df = arrow_table.to_pandas(). Verificar que es rápido (no copia memoria)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/034-parquet-arrow-pyarrow-duckdb/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/035-matplotlib-anatomia-figura-axes",
    "number": 35,
    "slug": "035-matplotlib-anatomia-figura-axes",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Matplotlib: anatomía figura/axes",
    "description": "Que el alumno entienda la jerarquía de objetos de matplotlib (Figure → Axes → Artist) y use la API orientada a objetos (fig, ax = plt.subplots()) en vez del interfaz pyplot estilo MATLAB.",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno entienda la jerarquía de objetos de matplotlib (Figure → Axes → Artist) y use la API orientada a objetos (fig, ax = plt.subplots()) en vez del interfaz pyplot estilo MATLAB. Esto es lo que separa gráficos publicables de notebooks de cualquier curso introductorio.",
    "outcomes": [
      "Explicar la jerarquía Figure → Axes → Artist y por qué la API OO es preferible.",
      "Crear una figura con fig, ax = plt.subplots(figsize=(8, 4)) y configurar título, ejes, leyenda.",
      "Guardar una figura a PNG/SVG/PDF con DPI controlado.",
      "Cerrar figuras explícitamente para liberar memoria en notebooks que generan muchas.",
      "Configurar defaults con plt.rcParams (font, line width, colors)."
    ],
    "topics": [
      "Figure (canvas) → Axes (gráfico) → Artist (elementos)",
      "pyplot vs OO API",
      "fig, ax = plt.subplots()",
      "fig.savefig y formatos",
      "Liberar memoria: plt.close(fig)",
      "plt.rcParams y stylesheets"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Hello world. Crea figura 8×4, plot de y = sin(x) para x ∈ [0, 2π]. Título, xlabel, ylabel.",
      "Dos líneas en un axes. Misma figura: sin(x) y cos(x) con colores distintos y leyenda.",
      "Guarda 3 formatos. Mismo plot a PNG (100 DPI), PNG (300 DPI), SVG. Compara tamaños.",
      "Loop sin leak. Genera 20 plots en loop. Cierra cada uno con plt.close(fig). Verifica que len(plt.get_fignums()) queda en 0.",
      "rcParams. Cambia font.size y lines.linewidth para tu sesión. Verifica el efecto."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/035-matplotlib-anatomia-figura-axes/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/036-matplotlib-line-scatter-bar-histogram-boxplot",
    "number": 36,
    "slug": "036-matplotlib-line-scatter-bar-histogram-boxplot",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Matplotlib: line, scatter, bar, histogram, boxplot",
    "description": "Que el alumno conozca los 5 plots básicos que cubren el 80% del trabajo de EDA, y sepa cuándo cada uno: line (tendencia temporal), scatter (relación dos variables), bar (categóricas), histogram (distribución), boxplot (…",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno conozca los 5 plots básicos que cubren el 80% del trabajo de EDA, y sepa cuándo cada uno: line (tendencia temporal), scatter (relación dos variables), bar (categóricas), histogram (distribución), boxplot (5 estadísticos + outliers).",
    "outcomes": [
      "Elegir el plot correcto según el tipo de variables (continua/categórica) y el objetivo.",
      "Ajustar marker, color, linestyle, alpha para legibilidad.",
      "Construir histogramas con bins adecuados (regla de Freedman-Diaconis o 'auto').",
      "Interpretar boxplot: mediana, Q1/Q3, whiskers, outliers.",
      "Combinar bar + error bars para mostrar incertidumbre."
    ],
    "topics": [
      "Line: tendencias y series temporales",
      "Scatter: relación entre dos variables",
      "Bar y barh: categóricas",
      "Histogram: distribución de una continua",
      "Boxplot: distribución resumida + outliers",
      "Errorbar y fill_between"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Line. Serie temporal de ventas mensuales (sintética). Anota máximo con flecha.",
      "Scatter. body_mass vs bill_length, color por species. Adicionalmente: s= con flipper_length para tamaño.",
      "Bar. Count por species, ordenado descendente. Vertical y horizontal — compara legibilidad.",
      "Histogram. Distribución de body_mass con bins='auto' y bins=10. Compara.",
      "Boxplot. body_mass por species: 3 cajas lado a lado. Identifica outliers."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/036-matplotlib-line-scatter-bar-histogram-boxplot/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/037-matplotlib-subplots-y-gridspec",
    "number": 37,
    "slug": "037-matplotlib-subplots-y-gridspec",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Matplotlib: subplots y gridspec",
    "description": "Que el alumno organice múltiples plots en una sola figura — con plt.subplots(n, m) para grillas regulares y con GridSpec para layouts irregulares (un plot grande + varios pequeños).",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno organice múltiples plots en una sola figura — con plt.subplots(n, m) para grillas regulares y con GridSpec para layouts irregulares (un plot grande + varios pequeños). Crítico para informes y dashboards.",
    "outcomes": [
      "Crear grillas regulares con fig, axes = plt.subplots(2, 3, figsize=...).",
      "Iterar sobre axes.flat para llenar la grilla con loops.",
      "Compartir ejes con sharex=True, sharey=True para comparar.",
      "Usar GridSpec para layouts irregulares (1 grande + 3 pequeños).",
      "Usar constrained_layout=True en vez de tight_layout() (más confiable)."
    ],
    "topics": [
      "plt.subplots(nrows, ncols)",
      "Iterar con .flat",
      "sharex/sharey",
      "GridSpec para layouts irregulares",
      "constrained_layout vs tight_layout",
      "add_subplot con posiciones custom"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Grilla 2×2. 4 histogramas de las 4 features numéricas de penguins en una figura.",
      "Grilla con loop. Itera axes.flat para plot consistente.",
      "sharey=True. 3 boxplots por species lado a lado con misma escala Y.",
      "GridSpec irregular. Un scatter grande (2×2) + 1 hist arriba (1×2) + 1 hist a la derecha (2×1) — marginal histograms.",
      "constrained_layout. Compara una figura compleja con tight_layout() vs constrained_layout=True — observa diferencia."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/037-matplotlib-subplots-y-gridspec/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/038-matplotlib-legends-colorbars-ticks-anotaciones",
    "number": 38,
    "slug": "038-matplotlib-legends-colorbars-ticks-anotaciones",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Matplotlib: legends, colorbars, ticks, anotaciones",
    "description": "Que el alumno controle los detalles que distinguen un plot ad-hoc de uno publicable: leyenda fuera del gráfico, colorbar discreto, ticks personalizados, y anotaciones (flechas, texto) para guiar la atención del lector.",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno controle los detalles que distinguen un plot ad-hoc de uno publicable: leyenda fuera del gráfico, colorbar discreto, ticks personalizados, y anotaciones (flechas, texto) para guiar la atención del lector.",
    "outcomes": [
      "Posicionar leyenda fuera del axes con bbox_to_anchor.",
      "Configurar colorbar con label, ticks discretos, y categoría.",
      "Personalizar ticks: rotación, formato (FuncFormatter, PercentFormatter), scale log.",
      "Anotar puntos con ax.annotate(..., xy=..., xytext=..., arrowprops=...).",
      "Añadir líneas de referencia con axhline/axvline (umbrales, medias)."
    ],
    "topics": [
      "Legend con bbox_to_anchor",
      "Colorbar con label y ticks discretos",
      "Tick formatters: percent, scientific, custom",
      "ax.annotate con flecha",
      "axhline / axvline / axhspan",
      "Log scale: ax.set_yscale('log')"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Leyenda fuera. Plot con 5 líneas, leyenda a la derecha fuera del axes.",
      "Colorbar. Scatter con c= continuo (ej: density), colorbar con label.",
      "PercentFormatter. Bar chart con eje Y formateado como porcentaje.",
      "Anotar outlier. Scatter con un punto extremo; flecha + texto identificándolo.",
      "Log scale. Plot de valores con rango grande (1, 10, 100, 1000); compara linear vs log."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/038-matplotlib-legends-colorbars-ticks-anotaciones/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/039-matplotlib-stylesheets",
    "number": 39,
    "slug": "039-matplotlib-stylesheets",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Matplotlib: stylesheets",
    "description": "Que el alumno aproveche stylesheets built-in y propios para mantener consistencia visual entre plots y proyectos — y deje de configurar manualmente rcParams en cada notebook.",
    "level": "Basico",
    "duration": "30 min",
    "theory": "Que el alumno aproveche stylesheets built-in y propios para mantener consistencia visual entre plots y proyectos — y deje de configurar manualmente rcParams en cada notebook.",
    "outcomes": [
      "Listar stylesheets disponibles con plt.style.available.",
      "Aplicar un style globalmente (plt.style.use(...)) o solo a un bloque (with plt.style.context(...)).",
      "Crear style propio en un archivo .mplstyle y usarlo.",
      "Combinar styles (uno + ajustes manuales).",
      "Elegir style según contexto (informe, presentación, B&N para impresión)."
    ],
    "topics": [
      "plt.style.available",
      "plt.style.use(...) global",
      "with plt.style.context(...)",
      "Archivo .mplstyle propio",
      "Stylesheets comunes",
      "rcParams override puntual"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Catalogo. Imprime plt.style.available. Identifica 5 que suenen útiles.",
      "Galería visual. Mismo scatter plot bajo 4 styles distintos (default, ggplot, seaborn-whitegrid, grayscale).",
      "Bloque temporal. Con with plt.style.context('seaborn-v0_8-darkgrid'): aplica style solo a 1 figura.",
      "Style propio. Crea mi_style.mplstyle con tus defaults preferidos. Úsalo.",
      "Style + override. Aplica ggplot y luego cambia figure.figsize para un plot específico."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/039-matplotlib-stylesheets/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/040-matplotlib-3d-plotting",
    "number": 40,
    "slug": "040-matplotlib-3d-plotting",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Matplotlib: 3D plotting",
    "description": "Que el alumno sepa cuándo (raramente) usar 3D y cómo hacerlo bien: scatter 3D, superficies (plot_surface), wireframes y contornos.",
    "level": "Basico",
    "duration": "45 min",
    "theory": "Que el alumno sepa cuándo (raramente) usar 3D y cómo hacerlo bien: scatter 3D, superficies (plot_surface), wireframes y contornos. Spoiler: la mayoría de las veces un buen 2D + color comunica mejor.",
    "outcomes": [
      "Crear axes 3D con projection='3d'.",
      "Scatter, line, surface, wireframe, contour en 3D.",
      "Controlar ángulo de vista con ax.view_init(elev, azim).",
      "Reconocer cuándo NO usar 3D: la mayoría de las veces hay una alternativa 2D mejor."
    ],
    "topics": [
      "projection='3d'",
      "Scatter 3D con codificación por color",
      "plot_surface para z = f(x, y)",
      "plot_wireframe y contour3D",
      "view_init: rotar interactivo",
      "Cuándo NO usar 3D"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Scatter 3D. 200 puntos con coords (x, y, z) y color por una 4ª variable.",
      "Superficie. z = sin(sqrt(x² + y²)) en mesh 50×50. plot_surface con colormap.",
      "Wireframe + contour. Misma función con plot_wireframe. Compara legibilidad con superficie llena.",
      "view_init. Cambia (elev, azim) a 4 ángulos y graba una grilla 2×2.",
      "Reto: 2D que vence al 3D. Para tu scatter 3D del ejercicio 1, propón un 2D + color/tamaño que comunique igual o mejor."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/040-matplotlib-3d-plotting/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/041-seaborn-distribuciones-relaciones-categoricas-facetas",
    "number": 41,
    "slug": "041-seaborn-distribuciones-relaciones-categoricas-facetas",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Seaborn: distribuciones, relaciones, categóricas, facetas",
    "description": "Que el alumno use seaborn cuando aporta sobre matplotlib puro: defaults estéticos, API tipada para DataFrames (x=, y=, hue=, col=), distribuciones (histplot, kdeplot, displot), relaciones (scatterplot, lmplot), categóri…",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno use seaborn cuando aporta sobre matplotlib puro: defaults estéticos, API tipada para DataFrames (x=, y=, hue=, col=), distribuciones (histplot, kdeplot, displot), relaciones (scatterplot, lmplot), categóricas (boxplot, violinplot, swarmplot), y facetas (grilla automática por categoría).",
    "outcomes": [
      "Usar la API moderna (figure-level vs axes-level) y elegir la correcta.",
      "Construir un pairplot para EDA rápido de un DataFrame.",
      "Codificar 3 dimensiones con hue, style, size.",
      "Hacer facetas con col= y row= para grillas automáticas.",
      "Personalizar themes con sns.set_theme(style=..., palette=...)."
    ],
    "topics": [
      "seaborn vs matplotlib",
      "Figure-level (displot, relplot, catplot) vs axes-level (histplot, scatterplot, boxplot)",
      "hue, style, size",
      "Facetas con col, row",
      "pairplot para EDA",
      "Themes y paletas"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Pairplot. Penguins, color por species. EDA en 1 línea.",
      "Scatter con hue + size. body_mass vs flipper, hue por species, size por bill_length.",
      "KDE distribución. body_mass por species (3 KDE en mismo plot).",
      "Boxplot + swarm. Combinar boxplot con swarm para ver puntos individuales.",
      "Facetas. sns.relplot(...col='species', row='sex') para 3×2 = 6 subplots automáticos."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/041-seaborn-distribuciones-relaciones-categoricas-facetas/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/042-visualizacion-geografica-plotly-folium",
    "number": 42,
    "slug": "042-visualizacion-geografica-plotly-folium",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Visualización geográfica (Plotly / folium)",
    "description": "Que el alumno construya mapas básicos cuando los datos tienen componente geográfico: folium (mapas Leaflet interactivos, markers, choropleth), plotly (choropleth, scatter geo).",
    "level": "Basico",
    "duration": "60 min",
    "theory": "Que el alumno construya mapas básicos cuando los datos tienen componente geográfico: folium (mapas Leaflet interactivos, markers, choropleth), plotly (choropleth, scatter geo). Sin entrar a GIS profundo (eso es geopandas, fuera del scope de Parte 0).",
    "outcomes": [
      "Crear mapa folium centrado, con tile layer básico.",
      "Añadir markers con popup, tooltip, color según valor.",
      "Construir choropleth (mapa de calor por región) con folium o plotly.",
      "Decidir entre folium y plotly geo según destino (HTML standalone vs dashboard).",
      "Citar fuentes de tiles y GeoJSON públicos."
    ],
    "topics": [
      "Sistemas de coordenadas: lat/lng",
      "folium: mapa + markers + popups",
      "folium choropleth con GeoJSON",
      "plotly choropleth y scatter_geo",
      "Tile providers (OSM, CartoDB)",
      "Cuándo geopandas"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Mapa con markers. 5 ciudades españolas con marker y popup mostrando nombre + población.",
      "Markers coloreados. Mismo, pero color verde si pop>1M, rojo si <500k.",
      "Choropleth folium. Mapa mundial con un valor sintético por país (ej: PIB).",
      "Choropleth plotly. Lo mismo con plotly.express.choropleth.",
      "Comparar. ¿Cuándo folium (mapa físico explorable) vs plotly (integra con dashboard)?"
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/042-visualizacion-geografica-plotly-folium/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/043-sql-fundamental-select-where-join-group-by-having",
    "number": 43,
    "slug": "043-sql-fundamental-select-where-join-group-by-having",
    "partSlug": "parte-0-prerrequisitos",
    "title": "SQL fundamental: SELECT, WHERE, JOIN, GROUP BY, HAVING",
    "description": "Que el alumno escriba consultas SQL no triviales — SELECT con filtros, JOINs (inner/left), agregaciones con GROUP BY y filtros sobre agregados con HAVING.",
    "level": "Basico",
    "duration": "120 min",
    "theory": "Que el alumno escriba consultas SQL no triviales — SELECT con filtros, JOINs (inner/left), agregaciones con GROUP BY y filtros sobre agregados con HAVING. Y entienda el orden de ejecución lógico (FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT), que es lo que confunde a todo el mundo al principio.",
    "outcomes": [
      "Escribir SELECT con filtros WHERE y operadores (=, <>, IN, BETWEEN, LIKE, IS NULL).",
      "Hacer JOIN (INNER, LEFT, RIGHT, FULL) y reconocer cuándo cada uno.",
      "Agrupar y agregar con GROUP BY + COUNT, SUM, AVG, MAX, MIN.",
      "Filtrar agregados con HAVING (no se puede con WHERE).",
      "Recitar el orden lógico: FROM → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT."
    ],
    "topics": [
      "SELECT, FROM, WHERE",
      "Operadores WHERE",
      "JOINs (inner/left/right/full)",
      "GROUP BY + agregadas",
      "HAVING vs WHERE",
      "ORDER BY, LIMIT, OFFSET",
      "Orden lógico ≠ orden escrito"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "SELECT básico. Lista de clientes con país = 'ES'.",
      "JOIN. Cada orden con el nombre del cliente.",
      "LEFT JOIN. Todos los clientes, sumando órdenes (NaN si no tienen).",
      "GROUP BY + HAVING. Clientes con más de 3 órdenes y monto total > 200.",
      "Orden lógico. Explica con tus palabras por qué WHERE total > 100 no funciona si total es SUM(monto) — necesitas HAVING."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/043-sql-fundamental-select-where-join-group-by-having/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/044-sql-avanzado-ctes-window-functions-subqueries-correlacionadas",
    "number": 44,
    "slug": "044-sql-avanzado-ctes-window-functions-subqueries-correlacionadas",
    "partSlug": "parte-0-prerrequisitos",
    "title": "SQL avanzado: CTEs, window functions, subqueries correlacionadas",
    "description": "Que el alumno escriba SQL legible y potente: CTEs (WITH) para descomponer queries complejas, window functions (OVER) para rankings/totales corridos/lag/lead sin perder filas, y subqueries correlacionadas cuando aportan.",
    "level": "Basico",
    "duration": "120 min",
    "theory": "Que el alumno escriba SQL legible y potente: CTEs (WITH) para descomponer queries complejas, window functions (OVER) para rankings/totales corridos/lag/lead sin perder filas, y subqueries correlacionadas cuando aportan.",
    "outcomes": [
      "Escribir CTEs con WITH name AS (...) para mejorar legibilidad.",
      "Encadenar múltiples CTEs: WITH a AS (...), b AS (...) SELECT ....",
      "Aplicar window functions: ROW_NUMBER(), RANK(), LAG(), LEAD(), SUM() OVER (PARTITION BY ... ORDER BY ...).",
      "Calcular ranking por grupo con ROW_NUMBER() OVER (PARTITION BY ...).",
      "Diferenciar subquery (independiente) vs correlacionada (depende de la outer)."
    ],
    "topics": [
      "CTEs: WITH name AS (...)",
      "Múltiples CTEs encadenadas",
      "Recursive CTEs",
      "Window functions: OVER (PARTITION BY ... ORDER BY ...)",
      "ROW_NUMBER, RANK, DENSE_RANK",
      "LAG, LEAD: comparar con fila anterior/siguiente",
      "Subqueries correlacionadas"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "CTE básica. Reescribe una query con subquery anidada usando WITH.",
      "ROW_NUMBER por grupo. Top-1 orden por cliente (mayor monto).",
      "Total corrido. SUM(monto) OVER (PARTITION BY cliente_id ORDER BY fecha) — total acumulado por cliente.",
      "LAG. Por cliente, diferencia entre el monto actual y el anterior.",
      "Recursive CTE. Genera serie de fechas día a día desde 2024-01-01 a 2024-01-31."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/044-sql-avanzado-ctes-window-functions-subqueries-correlacionadas/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/045-sql-desde-python-sqlite3-sqlalchemy-duckdb",
    "number": 45,
    "slug": "045-sql-desde-python-sqlite3-sqlalchemy-duckdb",
    "partSlug": "parte-0-prerrequisitos",
    "title": "SQL desde Python: sqlite3, SQLAlchemy, DuckDB",
    "description": "Que el alumno conecte Python con SQL de las 3 formas que va a encontrar en producción: sqlite3 (stdlib, demo local), SQLAlchemy (ORM/engine genérico para PostgreSQL/MySQL), y DuckDB (columnar embebido para análisis sobr…",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno conecte Python con SQL de las 3 formas que va a encontrar en producción: sqlite3 (stdlib, demo local), SQLAlchemy (ORM/engine genérico para PostgreSQL/MySQL), y DuckDB (columnar embebido para análisis sobre CSV/Parquet sin servidor).",
    "outcomes": [
      "Conectar y consultar con sqlite3 stdlib, usando placeholders ? (NUNCA concatenar SQL).",
      "Usar SQLAlchemy create_engine(URL) + pd.read_sql para queries a cualquier RDBMS.",
      "Usar DuckDB para hacer SQL sobre DataFrames y CSV/Parquet directamente.",
      "Prevenir SQL injection con queries parametrizadas.",
      "Decidir entre sqlite/SQLAlchemy/DuckDB según el caso."
    ],
    "topics": [
      "sqlite3 stdlib: connect, cursor, fetchall",
      "Placeholders ? y :nombre",
      "SQLAlchemy create_engine('postgresql://...')",
      "pd.read_sql y df.to_sql",
      "DuckDB: SQL sobre DataFrames y archivos",
      "Cuándo cada uno"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "sqlite3 con placeholders. Crea tabla, inserta 5 filas usando executemany con tuples, consulta con ? placeholder. Demuestra el bug si concatenas.",
      "df.to_sql y pd.read_sql. Carga un DataFrame a SQLite y consulta de vuelta.",
      "SQLAlchemy engine. Crea engine SQLite. Usa pd.read_sql con engine.",
      "DuckDB sobre DataFrame. Carga penguins en df. duckdb.query('SELECT species, AVG(body_mass_g) FROM df GROUP BY species').df().",
      "DuckDB sobre CSV. Mismo query pero FROM 'penguins.csv' directo, sin cargar a pandas."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/045-sql-desde-python-sqlite3-sqlalchemy-duckdb/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/046-nosql-mongodb-con-pymongo",
    "number": 46,
    "slug": "046-nosql-mongodb-con-pymongo",
    "partSlug": "parte-0-prerrequisitos",
    "title": "NoSQL: MongoDB con pymongo",
    "description": "Que el alumno entienda el modelo NoSQL documento (collections de JSON-like), cuándo conviene sobre SQL, y use pymongo para CRUD básico + queries con operadores típicos.",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno entienda el modelo NoSQL documento (collections de JSON-like), cuándo conviene sobre SQL, y use pymongo para CRUD básico + queries con operadores típicos. Sin pretender competir con un curso entero de MongoDB.",
    "outcomes": [
      "Diferenciar modelo relacional (tablas + filas) vs documento (collections + docs JSON).",
      "Reconocer cuándo NoSQL aporta (schema flexible, datos jerárquicos, escala horizontal).",
      "Conectar con pymongo, hacer insert/find/update/delete.",
      "Filtrar con operadores: $gt, $lt, $in, $regex, $and, $or.",
      "Hacer agregaciones con el pipeline ($match, $group, $sort)."
    ],
    "topics": [
      "SQL vs NoSQL — cuándo cada uno",
      "Modelo documento: collections + docs JSON",
      "pymongo: connect, insert_one, find, update_one",
      "Operadores de query: $gt/$lt/$in/$regex",
      "Aggregation pipeline",
      "Cuándo NO usar Mongo"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "CRUD básico. Conecta a Mongo (o mongomock), inserta 5 productos, lee todos, actualiza uno, borra uno.",
      "Find con operadores. Productos con precio > 100 y categoría en ['libros', 'musica'].",
      "Update con $set y $inc. Incrementa stock de un producto en 10 unidades.",
      "Aggregation pipeline. Promedio de precio por categoría con $group.",
      "Documento jerárquico. Inserta un producto con array de reviews (sub-documentos). Consulta los que tienen alguna review con rating < 3 usando $elemMatch."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/046-nosql-mongodb-con-pymongo/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/047-apis-rest-con-requests",
    "number": 47,
    "slug": "047-apis-rest-con-requests",
    "partSlug": "parte-0-prerrequisitos",
    "title": "APIs REST con requests",
    "description": "Que el alumno consuma APIs REST públicas con requests: GET con parámetros, manejo de status codes, autenticación (header, bearer token), paginación, rate limiting con Retry, y carga eficiente con Session.",
    "level": "Basico",
    "duration": "90 min",
    "theory": "Que el alumno consuma APIs REST públicas con requests: GET con parámetros, manejo de status codes, autenticación (header, bearer token), paginación, rate limiting con Retry, y carga eficiente con Session. Lo mínimo para no romper la API del proveedor ni tu pipeline.",
    "outcomes": [
      "Hacer GET/POST con requests, manejar params, headers, body JSON.",
      "Verificar status code (200 vs 4xx vs 5xx) y usar raise_for_status().",
      "Autenticarse con header Authorization: Bearer ... o API key en header/query.",
      "Paginar correctamente cuando la API devuelve resultados en páginas.",
      "Rate-limiting con urllib3.util.retry.Retry para reintentos exponenciales.",
      "Reusar conexión con requests.Session para múltiples requests."
    ],
    "topics": [
      "Métodos HTTP: GET, POST, PUT, DELETE",
      "Status codes: 2xx/3xx/4xx/5xx",
      "Params, headers, body",
      "Autenticación: Bearer token, API key",
      "Paginación: offset/limit, cursor, link header",
      "Rate limiting + retry exponencial",
      "requests.Session para reuso"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "GET básico. requests.get('https://api.github.com'). Inspecciona status_code, headers, .json().",
      "Con params. GitHub search: https://api.github.com/search/repositories?q=python+ml&sort=stars. Imprime top 5.",
      "raise_for_status + try. Pega a una URL que devuelve 404 (/notfound) y maneja la excepción.",
      "Paginación. GitHub events API. Itera 3 páginas con page=1,2,3.",
      "Session + Retry. Configura una Session con HTTPAdapter + Retry (3 intentos, backoff 1s). Verifica que reintenta en 5xx simulado."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/047-apis-rest-con-requests/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/048-web-scraping-con-beautifulsoup",
    "number": 48,
    "slug": "048-web-scraping-con-beautifulsoup",
    "partSlug": "parte-0-prerrequisitos",
    "title": "Web scraping con BeautifulSoup",
    "description": "Que el alumno extraiga datos de páginas HTML cuando no hay API disponible, usando requests + BeautifulSoup.",
    "level": "Basico",
    "duration": "75 min",
    "theory": "Que el alumno extraiga datos de páginas HTML cuando no hay API disponible, usando requests + BeautifulSoup. Y entienda los límites éticos y legales: robots.txt, rate limiting humano, ToS, datos personales, copyright. Lo último que debe hacer al scrapear es tirar abajo el sitio o meterse en problemas.",
    "outcomes": [
      "Parsear HTML con BeautifulSoup(html, 'html.parser').",
      "Encontrar elementos con find, find_all, select (CSS selectors).",
      "Extraer texto y atributos (.text, ['href']).",
      "Respetar robots.txt y rate limit (delay entre requests).",
      "Identificar cuándo scraping es buena idea vs cuándo buscar otra fuente (API, dataset público)."
    ],
    "topics": [
      "HTTP → HTML → parser tree",
      "BeautifulSoup: find vs select",
      "Extracción de texto y atributos",
      "Páginas dinámicas (JS) — requests no las renderiza",
      "robots.txt — qué dice y por qué respetar",
      "Ética: ToS, rate limiting, datos personales"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Parsea HTML local. Crea un HTML con 3 productos (<div class='product'>). Extrae nombres y precios con find_all.",
      "Selectores CSS. Lo mismo con soup.select('.product .price').",
      "Tabla a DataFrame. pd.read_html(url) para una tabla HTML — bonus: requests + BeautifulSoup para tablas custom.",
      "Scrape ético. Scrapea quotes.toscrape.com (público, diseñado para esto). Respeta Crawl-delay. 3 páginas con time.sleep(1) entre cada una.",
      "Inspeccionar robots.txt. Lee https://quotes.toscrape.com/robots.txt con requests. Identifica qué paths están Disallow."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/048-web-scraping-con-beautifulsoup/notebook.ipynb"
  },
  {
    "id": "parte-0-prerrequisitos/049-async-httpx-aiohttp-para-data-scientists",
    "number": 49,
    "slug": "049-async-httpx-aiohttp-para-data-scientists",
    "partSlug": "parte-0-prerrequisitos",
    "title": "async / httpx / aiohttp para data scientists",
    "description": "Aprender asyncio y httpx —el HTTP client moderno con soporte sync + async + HTTP/2— para hacer scraping y consumo de APIs en paralelo sin bloquear.",
    "level": "Basico",
    "duration": "80 min",
    "theory": "Aprender asyncio y httpx —el HTTP client moderno con soporte sync + async + HTTP/2— para hacer scraping y consumo de APIs en paralelo sin bloquear. Pasar de \"1 request por segundo\" con requests a \"100+ concurrentes\" con httpx.AsyncClient. Comparar con aiohttp (alternativa popular) y concurrent.futures (parallelism con threads).",
    "outcomes": [
      "Definir async def y await; ejecutar con asyncio.run.",
      "Usar httpx.AsyncClient para fetches concurrentes con asyncio.gather.",
      "Limitar concurrencia con asyncio.Semaphore para no DOS-ear a la API.",
      "Implementar rate limiting + retries con backoff exponencial.",
      "Decidir entre asyncio, threading, multiprocessing según I/O-bound vs CPU-bound."
    ],
    "topics": [
      "Event loop, coroutines, await.",
      "httpx: API unificada sync/async, HTTP/2, timeouts.",
      "asyncio.gather, asyncio.as_completed.",
      "Semaphore para limitar concurrencia.",
      "Backoff exponencial con tenacity o backoff lib.",
      "aiohttp como alternativa (más antigua, más utilities).",
      "Cuándo NO async: tareas CPU-bound (usar multiprocessing)."
    ],
    "materials": [
      "Una API pública lenta: https://httpbin.org/delay/2 (espera 2 seg).",
      "Lista de 100 URLs para fetcher.",
      "Librerías: httpx, aiohttp, opcional tenacity."
    ],
    "exercises": [
      "Sync baseline: fetcher de 50 URLs con requests.get en loop. Medir tiempo.",
      "Async con httpx: async with httpx.AsyncClient() as c: results = await asyncio.gather(*[c.get(url) for url in urls]). Comparar tiempo (debería ser ~20-50× más rápido).",
      "Semaphore: limitar a 10 concurrent. Útil para no ser bloqueado por rate limits.",
      "Retry exponencial: usar tenacity.retry(stop=stop_after_attempt(5), wait=wait_exponential(min=1, max=30)) sobre un fetcher.",
      "httpx vs aiohttp: hacer el mismo benchmark con ambos. Similar performance; httpx tiene mejor DX."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-0-prerrequisitos/049-async-httpx-aiohttp-para-data-scientists/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/050-panorama-del-ml-tipos-batch-vs-online-instance-vs-model-based",
    "number": 50,
    "slug": "050-panorama-del-ml-tipos-batch-vs-online-instance-vs-model-based",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Panorama del ML: tipos, batch vs online, instance vs model-based",
    "description": "Que el alumno arme un mapa mental claro del campo de ML antes de entrar en algoritmos concretos: qué tipos de aprendizaje existen, en qué se diferencia entrenar de una sola vez (batch) vs en streaming (online), y por qu…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno arme un mapa mental claro del campo de ML antes de entrar en algoritmos concretos: qué tipos de aprendizaje existen, en qué se diferencia entrenar de una sola vez (batch) vs en streaming (online), y por qué algunos modelos \"memorizan ejemplos\" (instance-based) y otros \"abstraen una regla\" (model-based). Sirve de andamio para ubicar cada algoritmo de las próximas clases dentro de esta taxonomía.",
    "outcomes": [
      "Clasificar un problema dado como supervisado, no supervisado, semi-supervisado o reforzado, justificando con la pinta de los datos (¿hay etiquetas?, ¿hay recompensa?).",
      "Decidir batch vs online según el volumen de datos, la velocidad a la que cambia la distribución y el costo de reentrenar.",
      "Distinguir instance-based de model-based y reconocer cuál usa scikit-learn por debajo en un algoritmo dado (KNN vs regresión lineal, por ejemplo).",
      "Detectar señales de mala generalización (overfitting / data drift) en términos del marco del cap. 1 — anticipo de la clase 048.",
      "Ubicar cualquier algoritmo del curso dentro de la grilla (supervisión × batch/online × instance/model) sin googlear."
    ],
    "topics": [
      "Qué es ML (Samuel 1959, Mitchell 1997)",
      "Aprendizaje supervisado",
      "Aprendizaje no supervisado",
      "Semi-supervisado y auto-supervisado",
      "Aprendizaje por refuerzo",
      "Batch vs online learning",
      "Instance-based vs model-based"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Clasificá 6 problemas reales. Para cada uno indicá supervisado/no-supervisado/semi/RL y por qué: (a) detectar fraude en transacciones con tarjeta; (b) segmentar clientes de un e-commerce; (c) traducir inglés→español; (d) jugar al ajedrez; (e) detectar caras duplicadas en una galería de 10k fotos donde solo 50 están taggeadas; (f) predecir el precio del dólar a 7 días.",
      "Batch o online. Decidí qué corresponde y justificá en una línea: (a) modelo de scoring crediticio que se reentrena trimestralmente; (b) recomendador de noticias que reacciona a clicks en tiempo real; (c) clasificador de imágenes médicas en un hospital; (d) detector de spam en Gmail.",
      "KNN vs LogReg en Iris. Entrená un KNeighborsClassifier(n_neighbors=5) y un LogisticRegression(max_iter=1000) sobre iris. Compará: accuracy en test, tamaño del modelo serializado (pickle.dumps), tiempo de inferencia sobre 1000 predicciones. ¿Cuál es instance-based? Verificalo mirando el tamaño.",
      "Out-of-core con SGDRegressor. Cargá California Housing y entrená un SGDRegressor en mini-batches de 500 filas usando partial_fit en un loop. Plotteá el MSE en train a medida que pasan los batches. Es el patrón canónico de online learning.",
      "Mapa mental. En papel (o draw.io), dibujá una grilla 2×2×2 con los ejes supervisión / batch-online / instance-model. Ubicá: KNN, regresión lineal, k-means, random forest, SGDClassifier, AlphaGo, autoencoder. Algunos van a quedar en celdas raras — anotá por qué."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/050-panorama-del-ml-tipos-batch-vs-online-instance-vs-model-based/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/051-desafios-del-ml-overfitting-underfitting-datos-insuficientes",
    "number": 51,
    "slug": "051-desafios-del-ml-overfitting-underfitting-datos-insuficientes",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Desafíos del ML: overfitting, underfitting, datos insuficientes",
    "description": "Que el alumno identifique los seis problemas que hacen fracasar un proyecto de ML — datos insuficientes, no representativos, de mala calidad, features irrelevantes, overfitting y underfitting — y sepa qué herramienta ap…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno identifique los seis problemas que hacen fracasar un proyecto de ML — datos insuficientes, no representativos, de mala calidad, features irrelevantes, overfitting y underfitting — y sepa qué herramienta aplicar a cada uno (más datos, mejor muestreo, limpieza, feature engineering, regularización, o un modelo más expresivo). El eje conceptual es el bias-variance tradeoff y la intuición de que \"el modelo memorizó vs. generalizó\".",
    "outcomes": [
      "Distinguir overfitting de underfitting mirando la brecha entre error de entrenamiento y error de validación.",
      "Diagnosticar cuál de los seis desafíos de Géron está rompiendo un pipeline concreto.",
      "Aplicar regularización (L1/L2, reducir capacidad del modelo, más datos) como contramedida al overfitting.",
      "Detectar sampling bias y data snooping bias antes de medir performance.",
      "Justificar por qué \"más datos\" suele ganarle a \"modelo más complejo\" (Banko & Brill 2001 / \"The Unreasonable Effectiveness of Data\")."
    ],
    "topics": [
      "Datos insuficientes",
      "Datos no representativos (sampling bias)",
      "Datos de mala calidad (outliers, NaN, ruido)",
      "Features irrelevantes / feature engineering",
      "Overfitting",
      "Underfitting",
      "Regularización (L1/L2, early stopping, dropout)"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Diagnóstico visual. Generá un dataset con make_regression(n_samples=50, noise=20). Ajustá PolynomialFeatures(degree=15) + LinearRegression. Compará train_score y test_score. ¿Es overfitting o underfitting? Repetí con degree=1 sobre datos no lineales.",
      "Learning curve. Usá sklearn.model_selection.learning_curve sobre un dataset. Plotea train_score y val_score vs. tamaño del train. Identificá: (a) si la brecha se cierra con más datos → vale la pena conseguir más, (b) si las dos convergen bajo → modelo demasiado simple.",
      "Ridge vs. Lasso. Sobre el mismo dataset polinomial del ej. 1, ajustá Ridge(alpha=...) para alpha ∈ [0.001, 0.01, 0.1, 1, 10, 100]. Plotea train_score y test_score vs. alpha (curva de validación). Encontrá el sweet spot.",
      "Sampling bias simulado. Generá un dataset clasificación binaria balanceado (n_samples=10000). Entrená un modelo con un train sesgado (90% clase 0, 10% clase 1) y testealo en un test balanceado. Reportá accuracy global y por clase. ¿Qué te dice el accuracy global solo?",
      "Feature engineering manual. Para un dataset (fecha_timestamp, monto), predecí monto (a) usando solo timestamp como número, (b) extrayendo día_semana, mes, es_finde. Compará R² — la diferencia es el valor de feature engineering."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/051-desafios-del-ml-overfitting-underfitting-datos-insuficientes/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/052-testing-validacion-hyperparameter-tuning-no-free-lunch-theorem",
    "number": 52,
    "slug": "052-testing-validacion-hyperparameter-tuning-no-free-lunch-theorem",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Testing, validación, hyperparameter tuning, no free lunch theorem",
    "description": "Que el alumno entienda cómo medir generalización sin engañarse — separar train/val/test correctamente, usar cross-validation para estimar performance con poca varianza, tunear hiperparámetros con GridSearchCV / Randomiz…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Que el alumno entienda cómo medir generalización sin engañarse — separar train/val/test correctamente, usar cross-validation para estimar performance con poca varianza, tunear hiperparámetros con GridSearchCV / RandomizedSearchCV, y aceptar el no free lunch theorem: ningún modelo gana en todos los datasets.",
    "outcomes": [
      "Separar un dataset en train/validation/test y justificar por qué el test no se toca hasta el final.",
      "Aplicar KFold y StratifiedKFold con cross_val_score para estimar generalización.",
      "Tunear hiperparámetros con GridSearchCV y RandomizedSearchCV, leyendo cv_results_.",
      "Reconocer cuándo KFold rompe (datos temporales, grupos) y elegir el splitter correcto.",
      "Explicar el no free lunch theorem y por qué siempre conviene comparar varios modelos."
    ],
    "topics": [
      "Train / validation / test split",
      "KFold y StratifiedKFold",
      "cross_val_score y cross_validate",
      "GridSearchCV vs RandomizedSearchCV",
      "Pipeline + CV (evitar leakage del scaler)",
      "No free lunch theorem"
    ],
    "materials": [
      "sklearn.datasets.load_breast_cancer para CV estratificado.",
      "sklearn.datasets.fetch_california_housing para tuning con GridSearchCV.",
      "Serie sintética con np.cumsum(np.random.randn(500)) para TimeSeriesSplit."
    ],
    "exercises": [
      "Hold-out vs CV. Sobre breast_cancer, comparar el score de un único train_test_split (varios random_state) vs cross_val_score(cv=5). Mostrar que el hold-out varía ±0.03 entre seeds, CV mucho menos.",
      "StratifiedKFold. Con un target desbalanceado 90/10, comparar KFold vs StratifiedKFold mirando la proporción de la clase minoritaria en cada fold.",
      "GridSearchCV en pipeline. Pipeline([('scaler', StandardScaler()), ('svc', SVC())]) + GridSearchCV sobre C y gamma. Verificar que el scaler se fitea dentro de cada fold (no leakage).",
      "RandomizedSearchCV. Mismo problema que (3) pero con RandomizedSearchCV(n_iter=30) y distribuciones (scipy.stats.loguniform). Comparar tiempo y best_score_.",
      "TimeSeriesSplit. Generar serie con tendencia + ruido. Aplicar TimeSeriesSplit(n_splits=5) y entrenar Ridge con features lag-1, lag-7. Reportar score por fold. Repetir con KFold(shuffle=True) y mostrar que el score se infla artificialmente (leakage temporal)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/052-testing-validacion-hyperparameter-tuning-no-free-lunch-theorem/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/053-validacion-temporal-timeseries-walk-forward",
    "number": 53,
    "slug": "053-validacion-temporal-timeseries-walk-forward",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Validación temporal: TimeSeriesSplit, walk-forward, blocking",
    "description": "Aplicar validación correcta para series temporales — donde KFold y train_test_split aleatorio causan leakage del futuro al pasado y métricas infladas.",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Aplicar validación correcta para series temporales — donde KFold y train_test_split aleatorio causan leakage del futuro al pasado y métricas infladas. Cubrir TimeSeriesSplit, walk-forward validation (rolling y expanding), blocking para datos con dependencias intra-cluster, purged + embargoed CV (López de Prado, finanzas).",
    "outcomes": [
      "Aplicar sklearn.model_selection.TimeSeriesSplit(n_splits, max_train_size, test_size, gap).",
      "Implementar walk-forward rolling (ventana fija) y expanding (acumulativo).",
      "Detectar leakage cuando KFold se usa sobre datos temporales.",
      "Aplicar purged + embargoed K-Fold para evitar leakage por feature engineering con lags.",
      "Reportar métricas multi-fold con dispersión (no solo promedio)."
    ],
    "topics": [
      "¿Por qué KFold falla en series? Aleatorización mezcla pasado y futuro.",
      "TimeSeriesSplit: split secuencial, train siempre antes que test.",
      "Expanding vs rolling window.",
      "gap (embargo) para target leakage con lags.",
      "Purged CV (López de Prado): elimina overlap entre train y test.",
      "CombinatorialPurgedKFold para backtesting."
    ],
    "materials": [
      "Serie temporal sintética o seaborn.load_dataset('flights').",
      "Librerías: scikit-learn, pandas, mlxtend (alternativa con más options)."
    ],
    "exercises": [
      "TSSplit vs KFold leak: con serie sintética con tendencia, comparar score CV con KFold aleatorio vs TimeSeriesSplit. KFold infla.",
      "Walk-forward expanding: tscv = TimeSeriesSplit(n_splits=5). Iterar y reportar score por fold.",
      "Rolling window: con max_train_size=100, simular walk-forward de window fijo.",
      "gap: con feature y_t-1 (target lag), aplicar gap=1 para evitar que test \"vea\" su propio target.",
      "Score con dispersión: reportar mean ± std de RMSE por fold, no solo mean."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/053-validacion-temporal-timeseries-walk-forward/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/054-proyecto-end-to-end-vision-datos-exploracion-preparacion",
    "number": 54,
    "slug": "054-proyecto-end-to-end-vision-datos-exploracion-preparacion",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Proyecto end-to-end: visión, datos, exploración, preparación",
    "description": "Que el alumno recorra la primera mitad de un proyecto de ML real de punta a punta: framear el problema en términos de negocio, conseguir los datos, hacer un EDA honesto, separar train/test sin contaminarse, y dejar el p…",
    "level": "Intermedio",
    "duration": "90 min",
    "theory": "Que el alumno recorra la primera mitad de un proyecto de ML real de punta a punta: framear el problema en términos de negocio, conseguir los datos, hacer un EDA honesto, separar train/test sin contaminarse, y dejar el pipeline de preparación (limpieza, encoding, scaling) listo para entrenar — todo sobre el dataset California Housing del capítulo 2 de Géron.",
    "outcomes": [
      "Framear el problema en términos de negocio: tipo de tarea (regresión/clasificación), métrica, baseline.",
      "Hacer un EDA reproducible: describe, info, hist, corr, scatter matrix, mapas geográficos.",
      "Separar train/test correctamente con train_test_split estratificado por una variable clave (income bucket).",
      "Construir un pipeline con Pipeline + ColumnTransformer que limpie, encode (OneHotEncoder) y escale (StandardScaler) en un solo objeto.",
      "Evitar data leakage: todo cálculo (medias, encodings, scalers) se ajusta solo en train y se aplica en test."
    ],
    "topics": [
      "Framing del problema",
      "EDA: describe, hist, corr, geo plot",
      "Stratified split por income bucket",
      "Limpieza: NaN, outliers, tipos",
      "Encoding categórico (OneHotEncoder, OrdinalEncoder)",
      "Scaling (StandardScaler, MinMaxScaler)",
      "Pipelines + ColumnTransformer"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "EDA mínimo. Cargá el dataset y producí: df.info(), df.describe(), df.hist(bins=50, figsize=(12,8)). Identificá al menos 2 anomalías (cap visual de median_house_value, distribución skewed de population).",
      "Stratified split por income bucket. Creá income_cat = pd.cut(df['median_income'], bins=[0, 1.5, 3, 4.5, 6, np.inf]) y usá StratifiedShuffleSplit para train/test 80/20. Verificá que la distribución de income_cat sea casi idéntica en train y test.",
      "Target encoding sin leakage. Tomá una variable categórica (creá zipcode_fake a partir de buckets de lat/long si querés). Implementá target encoding con category_encoders.TargetEncoder ajustado solo en train. Compará RMSE de un RandomForestRegressor con (a) one-hot vs (b) target encoded.",
      "KNNImputer vs SimpleImputer. Sobre total_bedrooms (que tiene NaN reales), comparen RMSE final del pipeline usando SimpleImputer(strategy='median') vs KNNImputer(n_neighbors=5). Reportá cuál ganó y en cuánto.",
      "Pipeline completo. Armá un ColumnTransformer con: numéricas → SimpleImputer(median) + StandardScaler; categóricas → OneHotEncoder(handle_unknown='ignore'). Envolvelo en un Pipeline con LinearRegression al final. fit en train, RMSE en test."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/054-proyecto-end-to-end-vision-datos-exploracion-preparacion/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/055-feature-engineering-avanzado-target-encoding-mice",
    "number": 55,
    "slug": "055-feature-engineering-avanzado-target-encoding-mice",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Feature Engineering avanzado: target encoding + MICE imputation",
    "description": "Dominar feature engineering moderno más allá de one-hot y SimpleImputer: target encoding con regularización + cross-validation (evita leakage), KNNImputer y IterativeImputer (MICE) para imputación multivariada inteligen…",
    "level": "Intermedio",
    "duration": "85 min",
    "theory": "Dominar feature engineering moderno más allá de one-hot y SimpleImputer: target encoding con regularización + cross-validation (evita leakage), KNNImputer y IterativeImputer (MICE) para imputación multivariada inteligente, y category_encoders library para codificaciones modernas (CatBoost, James-Stein, hashing).",
    "outcomes": [
      "Aplicar target encoding con CV (no leak): category_encoders.TargetEncoder(cv=5, smoothing=10.0).",
      "Aplicar KNNImputer: imputa basado en vecinos.",
      "Aplicar IterativeImputer (MICE) de sklearn — predice cada feature con modelo de las demás.",
      "Decidir entre métodos: SimpleImputer (baseline), KNN (correlaciones locales), MICE (multivariada).",
      "Reconocer leakage en target encoding y evitarlo con CV interno."
    ],
    "topics": [
      "Target encoding clásico + smoothing bayesiano.",
      "Leak en target encoding sin CV: features ven sus propios targets.",
      "KNNImputer (sklearn): nearest neighbors por filas.",
      "IterativeImputer / MICE: estima cada feature con regresión.",
      "category_encoders: CatBoost, James-Stein, target, hashing.",
      "Pipeline-safe imputation."
    ],
    "materials": [
      "fetch_openml('credit-g') o California Housing con NaN inyectados.",
      "Librerías: category_encoders (pip install category_encoders), scikit-learn, pandas."
    ],
    "exercises": [
      "Target encoding leak: encoding sobre train+test → métrica inflada. Mostrar.",
      "Target encoding con CV: TargetEncoder(cv=5, smoothing=10) dentro de pipeline. Sin leak.",
      "CatBoost encoder: alternativa sin CV. Comparar performance.",
      "KNNImputer: con dataset con NaN, imputar con k=5; comparar contra SimpleImputer (mean).",
      "MICE: IterativeImputer(estimator=BayesianRidge(), max_iter=10). Comparar."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/055-feature-engineering-avanzado-target-encoding-mice/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/056-seleccion-y-entrenamiento-de-modelo",
    "number": 56,
    "slug": "056-seleccion-y-entrenamiento-de-modelo",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Selección y entrenamiento de modelo",
    "description": "Que el alumno entrene varios modelos baseline sobre un dataset de regresión (el notebook usa load_diabetes de scikit-learn, sin descargas), los compare con cross-validation en vez de un único split, identifique sub/over…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno entrene varios modelos baseline sobre un dataset de regresión (el notebook usa load_diabetes de scikit-learn, sin descargas), los compare con cross-validation en vez de un único split, identifique sub/overfitting con learning curves, y elija el candidato más prometedor para pasar a fine-tuning — sin malgastar tiempo afinando un modelo que no tiene techo.",
    "outcomes": [
      "Entrenar baselines (LinearRegression, DecisionTreeRegressor, RandomForestRegressor) sobre el X_prepared del pipeline de la clase anterior.",
      "Evaluar con cross_val_score usando K-Fold y scoring='neg_root_mean_squared_error' en vez de un solo train/test.",
      "Leer learning curves para diagnosticar bias vs varianza (underfitting vs overfitting).",
      "Comparar modelos con media ± desvío de los folds y decidir cuál merece HPO.",
      "Persistir el modelo elegido con joblib.dump(...) para retomarlo en la próxima clase."
    ],
    "topics": [
      "Entrenar baseline LinearRegression y medir RMSE en train",
      "DecisionTreeRegressor con RMSE = 0 en train",
      "cross_val_score(..., cv=10, scoring='neg_root_mean_squared_error')",
      "RandomForestRegressor y comparación con los anteriores",
      "learning_curve — train vs validation score vs tamaño de muestra",
      "validation_curve — score vs un hiperparámetro",
      "Decidir cuándo pasar a HPO vs cuándo seguir feature-engineering"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Baseline lineal. Entrená LinearRegression() sobre X_prepared, predecí sobre los primeros 5 ejemplos, compará con los y reales. Calculá RMSE sobre todo el train. Esperá algo en el orden de ~68k USD.",
      "Árbol que memoriza. Entrená DecisionTreeRegressor(random_state=42) sin restringir profundidad. Calculá RMSE sobre train. Vas a obtener 0 (o casi). Discutí en una celda markdown por qué eso no significa que el modelo sea bueno.",
      "Cross-validation honesto. Corré cross_val_score(tree, X_prepared, y, scoring='neg_root_mean_squared_error', cv=10). Reportá media y desvío del RMSE (recordá negar el signo). Compará con el lineal evaluado con el mismo cv=10.",
      "Random Forest. Entrená RandomForestRegressor(n_estimators=100, random_state=42) y evaluá con CV de 10 folds. Esperá que la media baje a ~50k USD. Hacé una tabla markdown con los 3 modelos: media ± desvío.",
      "Learning curve. Usá sklearn.model_selection.learning_curve sobre el Random Forest con train_sizes=np.linspace(0.1, 1.0, 5). Plotteá train_score y val_score vs tamaño. Diagnosticá: ¿alta varianza, alto bias, o convergencia?"
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/056-seleccion-y-entrenamiento-de-modelo/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/057-fine-tuning-grid-search-randomized-search",
    "number": 57,
    "slug": "057-fine-tuning-grid-search-randomized-search",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Fine-tuning: grid search y randomized search",
    "description": "Que el alumno deje de tunear hiperparámetros \"a ojo\" y use búsquedas sistemáticas con validación cruzada — GridSearchCV cuando el espacio es chico y discreto, RandomizedSearchCV cuando es grande o continuo — integradas…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Que el alumno deje de tunear hiperparámetros \"a ojo\" y use búsquedas sistemáticas con validación cruzada — GridSearchCV cuando el espacio es chico y discreto, RandomizedSearchCV cuando es grande o continuo — integradas dentro de un Pipeline para evitar data leakage del preprocesamiento.",
    "outcomes": [
      "Distinguir parámetros entrenados (pesos del modelo) de hiperparámetros (los que vos fijás antes del fit).",
      "Configurar GridSearchCV con param_grid, cv, scoring, n_jobs=-1 y leer best_params_ / best_estimator_ / cv_results_.",
      "Usar RandomizedSearchCV con param_distributions (scipy.stats: randint, uniform, loguniform) y n_iter para presupuestar trials.",
      "Integrar HPO dentro de un Pipeline usando claves del tipo 'step__hparam' para tunear preprocesamiento + modelo juntos.",
      "Decidir grid vs random vs bayesiano según tamaño del espacio, costo por fit y continuidad de los hiperparámetros."
    ],
    "topics": [
      "Hiperparámetros vs parámetros",
      "param_grid y scoring",
      "cv y n_jobs=-1",
      "GridSearchCV",
      "RandomizedSearchCV con distribuciones (randint, loguniform)",
      "Pipelines + HPO con sintaxis step__hparam",
      "Inspeccionar cv_results_"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "GridSearchCV sobre RandomForestRegressor. California Housing. param_grid con n_estimators ∈ {50, 100, 200} y max_features ∈ {4, 6, 8}. cv=5, scoring='neg_root_mean_squared_error', n_jobs=-1. Reportá best_params_ y RMSE en test.",
      "RandomizedSearchCV con distribuciones. Mismo dataset, ahora con n_estimators=randint(50, 500), max_features=randint(2, 8), min_samples_leaf=randint(1, 20). n_iter=30. Compará tiempo y score vs el grid del ej. 1.",
      "Pipeline + HPO. Construí Pipeline([('scaler', StandardScaler()), ('svr', SVR())]). Tuneá svr__C con loguniform(1e-1, 1e3) y svr__gamma con loguniform(1e-4, 1e-1). Mostrá por qué meter el StandardScaler afuera del CV sería data leakage.",
      "Inspección de cv_results_. Cargá search.cv_results_ en un DataFrame, ordenalo por mean_test_score y plotteá score vs n_estimators. ¿Hay meseta? ¿Vale subir más?",
      "Optuna sobre el mismo problema. Repetí el ej. 2 pero con Optuna (n_trials=30, TPESampler, MedianPruner). Compará score final y tiempo con RandomizedSearchCV. Mostrá study.best_params y un plot de optuna.visualization.plot_optimization_history."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/057-fine-tuning-grid-search-randomized-search/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/058-optuna-bayesian-hpo-dedicado",
    "number": 58,
    "slug": "058-optuna-bayesian-hpo-dedicado",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Optuna y HPO bayesiano dedicado",
    "description": "Profundizar en Optuna —el framework de hyperparameter optimization estándar industrial 2026— aplicado a ML clásico (sklearn, XGBoost, LightGBM, CatBoost).",
    "level": "Intermedio",
    "duration": "80 min",
    "theory": "Profundizar en Optuna —el framework de hyperparameter optimization estándar industrial 2026— aplicado a ML clásico (sklearn, XGBoost, LightGBM, CatBoost). Pasar de Grid/Random Search (clase 052) a TPE (Tree-structured Parzen Estimator) + Hyperband Pruner + persistencia con SQLite. Aprender a interpretar plot_optimization_history, plot_param_importances y plot_slice para entender qué hiperparámetros mueven la aguja.",
    "outcomes": [
      "Definir un objective(trial) con suggest_int, suggest_float, suggest_categorical, suggest_float('lr', 1e-5, 1e-1, log=True).",
      "Aplicar TPE (default) vs CmaEs vs NSGAIISampler (multi-objective).",
      "Aplicar pruners (MedianPruner, HyperbandPruner) para cortar trials malos temprano.",
      "Persistir el study con storage='sqlite:///study.db' y resumir trials.",
      "Visualizar e interpretar los 5 plots de Optuna.",
      "Comparar costo total: Grid Search (1000 trials) vs Optuna (100 trials) llegan a mismo accuracy."
    ],
    "topics": [
      "TPE: modela P(x | y < γ) y P(x | y ≥ γ) con KDE; samplea de la primera.",
      "Pruning: callback que reporta progreso intermedio; si va mal vs históricos, kill.",
      "Multi-objective: optimizar accuracy AND latencia.",
      "Distributed: varios workers contra el mismo SQLite/PostgreSQL.",
      "Integration con sklearn, XGBoost, LightGBM, CatBoost."
    ],
    "materials": [
      "sklearn.datasets.fetch_california_housing (regresión) o fetch_openml('credit-g') (clasificación).",
      "Librerías: optuna, optuna-integration, scikit-learn, xgboost, lightgbm."
    ],
    "exercises": [
      "Objective básico: tunear LogisticRegression(C, penalty) y RandomForest(n_estimators, max_depth) con TPE. 50 trials.",
      "Search space compuesto: hiperparámetros condicionales (e.g., solver=liblinear solo permite ciertos penalty). Optuna lo maneja con if.",
      "Pruning en XGBoost: usar XGBoostPruningCallback que reporta validación por boosting round → mata trials malos.",
      "Persistencia: optuna.create_study(study_name='exp1', storage='sqlite:///opt.db', load_if_exists=True). Re-correr y agregar trials.",
      "Multi-objective: maximizar accuracy AND minimizar inference time; obtener Pareto front con optuna.create_study(directions=['maximize', 'minimize'])."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/058-optuna-bayesian-hpo-dedicado/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/059-launch-monitoreo-y-mantenimiento",
    "number": 59,
    "slug": "059-launch-monitoreo-y-mantenimiento",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Launch, monitoreo y mantenimiento de modelos",
    "description": "Que el alumno entienda que entrenar el modelo es la mitad del trabajo: el resto es ponerlo en producción de forma segura, monitorearlo para detectar degradación (data drift, model drift) y mantenerlo vivo con un ciclo d…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno entienda que entrenar el modelo es la mitad del trabajo: el resto es ponerlo en producción de forma segura, monitorearlo para detectar degradación (data drift, model drift) y mantenerlo vivo con un ciclo de retraining. Además, documentar el modelo con una Model Card para que terceros (compliance, negocio, usuarios) sepan qué hace, dónde falla y qué no hay que hacerle.",
    "outcomes": [
      "Diseñar un pipeline de deploy mínimo (serialización con joblib, servicio detrás de una API, versionado del artefacto).",
      "Distinguir data drift de model drift y elegir métricas para cada uno (PSI, KS, accuracy en holdout móvil).",
      "Definir un retraining trigger (calendario fijo vs. trigger por drift vs. trigger por caída de KPI de negocio).",
      "Comparar estrategias de release (canary, shadow deploy, A/B test) y elegir según riesgo.",
      "Redactar una Model Card con secciones mínimas (uso previsto, métricas por subgrupo, limitaciones)."
    ],
    "topics": [
      "Pipeline de deploy: joblib.dump, contenedor, endpoint",
      "Data drift (inputs cambian) vs. model drift (performance baja)",
      "Métricas de drift: PSI, KS-test, distancia de Wasserstein",
      "Retraining: calendario, trigger por drift, trigger por KPI",
      "Estrategias de release: shadow, canary, A/B",
      "Alertas y observabilidad",
      "Model Cards y Datasheets",
      "Governance y rollback"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Serializar y cargar. Entrená un RandomForestClassifier sobre Titanic. Guardalo con joblib.dump. Cargalo en otro notebook y verificá que predice idéntico.",
      "Detectar data drift con PSI. Calculá Population Stability Index entre dos snapshots de la feature edad. Interpretá: PSI < 0.1 estable, 0.1-0.25 leve, > 0.25 drift significativo.",
      "KS-test para drift. Aplicá scipy.stats.ks_2samp a la feature monto entre snapshot1 y snapshot2. ¿p-valor < 0.05?",
      "Simular shadow deploy. Tenés modelo A (viejo) y B (nuevo). Pasá 1000 requests por ambos, logueá las predicciones y reportá tasa de desacuerdo.",
      "Redactar una Model Card. Tomá tu mejor modelo de la Parte 1 hasta ahora y completá una model card con las 7 secciones del complemento. Incluí al menos una métrica desagregada por subgrupo."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/059-launch-monitoreo-y-mantenimiento/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/060-model-cards-y-responsible-ml",
    "number": 60,
    "slug": "060-model-cards-y-responsible-ml",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Model Cards y Responsible ML",
    "description": "Aprender a documentar modelos para producción y auditoría: el Model Card (Mitchell et al.",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Aprender a documentar modelos para producción y auditoría: el Model Card (Mitchell et al. 2018, adoptado por Google y luego por la industria) — ficha estandarizada con: propósito, métricas, limitaciones, distribución de datos, riesgos. Conocer el EU AI Act (en vigor 2025-2026), NIST AI RMF, y las plantillas modernas (HuggingFace model cards, Datasheets for Datasets).",
    "outcomes": [
      "Escribir un Model Card completo con las 9 secciones de Mitchell et al.",
      "Distinguir un Model Card (sobre el modelo) de un Datasheet (sobre el dataset, Gebru et al. 2018).",
      "Reportar métricas por subgrupo (no solo global) — clave en fairness.",
      "Reconocer los 4 tiers de riesgo del EU AI Act (prohibido, alto, transparencia, mínimo).",
      "Aplicar el NIST AI RMF (Map, Measure, Manage, Govern) en un proyecto real."
    ],
    "topics": [
      "Secciones de un Model Card: Model Details, Intended Use, Factors, Metrics, Evaluation Data, Training Data, Quant Analyses, Ethical Considerations, Caveats.",
      "Métricas por subgrupo (sexo, edad, raza, geografía).",
      "HuggingFace Model Card auto-generation.",
      "EU AI Act: clasificación de riesgo, obligaciones por tier.",
      "NIST AI RMF: framework de gestión.",
      "ISO/IEC 42001 — sistema de gestión de IA."
    ],
    "materials": [
      "Modelo del proyecto end-to-end (clase 050).",
      "Plantilla HuggingFace: <https://huggingface.co/docs/hub/model-cards>.",
      "Librerías: model-card-toolkit (Google)."
    ],
    "exercises": [
      "Model Card básico: para un Random Forest entrenado en California Housing, llenar las 9 secciones. Salvar como MODEL_CARD.md junto al modelo.",
      "Subgroup metrics: para un clasificador de credit-g, reportar accuracy y FPR por sex y age_group. Identificar disparidades.",
      "Risk classification (EU AI Act): para 5 use cases (recomendación de películas, score crediticio, recurso humano selection, marketing email, detector de spam), clasificar el tier.",
      "HuggingFace Card: usar el template de HF; subirla a un repo público si tenés modelo en Hub.",
      "NIST RMF: para un proyecto propio, llenar las 4 categorías (Map: contexto, Measure: métricas, Manage: mitigaciones, Govern: ownership)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/060-model-cards-y-responsible-ml/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/061-crisp-dm-como-framework-metodologico",
    "number": 61,
    "slug": "061-crisp-dm-como-framework-metodologico",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "CRISP-DM como framework metodológico",
    "description": "Que el alumno entienda CRISP-DM (Cross-Industry Standard Process for Data Mining) como esqueleto metodológico para todo proyecto de ML/DS — sus 6 fases, su naturaleza iterativa (no en cascada), y cuándo conviene complem…",
    "level": "Intermedio",
    "duration": "50 min",
    "theory": "Que el alumno entienda CRISP-DM (Cross-Industry Standard Process for Data Mining) como esqueleto metodológico para todo proyecto de ML/DS — sus 6 fases, su naturaleza iterativa (no en cascada), y cuándo conviene complementarlo o reemplazarlo por TDSP de Microsoft o por el \"ML lifecycle moderno\" con MLOps. La idea es dejar de improvisar el orden del trabajo y tener un mapa al que volver cuando un proyecto se trabe.",
    "outcomes": [
      "Enumerar y explicar las 6 fases de CRISP-DM y los entregables típicos de cada una.",
      "Identificar la fase actual de un proyecto real y la próxima transición esperada.",
      "Definir business success criteria antes de tocar datos, distinguiéndolos de métricas técnicas (accuracy, RMSE).",
      "Reconocer iteraciones legítimas (volver de Evaluation a Business Understanding) vs. retrabajo por mala planificación.",
      "Comparar CRISP-DM con TDSP y el ML lifecycle moderno y elegir según contexto (PoC, equipo chico, producción seria, MLOps)."
    ],
    "topics": [
      "Business Understanding",
      "Data Understanding",
      "Data Preparation",
      "Modeling",
      "Evaluation",
      "Deployment",
      "Iteración + comparación TDSP / ML lifecycle"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Identificar la fase. Dadas 6 situaciones de proyecto (ej. \"estoy probando XGBoost vs Random Forest\", \"estoy graficando histogramas para ver outliers\"), asigná cada una a su fase CRISP-DM.",
      "Business success criteria. Para un caso de detección de fraude bancario, escribí 3 criterios de éxito de negocio (no técnicos) y 3 técnicos. Distinguilos claramente.",
      "Aplicar las 6 fases a un caso real. Elegí un problema (churn de Netflix, recomendación de productos, predicción de demanda en una panadería). Redactá un párrafo por cada fase con entregables concretos. Mínimo 1 iteración explícita (ej. \"vuelvo de Modeling a Data Preparation porque…\").",
      "Comparar frameworks. Tabla de 3 columnas (CRISP-DM, TDSP, ML lifecycle moderno con MLOps) y 5 filas (origen, fases, foco, herramientas, cuándo usarlo).",
      "Detectar iteración legítima vs retrabajo. Dados 4 escenarios de \"estoy volviendo a una fase anterior\", clasificalos como iteración esperada o como síntoma de mala planificación en la fase anterior."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/061-crisp-dm-como-framework-metodologico/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/062-clasificacion-binaria-con-mnist",
    "number": 62,
    "slug": "062-clasificacion-binaria-con-mnist",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Clasificación binaria con MNIST",
    "description": "Que el alumno arme su primer clasificador binario \"de verdad\" sobre MNIST (¿este dígito es un 5 o no?), entrenando un SGDClassifier, evaluándolo con cross_val_score sobre StratifiedKFold, y entendiendo por qué la accura…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno arme su primer clasificador binario \"de verdad\" sobre MNIST (¿este dígito es un 5 o no?), entrenando un SGDClassifier, evaluándolo con cross_val_score sobre StratifiedKFold, y entendiendo por qué la accuracy sola miente cuando las clases están desbalanceadas.",
    "outcomes": [
      "Cargar MNIST con fetch_openml('mnist_784', as_frame=False) y separar train/test respetando el split original (60k/10k).",
      "Construir un target binario y_train_5 = (y_train == 5) y entrenar un SGDClassifier sobre él.",
      "Predecir y obtener scores con predict() y decision_function(), entendiendo la diferencia entre clase y score continuo.",
      "Validar con cross_val_score sobre StratifiedKFold y leer los 3 valores que devuelve.",
      "Detectar el accuracy paradox: comparar contra un clasificador trivial \"nunca-5\" y ver que también saca ~90%."
    ],
    "topics": [
      "fetch_openml('mnist_784')",
      "Target binario 5 vs no-5",
      "SGDClassifier(random_state=42)",
      "cross_val_score + StratifiedKFold",
      "Accuracy paradox",
      "predict vs decision_function vs predict_proba"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Cargar y explorar. Cargá MNIST, imprimí X.shape y y.shape, mostrá un dígito con matplotlib.imshow(X[0].reshape(28, 28), cmap='binary') y verificá que y[0] == 5.",
      "Target binario + SGD. Construí y_train_5, entrená SGDClassifier(random_state=42) y predecí sobre X[0]. ¿Devuelve True?",
      "decision_function. Sobre la misma instancia, llamá a decision_function([X[0]]) y compará el signo con el resultado de predict.",
      "Cross-validation. Corré cross_val_score(sgd, X_train, y_train_5, cv=3, scoring='accuracy'). ¿Qué tres valores te da? ¿Cuál es el promedio?",
      "Baseline trampa. Implementá un Never5Classifier (clase con fit que no hace nada y predict que devuelve np.zeros(len(X), dtype=bool)) y corré el mismo cross_val_score. Comparalo con el SGD: ¿la diferencia es la que esperabas?"
    ],
    "codeExamples": [
      {
        "id": "parte-1-machine-learning-clasico/062-clasificacion-binaria-con-mnist-code-1",
        "title": "Bloque 1",
        "explanation": "Código incluido en el material de la clase.",
        "schema": "python · 7 líneas",
        "language": "python",
        "code": "from sklearn.datasets import fetch_openml\nmnist = fetch_openml('mnist_784', as_frame=False, parser='auto')\nX, y = mnist.data, mnist.target.astype(int)\nX_train, X_test = X[:60000], X[60000:]\ny_train, y_test = y[:60000], y[60000:]\ny_train_5 = (y_train == 5)\ny_test_5  = (y_test == 5)"
      }
    ],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/062-clasificacion-binaria-con-mnist/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/063-metricas-confusion-matrix-precision-recall-f1",
    "number": 63,
    "slug": "063-metricas-confusion-matrix-precision-recall-f1",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Métricas: confusion matrix, precision, recall, F1",
    "description": "Que el alumno deje de mirar accuracy como métrica única y aprenda a leer una confusion matrix, a elegir entre precision, recall, F1 o F-beta según el costo de los errores, y a interpretar classification_report clase por…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Que el alumno deje de mirar accuracy como métrica única y aprenda a leer una confusion matrix, a elegir entre precision, recall, F1 o F-beta según el costo de los errores, y a interpretar classification_report clase por clase. En particular, entender por qué en problemas desbalanceados (fraude, churn, diagnóstico) accuracy miente y qué hacer al respecto.",
    "outcomes": [
      "Construir e interpretar una confusion matrix con sklearn.metrics.confusion_matrix identificando TP, FP, TN, FN.",
      "Calcular y comparar precision, recall, F1 y F-beta a mano y con precision_score, recall_score, f1_score, fbeta_score.",
      "Elegir la métrica adecuada según el costo asimétrico de los errores (FP vs FN) del problema.",
      "Leer classification_report y diferenciar macro avg vs weighted avg en multiclase.",
      "Diagnosticar class imbalance y aplicar class_weight='balanced', SMOTE o threshold tuning según corresponda."
    ],
    "topics": [
      "Confusion matrix (TP/FP/TN/FN)",
      "Precision = TP / (TP+FP)",
      "Recall = TP / (TP+FN)",
      "F1 y F-beta",
      "classification_report y macro/weighted avg",
      "Accuracy y por qué falla con clases desbalanceadas",
      "Class imbalance: class_weight, SMOTE, threshold tuning"
    ],
    "materials": [
      "MNIST 5-vs-not-5 (binarizado): clásico de Géron cap. 3. Imbalance ~10% positivo.",
      "Credit card fraud (Kaggle, opcional): ~0.17% positivo, ideal para ver SMOTE en acción.",
      "Sintético con make_classification(weights=[0.99, 0.01]) para experimentar sin descargar."
    ],
    "exercises": [
      "Confusion matrix a mano. Dado y_true = [0,1,1,0,1,1,0,0,1,0] y y_pred = [0,1,0,0,1,1,1,0,1,0]: calculá TP/FP/TN/FN, precision, recall y F1 con lápiz y papel. Verificá con sklearn.metrics.",
      "MNIST 5-detector. Entrená SGDClassifier sobre MNIST binarizado (5 vs no-5). Mostrá confusion matrix con ConfusionMatrixDisplay y reportá precision, recall y F1.",
      "classification_report multiclase. Sobre MNIST completo (10 clases) con LogisticRegression, imprimí classification_report. Identificá qué dígito tiene peor recall y por qué (mirá la confusion matrix).",
      "Class imbalance con class_weight. Generá un dataset con make_classification(n_samples=10000, weights=[0.99, 0.01], random_state=42). Entrená dos LogisticRegression: una sin class_weight y otra con class_weight='balanced'. Compará recall de la clase minoritaria.",
      "SMOTE dentro de Pipeline. Mismo dataset que el ejercicio 4. Armá un imblearn.pipeline.Pipeline con SMOTE + LogisticRegression, evaluá con cross_val_score(scoring='f1') y compará contra class_weight='balanced'. Verificá que SMOTE solo se aplica al train fold (leelo en docs)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/063-metricas-confusion-matrix-precision-recall-f1/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/064-class-imbalance-smote-adasyn-class-weight",
    "number": 64,
    "slug": "064-class-imbalance-smote-adasyn-class-weight",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Class imbalance: SMOTE, ADASYN, class_weight, threshold tuning",
    "description": "Tratar datasets desbalanceados —fraude (1 % positivo), churn (5 %), enfermedades raras—.",
    "level": "Intermedio",
    "duration": "80 min",
    "theory": "Tratar datasets desbalanceados —fraude (1 % positivo), churn (5 %), enfermedades raras—. Las trampas son sutiles: accuracy puede ser 99 % con un clasificador trivial. Cubrir las 4 estrategias estándar: class_weight, threshold tuning, oversampling (SMOTE, ADASYN), undersampling (Tomek, ENN). Y la decisión clave: ¿qué métrica reportar? (F1, PR-AUC, MCC, no accuracy).",
    "outcomes": [
      "Detectar imbalance: value_counts(normalize=True). Decidir si > 10:1 amerita tratamiento.",
      "Aplicar class_weight='balanced' o pesos custom en sklearn.",
      "Aplicar threshold tuning: optimizar el umbral de decisión sobre la curva PR según la métrica del negocio.",
      "Usar SMOTE (synthetic minority over-sampling) de imbalanced-learn: SMOTE(k_neighbors=5).fit_resample(X, y).",
      "Combinar oversampling + undersampling (SMOTETomek, SMOTEENN).",
      "Reportar PR-AUC y MCC (Matthews Correlation Coefficient) en lugar de accuracy."
    ],
    "topics": [
      "Imbalance ratio: >10:1 problemático.",
      "Métricas: precision, recall, F1, F-beta, PR-AUC, MCC.",
      "class_weight: penalizar más errores en minoría durante training.",
      "Threshold tuning: mover el umbral fuera del 0.5 default.",
      "SMOTE: interpola entre vecinos de la minoría.",
      "ADASYN: como SMOTE pero con más densidad en zonas \"difíciles\".",
      "Tomek links / ENN: remueve borderline de la mayoría.",
      "imbalanced-learn pipelines."
    ],
    "materials": [
      "fetch_openml('creditcardfraud') (Kaggle, 0.17 % positivo).",
      "Librerías: imbalanced-learn (pip install imbalanced-learn), scikit-learn."
    ],
    "exercises": [
      "Baseline sin tratamiento: LogisticRegression en creditcardfraud. Accuracy alto, recall pésimo.",
      "class_weight: LogisticRegression(class_weight='balanced'). Recall sube, precision baja.",
      "Threshold tuning: con probabilidades de predict_proba, barrer thresholds y plotear F1 vs threshold. Elegir el óptimo.",
      "SMOTE: from imblearn.over_sampling import SMOTE; X_res, y_res = SMOTE().fit_resample(X_train, y_train). Entrenar y evaluar.",
      "Pipeline imblearn: Pipeline([('smote', SMOTE()), ('clf', LogisticRegression())]). Importante: SMOTE solo se aplica en train (imblearn pipeline lo maneja)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/064-class-imbalance-smote-adasyn-class-weight/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/065-precision-recall-tradeoff",
    "number": 65,
    "slug": "065-precision-recall-tradeoff",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Precision/Recall tradeoff",
    "description": "Que el alumno entienda que no se puede maximizar precision y recall al mismo tiempo: mover el threshold de decisión sube uno y baja el otro.",
    "level": "Intermedio",
    "duration": "50 min",
    "theory": "Que el alumno entienda que no se puede maximizar precision y recall al mismo tiempo: mover el threshold de decisión sube uno y baja el otro. La clase enseña a usar decision_function + precision_recall_curve para elegir el threshold según el costo del negocio, no según el default de 0.",
    "outcomes": [
      "Explicar el tradeoff entre precision y recall en términos del threshold del clasificador.",
      "Obtener scores crudos con decision_function(X) (o predict_proba) en vez de quedarse con predict.",
      "Calcular la curva con precision_recall_curve(y_true, scores) y graficarla.",
      "Elegir un threshold que cumpla una restricción del negocio (ej: precision ≥ 90%).",
      "Reportar average_precision_score como métrica resumen única de la curva."
    ],
    "topics": [
      "Threshold de decisión: el default 0 no es sagrado",
      "decision_function vs predict_proba vs predict",
      "precision_recall_curve",
      "Elegir threshold según restricción de negocio",
      "average_precision_score (AP)",
      "Cuándo PR > ROC"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Score crudo. Entrená SGDClassifier sobre MNIST binario \"es 5\". Para una imagen concreta, llamá sgd.decision_function([X[0]]) y compará con sgd.predict([X[0]]). Mostrá que predict es decision_function > 0.",
      "Curva PR. Con cross_val_predict(sgd, X_train, y_train_5, cv=3, method='decision_function') obtené y_scores. Pasalos a precision_recall_curve y graficá precision y recall vs threshold en el mismo eje.",
      "Threshold para precision ≥ 90%. Encontrá el threshold mínimo que garantice precision >= 0.90. Pista: thresholds[np.argmax(precisions >= 0.90)]. Aplicalo: y_pred_90 = (y_scores >= threshold_90) y verificá precision y recall resultantes.",
      "Curva precision vs recall. Graficá precision (eje Y) contra recall (eje X) — la forma canónica de la curva PR. Marcá el punto correspondiente al threshold por default (0).",
      "Average precision. Calculá average_precision_score(y_train_5, y_scores). Compará con el F1 que sacaste en la clase 056. ¿Cuál te parece más informativo?"
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/065-precision-recall-tradeoff/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/066-curva-roc-y-auc",
    "number": 66,
    "slug": "066-curva-roc-y-auc",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Curva ROC y AUC",
    "description": "Que el alumno entienda qué mide la curva ROC, calcule el AUC con scikit-learn y sepa decidir cuándo ROC es la métrica adecuada y cuándo conviene usar Precision-Recall — sobre todo en datasets desbalanceados, donde ROC t…",
    "level": "Intermedio",
    "duration": "50 min",
    "theory": "Que el alumno entienda qué mide la curva ROC, calcule el AUC con scikit-learn y sepa decidir cuándo ROC es la métrica adecuada y cuándo conviene usar Precision-Recall — sobre todo en datasets desbalanceados, donde ROC tiende a mentir.",
    "outcomes": [
      "Construir la curva ROC con roc_curve graficando TPR vs FPR a distintos umbrales.",
      "Calcular el AUC con roc_auc_score e interpretar el valor (0.5 = azar, 1.0 = perfecto).",
      "Comparar dos clasificadores superponiendo sus curvas ROC y eligiendo por AUC.",
      "Decidir ROC vs PR según la prevalencia de la clase positiva.",
      "Evitar la trampa del desbalance: reconocer cuándo un AUC alto esconde mala precisión."
    ],
    "topics": [
      "TPR (recall) y FPR",
      "Curva ROC con roc_curve",
      "AUC con roc_auc_score",
      "Diagonal de azar y modelo perfecto",
      "ROC vs Precision-Recall",
      "Comparación de modelos"
    ],
    "materials": [
      "sklearn.datasets.fetch_openml('mnist_784') con el clasificador binario \"es un 5\" (Géron cap. 3), naturalmente desbalanceado (~10% positivos).",
      "Opcional: dataset sintético desbalanceado vía make_classification(weights=[0.99, 0.01]) para ver el contraste ROC vs PR en extremo."
    ],
    "exercises": [
      "Scores y curva ROC. Entrená un SGDClassifier sobre \"es un 5\", obtené scores con cross_val_predict(..., method='decision_function') y graficá la curva ROC con roc_curve.",
      "AUC. Calculá roc_auc_score(y_true, y_scores). Interpretá el valor en una línea.",
      "Comparar dos modelos. Entrená un RandomForestClassifier (usá predict_proba, columna 1) y superponé ambas curvas ROC en un mismo plot. Elegí el mejor por AUC.",
      "ROC vs PR en desbalance. Generá make_classification(weights=[0.99, 0.01], n_samples=10_000), entrená un modelo decente y graficá lado a lado curva ROC y curva PR (precision_recall_curve). Mostrá cómo ROC sigue \"linda\" mientras PR revela la pobreza real.",
      "Punto operativo. Sobre la curva ROC del ejercicio 1, encontrá el umbral que maximiza TPR - FPR (índice de Youden) y reportá precision y recall en ese punto."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/066-curva-roc-y-auc/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/067-clasificacion-multiclase-multilabel-multioutput",
    "number": 67,
    "slug": "067-clasificacion-multiclase-multilabel-multioutput",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Clasificación multiclase, multilabel, multioutput",
    "description": "Que el alumno distinga los tres escenarios de clasificación más allá del binario — multiclase (una salida con K>2 clases), multilabel (varias etiquetas por muestra) y multioutput (varias salidas, cada una con su propio…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno distinga los tres escenarios de clasificación más allá del binario — multiclase (una salida con K>2 clases), multilabel (varias etiquetas por muestra) y multioutput (varias salidas, cada una con su propio rango de valores) — y sepa qué estrategia de sklearn (OneVsRest, OneVsOne, MultiOutputClassifier) usar en cada caso, eligiendo además la métrica correcta (accuracy global, hamming loss, macro/micro F1).",
    "outcomes": [
      "Diferenciar multiclase, multilabel y multioutput con un ejemplo concreto de cada uno.",
      "Elegir entre OvR y OvO según el costo computacional del clasificador base y el tamaño del dataset.",
      "Entrenar un clasificador multilabel con KNeighborsClassifier y evaluarlo con f1_score(average='macro') y hamming_loss.",
      "Envolver un clasificador binario en MultiOutputClassifier para resolver un problema multioutput.",
      "Interpretar las salidas de predict_proba en cada escenario (lista de arrays vs array 2D)."
    ],
    "topics": [
      "Multiclase: definición y clasificadores nativos",
      "OneVsRestClassifier (OvR)",
      "OneVsOneClassifier (OvO)",
      "Multilabel: y es matriz binaria K-dim",
      "Métricas multilabel: hamming loss, macro/micro F1",
      "Multioutput: MultiOutputClassifier / MultiOutputRegressor"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Multiclase nativo vs OvR. Entrená SGDClassifier en MNIST (10 clases) y comparalo con OneVsRestClassifier(SGDClassifier()). ¿Cuántos clasificadores entrena cada uno? Mirá .estimators_.",
      "OvO con SVM. Entrená SVC() sobre un subset de 5k muestras de MNIST. Verificá que clf.decision_function(X[:1]) devuelve 45 scores = 10·9/2. Forzá luego OneVsRestClassifier(SVC()) y compará tiempos.",
      "Multilabel con KNN. Construí Y_multilabel = np.c_[y >= 7, y % 2 == 1]. Entrená KNeighborsClassifier() con ese Y. Reportá f1_score(Y_test, Y_pred, average='macro') y hamming_loss(Y_test, Y_pred).",
      "Macro vs micro F1. Con el modelo del ejercicio 3, calculá F1 con average='macro' y average='micro'. Si una de las etiquetas estuviera muy desbalanceada (ej.: solo 5% de positivos), ¿cuál cambiaría más y por qué?",
      "Multioutput denoising. Generá X_train_noisy = X_train + np.random.randint(0, 100, X_train.shape). Entrená KNeighborsClassifier() con X_noisy como features y X_clean como target (cada píxel es una salida multiclase 0–255). Predecí y visualizá una imagen denoised."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/067-clasificacion-multiclase-multilabel-multioutput/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/068-analisis-de-errores",
    "number": 68,
    "slug": "068-analisis-de-errores",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Análisis de errores",
    "description": "Que el alumno deje de mirar el accuracy global y empiece a auditar dónde se equivoca un clasificador: confusion matrix normalizada por fila, pares de clases confundidas, inspección visual de ejemplos mal clasificados, y…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno deje de mirar el accuracy global y empiece a auditar dónde se equivoca un clasificador: confusion matrix normalizada por fila, pares de clases confundidas, inspección visual de ejemplos mal clasificados, y el loop de error analysis como puerta de entrada al data-centric AI (mejorar datos, no solo modelos).",
    "outcomes": [
      "Construir y normalizar una confusion matrix por fila (recall por clase) y leerla sin confundir filas con columnas.",
      "Identificar pares de clases confundidas ordenando los off-diagonals normalizados de mayor a menor.",
      "Inspeccionar visualmente ejemplos mal clasificados (hard examples) para formular hipótesis de causa raíz.",
      "Decidir si la próxima iteración mejora el modelo (features, regularización, capacidad) o mejora los datos (relabel, augmentación, balancear).",
      "Ejecutar el error analysis loop: entrenar → matriz → slices → hipótesis → fix → re-entrenar."
    ],
    "topics": [
      "Confusion matrix cruda vs normalizada por fila",
      "Off-diagonals: qué clase se confunde con cuál",
      "Inspección visual de hard examples",
      "Slice analysis (error por subgrupo)",
      "Data-centric AI: cuándo arreglar datos",
      "Error analysis loop"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Matriz cruda y normalizada. Entrená un SGDClassifier sobre MNIST. Calculá confusion_matrix(y_true, y_pred) y normalizá por fila (cm / cm.sum(axis=1, keepdims=True)). Plotealá con plt.matshow y poné ceros en la diagonal para que los errores se vean.",
      "Top-5 confusiones. Del array normalizado, extraé los 5 pares (i, j) con mayor valor off-diagonal. Imprimí \"real=i → pred=j: XX%\".",
      "Galería de errores. Para el par (real, pred) peor del ejercicio 2, mostrá una grilla 5×5 de imágenes mal clasificadas. Anotá si te parecen ambiguas, mal labeladas o claramente del label real.",
      "Slice por grosor de trazo. Calculá la suma de píxeles por imagen como proxy de \"grosor\". Dividí el test set en terciles y reportá accuracy por tercil. ¿El modelo es peor con dígitos finos o gruesos?",
      "Intervención data-centric. Tomá el par confundido del ejercicio 2. Augmentá el set de entrenamiento solo con esa clase (shifts de 1px) y re-entrená. Reportá el cambio en el recall de esa clase y el accuracy global."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/068-analisis-de-errores/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/069-regresion-lineal-ecuacion-normal-vs-gradient-descent",
    "number": 69,
    "slug": "069-regresion-lineal-ecuacion-normal-vs-gradient-descent",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Regresión lineal: ecuación normal vs gradient descent",
    "description": "Que el alumno entienda regresión lineal desde adentro: la hipótesis $\\hat{y} = \\theta^T x$, por qué se usa MSE como costo, las dos formas de resolverla (ecuación normal cerrada vs gradient descent iterativo), y cuándo c…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno entienda regresión lineal desde adentro: la hipótesis $\\hat{y} = \\theta^T x$, por qué se usa MSE como costo, las dos formas de resolverla (ecuación normal cerrada vs gradient descent iterativo), y cuándo conviene cada una según el tamaño del dataset y la cantidad de features.",
    "outcomes": [
      "Escribir la hipótesis lineal $\\hat{y} = \\theta_0 + \\theta_1 x_1 + \\dots + \\theta_n x_n$ en forma matricial $X\\theta$.",
      "Derivar la ecuación normal $\\theta = (X^T X)^{-1} X^T y$ y resolverla con NumPy.",
      "Usar LinearRegression de sklearn y entender que internamente usa pseudoinversa SVD (más estable que la ecuación normal).",
      "Comparar complejidad: ecuación normal $O(n^3)$ en features vs gradient descent $O(n)$ por iteración.",
      "Justificar la elección entre forma cerrada y GD según $n$ features y $m$ muestras."
    ],
    "topics": [
      "Hipótesis lineal y notación vectorial",
      "MSE como función de costo",
      "Ecuación normal (forma cerrada)",
      "Pseudoinversa SVD",
      "Gradient descent (intuición)",
      "Complejidad computacional"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Hipótesis a mano. Generá $X$ sintético ($m=100$, $n=1$) con $y = 4 + 3x + \\mathcal{N}(0, 1)$. Resolvé $\\hat{\\theta}$ con la ecuación normal usando solo NumPy (np.linalg.inv, @). Verificá que $\\hat{\\theta} \\approx [4, 3]$.",
      "Pseudoinversa. Repetí el ejercicio 1 con np.linalg.pinv(X_b) @ y. Compará el resultado con la ecuación normal — deberían dar lo mismo en este caso bien-condicionado.",
      "sklearn. Ajustá LinearRegression al mismo dataset. Verificá que lin_reg.intercept_ ≈ 4 y lin_reg.coef_ ≈ [3]. Predecí en $x = [[0], [2]]$.",
      "Caso singular. Construí $X$ con dos features colineales ($x_2 = 2 x_1$). Intentá la ecuación normal — np.linalg.inv tira LinAlgError o devuelve basura. Usá np.linalg.pinv y observá que sí funciona (distribuye el peso entre las dos features).",
      "Complejidad empírica. Cronometrá LinearRegression().fit(X, y) con $n = 100, 1000, 10000$ features (y $m$ fijo). Graficá el tiempo — debería crecer cúbicamente."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/069-regresion-lineal-ecuacion-normal-vs-gradient-descent/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/070-gradient-descent-batch-stochastic-mini-batch",
    "number": 70,
    "slug": "070-gradient-descent-batch-stochastic-mini-batch",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Gradient Descent: batch, stochastic, mini-batch",
    "description": "Que el alumno entienda gradient descent como motor de optimización para entrenar modelos lineales cuando la ecuación normal no escala, y sepa elegir entre batch (BGD), stochastic (SGD) y mini-batch GD según tamaño del d…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno entienda gradient descent como motor de optimización para entrenar modelos lineales cuando la ecuación normal no escala, y sepa elegir entre batch (BGD), stochastic (SGD) y mini-batch GD según tamaño del dataset, ruido tolerable y costo por iteración. Que además dimensione el rol del learning rate y del feature scaling, y use SGDRegressor de scikit-learn.",
    "outcomes": [
      "Explicar el gradiente de la MSE en regresión lineal y por qué moverse en -∇ minimiza el costo.",
      "Diferenciar BGD vs SGD vs mini-batch en términos de costo por iteración, varianza del paso y memoria.",
      "Diagnosticar la curva de costo (divergente, oscilante, lenta, suave) e inferir si el learning_rate está mal seteado.",
      "Aplicar feature scaling (StandardScaler) antes de cualquier GD y justificar por qué sin escalado SGD diverge o tarda 100×.",
      "Entrenar SGDRegressor con learning_rate='invscaling' y comparar coeficientes contra LinearRegression (ecuación normal)."
    ],
    "topics": [
      "Gradiente de la MSE y regla de update θ := θ - η·∇",
      "Batch GD: usa todo el dataset por step",
      "Stochastic GD: 1 muestra por step",
      "Mini-batch GD: lotes de 32–256",
      "Learning rate η y learning schedule",
      "Feature scaling como prerrequisito",
      "SGDRegressor de sklearn"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "BGD a mano. Implementá BGD en NumPy para regresión lineal sobre un dataset sintético (y = 4 + 3x + ruido). Loopeá 1000 iteraciones con η=0.1. Graficá la trayectoria de θ₀, θ₁ y la curva de costo.",
      "SGD a mano. Mismo dataset. Implementá SGD con learning_schedule η_t = 5 / (50 + t). Compará la trayectoria contra BGD: tendría que ser visiblemente más ruidosa pero más rápida en wall-clock.",
      "Efecto del learning rate. Corré BGD con η ∈ {0.001, 0.01, 0.1, 0.5, 1.0}. Graficá las 5 curvas de costo en un mismo plot. Identificá cuál diverge y cuál es absurdamente lenta.",
      "Scaling sí/no. Sobre California Housing, entrená SGDRegressor (a) sin escalar y (b) con StandardScaler. Reportá n_iter_ y score en cada caso. Tiene que haber un orden de magnitud de diferencia.",
      "SGDRegressor vs LinearRegression. Entrená ambos sobre California Housing escalado. Compará coeficientes y R². Tienen que dar muy parecidos (SGD es aproximación estocástica de la solución cerrada)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/070-gradient-descent-batch-stochastic-mini-batch/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/071-regresion-polinomial",
    "number": 71,
    "slug": "071-regresion-polinomial",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Regresión polinomial",
    "description": "Que el alumno ajuste modelos lineales a relaciones no lineales usando PolynomialFeatures de scikit-learn, entienda la combinatoria de features que esto genera, y reconozca el riesgo de overfitting cuando el grado crece.",
    "level": "Intermedio",
    "duration": "50 min",
    "theory": "Que el alumno ajuste modelos lineales a relaciones no lineales usando PolynomialFeatures de scikit-learn, entienda la combinatoria de features que esto genera, y reconozca el riesgo de overfitting cuando el grado crece.",
    "outcomes": [
      "Transformar features con PolynomialFeatures(degree=d) y entender qué columnas produce.",
      "Ajustar un LinearRegression sobre features polinómicas y graficar la curva resultante.",
      "Calcular cuántas features genera grado d con n variables originales (combinatoria con repetición).",
      "Diagnosticar overfitting comparando RMSE en train vs test al subir el grado.",
      "Decidir cuándo usar interaction_only=True vs incluir potencias."
    ],
    "topics": [
      "Modelo lineal sobre features no lineales",
      "PolynomialFeatures(degree, include_bias, interaction_only)",
      "Combinatoria de features: C(n+d, d)",
      "Overfitting con grado alto",
      "Validación con train/test split",
      "Interaction-only vs full polynomial"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Generar dataset cuadrático. x = np.linspace(-3, 3, 100) + ruido. Graficar scatter.",
      "Ajustar grado 2. PolynomialFeatures(degree=2, include_bias=False) + LinearRegression. Imprimir coef_ e intercept_ y compararlos con los del DGP (0.5, 1, 2).",
      "Grafo de curvas. Ajustar grados 1, 2, 5, 30 sobre el mismo dataset y plotear las 4 curvas superpuestas al scatter. Observar oscilaciones en grado 30.",
      "Curva train/test vs grado. Para grado 1 a 20, calcular RMSE en train y en test. Graficar ambas curvas en función del grado. Identificar el punto donde test empieza a subir.",
      "Combinatoria. Con n_features=3 de entrada, contar columnas que devuelve PolynomialFeatures(degree=4, include_bias=False). Verificar con la fórmula C(n+d, d) - 1."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/071-regresion-polinomial/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/072-curvas-de-aprendizaje-bias-variance",
    "number": 72,
    "slug": "072-curvas-de-aprendizaje-bias-variance",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Curvas de aprendizaje y bias-variance tradeoff",
    "description": "Diagnosticar si un modelo sufre de alto sesgo o alta varianza leyendo curvas de aprendizaje (sklearn.model_selection.learning_curve) y decidir, con criterio, si conviene conseguir más datos, aumentar la capacidad del mo…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Diagnosticar si un modelo sufre de alto sesgo o alta varianza leyendo curvas de aprendizaje (sklearn.model_selection.learning_curve) y decidir, con criterio, si conviene conseguir más datos, aumentar la capacidad del modelo o regularizar.",
    "outcomes": [
      "Graficar una curva de aprendizaje (RMSE train vs. RMSE validación en función de train_size) con learning_curve.",
      "Identificar patrones canónicos: underfitting (curvas altas y juntas) vs. overfitting (gap persistente).",
      "Descomponer conceptualmente el error esperado en bias² + variance + irreducible noise.",
      "Decidir acción correctiva apropiada: más datos, más capacidad, features nuevas, o regularización.",
      "Justificar por qué \"más datos\" no siempre es la solución (caso de high bias)."
    ],
    "topics": [
      "Curva de aprendizaje: qué se plotea y cómo se lee.",
      "Patrón de underfitting: ambas curvas convergen alto → más datos no ayuda.",
      "Patrón de overfitting: gap grande train/val → más datos sí ayuda, o regularizar.",
      "Descomposición bias-variance del error de generalización.",
      "Error irreducible (ruido de Bayes): cota inferior inevitable.",
      "Tradeoff: aumentar capacidad ↓ bias pero ↑ variance.",
      "Diagnóstico operacional con learning_curve y validation_curve."
    ],
    "materials": [
      "Dataset sintético tipo \"noisy quadratic\": y = 0.5·x² + x + 2 + ε con np.random.randn. Permite controlar la",
      "sklearn.datasets.fetch_california_housing (subset) para una corrida sobre datos reales.",
      "API clave: sklearn.model_selection.learning_curve, validation_curve."
    ],
    "exercises": [
      "Curva base. Generá 200 puntos del dataset cuadrático ruidoso. Ajustá una regresión lineal y graficá la curva",
      "Aumentar capacidad. Repetí con PolynomialFeatures(degree=2) + LinearRegression. Comparalo con degree=10.",
      "¿Más datos ayudan? Para el polinomio de grado 10, extendé el dataset a 2000 puntos y volvé a plotear.",
      "Validation curve. Usá validation_curve para barrer degree de 1 a 15 sobre el mismo dataset. Encontrá el",
      "Bias-variance empírico. Entrená 100 modelos degree=10 sobre bootstraps del dataset y calculá, para una grilla"
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/072-curvas-de-aprendizaje-bias-variance/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/073-regularizacion-ridge-lasso-elastic-net",
    "number": 73,
    "slug": "073-regularizacion-ridge-lasso-elastic-net",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Regularización: Ridge, Lasso, Elastic Net",
    "description": "Aprender a controlar el overfitting en modelos lineales mediante regularización L2 (Ridge), L1 (Lasso) y su combinación (Elastic Net), entendiendo el rol del hiperparámetro alpha, la importancia del scaling, y cuándo co…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Aprender a controlar el overfitting en modelos lineales mediante regularización L2 (Ridge), L1 (Lasso) y su combinación (Elastic Net), entendiendo el rol del hiperparámetro alpha, la importancia del scaling, y cuándo conviene cada variante.",
    "outcomes": [
      "Explicar qué es la regularización y por qué reduce la varianza de un modelo lineal.",
      "Implementar Ridge, Lasso y ElasticNet de scikit-learn sobre un dataset escalado.",
      "Tunear alpha con RidgeCV / LassoCV / ElasticNetCV y leer los coeficientes resultantes.",
      "Justificar la elección entre L1, L2 y L1+L2 según el problema (multicolinealidad, sparsity, número de features).",
      "Diagnosticar por qué Lasso \"anula\" features y Ridge solo las \"encoge\"."
    ],
    "topics": [
      "Sesgo–varianza y motivación de la regularización.",
      "Ridge (L2): penalización α · Σβ². Encoge coeficientes hacia cero sin anularlos.",
      "Lasso (L1): penalización α · Σ|β|. Produce soluciones sparse (selección de features).",
      "Elastic Net: combinación L1+L2 con l1_ratio.",
      "Hiperparámetro alpha: efecto en bias/varianza; α=0 ≡ OLS; α→∞ ≡ modelo nulo.",
      "Scaling obligatorio (StandardScaler) antes de regularizar.",
      "Selección de α con CV: RidgeCV, LassoCV, ElasticNetCV."
    ],
    "materials": [
      "Dataset sugerido: sklearn.datasets.fetch_california_housing (regresión continua, 8 features con escalas distintas → ideal para mostrar scaling).",
      "Alternativa sintética: make_regression(n_features=50, n_informative=10, noise=10) para ver cómo Lasso anula las 40 no informativas.",
      "Stack: numpy, pandas, scikit-learn (Ridge, Lasso, ElasticNet, RidgeCV, LassoCV, ElasticNetCV, StandardScaler, Pipeline)."
    ],
    "exercises": [
      "OLS baseline: entrená LinearRegression sobre California Housing escalado. Reportá RMSE en train y test. Anotá los coeficientes.",
      "Ridge: entrená Ridge(alpha=1.0) sobre los mismos datos. Compará RMSE y la magnitud de los coeficientes vs OLS.",
      "Lasso: entrená Lasso(alpha=0.1). Contá cuántos coeficientes quedaron exactamente en 0. Subí alpha a 1.0 y a 10.0; observá la sparsity creciente.",
      "Elastic Net: entrená ElasticNet(alpha=0.1, l1_ratio=0.5). Compará con Ridge y Lasso puros.",
      "Tuning con CV: usá RidgeCV(alphas=np.logspace(-3, 3, 50)) y LassoCV(cv=5) para encontrar el mejor alpha. Graficá el path de coeficientes vs alpha (Lasso path)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/073-regularizacion-ridge-lasso-elastic-net/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/074-early-stopping",
    "number": 74,
    "slug": "074-early-stopping",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Early stopping",
    "description": "Aplicar early stopping como técnica de regularización implícita en entrenamientos iterativos: monitorear la pérdida de validación durante el descenso por gradiente y detener el ajuste cuando deja de mejorar, conservando…",
    "level": "Intermedio",
    "duration": "45 min",
    "theory": "Aplicar early stopping como técnica de regularización implícita en entrenamientos iterativos: monitorear la pérdida de validación durante el descenso por gradiente y detener el ajuste cuando deja de mejorar, conservando el mejor modelo visto.",
    "outcomes": [
      "Explicar por qué detener el entrenamiento antes del óptimo de train actúa como regularización.",
      "Configurar SGDRegressor(early_stopping=True) con validation_fraction, n_iter_no_change y tol.",
      "Graficar curvas de train loss vs. validation loss e identificar la best epoch.",
      "Implementar manualmente un loop con paciencia y snapshot del mejor modelo (partial_fit).",
      "Decidir cuándo early stopping reemplaza o complementa a Ridge/Lasso."
    ],
    "topics": [
      "Sobreajuste en entrenamientos iterativos (SGD, gradient boosting, redes neuronales).",
      "Curva de aprendizaje por época: train baja, validación baja y luego sube.",
      "Mecánica del early stopping: monitorear val loss + criterio de paciencia.",
      "API de scikit-learn: SGDRegressor / SGDClassifier con early_stopping=True.",
      "Implementación manual con partial_fit + copy.deepcopy del mejor estimador.",
      "Relación con otras regularizaciones (L1, L2, dropout en deep learning)."
    ],
    "materials": [
      "sklearn.datasets.fetch_california_housing para regresión.",
      "sklearn.datasets.make_regression(n_samples=2000, n_features=50, noise=20) para experimentos controlados.",
      "Géron, Hands-On ML (3ª ed.), cap. 4 § \"Early Stopping\" (figura de la \"U\" en val loss)."
    ],
    "exercises": [
      "Curva clásica: entrenar SGDRegressor(max_iter=1, warm_start=True, learning_rate='constant', eta0=0.0005) por 500 épocas sobre California Housing escalado. Graficar RMSE de train y validación por época. Marcar la best epoch.",
      "Early stopping automático: comparar SGDRegressor(early_stopping=True, validation_fraction=0.2, n_iter_no_change=10, tol=1e-4) contra el modelo sin early stopping. Reportar n.º de épocas reales (n_iter_) y RMSE en test.",
      "Paciencia: barrer n_iter_no_change ∈ {1, 5, 20, 100} y mostrar cómo afecta la época final y el error de test.",
      "Implementación manual: escribir un loop con partial_fit que mantenga best_loss, best_model = deepcopy(sgd) y un contador de paciencia. Devolver el mejor modelo.",
      "Comparación con Ridge: sobre make_regression con ruido, comparar (a) SGD sin regularización + early stopping, (b) Ridge con alpha tuneado por CV. Discutir cuál generaliza mejor y por qué."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/074-early-stopping/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/075-regresion-logistica-binaria-y-softmax",
    "number": 75,
    "slug": "075-regresion-logistica-binaria-y-softmax",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Regresión logística binaria y softmax",
    "description": "Que el alumno entienda la regresión logística como modelo lineal para clasificación: cómo la sigmoide convierte un score lineal en probabilidad, por qué se entrena minimizando log-loss (cross-entropy), y cómo se general…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Que el alumno entienda la regresión logística como modelo lineal para clasificación: cómo la sigmoide convierte un score lineal en probabilidad, por qué se entrena minimizando log-loss (cross-entropy), y cómo se generaliza a multiclase con softmax. Además, que sepa diagnosticar si las probabilidades que devuelve un clasificador están bien calibradas y cómo corregirlas si no.",
    "outcomes": [
      "Derivar la sigmoide σ(z) = 1/(1+e^-z) como puente entre score lineal y probabilidad, y explicar por qué no se usa MSE en clasificación.",
      "Entrenar LogisticRegression binaria de sklearn, interpretar coeficientes como log-odds y la frontera de decisión.",
      "Extender a multiclase con multi_class='multinomial' (softmax) y diferenciar de 'ovr' (one-vs-rest).",
      "Evaluar con log-loss y Brier score, no solo accuracy.",
      "Diagnosticar y corregir calibración con calibration_curve y CalibratedClassifierCV (Platt / isotonic)."
    ],
    "topics": [
      "Sigmoide y log-odds",
      "Log-loss (cross-entropy binaria)",
      "Regularización (C, penalty)",
      "Softmax para multiclase",
      "multinomial vs ovr",
      "Predict_proba y calibración"
    ],
    "materials": [
      "Iris (3 clases) para softmax — sklearn.datasets.load_iris().",
      "Breast cancer Wisconsin (binario) para logística y calibración — load_breast_cancer().",
      "Sintético desbalanceado con make_classification(weights=[0.9, 0.1]) para visualizar mis-calibración de un RandomForest."
    ],
    "exercises": [
      "Logística binaria desde cero. Entrená LogisticRegression() sobre breast cancer. Reportá accuracy, log-loss y matriz de confusión. Imprimí los 5 coeficientes con mayor |w| e interpretá uno como odds-ratio (exp(w)).",
      "Frontera de decisión. Con 2 features de iris (solo 2 clases primero), graficá la frontera lineal de la logística y los puntos. Cambiá C entre 0.01 y 100 y observá cómo la frontera se vuelve más/menos rígida.",
      "Softmax sobre iris. LogisticRegression(multi_class='multinomial', solver='lbfgs'). Comparalo con multi_class='ovr' en log_loss y accuracy. Imprimí predict_proba de 3 muestras y verificá que sumen 1.",
      "Reliability diagram de un RandomForest. Entrená RandomForestClassifier(n_estimators=100) sobre el dataset sintético desbalanceado. Computá calibration_curve con n_bins=10 y graficá vs diagonal. Reportá Brier score.",
      "Calibrar con CalibratedClassifierCV. Sobre el mismo RF: aplicá method='sigmoid' y method='isotonic' (cv=5). Re-graficá los tres reliability diagrams (RF crudo, +Platt, +isotonic) y compará Brier scores. Reportá cuál calibra mejor y por qué te parece."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/075-regresion-logistica-binaria-y-softmax/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/076-calibracion-de-probabilidades-platt-isotonic",
    "number": 76,
    "slug": "076-calibracion-de-probabilidades-platt-isotonic",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Calibración de probabilidades: Platt, isotonic, temperature scaling",
    "description": "Saber cuándo las probabilidades que devuelve predict_proba son calibradas — es decir, si el modelo dice \"70 %\" para un grupo, ¿realmente el 70 % es positivo?",
    "level": "Intermedio",
    "duration": "75 min",
    "theory": "Saber cuándo las probabilidades que devuelve predict_proba son calibradas — es decir, si el modelo dice \"70 %\" para un grupo, ¿realmente el 70 % es positivo? Modelos como Random Forest y SVM suelen estar mal calibrados; XGBoost mejor. Aplicar Platt scaling (sigmoid) y isotonic regression para corregir. Evaluar con Brier score, ECE (Expected Calibration Error) y reliability diagrams.",
    "outcomes": [
      "Generar un reliability diagram: agrupar predicciones por bin de probabilidad y plotear \"predicho vs real\".",
      "Calcular Brier score = mean((p - y)²). Más bajo = mejor calibración.",
      "Calcular ECE: Σ (n_b/N) · |acc_b - conf_b|.",
      "Aplicar sklearn.calibration.CalibratedClassifierCV(estimator, method='sigmoid' | 'isotonic', cv=5).",
      "Decidir: Platt cuando muestra chica (n < 1000), isotonic cuando hay datos."
    ],
    "topics": [
      "¿Por qué importa? Decisiones que dependen de threshold ≠ 0.5 requieren probs reales.",
      "Reliability diagram: predicción vs frecuencia real.",
      "Platt scaling: ajustar σ(A·logit + B) con MLE sobre val set.",
      "Isotonic regression: monótono pero más flexible (puede sobreajustar).",
      "Temperature scaling: solo divide logits por T aprendido — para multiclase, eficiente.",
      "Modelos típicamente calibrados (logistic regression) vs no (RF, SVM)."
    ],
    "materials": [
      "fetch_openml('credit-g') o load_breast_cancer.",
      "Librerías: sklearn.calibration, matplotlib."
    ],
    "exercises": [
      "Reliability diagram: entrenar RandomForest, generar predict_proba, bin en 10 grupos, plotear curva calibration vs y=x. Suele desviar.",
      "Brier + ECE: implementar ambas y comparar entre RF (mala calibración) y LogReg (buena).",
      "CalibratedClassifierCV: CalibratedClassifierCV(RF, method='sigmoid', cv=5).fit(X, y). Re-evaluar Brier.",
      "Isotonic vs Platt: comparar ambos sobre el mismo modelo. Con n=10_000 ambos similares; con n=300 Platt mejor.",
      "Threshold tuning post-calibración: con probs calibradas, F1 vs threshold es más interpretable."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/076-calibracion-de-probabilidades-platt-isotonic/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/077-svm-lineal",
    "number": 77,
    "slug": "077-svm-lineal",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "SVM lineal",
    "description": "Entender el principio de maximización del margen que define a las Support Vector Machines lineales, distinguir entre hard margin y soft margin, y entrenar un clasificador con LinearSVC controlando el trade-off bias/vari…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Entender el principio de maximización del margen que define a las Support Vector Machines lineales, distinguir entre hard margin y soft margin, y entrenar un clasificador con LinearSVC controlando el trade-off bias/varianza mediante el hiperparámetro C.",
    "outcomes": [
      "Explicar qué es el margen y por qué SVM busca el hiperplano que lo maximiza.",
      "Diferenciar hard margin (datos linealmente separables, sin tolerancia) de soft margin (admite violaciones).",
      "Interpretar el hiperparámetro C y su efecto sobre el ancho del margen y las violaciones permitidas.",
      "Entrenar un LinearSVC en scikit-learn con un Pipeline que incluya StandardScaler.",
      "Identificar los vectores soporte y entender por qué son los únicos puntos que definen la frontera."
    ],
    "topics": [
      "Intuición geométrica: hiperplano separador y margen.",
      "Hard margin: condiciones y limitaciones (sensibilidad a outliers, exige separabilidad).",
      "Soft margin: introducción de variables de holgura (slack).",
      "Hiperparámetro C: regularización, trade-off margen ancho vs. violaciones.",
      "Función de pérdida hinge loss.",
      "API de scikit-learn: LinearSVC, loss, C, dual, max_iter.",
      "Importancia crítica del escalado de features en SVM."
    ],
    "materials": [
      "Iris (sklearn.datasets.load_iris) — filtrado a dos clases (Iris-Virginica vs. resto) usando los features petal length y petal width. Es el ejemplo canónico del capítulo 5 de Géron.",
      "Opcional: dataset sintético con make_classification o make_blobs para visualizar el efecto de C y de outliers."
    ],
    "exercises": [
      "Cargá Iris, quedate con dos features (petal length, petal width) y la clase Virginica como problema binario. Entrená un Pipeline([StandardScaler, LinearSVC(C=1, loss=\"hinge\")]) y reportá accuracy sobre un split train/test.",
      "Repetí el entrenamiento con C=0.1, C=1, C=100. Compará accuracy, número de vectores soporte estimados y ancho del margen. ¿Qué pasa en los extremos?",
      "Graficá la frontera de decisión y el margen para los tres valores de C del ejercicio anterior (scatter de los datos + línea + márgenes punteados).",
      "Agregá un outlier artificial a la clase minoritaria y volvé a entrenar con C alto y C bajo. Mostrá cómo C bajo absorbe mejor el outlier.",
      "Compará tiempo de entrenamiento de LinearSVC vs. SVC(kernel=\"linear\") sobre un dataset de ~10.000 muestras (make_classification). Confirmá que LinearSVC es más rápido."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/077-svm-lineal/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/078-svm-no-lineal-kernel-polinomial-rbf",
    "number": 78,
    "slug": "078-svm-no-lineal-kernel-polinomial-rbf",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "SVM no lineal: kernel polinomial y RBF",
    "description": "Que el alumno entrene SVMs sobre datos no linealmente separables usando el kernel trick: en lugar de generar features polinómicas a mano (caro en memoria), SVC calcula el producto interno en el espacio expandido vía una…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Que el alumno entrene SVMs sobre datos no linealmente separables usando el kernel trick: en lugar de generar features polinómicas a mano (caro en memoria), SVC calcula el producto interno en el espacio expandido vía una función kernel. Foco en kernel polinomial y RBF (Gaussian), y cómo gamma y C controlan el bias-variance trade-off.",
    "outcomes": [
      "Explicar el kernel trick: por qué K(x, x') evita materializar el feature map φ(x).",
      "Entrenar SVC(kernel='poly') y SVC(kernel='rbf') en datasets no lineales (moons, circles).",
      "Tunear gamma y C con GridSearchCV entendiendo el efecto en la frontera.",
      "Elegir kernel según geometría del problema (polinomial vs RBF vs lineal).",
      "Reconocer el límite computacional de SVC: complejidad entre O(n²) y O(n³), no escala a >100k filas."
    ],
    "topics": [
      "Datos no linealmente separables (moons, circles)",
      "Polynomial features manuales vs kernel trick",
      "Kernel polinomial: degree, coef0, gamma",
      "Kernel RBF (Gaussian): gamma como inverso del ancho",
      "C (regularización) × gamma (forma)",
      "Complejidad O(n²)–O(n³) y LinearSVC / SGDClassifier para N grande"
    ],
    "materials": [
      "sklearn.datasets.make_moons(n_samples=500, noise=0.15) — clásico no lineal.",
      "sklearn.datasets.make_circles(n_samples=500, noise=0.1, factor=0.4) — radial puro, ideal para mostrar RBF."
    ],
    "exercises": [
      "Lineal falla. Entrená SVC(kernel='linear') sobre make_moons. Reportá accuracy y graficá la frontera. Mostrá visualmente que es inadecuada.",
      "Polynomial kernel. SVC(kernel='poly', degree=3, coef0=1, C=5) sobre moons. Comparar accuracy y forma de la frontera vs lineal.",
      "RBF kernel. SVC(kernel='rbf', gamma=5, C=1) sobre circles. Variar gamma ∈ {0.1, 1, 10, 100} con el mismo C y graficar las 4 fronteras lado a lado.",
      "Grid search 2D. GridSearchCV sobre gamma ∈ {0.01, 0.1, 1, 10} × C ∈ {0.1, 1, 10, 100} con cv=5 sobre moons. Reportar el mejor par y matriz de scores como heatmap.",
      "Pipeline con StandardScaler. SVMs son sensibles a escala. Armá Pipeline([('sc', StandardScaler()), ('svc', SVC(kernel='rbf'))]) y comparar accuracy con y sin scaler en un dataset con features de magnitudes muy distintas."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/078-svm-no-lineal-kernel-polinomial-rbf/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/079-svm-para-regresion",
    "number": 79,
    "slug": "079-svm-para-regresion",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "SVM para regresión (SVR)",
    "description": "Aplicar Support Vector Machines al problema de regresión: entender el truco del epsilon-insensitive loss (ajustar dentro de un tubo de tolerancia en vez de minimizar el error puntual), entrenar LinearSVR y SVR con kerne…",
    "level": "Intermedio",
    "duration": "50 min",
    "theory": "Aplicar Support Vector Machines al problema de regresión: entender el truco del epsilon-insensitive loss (ajustar dentro de un tubo de tolerancia en vez de minimizar el error puntual), entrenar LinearSVR y SVR con kernel, y elegir cuándo conviene SVR sobre regresión lineal clásica.",
    "outcomes": [
      "Explicar la lógica de SVR: maximizar el ancho del tubo ε mientras se contienen la mayoría de los puntos dentro.",
      "Entrenar un LinearSVR y un SVR(kernel=\"rbf\") de scikit-learn con sus hiperparámetros (epsilon, C, gamma).",
      "Interpretar el efecto de epsilon (ancho del tubo) y C (penalización por puntos fuera del tubo) en el bias-variance trade-off.",
      "Comparar SVR vs LinearRegression / Ridge en un dataset con outliers.",
      "Justificar cuándo SVR escala mal (SVR es O(m²–m³)) y conviene LinearSVR u otro modelo."
    ],
    "topics": [
      "De SVM clasificación a SVM regresión: invertir el objetivo.",
      "Epsilon-insensitive loss: errores menores a ε no se penalizan.",
      "LinearSVR: caso lineal, escala bien (O(m)).",
      "SVR con kernel RBF: regresión no lineal, costo cuadrático.",
      "Hiperparámetros clave: epsilon, C, gamma, kernel.",
      "Robustez frente a outliers comparada con OLS."
    ],
    "materials": [
      "California Housing (sklearn.datasets.fetch_california_housing) para regresión realista.",
      "Dataset sintético con outliers (make_regression + ruido pesado) para mostrar robustez.",
      "Géron, Hands-On ML (3ª ed.), cap. 5, sección \"SVM Regression\"."
    ],
    "exercises": [
      "Tubo ε en 2D. Generá y = 0.5x + ruido, entrená LinearSVR(epsilon=0.5) y graficá la recta junto al tubo ±ε. Marcá los vectores de soporte (puntos fuera del tubo).",
      "Efecto de epsilon. Repetí el ejercicio 1 con ε ∈ {0.1, 0.5, 1.5}. ¿Cómo cambia la cantidad de vectores de soporte y el MSE en test?",
      "Kernel RBF. En un dataset no lineal (y = sin(x) + ruido), compará LinearSVR vs SVR(kernel=\"rbf\", gamma=\"scale\"). Reportá MAE y graficá ambas curvas.",
      "Grid search. Sobre California Housing, hacé GridSearchCV con SVR variando C ∈ {0.1, 1, 10} y gamma ∈ {\"scale\", 0.01, 0.1}. No uses más de 5 000 muestras (cuidado con el costo cuadrático).",
      "Robustez vs OLS. Inyectá 5% de outliers en un dataset lineal y compará LinearRegression, Ridge y LinearSVR. ¿Cuál degrada menos?"
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/079-svm-para-regresion/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/080-arboles-de-decision-entrenamiento-visualizacion-cart",
    "number": 80,
    "slug": "080-arboles-de-decision-entrenamiento-visualizacion-cart",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Árboles de decisión: entrenamiento, visualización, CART",
    "description": "Que el alumno entrene un DecisionTreeClassifier con el algoritmo CART, entienda cómo se elige cada split (criterio Gini/Entropy), y sepa leer el árbol — tanto el dibujo (plot_tree) como el código (export_graphviz) — par…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno entrene un DecisionTreeClassifier con el algoritmo CART, entienda cómo se elige cada split (criterio Gini/Entropy), y sepa leer el árbol — tanto el dibujo (plot_tree) como el código (export_graphviz) — para auditar las decisiones del modelo.",
    "outcomes": [
      "Entrenar un DecisionTreeClassifier de scikit-learn sobre un dataset tabular (Iris) y predecir clases / probabilidades.",
      "Explicar el algoritmo CART: greedy, binario, busca el par (feature, threshold) que minimiza la impureza ponderada de los dos hijos.",
      "Calcular Gini y entropía a mano sobre un nodo con k clases y elegir el split óptimo entre candidatos.",
      "Visualizar el árbol entrenado con plot_tree (matplotlib) y export_graphviz (DOT → PNG/SVG), interpretando samples, value, class, gini.",
      "Identificar la decision boundary axis-aligned: cada split es ortogonal a un eje, lo que limita al árbol frente a fronteras oblicuas."
    ],
    "topics": [
      "DecisionTreeClassifier API",
      "Algoritmo CART",
      "Criterio Gini vs Entropy",
      "Visualización: plot_tree y Graphviz",
      "Interpretación de nodos",
      "Decision boundary axis-aligned"
    ],
    "materials": [
      "Iris (sklearn.datasets.load_iris): 150 muestras, 4 features, 3 clases. Géron lo usa porque permite dibujar el árbol completo en una página y la frontera en 2D (pétalo largo × ancho).",
      "Opcional: moons (make_moons) para ver la limitación axis-aligned."
    ],
    "exercises": [
      "Fit + score baseline. Entrená DecisionTreeClassifier(max_depth=2, random_state=42) sobre Iris (todas las features). Reportá accuracy en train. Probabilidades de la primera flor con .predict_proba.",
      "Gini a mano. Para el nodo raíz de Iris (50/50/50), calculá Gini. Verificá contra tree_.impurity[0] del estimador entrenado.",
      "Gini vs Entropy. Entrená dos árboles max_depth=3, uno con cada criterio. Compará accuracy y el set de features usadas en los splits (tree_.feature). ¿Cambia algo material?",
      "plot_tree. Renderizá el árbol del ejercicio 1 con sklearn.tree.plot_tree(clf, feature_names=..., class_names=..., filled=True). Identificá: feature del root split, threshold, y la clase predicha por cada hoja.",
      "Boundary axis-aligned. Entrená un árbol max_depth=4 sobre make_moons(n_samples=300, noise=0.2). Graficá la decision boundary con un meshgrid. Observá los rectángulos."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/080-arboles-de-decision-entrenamiento-visualizacion-cart/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/081-regularizacion-de-arboles",
    "number": 81,
    "slug": "081-regularizacion-de-arboles",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Regularización de árboles",
    "description": "Que el alumno controle el overfitting de un DecisionTreeClassifier/Regressor usando hiperparámetros de regularización (pre-pruning) y cost-complexity pruning (post-pruning), y sepa elegir entre ambas estrategias en func…",
    "level": "Intermedio",
    "duration": "50 min",
    "theory": "Que el alumno controle el overfitting de un DecisionTreeClassifier/Regressor usando hiperparámetros de regularización (pre-pruning) y cost-complexity pruning (post-pruning), y sepa elegir entre ambas estrategias en función del problema.",
    "outcomes": [
      "Identificar overfitting en un árbol sin regularizar (train accuracy ≈ 1, test bajo).",
      "Tunear max_depth, min_samples_split, min_samples_leaf, max_leaf_nodes, max_features con GridSearchCV.",
      "Aplicar cost-complexity pruning vía ccp_alpha y leer la curva cost_complexity_pruning_path.",
      "Diferenciar pre-pruning (frenar el crecimiento) de post-pruning (podar después).",
      "Justificar la elección de hiperparámetros con curvas de validación, no a ojo."
    ],
    "topics": [
      "Árboles sin regularizar = overfitting garantizado",
      "max_depth y max_leaf_nodes",
      "min_samples_split / min_samples_leaf",
      "max_features",
      "ccp_alpha (cost-complexity pruning)",
      "Pre-pruning vs post-pruning"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Overfit baseline. Entrená un DecisionTreeClassifier() sin tocar nada sobre moons. Reportá train vs test accuracy. ¿Cuánto gap hay?",
      "max_depth sweep. Para max_depth ∈ {1, 2, 3, 5, 10, None} graficá train y test accuracy. Identificá el punto donde empieza el overfit.",
      "GridSearch. Buscá con GridSearchCV(cv=5) la mejor combinación de max_depth, min_samples_leaf y max_leaf_nodes. Reportá mejores params y test score.",
      "Cost-complexity path. Llamá tree.cost_complexity_pruning_path(X_train, y_train) para obtener ccp_alphas. Entrená un árbol por cada α y graficá test accuracy vs α. Elegí el óptimo.",
      "Visualización de fronteras. Plotteá la decision boundary de (a) árbol sin regularizar y (b) árbol con max_depth=4. Compará overfit visual."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/081-regularizacion-de-arboles/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/082-regresion-con-arboles",
    "number": 82,
    "slug": "082-regresion-con-arboles",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Regresión con árboles",
    "description": "Entrenar árboles de decisión para problemas de regresión con DecisionTreeRegressor, entender por qué sus predicciones son escalonadas (constantes por hoja) y reconocer su incapacidad para extrapolar fuera del rango de e…",
    "level": "Intermedio",
    "duration": "45 min",
    "theory": "Entrenar árboles de decisión para problemas de regresión con DecisionTreeRegressor, entender por qué sus predicciones son escalonadas (constantes por hoja) y reconocer su incapacidad para extrapolar fuera del rango de entrenamiento.",
    "outcomes": [
      "Ajustar un DecisionTreeRegressor de scikit-learn y predecir sobre datos nuevos.",
      "Explicar cómo el criterio MSE (squared error) decide los splits en regresión.",
      "Visualizar la predicción escalonada del árbol contra el target real en 1D.",
      "Identificar el problema de no-extrapolación y contrastarlo con regresión lineal.",
      "Regular max_depth / min_samples_leaf para balancear bias y varianza."
    ],
    "topics": [
      "DecisionTreeRegressor: API e hiperparámetros principales.",
      "Criterio de split: squared_error (MSE) y friedman_mse.",
      "Predicción como media del target dentro de cada hoja → función escalonada.",
      "Sobreajuste con árboles profundos y regularización vía max_depth, min_samples_leaf, min_samples_split.",
      "Limitación clave: el árbol no extrapola — predice el último valor visto en los extremos.",
      "Comparación rápida con regresión lineal en datos con tendencia."
    ],
    "materials": [
      "Dataset sintético 1D: x = np.linspace(-3, 3, 200), y = np.sin(x) + ruido_gaussiano(0, 0.1) — sirve para ver la escalera y la no-extrapolación.",
      "Alternativa real: sklearn.datasets.fetch_california_housing (regresión, 8 features) para evaluar con cross_val_score.",
      "Géron, Hands-On ML, cap. 6, sección \"Regression\" (incluye figura 6-5 con la predicción escalonada)."
    ],
    "exercises": [
      "Ajuste básico: generá los datos sin(x) + ruido, entrená DecisionTreeRegressor(max_depth=2) y max_depth=5, y graficá ambas predicciones sobre los puntos. Observá las escaleras.",
      "MSE en train vs test: hacé train_test_split(test_size=0.3), calculá mean_squared_error en train y test para max_depth ∈ {1, 2, 4, 8, None}. ¿Dónde empieza el sobreajuste?",
      "No extrapolación: predecí con el modelo entrenado sobre x_new = np.linspace(-5, 5, 200) (rango más ancho que el train). Graficá: vas a ver mesetas planas en los extremos.",
      "Árbol vs lineal: entrená LinearRegression sobre los mismos datos. Comparalo con el árbol fuera del rango de entrenamiento. ¿Cuál extrapola \"bien\" y por qué?",
      "California Housing: corré cross_val_score(DecisionTreeRegressor(max_depth=6), X, y, scoring='neg_mean_squared_error', cv=5) y compará contra max_depth=None."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/082-regresion-con-arboles/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/083-voting-classifiers-hard-soft",
    "number": 83,
    "slug": "083-voting-classifiers-hard-soft",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Voting classifiers: hard y soft",
    "description": "Combinar varios modelos heterogéneos en un ensemble por votación y entender cuándo conviene hard voting (voto por mayoría) versus soft voting (promedio de probabilidades), apoyándonos en el principio de wisdom of the cr…",
    "level": "Intermedio",
    "duration": "45 min",
    "theory": "Combinar varios modelos heterogéneos en un ensemble por votación y entender cuándo conviene hard voting (voto por mayoría) versus soft voting (promedio de probabilidades), apoyándonos en el principio de wisdom of the crowd.",
    "outcomes": [
      "Explicar por qué un ensemble de clasificadores diversos suele superar al mejor modelo individual.",
      "Implementar un VotingClassifier de scikit-learn con voting=\"hard\" y voting=\"soft\".",
      "Decidir entre hard y soft voting según si los modelos base estiman probabilidades calibradas.",
      "Comparar la accuracy del ensemble contra la de cada modelo base en un dataset de clasificación.",
      "Identificar errores frecuentes al armar el ensemble (modelos correlacionados, probabilidades mal calibradas, pesos sin justificar)."
    ],
    "topics": [
      "Wisdom of the crowd: por qué combinar predicciones reduce error.",
      "Hard voting: predicción final = clase con más votos entre los modelos base.",
      "Soft voting: predicción final = clase con mayor promedio de probabilidades estimadas.",
      "Requisitos para soft voting: que cada modelo exponga predict_proba y esté bien calibrado.",
      "Diversidad entre modelos base (algoritmos distintos, no sólo hiperparámetros distintos).",
      "VotingClassifier(estimators=[...], voting=..., weights=...).",
      "Limitaciones: si los modelos se equivocan en los mismos ejemplos, el ensemble no ayuda."
    ],
    "materials": [
      "Dataset sugerido: make_moons(n_samples=500, noise=0.30, random_state=42) (mismo que usa Géron en el cap. 7).",
      "Alternativa: load_breast_cancer() de sklearn.datasets para un caso real.",
      "Imports clave: LogisticRegression, RandomForestClassifier, SVC, VotingClassifier, train_test_split, accuracy_score."
    ],
    "exercises": [
      "Cargar make_moons y partir en train/test (80/20, random_state=42). Entrenar por separado LogisticRegression, RandomForestClassifier y SVC(probability=True). Reportar accuracy de cada uno.",
      "Armar un VotingClassifier con esos tres modelos y voting=\"hard\". Comparar accuracy contra cada modelo base.",
      "Repetir con voting=\"soft\" (recordá SVC(probability=True)). ¿Mejora? ¿Por qué?",
      "Probar weights=[1, 2, 1] favoreciendo al Random Forest. ¿Cómo cambia la performance? Justificar.",
      "Reemplazar uno de los modelos por una copia casi idéntica de otro (ej.: dos regresiones logísticas con C muy parecido). Observar y explicar por qué el ensemble deja de ganar."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/083-voting-classifiers-hard-soft/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/084-bagging-y-pasting",
    "number": 84,
    "slug": "084-bagging-y-pasting",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Bagging y pasting",
    "description": "Que el alumno entrene ensembles entrenando el mismo algoritmo sobre distintos subsets del training set —bagging (con reemplazo) y pasting (sin reemplazo)— y evalúe sin held-out usando out-of-bag (OOB).",
    "level": "Intermedio",
    "duration": "55 min",
    "theory": "Que el alumno entrene ensembles entrenando el mismo algoritmo sobre distintos subsets del training set —bagging (con reemplazo) y pasting (sin reemplazo)— y evalúe sin held-out usando out-of-bag (OOB). Cierre con sampling de features (random patches y random subspaces) como puente conceptual a Random Forests.",
    "outcomes": [
      "Distinguir bagging vs pasting y justificar cuándo elegir uno u otro.",
      "Entrenar un BaggingClassifier de scikit-learn con un base estimator y n_estimators razonable.",
      "Usar oob_score=True para estimar el error de generalización sin tocar el test set.",
      "Aplicar sampling de features (max_features < 1.0, bootstrap_features=True) para random patches / random subspaces.",
      "Comparar bias/variance del ensemble vs un único árbol, en accuracy y en frontera de decisión."
    ],
    "topics": [
      "Bagging (bootstrap aggregating)",
      "Pasting",
      "BaggingClassifier API",
      "OOB evaluation",
      "Random patches",
      "Random subspaces",
      "Paralelización con n_jobs=-1"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Bagging vs árbol único. Entrená un DecisionTreeClassifier y un BaggingClassifier(DecisionTreeClassifier(), n_estimators=500, max_samples=100, bootstrap=True) sobre make_moons. Compará accuracy en test.",
      "Bagging vs pasting. Repetí (1) con bootstrap=False. Reportá diferencia de accuracy y discutí.",
      "OOB. Entrená con oob_score=True, bootstrap=True. Imprimí bag.oob_score_ y compará con accuracy en test — deberían ser parecidos.",
      "Curva de n_estimators. Variá n_estimators ∈ {1, 10, 50, 100, 500, 1000}. Plotteá accuracy test vs n_estimators.",
      "Random subspaces. Sobre load_digits() (64 features), entrená con bootstrap=False, max_samples=1.0, bootstrap_features=True, max_features=0.5. Compará con bagging clásico."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/084-bagging-y-pasting/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/085-random-forests-y-extra-trees",
    "number": 85,
    "slug": "085-random-forests-y-extra-trees",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Random Forests y Extra Trees",
    "description": "Entender Random Forests y Extra Trees como ensambles de árboles decorrelacionados, diferenciar sus mecanismos de aleatoriedad y elegir hiperparámetros razonables para problemas reales de clasificación y regresión.",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Entender Random Forests y Extra Trees como ensambles de árboles decorrelacionados, diferenciar sus mecanismos de aleatoriedad y elegir hiperparámetros razonables para problemas reales de clasificación y regresión.",
    "outcomes": [
      "Explicar por qué un Random Forest reduce varianza respecto a un árbol único, usando los conceptos de bagging y subsampling de features.",
      "Diferenciar Random Forest vs Extra Trees (thresholds óptimos vs aleatorios) y argumentar cuándo conviene cada uno.",
      "Configurar los hiperparámetros clave (n_estimators, max_features, max_depth, bootstrap, min_samples_leaf) con criterios fundados.",
      "Entrenar y comparar RandomForestClassifier y ExtraTreesClassifier de scikit-learn en un dataset tabular, midiendo accuracy y tiempo.",
      "Interpretar oob_score_ como estimación honesta del error de generalización sin necesidad de validación cruzada."
    ],
    "topics": [
      "Repaso de bagging: bootstrap + agregación → reducción de varianza.",
      "Random Forest: bagging de árboles + subsampling de features en cada split.",
      "Extra Trees (Extremely Randomized Trees): thresholds aleatorios en lugar de óptimos.",
      "Hiperparámetros: n_estimators, max_features, max_depth, min_samples_leaf, bootstrap, oob_score.",
      "Out-of-Bag (OOB) score y su uso como reemplazo de CV.",
      "Comparativa empírica: bias, varianza, tiempo de entrenamiento."
    ],
    "materials": [
      "Dataset principal: sklearn.datasets.load_breast_cancer() (569 muestras, 30 features, binario).",
      "Dataset secundario (regresión): sklearn.datasets.fetch_california_housing().",
      "Librerías: scikit-learn >= 1.3, numpy, pandas, matplotlib.",
      "Notebook: notebook.ipynb con ejemplos guiados."
    ],
    "exercises": [
      "Baseline: entrená un DecisionTreeClassifier único sobre load_breast_cancer con random_state=42 y reportá accuracy en test (split 80/20).",
      "Random Forest: entrená un RandomForestClassifier(n_estimators=200, random_state=42) y compará accuracy y tiempo contra el árbol único.",
      "Extra Trees: entrená un ExtraTreesClassifier(n_estimators=200, random_state=42) y compará contra RF en accuracy y tiempo de entrenamiento.",
      "OOB: entrená un RF con oob_score=True, bootstrap=True y compará oob_score_ contra el accuracy de test; ¿se parecen?",
      "Sensibilidad a max_features: variá max_features en [1, 'sqrt', 'log2', 0.5, 1.0] y graficá accuracy de CV; identificá el óptimo."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/085-random-forests-y-extra-trees/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/086-feature-importance",
    "number": 86,
    "slug": "086-feature-importance",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Feature importance",
    "description": "Aprender a medir y comunicar qué variables aportan a un modelo basado en árboles, distinguiendo entre Mean Decrease in Impurity (MDI) —el feature_importances_ por default de scikit-learn— y permutation importance, enten…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Aprender a medir y comunicar qué variables aportan a un modelo basado en árboles, distinguiendo entre Mean Decrease in Impurity (MDI) —el feature_importances_ por default de scikit-learn— y permutation importance, entendiendo los sesgos de cada método. Como complemento, conocer las herramientas modernas de interpretabilidad SHAP y LIME para explicar predicciones individuales.",
    "outcomes": [
      "Calcular feature_importances_ en un RandomForestClassifier / GradientBoostingRegressor y explicar qué mide MDI.",
      "Aplicar sklearn.inspection.permutation_importance sobre el set de validación y comparar el ranking con MDI.",
      "Identificar los sesgos de MDI (favorece features de alta cardinalidad y continuas) y de permutation (problemas con features correlacionadas).",
      "Generar explicaciones locales con shap.TreeExplainer e interpretar summary_plot y waterfall_plot.",
      "Decidir cuándo usar MDI, permutation, SHAP o LIME según contexto (auditoría, debugging, comunicación)."
    ],
    "topics": [
      "Recordatorio: cómo los árboles eligen splits (impurity / variance reduction).",
      "MDI: suma ponderada de la reducción de impureza por feature, promediada sobre los árboles.",
      "Permutation importance: caída del score al permutar aleatoriamente los valores de una feature.",
      "Sesgos: cardinalidad alta infla MDI; correlación infla/desinfla permutation.",
      "MDI se calcula sobre train (riesgo de overfitting); permutation se calcula sobre test/valid.",
      "Interpretabilidad global vs local.",
      "Complemento moderno: SHAP, LIME, PDP, ICE."
    ],
    "materials": [
      "Dataset: sklearn.datasets.fetch_california_housing (regresión) y/o load_breast_cancer (clasificación).",
      "Librerías: scikit-learn, shap, lime, matplotlib.",
      "Instalación: pip install shap lime."
    ],
    "exercises": [
      "Entrená un RandomForestRegressor sobre California Housing. Imprimí feature_importances_ ordenado y graficalo como barh.",
      "Calculá permutation_importance sobre el set de test con n_repeats=10. Comparalo con MDI en un DataFrame lado a lado. ¿Coincide el top-3?",
      "Agregá una columna random_id = np.arange(len(X)) y reentrená. Mostrá cómo MDI le asigna importancia espuria mientras permutation la ignora.",
      "Generá shap.summary_plot con TreeExplainer y explicá la diferencia entre el plot tipo beeswarm (impacto + dirección) y un bar plot de MDI.",
      "Elegí una instancia mal clasificada (o con error grande en regresión) y explicala con shap.waterfall_plot. Anotá las 3 features que más empujaron la predicción."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/086-feature-importance/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/087-shap-en-profundidad-treeexplainer-deepexplainer",
    "number": 87,
    "slug": "087-shap-en-profundidad-treeexplainer-deepexplainer",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "SHAP en profundidad: TreeExplainer, KernelExplainer, DeepExplainer",
    "description": "Dominar SHAP (SHapley Additive exPlanations) en profundidad: teoría de Shapley values (teoría de juegos cooperativos), TreeExplainer (rápido y exacto para árboles), KernelExplainer (model-agnostic, lento), DeepExplainer…",
    "level": "Intermedio",
    "duration": "90 min",
    "theory": "Dominar SHAP (SHapley Additive exPlanations) en profundidad: teoría de Shapley values (teoría de juegos cooperativos), TreeExplainer (rápido y exacto para árboles), KernelExplainer (model-agnostic, lento), DeepExplainer (para NN), y los plots clave: summary_plot, waterfall_plot, force_plot, dependence_plot, decision_plot.",
    "outcomes": [
      "Explicar Shapley value intuitivamente: contribución marginal promedio sobre todos los órdenes de inclusión.",
      "Aplicar TreeExplainer en XGBoost/LightGBM/RF (segundos para millones de samples).",
      "Generar e interpretar los 5 plots SHAP principales.",
      "Diferenciar explicación global (summary_plot beeswarm) de local (waterfall de una predicción).",
      "Reconocer las limitaciones: SHAP asume cierta forma de \"feature attribution\" pero no es causal."
    ],
    "topics": [
      "Shapley value: φ_i = Σ |S|!(M-|S|-1)! / M! · [v(S ∪ {i}) - v(S)].",
      "4 propiedades únicas: efficiency, symmetry, dummy, additivity.",
      "TreeExplainer: exacto para tree-based, O(TLD²).",
      "KernelExplainer: LIME-style con kernel especial → SHAP values aproximados.",
      "DeepExplainer: para Keras/PyTorch.",
      "Permutation explainer: alternativa moderna sin necesidad de árbol/red."
    ],
    "materials": [
      "fetch_california_housing o load_breast_cancer.",
      "Librerías: shap (pip install shap), xgboost, matplotlib."
    ],
    "exercises": [
      "TreeExplainer: XGBoost en California Housing → explainer = shap.TreeExplainer(model); shap_values = explainer(X_test).",
      "Summary plot: shap.summary_plot(shap_values, X_test). Identificar las 3 features más importantes y su dirección.",
      "Waterfall: elegir 1 muestra concreta → shap.waterfall_plot(shap_values[0]). Sumar contribuciones y verificar que reconstruye la predicción.",
      "Dependence plot: shap.dependence_plot('MedInc', shap_values.values, X_test). Detectar non-linearity.",
      "Interaction values: shap_interaction = explainer.shap_interaction_values(X_test). Identificar par de features con mayor interacción."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/087-shap-en-profundidad-treeexplainer-deepexplainer/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/088-boosting-adaboost-gradient-boosting",
    "number": 88,
    "slug": "088-boosting-adaboost-gradient-boosting",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Boosting: AdaBoost y Gradient Boosting",
    "description": "Entender la idea de boosting como combinación secuencial de aprendices débiles, dominar los dos enfoques clásicos —AdaBoost (reponderar errores) y Gradient Boosting (ajustar al residuo)— y saber tunear learning_rate, n_…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Entender la idea de boosting como combinación secuencial de aprendices débiles, dominar los dos enfoques clásicos —AdaBoost (reponderar errores) y Gradient Boosting (ajustar al residuo)— y saber tunear learning_rate, n_estimators y aplicar early stopping con staged_predict.",
    "outcomes": [
      "Explicar la diferencia conceptual entre bagging (paralelo, varianza) y boosting (secuencial, sesgo).",
      "Entrenar un AdaBoostClassifier y un GradientBoostingClassifier de scikit-learn, leyendo correctamente sus hiperparámetros.",
      "Entender por qué learning_rate y n_estimators se mueven en sentidos opuestos (shrinkage).",
      "Implementar early stopping en boosting usando staged_predict sobre un set de validación.",
      "Decidir cuándo conviene AdaBoost, cuándo Gradient Boosting clásico y cuándo saltar directo a las librerías de la 079."
    ],
    "topics": [
      "Intuición: muchos clasificadores débiles → uno fuerte.",
      "AdaBoost: peso a las muestras mal clasificadas; SAMME y SAMME.R.",
      "Gradient Boosting: cada árbol ajusta el residuo (gradiente de la loss) del ensemble previo.",
      "Hiperparámetros clave: n_estimators, learning_rate, max_depth, subsample (stochastic gradient boosting).",
      "staged_predict / staged_predict_proba: predicciones intermedias para early stopping.",
      "Curvas de error vs. número de estimadores: detectar el \"codo\".",
      "Limitaciones: entrenamiento secuencial (no se paraleliza tan bien como bagging)."
    ],
    "materials": [
      "sklearn.datasets.make_moons(n_samples=500, noise=0.30, random_state=42) para la parte visual.",
      "sklearn.datasets.load_breast_cancer() para comparar AdaBoost vs. Gradient Boosting en un problema real.",
      "sklearn.ensemble.AdaBoostClassifier, GradientBoostingClassifier, GradientBoostingRegressor.",
      "Géron, cap. 7, sección \"Boosting\" (AdaBoost + Gradient Boosting + Early Stopping)."
    ],
    "exercises": [
      "AdaBoost desde cero conceptual: entrená un AdaBoostClassifier(n_estimators=200, learning_rate=0.5) sobre make_moons. Graficá la frontera de decisión con 1, 10, 50 y 200 estimadores.",
      "Gradient Boosting paso a paso: usá GradientBoostingRegressor(max_depth=2, n_estimators=3, learning_rate=1.0) sobre datos sintéticos y = x² + ruido. Mostrá las predicciones intermedias entrenando 3 árboles a mano sobre residuos sucesivos y verificá que coinciden con el ensemble.",
      "Trade-off learning_rate ↔ n_estimators: comparé (lr=1.0, n=50) vs. (lr=0.1, n=500) vs. (lr=0.01, n=5000) en breast_cancer. Reportá accuracy y tiempo de fit.",
      "Early stopping con staged_predict: entrené GradientBoostingClassifier(n_estimators=500, learning_rate=0.05) y, usando staged_predict sobre validación, encontrá el n_estimators óptimo. Re-entrené con ese valor.",
      "Stochastic Gradient Boosting: agregale subsample=0.5 al modelo de (4). ¿Mejora la generalización? ¿Por qué?"
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/088-boosting-adaboost-gradient-boosting/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/089-xgboost-lightgbm-catboost",
    "number": 89,
    "slug": "089-xgboost-lightgbm-catboost",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "XGBoost, LightGBM y CatBoost",
    "description": "Conocer las tres librerías de gradient boosting moderno que dominan tabular ML —XGBoost, LightGBM y CatBoost—, entender sus diferencias algorítmicas (level-wise vs leaf-wise, manejo de categóricas, regularización) y sab…",
    "level": "Intermedio",
    "duration": "80 min",
    "theory": "Conocer las tres librerías de gradient boosting moderno que dominan tabular ML —XGBoost, LightGBM y CatBoost—, entender sus diferencias algorítmicas (level-wise vs leaf-wise, manejo de categóricas, regularización) y saber elegir la adecuada según el problema, usando sus APIs sklearn-compatibles con early_stopping_rounds.",
    "outcomes": [
      "Instalar y usar xgboost, lightgbm y catboost con la API sklearn (fit/predict/predict_proba).",
      "Explicar la diferencia entre crecimiento level-wise (XGBoost por defecto) y leaf-wise (LightGBM) y sus implicancias en velocidad y overfitting.",
      "Configurar early stopping con eval_set y early_stopping_rounds para evitar overfitting y ahorrar tiempo.",
      "Manejar features categóricas: encoding manual para XGBoost, categorical_feature en LightGBM, cat_features nativo en CatBoost con ordered boosting.",
      "Elegir la librería apropiada según tamaño de dataset, presencia de categóricas y necesidad de velocidad de entrenamiento o inferencia."
    ],
    "topics": [
      "XGBoost",
      "Level-wise (default)",
      "Media",
      "Rápida",
      "❌ (requiere encoding)",
      "✅",
      "Bajo",
      "max_depth",
      "✅"
    ],
    "materials": [
      "sklearn.datasets.fetch_openml('adult') o 'credit-g' — datasets con mezcla de numéricas y categóricas, ideales para comparar las 3 librerías.",
      "Alternativa: cualquier dataset tabular con >10k filas y columnas categóricas.",
      "Notebook: notebook.ipynb (no editar — se entrega)."
    ],
    "exercises": [
      "Instalación y smoke test: instalar las 3 librerías, importarlas e imprimir versiones. Confirmar que cargan sin error.",
      "XGBoost básico: entrenar XGBClassifier sobre adult (con OneHotEncoder para categóricas), usar eval_set y early_stopping_rounds=20, reportar accuracy en test y la mejor iteración.",
      "LightGBM con leaf-wise: entrenar LGBMClassifier pasando categorical_feature con los índices de columnas categóricas (encoding ordinal previo). Comparar tiempo de entrenamiento vs XGBoost.",
      "CatBoost nativo: entrenar CatBoostClassifier pasando cat_features con los nombres de columnas — sin encoding manual. Verificar que la accuracy se mantiene o mejora respecto a 2 y 3.",
      "Comparativa final: entrenar los 3 modelos sobre el mismo dataset con los mismos splits, reportar en una tabla: accuracy test, tiempo de fit, tiempo de predict y mejor iteración. Concluir cuál elegirías."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/089-xgboost-lightgbm-catboost/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/090-stacking",
    "number": 90,
    "slug": "090-stacking",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Stacking (stacked generalization)",
    "description": "Que el alumno combine modelos heterogéneos vía stacking: entrenar varios modelos base, generar predicciones out-of-fold, y entrenar un meta-modelo (blender) sobre esas predicciones — todo con StackingClassifier / Stacki…",
    "level": "Intermedio",
    "duration": "60 min",
    "theory": "Que el alumno combine modelos heterogéneos vía stacking: entrenar varios modelos base, generar predicciones out-of-fold, y entrenar un meta-modelo (blender) sobre esas predicciones — todo con StackingClassifier / StackingRegressor de sklearn, sin leakage.",
    "outcomes": [
      "Explicar la idea de stacking como ensamble donde un meta-modelo aprende a combinar las predicciones de los base learners.",
      "Construir un StackingClassifier con varios estimadores base y un blender (típicamente regresión logística).",
      "Justificar las predicciones out-of-fold (CV interna) como mecanismo para evitar que el blender vea predicciones in-sample.",
      "Comparar stacking contra voting y contra un solo modelo bien tuneado, en accuracy y costo computacional.",
      "Usar passthrough=True para que el blender vea también las features originales, no solo las predicciones de los base."
    ],
    "topics": [
      "Idea: ensamble de dos niveles",
      "Base learners heterogéneos",
      "Meta-modelo (blender)",
      "Out-of-fold predictions",
      "StackingClassifier / StackingRegressor",
      "passthrough",
      "Costo y cuándo conviene"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Stacking básico. Construí un StackingClassifier con tres base learners (RandomForest, SVC con probability=True, KNN) y LogisticRegression como blender. Reportá accuracy con cross_val_score(cv=5).",
      "Comparación contra base learners solos. Evaluá los tres base learners individualmente con el mismo CV. ¿El stacking supera al mejor solo? ¿Por cuánto?",
      "passthrough=True. Repetí el ejercicio 1 con passthrough=True. ¿Mejora la accuracy? Pensá por qué (el blender ve features originales además de las predicciones).",
      "Variando cv. Probá cv=3, cv=5, cv=10 en el stacking. Mirá accuracy y tiempo de entrenamiento. Trade-off típico.",
      "Stacking vs Voting. Entrená un VotingClassifier(voting='soft') con los mismos tres base. Compará accuracy contra stacking. Discutí costo computacional."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/090-stacking/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/091-maldicion-de-la-dimensionalidad",
    "number": 91,
    "slug": "091-maldicion-de-la-dimensionalidad",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "La maldición de la dimensionalidad",
    "description": "Que el alumno entienda por qué los algoritmos basados en distancia (kNN, k-means, SVM-RBF) degradan en alta dimensión: el espacio se vuelve mayormente vacío, las distancias entre puntos colapsan a un mismo valor, y los…",
    "level": "Intermedio",
    "duration": "45 min",
    "theory": "Que el alumno entienda por qué los algoritmos basados en distancia (kNN, k-means, SVM-RBF) degradan en alta dimensión: el espacio se vuelve mayormente vacío, las distancias entre puntos colapsan a un mismo valor, y los modelos overfittean. Esto motiva la reducción de dimensionalidad (PCA, manifold learning) que viene en las próximas clases.",
    "outcomes": [
      "Explicar la sparsity exponencial: por qué llenar uniformemente un hipercubo unitario requiere n^d puntos.",
      "Calcular numéricamente que en d=100 la razón (d_max - d_min) / d_min entre distancias euclidianas tiende a 0.",
      "Identificar qué algoritmos sufren la maldición (basados en distancia/densidad) y cuáles menos (árboles, modelos lineales con regularización).",
      "Reconocer la manifold hypothesis como justificación de PCA, t-SNE, UMAP: los datos reales viven en un subespacio de baja dimensión.",
      "Decidir cuándo reducir dimensionalidad vs. cuándo regularizar o usar otro modelo."
    ],
    "topics": [
      "Intuición geométrica: hipercubo y volumen del borde",
      "Sparsity exponencial",
      "Concentración de la medida",
      "Distancia euclidiana pierde sentido",
      "Hubness",
      "Manifold hypothesis",
      "Implicaciones prácticas para ML"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Volumen del borde. Calculá la fracción de volumen del hipercubo [0,1]^d que está a menos de 0.01 del borde, para d=2, 10, 100. Fórmula: 1 - 0.98^d.",
      "Concentración de distancias. Sampleá 1000 puntos uniformes en [0,1]^d. Para d ∈ {2, 10, 100, 1000}, calculá (d_max - d_min) / d_min sobre todas las distancias pairwise. Verificá que tiende a 0.",
      "Distancia al vecino más cercano. Con n=1000 puntos uniformes y d variable, graficá la distancia media al 1-NN. Mostrá que crece con d (el \"vecino\" está cada vez más lejos).",
      "kNN degrada. Generá clasificación sintética con n=500, agregando d features de ruido puro (irrelevantes). Evaluá accuracy de KNeighborsClassifier para d = 2, 10, 50, 200. Curva debería caer.",
      "Manifold hipótesis empírica. Cargá sklearn.datasets.load_digits. Calculá cuántos componentes PCA explican el 95% de la varianza vs. d=64 originales — estimación grosera de dimensión intrínseca."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/091-maldicion-de-la-dimensionalidad/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/092-pca-proyeccion-varianza-explicada-incremental-randomized-kernel",
    "number": 92,
    "slug": "092-pca-proyeccion-varianza-explicada-incremental-randomized-kernel",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "PCA: proyección, varianza explicada, incremental, randomized, kernel",
    "description": "Dominar PCA como técnica de reducción de dimensionalidad lineal: entender la proyección al subespacio de máxima varianza vía SVD, elegir el número de componentes con explained_variance_ratio_, y aplicar las variantes (I…",
    "level": "Intermedio",
    "duration": "80 min",
    "theory": "Dominar PCA como técnica de reducción de dimensionalidad lineal: entender la proyección al subespacio de máxima varianza vía SVD, elegir el número de componentes con explained_variance_ratio_, y aplicar las variantes (Incremental, Randomized, Kernel) según el tamaño y la geometría del dataset.",
    "outcomes": [
      "Explicar geométricamente qué hace PCA (proyección al hiperplano que maximiza la varianza).",
      "Ajustar PCA de scikit-learn y leer components_, explained_variance_ratio_ y singular_values_.",
      "Elegir el número de componentes vía umbral de varianza acumulada (ej. 95%) o codo del scree plot.",
      "Decidir entre PCA, IncrementalPCA y PCA(svd_solver=\"randomized\") según memoria y velocidad.",
      "Aplicar KernelPCA (RBF/poly) para datasets con estructura no-lineal y tunear gamma con GridSearchCV."
    ],
    "topics": [
      "Maldición de la dimensionalidad y motivación de PCA.",
      "Proyección al subespacio de máxima varianza: intuición geométrica.",
      "SVD como motor algebraico de PCA.",
      "Varianza explicada y elección de n_components (entero, ratio, \"mle\").",
      "IncrementalPCA para datasets que no entran en RAM (partial_fit).",
      "Randomized PCA (svd_solver=\"randomized\") para acelerar en alta dimensión.",
      "KernelPCA con kernels RBF, polinómico y sigmoide; tuning de gamma.",
      "Pipeline completo: StandardScaler → PCA → modelo."
    ],
    "materials": [
      "MNIST (fetch_openml(\"mnist_784\")) — 70.000 × 784, ideal para mostrar reducción a ~150 componentes preservando 95% de varianza.",
      "Swiss roll (sklearn.datasets.make_swiss_roll) — para contrastar PCA lineal vs KernelPCA RBF.",
      "Géron, Hands-On ML, cap. 8 — Dimensionality Reduction, sección \"PCA\"."
    ],
    "exercises": [
      "Cargá MNIST, aplicá StandardScaler + PCA(n_components=0.95) y reportá cuántos componentes quedaron.",
      "Graficá la curva de varianza acumulada (cumsum(explained_variance_ratio_)) y marcá el codo.",
      "Compará tiempos de PCA(svd_solver=\"full\") vs \"randomized\" sobre MNIST con %timeit.",
      "Usá IncrementalPCA con n_batches=100 y verificá que el resultado se aproxima al PCA full (cosine similarity entre componentes > 0.99).",
      "Sobre make_swiss_roll(n_samples=1000), aplicá KernelPCA(kernel=\"rbf\", gamma=0.04, n_components=2) y comparalo con PCA lineal en un scatter 2D."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/092-pca-proyeccion-varianza-explicada-incremental-randomized-kernel/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/093-lle",
    "number": 93,
    "slug": "093-lle",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "LLE (Locally Linear Embedding)",
    "description": "Entender LLE como técnica no lineal de reducción de dimensionalidad basada en manifold learning: preservar las relaciones lineales locales entre cada punto y sus vecinos para \"desenrollar\" estructuras curvas (Swiss roll…",
    "level": "Intermedio",
    "duration": "45 min",
    "theory": "Entender LLE como técnica no lineal de reducción de dimensionalidad basada en manifold learning: preservar las relaciones lineales locales entre cada punto y sus vecinos para \"desenrollar\" estructuras curvas (Swiss roll, S-curve) donde PCA falla.",
    "outcomes": [
      "Explicar la intuición de LLE: cada punto se reconstruye como combinación lineal de sus k vecinos, y esa relación se preserva en baja dimensión.",
      "Aplicar sklearn.manifold.LocallyLinearEmbedding sobre un dataset no lineal (Swiss roll) y visualizar el resultado en 2D.",
      "Elegir el hiperparámetro n_neighbors y discutir su impacto (sub/sobre-ajuste local).",
      "Comparar LLE contra PCA y otras técnicas no lineales (Isomap, t-SNE) en términos de qué preservan.",
      "Identificar cuándo LLE es apropiado y cuándo conviene usar la variante Modified LLE."
    ],
    "topics": [
      "Motivación: limitaciones de PCA en manifolds curvos.",
      "Algoritmo LLE en dos pasos: (1) pesos de reconstrucción local, (2) embedding que preserva esos pesos.",
      "Hiperparámetros: n_neighbors, n_components, method (standard, modified, hessian, ltsa).",
      "Variantes: Modified LLE (MLLE), Hessian LLE, LTSA.",
      "Visualización del Swiss roll antes y después.",
      "Limitaciones: costo computacional O(m log(m) · n · k³ + m · n · k²) y sensibilidad al ruido."
    ],
    "materials": [
      "sklearn.datasets.make_swiss_roll(n_samples=1000, noise=0.2) — dataset clásico para visualizar reducción no lineal.",
      "sklearn.datasets.make_s_curve(n_samples=1000) — manifold alternativo en forma de S.",
      "sklearn.manifold.LocallyLinearEmbedding.",
      "Géron, cap. 8 — sección \"LLE\" y figuras del Swiss roll."
    ],
    "exercises": [
      "Swiss roll básico: generá un Swiss roll de 1000 puntos, aplicá LocallyLinearEmbedding(n_neighbors=10, n_components=2) y graficá el resultado coloreando por la coordenada original t. Verificá que el rollo quede \"desenrollado\".",
      "Comparación con PCA: sobre el mismo Swiss roll, aplicá PCA(n_components=2) y compará visualmente. Discutí por qué PCA aplasta el rollo en lugar de desenrollarlo.",
      "Barrido de n_neighbors: probá n_neighbors ∈ {5, 10, 30, 100} y graficá los 4 embeddings en una grilla 2×2. Describí qué pasa en cada extremo.",
      "Modified LLE: repetí el ejercicio 1 con method='modified' y n_neighbors=12. Compará con el LLE estándar — ¿qué embedding se ve más limpio?",
      "LLE sobre datos reales: cargá load_digits() (64 dimensiones) y proyectá a 2D con LLE. Coloreá por dígito. ¿Se separan las clases?"
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/093-lle/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/094-mds-isomap-t-sne-umap-lda",
    "number": 94,
    "slug": "094-mds-isomap-t-sne-umap-lda",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "MDS, Isomap, t-SNE, UMAP, LDA",
    "description": "Conocer y aplicar técnicas de reducción de dimensionalidad más allá de PCA: MDS, Isomap, t-SNE, UMAP y LDA.",
    "level": "Intermedio",
    "duration": "80 min",
    "theory": "Conocer y aplicar técnicas de reducción de dimensionalidad más allá de PCA: MDS, Isomap, t-SNE, UMAP y LDA. Entender qué preserva cada una (distancias, geodésicas, vecindarios locales, estructura global, separación entre clases) y cuándo elegir cada método según el problema (visualización 2D, preprocesamiento para clasificación, datos en variedades no lineales).",
    "outcomes": [
      "Distinguís entre métodos lineales (PCA, LDA) y no lineales (Isomap, t-SNE, UMAP) y sabés cuándo usar cada uno.",
      "Aplicás MDS, Isomap, TSNE, umap.UMAP y LinearDiscriminantAnalysis de scikit-learn / umap-learn sobre datasets reales.",
      "Configurás los hiperparámetros clave: perplexity (t-SNE), n_neighbors y min_dist (UMAP), n_neighbors (Isomap).",
      "Interpretás correctamente embeddings 2D: qué significan los clusters, qué NO significan las distancias entre clusters en t-SNE.",
      "Justificás por qué UMAP suele ser preferible a t-SNE: más rápido, preserva mejor la estructura global y es determinista con random_state."
    ],
    "topics": [
      "Tipo",
      "No lineal",
      "No lineal",
      "No lineal",
      "No lineal",
      "Lineal supervisado"
    ],
    "materials": [
      "sklearn.datasets.make_swiss_roll — clásico para Isomap vs PCA.",
      "sklearn.datasets.load_digits — 8x8 = 64 dims, ideal para visualizar con t-SNE/UMAP.",
      "sklearn.datasets.fetch_openml('mnist_784') — 70k × 784, para comparar tiempos t-SNE vs UMAP.",
      "Librerías: scikit-learn (MDS, Isomap, TSNE, LDA) + umap-learn (pip install umap-learn)."
    ],
    "exercises": [
      "Generá un Swiss roll con make_swiss_roll(n_samples=1500) y reducí a 2D con PCA, MDS e Isomap. Graficá los tres y comentá cuál \"desenrolla\" la variedad.",
      "Cargá load_digits y aplicá t-SNE con perplexity ∈ {5, 30, 50, 100}. Mostrá los 4 plots y explicá el efecto.",
      "Sobre load_digits, compará t-SNE vs UMAP: medí tiempo de ejecución con time.perf_counter() y reportá ambos embeddings 2D.",
      "Aplicá LDA a load_digits reduciendo a 2D y a 9D. Entrená un LogisticRegression sobre cada versión y compará accuracy con el original (64 dims).",
      "Con UMAP sobre load_digits, probá n_neighbors ∈ {2, 15, 100} con min_dist=0.1. Graficá los tres y explicá el trade-off local vs global."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/094-mds-isomap-t-sne-umap-lda/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/095-clustering-k-means-seleccion-de-k-mini-batch",
    "number": 95,
    "slug": "095-clustering-k-means-seleccion-de-k-mini-batch",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Clustering K-Means: selección de K, MiniBatch",
    "description": "Aplicar K-Means para segmentar datos no etiquetados, elegir el número de clusters K con criterios reproducibles (elbow, silhouette) y escalar el algoritmo con MiniBatchKMeans cuando el dataset no entra cómodo en memoria.",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Aplicar K-Means para segmentar datos no etiquetados, elegir el número de clusters K con criterios reproducibles (elbow, silhouette) y escalar el algoritmo con MiniBatchKMeans cuando el dataset no entra cómodo en memoria.",
    "outcomes": [
      "Explicar el algoritmo de Lloyd y por qué K-Means++ mejora la inicialización aleatoria.",
      "Ajustar KMeans de scikit-learn fijando n_init y random_state para resultados estables.",
      "Elegir K combinando elbow method (inercia vs K) y silhouette score.",
      "Reemplazar KMeans por MiniBatchKMeans y discutir el trade-off velocidad / calidad.",
      "Diagnosticar por qué K-Means falla sin escalado o frente a clusters no esféricos."
    ],
    "topics": [
      "Clustering no supervisado: planteo del problema.",
      "Algoritmo de Lloyd: asignación + actualización de centroides.",
      "Inicialización: random vs K-Means++; rol de n_init.",
      "Inercia (within-cluster sum of squares) como objetivo.",
      "Selección de K: elbow method, silhouette score, gap statistic (mención).",
      "MiniBatchKMeans para datasets grandes / streaming.",
      "Limitaciones: clusters no convexos, densidades distintas, sensibilidad al escalado."
    ],
    "materials": [
      "sklearn.datasets.make_blobs(n_samples=2000, centers=5, cluster_std=0.8, random_state=42) para los ejercicios de exploración.",
      "sklearn.datasets.load_digits() (1797 × 64) para el ejercicio de MiniBatchKMeans.",
      "Opcional: dataset Mall_Customers.csv o cualquier CSV tabular numérico ya escalado."
    ],
    "exercises": [
      "Generá blobs con 5 centros, ajustá KMeans(n_clusters=5, n_init=10, random_state=42) y graficá los puntos coloreados por etiqueta junto con cluster_centers_.",
      "Para K en range(2, 11), calculá inertia_ y silhouette_score. Graficá ambas curvas y justificá el K elegido.",
      "Repetí el ajuste sin escalar un dataset donde una feature tenga escala 100× mayor que la otra. Compará con StandardScaler previo y comentá el cambio en las etiquetas.",
      "Sobre load_digits(), ajustá KMeans(n_clusters=10) y MiniBatchKMeans(n_clusters=10, batch_size=256). Cronometrá ambos con %timeit y compará inercias.",
      "Probá K-Means sobre make_moons(noise=0.05). Mostrá visualmente por qué falla y proponé qué algoritmo usarías en su lugar (te lo vamos a contestar en la clase 096)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/095-clustering-k-means-seleccion-de-k-mini-batch/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/096-dbscan",
    "number": 96,
    "slug": "096-dbscan",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "DBSCAN",
    "description": "Que el alumno aplique DBSCAN (Density-Based Spatial Clustering of Applications with Noise) para descubrir clusters de forma arbitraria e identificar outliers nativamente, sin tener que predefinir k como en K-Means.",
    "level": "Intermedio",
    "duration": "55 min",
    "theory": "Que el alumno aplique DBSCAN (Density-Based Spatial Clustering of Applications with Noise) para descubrir clusters de forma arbitraria e identificar outliers nativamente, sin tener que predefinir k como en K-Means. Que sepa elegir eps con un k-distance plot y entienda cuándo conviene escalar a HDBSCAN.",
    "outcomes": [
      "Ejecutar DBSCAN con sklearn.cluster.DBSCAN y tunear eps y min_samples para un dataset 2D.",
      "Elegir eps mirando el codo del k-distance plot (no a ojo).",
      "Identificar outliers vía la etiqueta -1 que DBSCAN asigna a los puntos ruido.",
      "Distinguir core / border / noise points y entender la noción de density-reachable.",
      "Comparar DBSCAN vs K-Means y saber cuándo usar HDBSCAN (eps variable, clusters de densidad mixta)."
    ],
    "topics": [
      "Intuición de densidad vs centroides",
      "Hiperparámetros eps y min_samples",
      "Core / border / noise points",
      "k-distance plot para elegir eps",
      "Etiqueta -1 y detección de outliers",
      "Limitaciones: densidad uniforme, curse of dimensionality",
      "HDBSCAN como evolución"
    ],
    "materials": [
      "make_moons(n_samples=1000, noise=0.05) de scikit-learn — dos lunas entrelazadas, el caso canónico donde K-Means falla y DBSCAN brilla.",
      "make_blobs con densidades distintas para mostrar la limitación de DBSCAN y motivar HDBSCAN."
    ],
    "exercises": [
      "DBSCAN sobre moons. Entrená DBSCAN(eps=0.2, min_samples=5) sobre make_moons. Graficá los clusters y contá cuántos puntos quedaron como -1.",
      "K-distance plot. Calculá la distancia al k-ésimo vecino más cercano (k=min_samples) para todos los puntos, ordenala y graficala. Identificá el codo y usalo como eps.",
      "Sensibilidad a eps. Probá eps ∈ {0.05, 0.1, 0.2, 0.5} y reportá número de clusters y % de ruido en cada caso. Mostrá cómo eps chico = todo ruido y eps grande = un cluster.",
      "DBSCAN vs K-Means. Sobre el mismo make_moons, corré ambos con k=2. Mostrá visualmente que K-Means parte las lunas por la mitad y DBSCAN las separa bien.",
      "HDBSCAN sobre densidades mixtas. Generá blobs con cluster_std distinto por blob. Mostrá que un eps único en DBSCAN no puede capturar ambos, y que HDBSCAN(min_cluster_size=20) sí."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/096-dbscan/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/097-clustering-agglomerative-birch-mean-shift-affinity-propagation-spectra",
    "number": 97,
    "slug": "097-clustering-agglomerative-birch-mean-shift-affinity-propagation-spectra",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Agglomerative, BIRCH, Mean Shift, Affinity Propagation, Spectral",
    "description": "Que el alumno conozca el zoológico de algoritmos de clustering más allá de K-Means y DBSCAN — Agglomerative (jerárquico, lee dendrogramas), BIRCH (escalable a millones de filas), Mean Shift (denso, sin especificar k), A…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Que el alumno conozca el zoológico de algoritmos de clustering más allá de K-Means y DBSCAN — Agglomerative (jerárquico, lee dendrogramas), BIRCH (escalable a millones de filas), Mean Shift (denso, sin especificar k), Affinity Propagation (elige exemplars por message-passing) y Spectral Clustering (clustering vía autovectores del grafo de similitud) — y sepa cuándo elegir cada uno según tamaño del dataset, forma de los clusters y necesidad de jerarquía.",
    "outcomes": [
      "Construir un dendrograma con scipy.cluster.hierarchy.linkage y cortarlo a una altura dada para obtener clusters.",
      "Elegir un linkage (ward, complete, average, single) según la forma esperada de los clusters y conocer el efecto del chaining en single.",
      "Usar BIRCH para datasets que no entran en memoria, ajustando threshold y branching_factor.",
      "Aplicar Mean Shift ajustando bandwidth (con estimate_bandwidth) y entender por qué descubre el número de clusters automáticamente.",
      "Decidir entre Affinity Propagation y Spectral Clustering según escalabilidad (AP es O(n²) en memoria) y geometría (Spectral funciona en clusters no convexos)."
    ],
    "topics": [
      "Agglomerative",
      "BIRCH",
      "Mean Shift",
      "Affinity Propagation",
      "Spectral"
    ],
    "materials": [
      "make_blobs (sklearn) — para Agglomerative y BIRCH (clusters convexos).",
      "make_moons y make_circles — clusters no convexos, donde Spectral brilla y K-Means/Agglomerative-ward fallan.",
      "Dataset opcional escalable: generá 1M de puntos sintéticos para probar BIRCH vs K-Means en tiempo y memoria."
    ],
    "exercises": [
      "Dendrograma sobre make_blobs. Generá 50 puntos en 4 blobs. Calculá Z = linkage(X, method='ward') y graficá el dendrograma. Cortá a una altura que dé 4 clusters. Comparalo con AgglomerativeClustering(n_clusters=4).",
      "Linkage comparison. Sobre make_moons(n_samples=300, noise=0.05), ajustá AgglomerativeClustering(n_clusters=2) con linkage='ward', 'complete', 'average', 'single'. Ploteá los 4 resultados lado a lado. ¿Cuál recupera las dos lunas? ¿Por qué?",
      "BIRCH escalable. Generá 100k puntos con make_blobs. Medí tiempo y memoria de BIRCH(n_clusters=5) vs KMeans(n_clusters=5). Variá threshold ∈ {0.1, 0.5, 1.0} y mostrá cómo cambia el número de sub-clusters internos del CF-tree.",
      "Mean Shift sin saber k. Sobre 3 blobs claros, corré MeanShift(bandwidth=estimate_bandwidth(X, quantile=0.2)). Verificá que recupera 3 clusters automáticamente. Después poné quantile=0.5 y observá cómo colapsa a menos clusters.",
      "Spectral vs K-Means en make_circles. Generá dos círculos concéntricos con make_circles(n_samples=500, factor=0.5, noise=0.05). Ajustá KMeans(n_clusters=2) y SpectralClustering(n_clusters=2, affinity='nearest_neighbors'). Graficá ambos. Documentá por qué Spectral funciona y K-Means no."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/097-clustering-agglomerative-birch-mean-shift-affinity-propagation-spectra/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/098-gaussian-mixture-models",
    "number": 98,
    "slug": "098-gaussian-mixture-models",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Gaussian Mixture Models",
    "description": "Entender los Gaussian Mixture Models (GMM) como modelo probabilístico de soft clustering, ajustarlos con el algoritmo EM en scikit-learn, elegir el número de componentes con BIC/AIC, y conocer las variantes (covariance_…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Entender los Gaussian Mixture Models (GMM) como modelo probabilístico de soft clustering, ajustarlos con el algoritmo EM en scikit-learn, elegir el número de componentes con BIC/AIC, y conocer las variantes (covariance_type, BayesianGaussianMixture) para aplicarlas en clustering, densidad y detección de anomalías.",
    "outcomes": [
      "Explicar qué es un GMM y cómo se diferencia de K-Means (asignación dura vs. probabilística).",
      "Ajustar un GaussianMixture con scikit-learn y obtener predict, predict_proba y score_samples.",
      "Seleccionar el número óptimo de componentes comparando BIC y AIC en una grilla.",
      "Elegir el covariance_type apropiado (full, tied, diag, spherical) según supuestos y tamaño del dataset.",
      "Usar BayesianGaussianMixture para que el modelo descarte componentes innecesarios automáticamente."
    ],
    "topics": [
      "Modelos de mezcla: intuición y fórmula.",
      "Algoritmo Expectation-Maximization (EM): paso E (responsabilidades) + paso M (actualizar medias, covarianzas, pesos).",
      "API de sklearn.mixture.GaussianMixture: n_components, covariance_type, n_init, tol.",
      "Métodos: predict_proba (soft), score_samples (log-densidad), sample (generar datos).",
      "Selección de modelo con BIC y AIC.",
      "Variantes de covarianza y su impacto en parámetros / sesgo / varianza.",
      "Bayesian GMM con prior de Dirichlet: aprende cuántos componentes hacen falta.",
      "Detección de anomalías por umbral sobre densidad."
    ],
    "materials": [
      "sklearn.datasets.make_blobs con clusters de varianzas distintas (para ver el aporte vs. K-Means).",
      "sklearn.datasets.load_iris para validar agrupamiento contra etiquetas reales.",
      "Opcional: dataset Old Faithful (geyser) — clásico ejemplo de mezcla bimodal."
    ],
    "exercises": [
      "Ajuste básico: generá make_blobs con 3 centros y cluster_std variable. Ajustá GaussianMixture(n_components=3) y compará predict con las etiquetas reales (ARI).",
      "Soft vs. hard: sobre el mismo dataset, mostrá predict_proba de 5 puntos cerca de la frontera. Compará con la asignación dura de K-Means.",
      "Selección de K con BIC/AIC: ajustá GMMs con n_components de 1 a 10. Graficá BIC y AIC vs. K e identificá el mínimo.",
      "covariance_type: repetí el ajuste con los 4 tipos sobre un dataset con clusters elípticos rotados. Compará BIC y visualizá las elipses de covarianza.",
      "Bayesian GMM: ajustá BayesianGaussianMixture(n_components=10, weight_concentration_prior=0.01) sobre datos con 3 clusters reales y mostrá que los pesos efectivos son ≈ 3."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/098-gaussian-mixture-models/notebook.ipynb"
  },
  {
    "id": "parte-1-machine-learning-clasico/099-deteccion-de-anomalias-isolation-forest-lof-one-class-svm",
    "number": 99,
    "slug": "099-deteccion-de-anomalias-isolation-forest-lof-one-class-svm",
    "partSlug": "parte-1-machine-learning-clasico",
    "title": "Detección de anomalías: Isolation Forest, LOF, One-Class SVM",
    "description": "Que el alumno detecte puntos anómalos (fraude, fallas, outliers) en datos sin etiquetas, eligiendo entre Isolation Forest, LOF, One-Class SVM y Elliptic Envelope según la geometría del problema, y entendiendo la diferen…",
    "level": "Intermedio",
    "duration": "70 min",
    "theory": "Que el alumno detecte puntos anómalos (fraude, fallas, outliers) en datos sin etiquetas, eligiendo entre Isolation Forest, LOF, One-Class SVM y Elliptic Envelope según la geometría del problema, y entendiendo la diferencia entre outlier detection (entrenar con datos sucios) y novelty detection (entrenar limpio, predecir sobre nuevos).",
    "outcomes": [
      "Distinguir outlier detection vs novelty detection y elegir el algoritmo acorde.",
      "Entrenar IsolationForest y ajustar el hiperparámetro contamination.",
      "Usar LocalOutlierFactor en modo novelty=False (fit_predict) y novelty=True (predict).",
      "Aplicar OneClassSVM y EllipticEnvelope, reconociendo sus supuestos (kernel, gaussianidad).",
      "Evaluar detectores de anomalías con score_samples, ROC-AUC y reglas de negocio (top-k)."
    ],
    "topics": [
      "Outlier vs novelty detection",
      "Isolation Forest",
      "Local Outlier Factor (LOF)",
      "One-Class SVM",
      "Elliptic Envelope",
      "score_samples y umbrales",
      "Evaluación sin labels"
    ],
    "materials": [
      "Material de la clase en el repositorio"
    ],
    "exercises": [
      "Isolation Forest baseline. Generá 2 blobs + 5% de outliers uniformes. Ajustá IsolationForest(contamination=0.05). Plot 2D con inliers vs outliers detectados.",
      "LOF local. Usá el mismo dataset pero metiendo un outlier dentro de uno de los blobs (anomalía local). Comparar Isolation Forest vs LocalOutlierFactor(n_neighbors=20): ¿cuál lo agarra?",
      "One-Class SVM con escalado. Entrená OneClassSVM(kernel='rbf', nu=0.05) con y sin StandardScaler. Comparar fronteras de decisión.",
      "Top-k con score_samples. Usá score_samples de Isolation Forest, ordená ascendente, y devolvé los 10 puntos más anómalos. Inspeccionálos visualmente.",
      "Evaluación con labels. Sobre fetch_kddcup99 (subset), entrená Isolation Forest sin usar labels. Después calculá ROC-AUC contra las labels reales (normal. vs ataque). Reportá AUC."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-1-machine-learning-clasico/099-deteccion-de-anomalias-isolation-forest-lof-one-class-svm/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/100-perceptron-mlp-y-backpropagation",
    "number": 100,
    "slug": "100-perceptron-mlp-y-backpropagation",
    "partSlug": "parte-2-deep-learning",
    "title": "Perceptrón, MLP y backpropagation",
    "description": "Que el alumno entienda la unidad fundamental del Deep Learning: la neurona artificial (perceptrón de Rosenblatt 1957), por qué un solo perceptrón no puede aprender XOR, cómo el MLP (Multi-Layer Perceptron) lo resuelve a…",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Que el alumno entienda la unidad fundamental del Deep Learning: la neurona artificial (perceptrón de Rosenblatt 1957), por qué un solo perceptrón no puede aprender XOR, cómo el MLP (Multi-Layer Perceptron) lo resuelve apilando capas con activaciones no lineales, y cómo backpropagation (regla de la cadena) permite calcular gradientes en cualquier grafo computacional — el algoritmo que destrabó el Deep Learning moderno.",
    "outcomes": [
      "Implementar a mano un perceptrón (y = step(w·x + b)) y mostrar por qué no separa XOR.",
      "Construir un MLP con keras.Sequential([Dense(...), Dense(...)]) y entrenarlo sobre un dataset simple.",
      "Explicar forward pass (compute layer by layer) y backward pass (propagar gradientes con la regla de la cadena).",
      "Calcular a mano los gradientes para un MLP de 2 capas con una sola muestra.",
      "Reconocer que la diferenciación automática (autograd) hace innecesario derivar a mano para modelos arbitrarios."
    ],
    "topics": [
      "Perceptrón clásico (Rosenblatt 1957)",
      "El problema XOR",
      "MLP: input → hidden → output",
      "Activación no lineal",
      "Backpropagation (Rumelhart, Hinton & Williams 1986)",
      "Autograd / autodiff"
    ],
    "materials": [
      "sklearn.datasets.make_moons(n_samples=500, noise=0.2) — clásico para mostrar no linealidad.",
      "XOR como dataset de 4 puntos (ejercicio motivacional).",
      "Librerías: tensorflow, keras (incluido), numpy, matplotlib."
    ],
    "exercises": [
      "Perceptrón a mano: implementá un perceptrón en numpy y entrenalo en AND/OR (separables). Después probá con XOR; mostrá que no converge.",
      "MLP con Keras: model = keras.Sequential([Dense(8, activation='relu', input_shape=(2,)), Dense(1, activation='sigmoid')]). Entrenalo sobre XOR; debería llegar a accuracy 1.0.",
      "Visualización decision boundary: con make_moons, entrená un MLP [16, 8] y graficá la frontera con un meshgrid.",
      "Backprop a mano: para un MLP con 1 input, 1 hidden (2 neuronas), 1 output, con MSE, calculá ∂L/∂w para una muestra y comparalo con tf.GradientTape.",
      "¿Y sin activación no lineal?: cambiá las activaciones a linear en el MLP de XOR y mostrá que ya no puede aprenderlo."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/100-perceptron-mlp-y-backpropagation/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/101-regresion-y-clasificacion-con-mlp",
    "number": 101,
    "slug": "101-regresion-y-clasificacion-con-mlp",
    "partSlug": "parte-2-deep-learning",
    "title": "Regresión y clasificación con MLP",
    "description": "Saber construir y entrenar un MLP para los tres tipos de problemas tabulares estándar — regresión, clasificación binaria y clasificación multiclase — eligiendo correctamente la activación de salida y la loss para cada c…",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Saber construir y entrenar un MLP para los tres tipos de problemas tabulares estándar — regresión, clasificación binaria y clasificación multiclase — eligiendo correctamente la activación de salida y la loss para cada caso. Hacer un train/val/test split adecuado y leer las curvas de entrenamiento.",
    "outcomes": [
      "Mapear problema → activación de salida → loss: regresión → linear + MSE; binario → sigmoid + binary_crossentropy; multiclase → softmax + sparse_categorical_crossentropy.",
      "Hacer split train / validation / test con train_test_split y pasar validation_data a model.fit.",
      "Leer history.history['loss'] y ['val_loss'], identificar overfitting (val sube mientras train baja).",
      "Aplicar EarlyStopping y ModelCheckpoint callbacks como protección estándar.",
      "Diferenciar sparse_categorical_crossentropy (labels enteros) de categorical_crossentropy (labels one-hot)."
    ],
    "topics": [
      "Mapeo problema → arquitectura de salida + loss.",
      "Activación de salida: linear, sigmoid, softmax.",
      "Train/val/test split — por qué hace falta los tres (val para selección, test para reporte final).",
      "Curvas de aprendizaje: lectura visual (subfitting / overfitting).",
      "Callbacks: EarlyStopping(patience=5, restore_best_weights=True), ModelCheckpoint.",
      "Normalización de inputs con Normalization() layer o StandardScaler."
    ],
    "materials": [
      "Regresión: sklearn.datasets.fetch_california_housing().",
      "Clasificación binaria: sklearn.datasets.load_breast_cancer().",
      "Multiclase: keras.datasets.fashion_mnist.load_data() (10 clases).",
      "Librerías: tensorflow, keras, scikit-learn, matplotlib."
    ],
    "exercises": [
      "MLP regresión: California Housing, MLP [64, 32] con Normalization(), salida linear, loss mse. Reportar MAE en test.",
      "MLP binario: breast_cancer, MLP [32, 16], salida sigmoid, loss binary_crossentropy. Reportar accuracy y AUC.",
      "MLP multiclase: Fashion-MNIST (aplastado a 784), MLP [256, 128], salida softmax(10), loss sparse_categorical_crossentropy. Reportar accuracy.",
      "Curvas y overfitting: entrenar el modelo 3 por 50 épocas sin early stopping. Graficar loss y val_loss; identificar la época donde arranca overfitting.",
      "EarlyStopping: repetir con EarlyStopping(patience=5, restore_best_weights=True). Verificar que cortó antes y los pesos guardados son los mejores."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/101-regresion-y-clasificacion-con-mlp/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/102-keras-sequential-api",
    "number": 102,
    "slug": "102-keras-sequential-api",
    "partSlug": "parte-2-deep-learning",
    "title": "Keras Sequential API",
    "description": "Dominar la Sequential API de Keras — la forma más simple y declarativa de construir un modelo cuando es una pila lineal de capas.",
    "level": "Avanzado",
    "duration": "60 min",
    "theory": "Dominar la Sequential API de Keras — la forma más simple y declarativa de construir un modelo cuando es una pila lineal de capas. Saber cuándo NO alcanza (cualquier topología con ramas, skip connections, multi-input/multi-output → Functional API, clase 103).",
    "outcomes": [
      "Construir un modelo con keras.Sequential([...]) o model.add(...) incrementalmente.",
      "Inspeccionar la arquitectura con model.summary() (parámetros por capa, output shape, total).",
      "Calcular a mano el número de parámetros de una Dense(n) (= input_dim * n + n por el bias).",
      "Compilar (compile), entrenar (fit), evaluar (evaluate) y predecir (predict).",
      "Guardar y cargar con el formato moderno .keras (HDF5 legacy)."
    ],
    "topics": [
      "Dos formas equivalentes: lista en el constructor vs .add() incremental.",
      "Input layer explícito vs input_shape en la primera capa.",
      "model.summary(): leer parámetros por capa + total trainable / non-trainable.",
      "compile(optimizer, loss, metrics).",
      "fit(X, y, epochs, batch_size, validation_split, callbacks, verbose).",
      "model.save('m.keras') (formato nativo Keras 3+) y keras.models.load_model('m.keras')."
    ],
    "materials": [
      "Reutilizar Fashion-MNIST de la clase anterior.",
      "Librerías: tensorflow, keras (≥ 3.0)."
    ],
    "exercises": [
      "Dos sintaxis: construir el mismo modelo dos veces — una con Sequential([...]) y otra con model = Sequential(); model.add(...). Verificar que summary() produce el mismo resultado.",
      "Conteo de parámetros: para Sequential([Dense(128, input_shape=(784,)), Dense(64), Dense(10)]), calcular a mano los parámetros y verificar contra model.summary().",
      "Guardado/carga: entrenar 5 épocas, model.save('m.keras'), recargar con load_model, verificar que predict da idéntico.",
      "Predict en batch vs individual: predecir 1 sola muestra (¿cómo cambia la shape?) vs predecir 100. Cuidado con la dimensión batch.",
      "Verbose: probá fit(..., verbose=0), verbose=1 (barra), verbose=2 (1 línea por época). Útil para notebooks vs scripts."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/102-keras-sequential-api/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/103-keras-functional-api-y-subclassing",
    "number": 103,
    "slug": "103-keras-functional-api-y-subclassing",
    "partSlug": "parte-2-deep-learning",
    "title": "Keras Functional API y Subclassing",
    "description": "Construir modelos con topologías no lineales —skip connections, multi-input, multi-output, capas compartidas— usando la Functional API (estilo \"grafo de capas\"), y modelos con flujo de control dinámico (loops, ifs) usan…",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Construir modelos con topologías no lineales —skip connections, multi-input, multi-output, capas compartidas— usando la Functional API (estilo \"grafo de capas\"), y modelos con flujo de control dinámico (loops, ifs) usando Subclassing (estilo class MyModel(Model) con call()). Saber elegir entre las tres APIs según el caso.",
    "outcomes": [
      "Construir un modelo Wide & Deep (clásico de Cheng et al. 2016) con Functional API.",
      "Construir un modelo multi-output con dos Dense finales y dos losses.",
      "Implementar un MyResBlock con Subclassing que tiene una skip connection.",
      "Reconocer el trade-off: Sequential (simple) → Functional (la mayoría de los casos) → Subclassing (cuando hace falta control dinámico).",
      "Convertir un modelo Functional en JSON / cargar con model_from_json (útil para serialización separada de pesos)."
    ],
    "topics": [
      "Functional API: x = layer(prev_x); al final Model(inputs=[...], outputs=[...]).",
      "Multi-input / multi-output: pasar listas o dicts a inputs= / outputs=.",
      "Capas compartidas (siamese networks): aplicar la misma instancia de capa a dos entradas distintas.",
      "Subclassing: heredar de keras.Model, definir __init__ (capas) y call(self, inputs, training=False).",
      "Cuándo subclassing: control de flujo dinámico, modelos imperativos estilo PyTorch."
    ],
    "materials": [
      "California Housing para Wide & Deep.",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "Wide & Deep: implementá el modelo de Cheng et al. con Functional API — input → wide path (directo a salida) + deep path (Dense × 2 → salida) → Add() → output.",
      "Multi-output: predecir simultáneamente precio (regresión) Y rango de precio (clasificación 3 clases) sobre California Housing. Compilar con dict de losses.",
      "Capa compartida (siamese): dos imágenes de entrada → mismo encoder Dense(64) aplicado a ambas → concatenar embeddings → clasificación \"same/different\".",
      "ResBlock con Subclassing: implementá una clase ResBlock(Layer) con dos Dense y skip connection. Usala en un modelo Sequential.",
      "plot_model: graficá el modelo Wide & Deep con keras.utils.plot_model(model, show_shapes=True). Identificá visualmente las dos rutas."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/103-keras-functional-api-y-subclassing/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/104-callbacks-tensorboard-guardar-restaurar-modelos",
    "number": 104,
    "slug": "104-callbacks-tensorboard-guardar-restaurar-modelos",
    "partSlug": "parte-2-deep-learning",
    "title": "Callbacks, TensorBoard, guardar/restaurar modelos",
    "description": "Inyectar lógica al loop de entrenamiento sin modificarlo, mediante callbacks (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, custom).",
    "level": "Avanzado",
    "duration": "60 min",
    "theory": "Inyectar lógica al loop de entrenamiento sin modificarlo, mediante callbacks (EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, custom). Visualizar el progreso del training en TensorBoard (loss, métricas, histogramas de pesos, embeddings). Saber guardar y restaurar correctamente — arquitectura + pesos + estado del optimizador.",
    "outcomes": [
      "Aplicar los 4 callbacks más usados: EarlyStopping, ModelCheckpoint, ReduceLROnPlateau, TensorBoard.",
      "Configurar TensorBoard: keras.callbacks.TensorBoard(log_dir='./logs') y abrirlo con tensorboard --logdir=./logs.",
      "Escribir un callback custom heredando de keras.callbacks.Callback con hooks como on_epoch_end.",
      "Distinguir guardado completo (model.save('m.keras')) vs solo pesos (model.save_weights('w.weights.h5')).",
      "Restaurar y continuar entrenamiento desde checkpoint sin pérdida."
    ],
    "topics": [
      "Callbacks: hooks (on_train_begin, on_epoch_end, on_batch_end, ...).",
      "EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True).",
      "ModelCheckpoint(filepath, save_best_only=True, monitor='val_accuracy', mode='max').",
      "ReduceLROnPlateau(factor=0.5, patience=5) — bajar LR cuando se estanca.",
      "TensorBoard: scalars, histograms, distributions, images, projector (embeddings).",
      "Custom callbacks: class MyCallback(keras.callbacks.Callback): def on_epoch_end(self, epoch, logs): ...."
    ],
    "materials": [
      "Fashion-MNIST o cualquier modelo entrenable de clases anteriores.",
      "Librerías: tensorflow, keras, tensorboard (incluido)."
    ],
    "exercises": [
      "EarlyStopping + Checkpoint: entrenar Fashion-MNIST con ambos callbacks. Verificar que cortó cuando val_loss se estancó y que 'best.keras' contiene los mejores pesos.",
      "TensorBoard: agregar TensorBoard(log_dir=f'./logs/run-{time}'), entrenar 10 épocas. Lanzar tensorboard --logdir=./logs y revisar scalars + histograms.",
      "ReduceLROnPlateau: configurar factor=0.5, patience=3, min_lr=1e-6. Graficar el LR a lo largo de las épocas (usar el logs del callback).",
      "Custom callback: escribir uno que loggee a un CSV el (epoch, loss, val_loss, lr_actual) para análisis offline.",
      "Restaurar y continuar: entrenar 10 épocas, guardar, recargar y continuar 5 épocas más. Verificar que el optimizer state (momentum de Adam) se preservó."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/104-callbacks-tensorboard-guardar-restaurar-modelos/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/105-keras-tuner",
    "number": 105,
    "slug": "105-keras-tuner",
    "partSlug": "parte-2-deep-learning",
    "title": "Keras Tuner (+ Optuna, Ray Tune)",
    "description": "Hacer hyperparameter tuning sistemático en redes neuronales — buscar n_layers, units, lr, dropout, etc.",
    "level": "Avanzado",
    "duration": "85 min",
    "theory": "Hacer hyperparameter tuning sistemático en redes neuronales — buscar n_layers, units, lr, dropout, etc. con estrategias modernas: Random Search, Hyperband y Bayesian Optimization. Conocer las tres herramientas estándar de Python — Keras Tuner (TF-native, simple), Optuna (multi-framework, default industrial) y Ray Tune (distribuido, escalable a clusters).",
    "outcomes": [
      "Definir un model-building function con hiperparámetros declarados vía hp.Int, hp.Float, hp.Choice.",
      "Lanzar tuners de Keras Tuner: RandomSearch, Hyperband, BayesianOptimization.",
      "Migrar el mismo problema a Optuna con optuna.create_study(direction='minimize') y trial.suggest_float.",
      "Lanzar Ray Tune con tune.run para distribuir trials en múltiples GPUs/nodos.",
      "Comparar las 3 estrategias (Random vs Hyperband vs Bayesian) en términos de eficiencia."
    ],
    "topics": [
      "¿Por qué tuning? Los defaults (Adam lr=1e-3, dropout 0.5) rara vez son óptimos.",
      "Random Search vs Grid Search: Bergstra & Bengio (2012) — random gana casi siempre por el \"curse of low effective dimensionality\".",
      "Hyperband (Li et al. 2017): asignar más cómputo a configs prometedoras (successive halving).",
      "Bayesian Optimization (TPE, GP): construye un modelo del paisaje y elige el siguiente trial inteligentemente.",
      "Trade-off cómputo vs ganancia: típicamente 50-200 trials para una primera optimización.",
      "Complemento moderno: Optuna y Ray Tune como alternativas multi-framework."
    ],
    "materials": [
      "Fashion-MNIST como dataset chico para iterar rápido.",
      "Librerías: keras-tuner (pip install keras-tuner), optuna, ray[tune]."
    ],
    "exercises": [
      "Keras Tuner — RandomSearch: tunear units ∈ {32, 64, 128} y lr ∈ [1e-4, 1e-2] log con 20 trials. Reportar mejores hiperparámetros y val_accuracy.",
      "Keras Tuner — Hyperband: el mismo espacio, 50 trials con Hyperband. Comparar tiempo total vs RandomSearch.",
      "Optuna: traducir el espacio a Optuna; correr 50 trials con HyperbandPruner; graficar plot_optimization_history y plot_param_importances.",
      "Multi-objective: optimizar simultáneamente val_accuracy (max) y n_params (min) con optuna.create_study(directions=['maximize', 'minimize']). Inspeccionar la Pareto front.",
      "Visualización: con Optuna, generar plot_parallel_coordinate(study) y entender qué dimensiones son las más sensibles."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/105-keras-tuner/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/106-ray-tune-hpo-distribuido",
    "number": 106,
    "slug": "106-ray-tune-hpo-distribuido",
    "partSlug": "parte-2-deep-learning",
    "title": "Ray Tune: HPO distribuido y a escala",
    "description": "Escalar hyperparameter tuning de DL a cluster con Ray Tune — el framework distribuido que la industria (Uber, Anyscale, OpenAI) usa cuando los trials toman horas y se necesitan decenas en paralelo.",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Escalar hyperparameter tuning de DL a cluster con Ray Tune — el framework distribuido que la industria (Uber, Anyscale, OpenAI) usa cuando los trials toman horas y se necesitan decenas en paralelo. Cubrir orquestación, schedulers modernos (ASHA, PBT Population Based Training), integración con W&B, MLflow, y combinación con Optuna como search algorithm.",
    "outcomes": [
      "Definir trainable(config) y reportar progreso con tune.report(loss=...).",
      "Configurar ASHA (Async Successive Halving) para podar trials malos.",
      "Aplicar Population Based Training (PBT) para evolución de hyperparams durante training.",
      "Asignar recursos: resources_per_trial={'cpu': 2, 'gpu': 1}.",
      "Usar OptunaSearch como search algorithm + Ray Tune como orchestrator."
    ],
    "topics": [
      "Ray cluster: local vs multi-node.",
      "Trainable: function-based vs class-based.",
      "ASHA scheduler — async successive halving.",
      "PBT — evoluciona hyperparams + checkpoints.",
      "BOHB — Bayesian opt + Hyperband.",
      "Loggers: TensorBoard, W&B, MLflow."
    ],
    "materials": [
      "Fashion-MNIST o cualquier dataset DL.",
      "Librerías: ray[tune], opcional optuna, lightning."
    ],
    "exercises": [
      "Trainable básico: train de CNN con metric report each epoch. tune.run(trainable, num_samples=20).",
      "ASHA: ASHAScheduler(metric='val_loss', mode='min', max_t=20, grace_period=3). Verificar pruning.",
      "PBT: 8 workers, copy + perturb each 5 epochs. Plot evolution de LR.",
      "OptunaSearch + ASHA: combination — Optuna sugiere, ASHA poda.",
      "Resources: gpus_per_trial=0.5 (fractional GPU sharing)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/106-ray-tune-hpo-distribuido/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/107-vanishing-exploding-gradients",
    "number": 107,
    "slug": "107-vanishing-exploding-gradients",
    "partSlug": "parte-2-deep-learning",
    "title": "Vanishing/exploding gradients",
    "description": "Entender el problema central que estancó el Deep Learning hasta 2010: cuando un gradiente atraviesa muchas capas, se desvanece (sigmoid/tanh saturadas → multiplicas números < 1 muchas veces → ≈ 0) o explota (pesos grand…",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Entender el problema central que estancó el Deep Learning hasta 2010: cuando un gradiente atraviesa muchas capas, se desvanece (sigmoid/tanh saturadas → multiplicas números < 1 muchas veces → ≈ 0) o explota (pesos grandes → > 1 muchas veces → ∞). Identificar los 4 culpables (activación, inicialización, profundidad, LR) y conocer las soluciones que destrabaron el campo: Glorot/He init (097), ReLU y variantes (098), BatchNorm (099), Gradient clipping (100).",
    "outcomes": [
      "Diagnosticar vanishing gradient: gradients en capas tempranas con norma ~ 1e-8.",
      "Diagnosticar exploding: loss = nan o gradients con norma ~ 1e+10.",
      "Inspeccionar gradientes con tf.GradientTape + tf.norm.",
      "Mapear cada solución al problema: init para arrancar bien, ReLU para no saturar, BN para estabilizar, clipping para evitar explosión.",
      "Explicar por qué sigmoid en MLPs profundos no escala (derivada máx. 0.25 → gradiente decae rápido)."
    ],
    "topics": [
      "Backprop como producto de derivadas a lo largo de capas.",
      "Sigmoid: σ(x) · (1 - σ(x)) máxima 0.25 en x=0; satura a 0 en colas.",
      "Tanh: derivada máx. 1, pero también satura.",
      "ReLU: derivada 0 o 1 — no decae al multiplicar, pero genera \"dying ReLU\".",
      "Inicialización mala: pesos N(0, 1) → activaciones explotan; pesos N(0, 0.01) → vanishing.",
      "BatchNorm: normaliza dentro del forward pass para que cada capa reciba inputs con varianza controlada."
    ],
    "materials": [
      "Fashion-MNIST.",
      "Librerías: tensorflow, keras, matplotlib."
    ],
    "exercises": [
      "Diagnóstico vanishing: entrenar un MLP de 10 capas con sigmoid activations e init default. Inspeccionar gradientes de la primera capa vs la última. Verificar que los de la primera son órdenes de magnitud más chicos.",
      "Mismo experimento con ReLU: comparar gradients. Mejor pero aún heterogéneo.",
      "Exploding: forzar init RandomNormal(stddev=5). Observar loss = nan en pocas iteraciones.",
      "Norma del gradiente por capa: con tf.GradientTape, calcular tf.norm(g) para cada peso y graficar a lo largo del entrenamiento.",
      "Solución sencilla: cambiar a He init + ReLU + BatchNorm y mostrar que el problema desaparece (anticipa las siguientes 4 clases)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/107-vanishing-exploding-gradients/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/108-inicializacion-glorot-he",
    "number": 108,
    "slug": "108-inicializacion-glorot-he",
    "partSlug": "parte-2-deep-learning",
    "title": "Inicialización (Glorot, He)",
    "description": "Saber inicializar los pesos de cada capa para que la varianza de las activaciones y de los gradientes se mantenga estable a lo largo del forward y backward pass.",
    "level": "Avanzado",
    "duration": "55 min",
    "theory": "Saber inicializar los pesos de cada capa para que la varianza de las activaciones y de los gradientes se mantenga estable a lo largo del forward y backward pass. Diferenciar Glorot (Xavier) —para sigmoid/tanh— de He (Kaiming) —para ReLU y variantes—. Saber cuál usa Keras por default y cuándo cambiarlo.",
    "outcomes": [
      "Explicar la idea: Var(W) ≈ 1 / fan_in (o promedio fan_in/fan_out) para preservar varianza.",
      "Aplicar kernel_initializer='glorot_uniform' (default Keras), 'he_normal', 'he_uniform'.",
      "Calcular a mano los límites de la distribución para Glorot uniform: ±√(6/(fan_in+fan_out)).",
      "Reconocer que la combinación correcta es He init + ReLU, Glorot + tanh/sigmoid.",
      "Inspeccionar el efecto visualmente: histogramas de activaciones por capa."
    ],
    "topics": [
      "¿Por qué importa la varianza? Productos de N capas amplifican o atenúan exponencialmente.",
      "Glorot (2010): Var(W) = 2/(fan_in + fan_out). Asume activación lineal/simétrica.",
      "He (2015): Var(W) = 2/fan_in. Compensa que ReLU \"mata\" la mitad de las salidas.",
      "Distribuciones: uniform o normal. Equivalentes prácticamente.",
      "LeCun init: Var(W) = 1/fan_in. Para SELU."
    ],
    "materials": [
      "Fashion-MNIST.",
      "Librerías: tensorflow, keras, matplotlib."
    ],
    "exercises": [
      "Inspección de defaults: para Dense(128, input_shape=(784,)), imprimir model.layers[0].kernel.numpy(). Calcular la varianza empírica y compararla con la teórica de Glorot.",
      "Comparación: entrenar MLP [512, 256, 128, 64, 10] con ReLU. Probar 3 inits: Glorot, He, RandomNormal(stddev=0.01). Graficar val_loss en las 3.",
      "Histogramas de activaciones: para cada capa del modelo bien inicializado, plot del histograma de salidas para un batch. Verificar que la varianza se mantiene similar entre capas.",
      "He init + Tanh: probar la combinación incorrecta (He con tanh). Comparar contra Glorot + tanh. Verificar que importa.",
      "Reset y reproducibilidad: con tf.random.set_seed(42) + np.random.seed(42), entrenar 2 veces y verificar que da idéntico. Sin seed, varía."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/108-inicializacion-glorot-he/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/109-activaciones-relu-elu-gelu-swish-mish",
    "number": 109,
    "slug": "109-activaciones-relu-elu-gelu-swish-mish",
    "partSlug": "parte-2-deep-learning",
    "title": "Activaciones: ReLU, ELU, GELU, Swish, Mish",
    "description": "Conocer la familia de activaciones modernas — desde ReLU (Krizhevsky et al.",
    "level": "Avanzado",
    "duration": "60 min",
    "theory": "Conocer la familia de activaciones modernas — desde ReLU (Krizhevsky et al. 2012) hasta GELU (BERT, GPT) y Swish/SiLU (EfficientNet) — entendiendo qué problema resuelve cada una y por qué los Transformers modernos usan GELU y no ReLU. Saber elegir según arquitectura.",
    "outcomes": [
      "Definir matemáticamente las 5 activaciones: ReLU, Leaky ReLU, ELU, GELU, Swish (SiLU), Mish.",
      "Identificar dying ReLU y aplicar Leaky ReLU / ELU como mitigación.",
      "Reconocer que GELU es la activación default en Transformers (BERT, GPT, ViT) y Swish/SiLU en EfficientNet, modelos modernos de visión.",
      "Aplicar cada activación en Keras: Dense(64, activation='relu' | 'gelu' | 'swish' | 'elu' | LeakyReLU()).",
      "Saber que el costo computacional de GELU/Swish es mayor (sigmoid/erf internos) pero el beneficio supera en arquitecturas profundas."
    ],
    "topics": [
      "ReLU: max(0, x). Rápida, simple, default histórico. Dying ReLU.",
      "Leaky ReLU: max(αx, x) con α≈0.01. Sin dying.",
      "ELU (Clevert et al. 2015): x si x>0, α(eˣ-1) si x<0. Suave, sin dying, pero más cara.",
      "GELU (Hendrycks & Gimpel 2016): x · Φ(x) (Φ = CDF gaussiana). Suave, no monótona. Default en Transformers.",
      "Swish / SiLU (Ramachandran et al. 2017): x · sigmoid(x). Encontrada por NAS. Casi idéntica a GELU.",
      "Mish (Misra 2019): x · tanh(softplus(x)). Marginalmente mejor en algunos benchmarks."
    ],
    "materials": [
      "Fashion-MNIST.",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "Plot de funciones: graficar las 6 activaciones en x ∈ [-3, 3].",
      "Comparación empírica: entrenar MLP [256, 128, 64] con cada activación, mismo init He, mismo LR. Comparar val_accuracy tras 15 épocas.",
      "Dying ReLU: con LR alto (0.1), entrenar con ReLU. Contar cuántas neuronas tienen mean(activation) = 0 al final.",
      "Leaky ReLU al rescate: repetir con Leaky. Verificar que el % de neuronas muertas baja.",
      "GELU vs ReLU en profundidad: armar un MLP de 12 capas. Comparar GELU vs ReLU. GELU suele ganar."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/109-activaciones-relu-elu-gelu-swish-mish/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/110-batch-normalization-layer-normalization",
    "number": 110,
    "slug": "110-batch-normalization-layer-normalization",
    "partSlug": "parte-2-deep-learning",
    "title": "Batch Normalization, Layer Normalization",
    "description": "Entender BatchNorm (Ioffe & Szegedy 2015) — la técnica que destrabó el entrenamiento de redes muy profundas estandarizando las activaciones en cada capa — y su variante LayerNorm (Ba, Kiros & Hinton 2016) — usada en Tra…",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Entender BatchNorm (Ioffe & Szegedy 2015) — la técnica que destrabó el entrenamiento de redes muy profundas estandarizando las activaciones en cada capa — y su variante LayerNorm (Ba, Kiros & Hinton 2016) — usada en Transformers y RNN porque no depende del batch. Saber dónde poner BN en la arquitectura, qué problemas tiene (batch chico, distribución entre train/inference) y cuándo preferir LN.",
    "outcomes": [
      "Aplicar BatchNormalization() antes o después de la activación (debate clásico — moderno: antes suele ser mejor para ReLU, después para GELU).",
      "Explicar qué hace BN en train (normaliza con stats del batch) vs inference (usa moving averages acumulados).",
      "Aplicar LayerNormalization() en RNN y Transformers; saber por qué allí BN falla.",
      "Reconocer las 3 variantes: BN, LN, GroupNorm (Wu & He 2018, para batch chico en visión).",
      "Diagnosticar el problema de \"train-test mismatch\" cuando el batch en inference es muy distinto al de train."
    ],
    "topics": [
      "BN: y = γ · (x - μ_batch)/σ_batch + β. γ, β trainables.",
      "Beneficios: convergencia más rápida, regularización mild, permite LR más altos.",
      "BN en train vs inference: moving avg de μ, σ acumulados.",
      "LN: normaliza sobre los features de una sola muestra (no sobre el batch).",
      "GroupNorm: agrupa canales, normaliza dentro de cada grupo. Para batch chico (segmentación, detección).",
      "¿Antes o después de la activación? Géron y la práctica moderna: antes funciona mejor con ReLU, después con GELU/Swish."
    ],
    "materials": [
      "Fashion-MNIST + un modelo profundo ([512, 256, 128, 64, 10]).",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "BN vs sin BN: entrenar el mismo MLP con y sin BN. Comparar curvas de val_loss y tiempo hasta llegar a accuracy 0.85.",
      "¿Antes o después de la activación?: probar las dos variantes (Dense → BN → ReLU vs Dense → ReLU → BN). Comparar.",
      "Inference mode: entrenar con BN, cambiar a training=False, predecir un batch y comparar con training=True. Las predicciones cambian (correcto).",
      "Batch chico: forzar batch_size=4 y entrenar con BN. Observar inestabilidad. Cambiar a LayerNormalization y verificar que se estabiliza.",
      "LayerNorm en RNN: aplicar keras.layers.LSTM con recurrent_activation y un LayerNormalization previo. Útil como anticipo de Transformers."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/110-batch-normalization-layer-normalization/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/111-gradient-clipping",
    "number": 111,
    "slug": "111-gradient-clipping",
    "partSlug": "parte-2-deep-learning",
    "title": "Gradient clipping",
    "description": "Aplicar gradient clipping —limitar la norma o el valor de los gradientes antes de actualizar pesos— como protección contra exploding gradients, especialmente crítico en RNN/LSTM (clase 120) y en entrenamiento de LLMs.",
    "level": "Avanzado",
    "duration": "45 min",
    "theory": "Aplicar gradient clipping —limitar la norma o el valor de los gradientes antes de actualizar pesos— como protección contra exploding gradients, especialmente crítico en RNN/LSTM (clase 120) y en entrenamiento de LLMs. Diferenciar clipnorm (preserva dirección) de clipvalue (clipea por elemento).",
    "outcomes": [
      "Configurar clipping en cualquier optimizer Keras: Adam(clipnorm=1.0) o Adam(clipvalue=0.5).",
      "Saber cuándo clipnorm es preferible (default moderno): preserva dirección del gradiente.",
      "Implementar clipping manual en custom training loop con tf.clip_by_global_norm.",
      "Detectar exploding monitoreando la norma del gradiente.",
      "Reconocer que en Transformers de LLM, clipnorm=1.0 es estándar."
    ],
    "topics": [
      "Exploding revisitado: ¿qué pasa cuando ||grad|| crece exponencialmente?",
      "clipnorm: si ||g|| > c, escalar g ← g · c/||g||. Preserva dirección.",
      "clipvalue: g_i ← clip(g_i, -c, +c) por elemento. Cambia dirección.",
      "Global norm vs per-variable: clip_by_global_norm mira el norm del tensor concatenado de todos los pesos."
    ],
    "materials": [
      "Fashion-MNIST + un MLP propenso a exploding (LR alto + sin BN).",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "Forzar exploding: entrenar MLP con Adam(lr=10.0) sobre Fashion-MNIST. loss = nan rápido.",
      "Clipping al rescate: repetir con Adam(lr=10.0, clipnorm=1.0). Verificar que no explota (aunque sigue malo el LR — clipping no es solución a LR mal calibrado, solo a explosión).",
      "clipnorm vs clipvalue: comparar las dos con LR razonable. Para problemas estables son ~equivalentes; diferencias aparecen en patrones específicos.",
      "Custom loop: implementar el paso con gradients = tape.gradient(loss, model.trainable_variables); gradients, _ = tf.clip_by_global_norm(gradients, 1.0); optimizer.apply_gradients(...).",
      "Monitoreo: graficar ||grad|| por step. Verificar que no excede el clipnorm configurado."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/111-gradient-clipping/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/112-transfer-learning-unsupervised-pretraining",
    "number": 112,
    "slug": "112-transfer-learning-unsupervised-pretraining",
    "partSlug": "parte-2-deep-learning",
    "title": "Transfer learning, unsupervised pretraining",
    "description": "Aplicar transfer learning — el patrón dominante en producción cuando hay pocos datos: tomar un modelo preentrenado (ImageNet para visión, BERT/GPT para texto), reemplazar la cabeza, congelar las capas base, fine-tunear…",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Aplicar transfer learning — el patrón dominante en producción cuando hay pocos datos: tomar un modelo preentrenado (ImageNet para visión, BERT/GPT para texto), reemplazar la cabeza, congelar las capas base, fine-tunear la cabeza, y opcionalmente descongelar gradualmente para una segunda fase con LR muy bajo. Conocer unsupervised pretraining como hermano histórico (autoencoders, contrastive learning).",
    "outcomes": [
      "Cargar un modelo preentrenado: keras.applications.MobileNetV3Small(weights='imagenet', include_top=False).",
      "Congelar capas: base.trainable = False.",
      "Construir un modelo nuevo con la base + un head custom (GlobalAveragePooling2D + Dense).",
      "Fine-tunear en dos etapas: (a) solo head con LR normal, (b) toda la red con LR 10× más bajo.",
      "Reconocer cuándo NO usar transfer (dataset muy distinto al de origen)."
    ],
    "topics": [
      "Por qué funciona: las capas tempranas aprenden features generales (bordes, texturas); las tardías son task-specific.",
      "Pipeline estándar: load → freeze → new head → fit → unfreeze → fit con LR bajo.",
      "LR diferencial: capas tempranas más bajo (1e-5), capas tardías más alto (1e-3).",
      "Unsupervised pretraining: autoencoders (clase 130), contrastive (SimCLR, MoCo, CLIP).",
      "Self-supervised: cómo BERT/GPT se pre-entrenan sin labels (masked LM / autoregressive)."
    ],
    "materials": [
      "Visión: dataset chico de 2-5 clases (perros/gatos, flores). tf.keras.utils.image_dataset_from_directory.",
      "Modelo base: MobileNetV3Small o EfficientNetB0 (más liviano que ResNet50).",
      "Librerías: tensorflow, keras, keras.applications."
    ],
    "exercises": [
      "Carga: base = MobileNetV3Small(weights='imagenet', include_top=False, input_shape=(224,224,3)); base.trainable = False.",
      "Modelo completo: model = Sequential([base, GlobalAveragePooling2D(), Dropout(0.2), Dense(num_classes, activation='softmax')]).",
      "Etapa 1: compilar con Adam(1e-3) y entrenar 10 épocas. Reportar accuracy.",
      "Etapa 2: base.trainable = True y recompilar con Adam(1e-5). Entrenar 10 épocas más. Verificar mejora.",
      "Sin transfer: entrenar la misma arquitectura desde cero (weights=None). Comparar cuántas épocas necesita para igualar accuracy de transfer (típicamente: nunca lo iguala con dataset chico)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/112-transfer-learning-unsupervised-pretraining/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/113-optimizadores-momentum-nesterov-adagrad-rmsprop-adam-adamw",
    "number": 113,
    "slug": "113-optimizadores-momentum-nesterov-adagrad-rmsprop-adam-adamw",
    "partSlug": "parte-2-deep-learning",
    "title": "Optimizadores: Momentum, Nesterov, AdaGrad, RMSProp, Adam, AdamW (+ Lion, Sophia)",
    "description": "Conocer la evolución de los optimizadores —SGD → Momentum → Nesterov → AdaGrad → RMSProp → Adam → AdamW— entendiendo qué problema resuelve cada uno.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Conocer la evolución de los optimizadores —SGD → Momentum → Nesterov → AdaGrad → RMSProp → Adam → AdamW— entendiendo qué problema resuelve cada uno. Aplicar los optimizadores 2023+ (Lion, Sophia) que están reemplazando a Adam en LLMs grandes por mejor performance y memoria. Saber elegir según contexto (Adam para casi todo, SGD+momentum para visión clásica, Lion para LLMs).",
    "outcomes": [
      "Explicar la fórmula de cada uno: SGD (w ← w - η·g), Momentum (acumulación), Nesterov (lookahead), Adam (mom 1er + 2do orden).",
      "Diferenciar Adam vs AdamW — la corrección de weight decay que Loshchilov & Hutter (2019) demostraron esencial.",
      "Usar Lion (tf.keras.optimizers.Lion en Keras 3+) con LR 3-10× más bajo que Adam.",
      "Reconocer cuándo SGD+Momentum supera a Adam: visión clásica con datasets grandes (ImageNet), donde el modelo final generaliza mejor.",
      "Inspeccionar y entender los hiperparámetros beta_1, beta_2, epsilon, weight_decay."
    ],
    "topics": [
      "SGD vanilla y por qué es lento en cañones (zigzaguea).",
      "Momentum (Polyak 1964): acelera en direcciones consistentes.",
      "Nesterov (1983): \"miro hacia adelante\" antes de calcular gradiente.",
      "AdaGrad: tasa adaptativa por parámetro; bueno para sparse data, malo para LR que decae a 0.",
      "RMSProp (Hinton, sin publicar): suaviza AdaGrad con EMA.",
      "Adam (Kingma & Ba 2014): Momentum + RMSProp = caballito industrial.",
      "AdamW (Loshchilov & Hutter 2019): weight decay separado del gradiente.",
      "Complemento moderno: Lion (Chen et al. 2023, signo en lugar de gradient adaptive), Sophia (Liu et al. 2023, Hessian aproximada)."
    ],
    "materials": [
      "Fashion-MNIST + un modelo razonable.",
      "Librerías: tensorflow, keras (Lion incluido en Keras 3+)."
    ],
    "exercises": [
      "Comparar 5 optimizadores: SGD(0.01), SGD+Momentum(0.9), Adam(1e-3), AdamW(1e-3, wd=1e-2), Lion(1e-4, wd=0.1). Mismo modelo, mismo dataset, 20 épocas. Graficar val_loss.",
      "Tuning del LR: para Adam y Lion, hacer un sweep de LR ∈ [1e-5, 1e-2] log. Encontrar el LR óptimo de cada uno. Verificar que el de Lion es ~5× más chico.",
      "AdamW vs Adam con L2: comparar Adam + keras.regularizers.L2(1e-2) en cada capa vs AdamW con weight_decay=1e-2. AdamW gana en val_loss.",
      "Inspección de buffer: imprimir optimizer.variables. Adam tiene m y v por parámetro; Lion solo m. Verificar memoria total.",
      "LR alto + Momentum: SGD con LR=0.1 explota; SGD+Momentum(0.9) con LR=0.1 puede funcionar. Probar."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/113-optimizadores-momentum-nesterov-adagrad-rmsprop-adam-adamw/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/114-optimizadores-modernos-lion-sophia",
    "number": 114,
    "slug": "114-optimizadores-modernos-lion-sophia",
    "partSlug": "parte-2-deep-learning",
    "title": "Optimizadores modernos: Lion, Sophia, Schedule-Free",
    "description": "Conocer la nueva generación de optimizadores 2023-2024 que está reemplazando a AdamW en LLM training a escala: Lion (Google, signo del gradiente), Sophia (Stanford, segundo orden aproximado), Schedule-Free (Meta, sin LR…",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Conocer la nueva generación de optimizadores 2023-2024 que está reemplazando a AdamW en LLM training a escala: Lion (Google, signo del gradiente), Sophia (Stanford, segundo orden aproximado), Schedule-Free (Meta, sin LR scheduling). Saber cuándo justifican el cambio.",
    "outcomes": [
      "Aplicar Lion con LR 3-10× más chico que AdamW y weight_decay 3-10× más grande.",
      "Aplicar Sophia con estimación diagonal del Hessiano (Hutchinson sampling).",
      "Aplicar Schedule-Free (schedulefree.AdamWScheduleFree) sin warmup/cosine.",
      "Comparar memoria, velocidad y calidad final.",
      "Reconocer cuándo Lion supera AdamW (modelos grandes, ViT, CLIP) y cuándo no."
    ],
    "topics": [
      "Lion: update = sign(β·m + (1-β)·g). 1 buffer en lugar de 2.",
      "Sophia: pre-condicionador diagonal del Hessiano vía Hutchinson.",
      "Schedule-Free: aprende sin schedule explícito, sin warmup.",
      "Memory: Lion ahorra 50 % vs AdamW.",
      "Trade-off: Lion + LR alto explota fácilmente."
    ],
    "materials": [
      "Fashion-MNIST o CIFAR-10 + ViT-Tiny.",
      "Librerías: torch, torch.optim, schedulefree (pip), implementaciones Lion/Sophia community."
    ],
    "exercises": [
      "AdamW baseline: ViT-Tiny en CIFAR-10. LR=1e-3, wd=0.05.",
      "Lion: misma red, LR=1e-4, wd=0.5. Comparar accuracy y memoria.",
      "Sophia: con Hutchinson cada 10 steps. Comparar convergencia.",
      "Schedule-Free: AdamWScheduleFree(lr=1e-3, warmup_steps=500). Sin cosine.",
      "Memory: para modelo grande, medir VRAM con cada uno."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/114-optimizadores-modernos-lion-sophia/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/115-learning-rate-scheduling",
    "number": 115,
    "slug": "115-learning-rate-scheduling",
    "partSlug": "parte-2-deep-learning",
    "title": "Learning rate scheduling",
    "description": "Saber variar el LR durante el entrenamiento —no dejarlo fijo— porque ningún LR es óptimo en todas las fases.",
    "level": "Avanzado",
    "duration": "60 min",
    "theory": "Saber variar el LR durante el entrenamiento —no dejarlo fijo— porque ningún LR es óptimo en todas las fases. Aplicar las 4 estrategias estándar: step decay, exponential decay, cosine annealing (default moderno), y warmup + decay (estándar en Transformers).",
    "outcomes": [
      "Configurar keras.optimizers.schedules.CosineDecay y pasarlo como learning_rate= al optimizer.",
      "Diferenciar ExponentialDecay, PiecewiseConstantDecay y CosineDecayRestarts.",
      "Implementar warmup lineal + cosine — receta default en BERT/GPT.",
      "Usar ReduceLROnPlateau (reactivo) vs schedule (proactivo).",
      "Graficar la curva de LR a lo largo del entrenamiento para verificar."
    ],
    "topics": [
      "LR fijo: arrancás bien, terminás demasiado alto para refinar.",
      "Step decay: cortar LR cada N épocas. Simple, anticuado.",
      "Exponential decay: lr = lr_0 · γ^t.",
      "Cosine annealing (Loshchilov & Hutter 2017): lr = 0.5·lr_0·(1 + cos(πt/T)).",
      "Warmup: empezar bajo y subir linealmente las primeras X steps. Esencial en Transformers.",
      "One-cycle policy (Smith 2018): warmup + cosine descent + tail decay."
    ],
    "materials": [
      "Fashion-MNIST con un MLP medio.",
      "Librerías: tensorflow, keras, matplotlib."
    ],
    "exercises": [
      "Schedule básica: lr = CosineDecay(initial_learning_rate=1e-3, decay_steps=10_000); Adam(learning_rate=lr). Entrenar y graficar val_loss.",
      "Visualizar el LR: para una schedule, evaluarla en steps 0, 100, 1000, 5000, 10000 y graficar.",
      "Warmup + Cosine: implementar custom callback (o usar CosineDecay(warmup_steps=...) en Keras 3) y entrenar un Transformer chico (anticipo). Comparar contra sin warmup.",
      "ReduceLROnPlateau: alternativa reactiva — ReduceLROnPlateau(factor=0.5, patience=3). Comparar con cosine.",
      "One-cycle: implementar con LearningRateScheduler callback. Probar y comparar."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/115-learning-rate-scheduling/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/116-regularizacion-l1-l2-dropout-max-norm-mc-dropout",
    "number": 116,
    "slug": "116-regularizacion-l1-l2-dropout-max-norm-mc-dropout",
    "partSlug": "parte-2-deep-learning",
    "title": "Regularización: L1/L2, dropout, max-norm, MC dropout (+ Stochastic Depth, DropPath)",
    "description": "Conocer las técnicas de regularización en DL —L1/L2, dropout (Srivastava et al.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Conocer las técnicas de regularización en DL —L1/L2, dropout (Srivastava et al. 2014), max-norm, MC dropout para incertidumbre— y las técnicas modernas que se usan en arquitecturas profundas (ResNets, ViT, Transformers): Stochastic Depth, DropPath y LayerDrop.",
    "outcomes": [
      "Aplicar keras.regularizers.l1(...), l2(...), l1_l2(...) en una capa.",
      "Aplicar Dropout(rate=0.5) y entender qué hace en train vs en inference (default desactivado).",
      "Implementar Monte Carlo dropout (Dropout(0.5) activo en inference → predicciones diferentes → incertidumbre).",
      "Aplicar Stochastic Depth en una ResNet: dropear bloques residuales completos al azar durante training.",
      "Aplicar DropPath (estándar en ViT, Swin Transformer, ConvNeXt)."
    ],
    "topics": [
      "L1/L2 como penalización en la loss. λ típicamente 1e-4 a 1e-2.",
      "Dropout: enmascarar fracción r de las activaciones por batch.",
      "Inverted dropout: en inference no se hace nada porque train ya escala por 1/(1-r).",
      "Max-norm constraint: ||w|| ≤ c por neurona después de cada update.",
      "MC Dropout (Gal & Ghahramani 2016): incertidumbre bayesiana aproximada.",
      "Complemento moderno: Stochastic Depth, DropPath (= Stochastic Depth aplicado a paths de attention/FFN), LayerDrop (Fan et al. 2020)."
    ],
    "materials": [
      "Fashion-MNIST + un MLP propenso a overfit.",
      "Librerías: tensorflow, keras, matplotlib."
    ],
    "exercises": [
      "Sin regularización: entrenar un MLP grande ([512, 256, 128]) en Fashion-MNIST y observar overfitting (gap train/val ≥ 5 pp).",
      "L2: agregar kernel_regularizer=keras.regularizers.l2(1e-3) a cada Dense. Comparar.",
      "Dropout: agregar Dropout(0.3) entre Dense layers. Comparar.",
      "MC Dropout: para 1 sample de test, hacer 100 predicciones con model(x, training=True). Calcular mean ± std de las probabilidades. Interpretar la incertidumbre.",
      "Stochastic Depth simulado: en un mini ResNet con 8 bloques, dropear cada bloque con prob 0.1 lineal. Comparar contra sin stochastic depth."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/116-regularizacion-l1-l2-dropout-max-norm-mc-dropout/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/117-stochastic-depth-droppath-layerdrop",
    "number": 117,
    "slug": "117-stochastic-depth-droppath-layerdrop",
    "partSlug": "parte-2-deep-learning",
    "title": "Regularización moderna: Stochastic Depth, DropPath, LayerDrop",
    "description": "Aplicar regularización por paths/bloques —más allá del dropout clásico— en arquitecturas profundas modernas (ResNet, ViT, ConvNeXt, Swin Transformer).",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Aplicar regularización por paths/bloques —más allá del dropout clásico— en arquitecturas profundas modernas (ResNet, ViT, ConvNeXt, Swin Transformer). Cubrir Stochastic Depth (drop bloque residual), DropPath (drop path en transformer), LayerDrop (drop layer completa). Beneficio doble: regularización + reducción de cómputo durante training.",
    "outcomes": [
      "Aplicar keras.layers.StochasticDepth(rate) o DropPath(rate) en bloques residuales.",
      "Diseñar rate lineal por profundidad: capa 0 → 0.0, capa N → 0.2.",
      "Aplicar LayerDrop durante pretraining para permitir inference con menos capas.",
      "Diferenciar Dropout (neurona) vs Stochastic Depth (bloque) vs LayerDrop (layer).",
      "Reconocer el speedup de training: 25 % más rápido en ResNet-110 (Huang 2016)."
    ],
    "topics": [
      "Dropout clásico vs Stochastic Depth.",
      "DropPath = Stochastic Depth para Transformers.",
      "Rate lineal: p_i = i/N · p_max.",
      "LayerDrop para compresión de Transformers.",
      "Combinaciones: Dropout + DropPath + Label Smoothing."
    ],
    "materials": [
      "CIFAR-10/100 con ResNet propia.",
      "ViT-Tiny preentrenado.",
      "Librerías: torch, timm (donde DropPath es default)."
    ],
    "exercises": [
      "ResNet con Stochastic Depth: implementar BasicBlock con StochasticDepth(p). Train CIFAR-10.",
      "Rate lineal: aplicar p_i = i/N · 0.2 en cada bloque. Comparar contra rate constante.",
      "ViT con DropPath: timm.create_model('vit_tiny_patch16_224', drop_path_rate=0.1). Comparar contra 0.0.",
      "LayerDrop: simular con 12-layer BERT mini — drop 50 % layers. Verificar accuracy aún razonable.",
      "Speed: medir wall-clock training con vs sin Stochastic Depth."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/117-stochastic-depth-droppath-layerdrop/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/118-tensorflow-tensores-variables-operaciones",
    "number": 118,
    "slug": "118-tensorflow-tensores-variables-operaciones",
    "partSlug": "parte-2-deep-learning",
    "title": "TensorFlow: tensores, variables, operaciones",
    "description": "Bajar un nivel por debajo de Keras: trabajar directamente con tensores (tf.Tensor) y variables (tf.Variable), entender la API NumPy-like de TF (tf.matmul, tf.reduce_*, tf.cast, tf.reshape), y diferenciar inmutable (Tens…",
    "level": "Avanzado",
    "duration": "60 min",
    "theory": "Bajar un nivel por debajo de Keras: trabajar directamente con tensores (tf.Tensor) y variables (tf.Variable), entender la API NumPy-like de TF (tf.matmul, tf.reduce_*, tf.cast, tf.reshape), y diferenciar inmutable (Tensor) de mutable (Variable, base de los pesos).",
    "outcomes": [
      "Crear tensores con tf.constant, tf.zeros, tf.ones, tf.random.normal.",
      "Aplicar operaciones: aritméticas, matmul, broadcasting, indexing/slicing, reduce_mean/sum/max.",
      "Convertir entre TF y NumPy (.numpy(), tf.convert_to_tensor).",
      "Crear y modificar tf.Variable con .assign, .assign_add.",
      "Reconocer dtypes (float32, float64, int32, bool) y forzar cast cuando hace falta."
    ],
    "topics": [
      "tf.Tensor: inmutable, similar a np.ndarray.",
      "tf.Variable: mutable, base de los pesos.",
      "Broadcasting (idéntico a NumPy).",
      "Operaciones reduce con axis=.",
      "tf.function (anticipo clase 107) — convierte una función Python en grafo.",
      "TF en GPU: ops sobre tensores van a GPU automáticamente si está disponible."
    ],
    "materials": [
      "Operaciones a mano (no requiere dataset).",
      "Librerías: tensorflow, numpy."
    ],
    "exercises": [
      "Tensores básicos: crear t = tf.constant([[1.0, 2.0], [3.0, 4.0]]). Imprimir shape, dtype, t.numpy().",
      "Operaciones: tf.matmul(t, t), tf.transpose(t), tf.reduce_sum(t, axis=0). Verificar shapes.",
      "Broadcasting: a = tf.constant([[1.], [2.], [3.]]) (shape 3,1), b = tf.constant([10., 20., 30.]) (3,). a + b → ¿qué shape?",
      "Variable y assign: v = tf.Variable([1., 2., 3.]); v.assign([4., 5., 6.]); v.assign_add([1., 1., 1.]). Verificar.",
      "dtype mismatch: tf.constant([1, 2, 3]) + tf.constant([1.0, 2.0, 3.0]) → error. Arreglar con tf.cast."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/118-tensorflow-tensores-variables-operaciones/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/119-losses-metricas-capas-modelos-custom",
    "number": 119,
    "slug": "119-losses-metricas-capas-modelos-custom",
    "partSlug": "parte-2-deep-learning",
    "title": "Losses, métricas, capas, modelos custom",
    "description": "Crear losses, métricas y capas custom cuando los builtins de Keras no alcanzan: focal loss, métrica F1 macro, una capa con normalización custom, modelo subclassed con train_step propio.",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Crear losses, métricas y capas custom cuando los builtins de Keras no alcanzan: focal loss, métrica F1 macro, una capa con normalización custom, modelo subclassed con train_step propio. Diferenciar stateless (función) de stateful (clase con estado acumulado por época).",
    "outcomes": [
      "Definir loss custom como función: def my_loss(y_true, y_pred): return ....",
      "Definir métrica stateful heredando keras.metrics.Metric con update_state, result, reset_state.",
      "Crear capa custom heredando keras.layers.Layer con build (declara pesos) y call (forward).",
      "Overridar train_step de un modelo subclassed (Model) para custom training logic.",
      "Saber cuándo usar custom vs cuándo los builtins de Keras alcanzan (casi siempre)."
    ],
    "topics": [
      "Loss como función simple: 2 args (y_true, y_pred), devuelve un tensor.",
      "Métrica stateless (función) vs stateful (Metric class).",
      "Capa custom: __init__ (config), build (pesos), call (forward).",
      "Model subclass con train_step(self, data) custom."
    ],
    "materials": [
      "Fashion-MNIST o cualquier dataset previo.",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "Loss custom: implementar Focal Loss FL(p_t) = -α(1-p_t)^γ log(p_t) (Lin et al. 2017, útil para imbalance). Aplicar a Fashion-MNIST y comparar contra cross-entropy.",
      "Métrica F1 macro: heredar keras.metrics.Metric, mantener confusion matrix acumulada por época, calcular F1 macro en result().",
      "Capa custom: class L2Normalize(Layer) que normaliza cada vector a norma 1. Probarla en un modelo.",
      "Modelo con train_step custom: subclass que en cada batch aplica gradient clipping manual + logging extra.",
      "get_config: agregar a una capa custom; verificar que model.save() y load_model(custom_objects=...) funciona."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/119-losses-metricas-capas-modelos-custom/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/120-funciones-y-grafos-autograph",
    "number": 120,
    "slug": "120-funciones-y-grafos-autograph",
    "partSlug": "parte-2-deep-learning",
    "title": "Funciones y grafos (autograph)",
    "description": "Entender qué hace @tf.function —compila una función Python a un grafo TF estático, acelerando 2-10× y permitiendo deploy en TF Serving / TFLite—.",
    "level": "Avanzado",
    "duration": "55 min",
    "theory": "Entender qué hace @tf.function —compila una función Python a un grafo TF estático, acelerando 2-10× y permitiendo deploy en TF Serving / TFLite—. Conocer AutoGraph (traduce automáticamente if/for/while Python a operaciones TF), saber los gotchas clásicos (efectos colaterales, prints, listas Python) y cuándo el decorator deteriora la experiencia de debugging.",
    "outcomes": [
      "Aplicar @tf.function a una función custom y verificar speedup.",
      "Identificar cuándo NO usarlo (debugging, lógica con efectos colaterales no determinísticos).",
      "Entender retracing: cada vez que cambias la shape o dtype del input, TF reconstruye el grafo.",
      "Usar tf.function(input_signature=...) para evitar retracing.",
      "Diferenciar eager mode (default, dinámico) de graph mode (compilado)."
    ],
    "topics": [
      "Eager vs graph execution.",
      "@tf.function y AutoGraph.",
      "Retracing: por qué pasar Python ints vs tensors causa retraces.",
      "Print en grafo: tf.print (corre en graph) vs print (solo en tracing).",
      "Cuándo @tf.function vale la pena (loops, training step) y cuándo no (one-shot, debugging)."
    ],
    "materials": [
      "Operaciones aisladas para medir velocidad.",
      "Librerías: tensorflow, time."
    ],
    "exercises": [
      "Speedup básico: definir def f(x): return tf.reduce_sum(x ** 2 + 3*x + 1). Medir tiempo eager vs @tf.function-wrapped en un loop de 10 000 iteraciones.",
      "Retracing: definir una función con @tf.function. Llamarla con tensores de shapes distintas; usar tf.config.experimental_run_functions_eagerly(True) y print para detectar retraces.",
      "AutoGraph: una función con un for Python y un if. Verificar que se convierte correctamente (tf.autograph.to_code(f)).",
      "tf.print vs print: dentro de @tf.function, demostrar que print solo se ejecuta en tracing (1ª llamada), tf.print siempre.",
      "input_signature: fijar input_signature para evitar retracing con shape (None, 784)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/120-funciones-y-grafos-autograph/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/121-custom-training-loops",
    "number": 121,
    "slug": "121-custom-training-loops",
    "partSlug": "parte-2-deep-learning",
    "title": "Custom training loops (+ PyTorch & PyTorch Lightning)",
    "description": "Escribir un training loop manual en TF con GradientTape — control absoluto sobre cada paso (útil para GANs, RL, multi-step optimizers, debugging).",
    "level": "Avanzado",
    "duration": "85 min",
    "theory": "Escribir un training loop manual en TF con GradientTape — control absoluto sobre cada paso (útil para GANs, RL, multi-step optimizers, debugging). Conocer el equivalente en PyTorch (el framework dominante de la industria en 2026) y cómo PyTorch Lightning abstrae los boilerplate del loop, devolviendo la productividad de Keras con la flexibilidad de PyTorch.",
    "outcomes": [
      "Escribir un training loop TF con for batch in dataset: with GradientTape() as tape: ...; grads = tape.gradient(loss, vars); optimizer.apply_gradients(...).",
      "Hacer el equivalente en PyTorch: optimizer.zero_grad(); loss.backward(); optimizer.step().",
      "Usar PyTorch Lightning para el mismo problema con boilerplate mínimo (LightningModule.training_step).",
      "Reconocer cuándo el loop manual es necesario (modelo con dos optimizadores, schedule custom step-wise, RL).",
      "Comparar productividad y flexibilidad de los 3 frameworks."
    ],
    "topics": [
      "Loop básico TF: epochs → batches → tape → grads → apply.",
      "tape.watch(...) para watch tensors que no son tf.Variable.",
      "Métricas y logging manual.",
      "Equivalente PyTorch.",
      "Lightning como capa de abstracción.",
      "Complemento moderno: PyTorch + Lightning en paralelo a TF/Keras."
    ],
    "materials": [
      "Fashion-MNIST o MNIST.",
      "Librerías: tensorflow, torch, lightning (pip install lightning)."
    ],
    "exercises": [
      "TF loop manual: entrenar un MLP en Fashion-MNIST con GradientTape. Implementar logging de loss y métrica manual.",
      "PyTorch equivalente: reimplementar el mismo loop en PyTorch.",
      "Lightning: mismo problema con LightningModule.",
      "Speedup con jit: tf.function en TF; torch.compile en PyTorch. Medir.",
      "Multi-optimizer: con TF, escribir un loop que aplica un optimizer para las capas frozen-ish (LR bajo) y otro para las nuevas (LR alto). Esto en model.fit requiere mucho boilerplate."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/121-custom-training-loops/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/122-pytorch-fundamentos-tensores-autograd",
    "number": 122,
    "slug": "122-pytorch-fundamentos-tensores-autograd",
    "partSlug": "parte-2-deep-learning",
    "title": "PyTorch fundamentos: tensores, autograd, nn.Module",
    "description": "Aprender PyTorch —el framework dominante en research y en LLMs/multimodal 2026—.",
    "level": "Avanzado",
    "duration": "90 min",
    "theory": "Aprender PyTorch —el framework dominante en research y en LLMs/multimodal 2026—. Cubrir: tensores (similar a NumPy, en GPU), autograd (requires_grad, .backward()), nn.Module (forma de definir modelos), Dataset/DataLoader para data pipelines. Equivalencias 1:1 con Keras/TF de las clases anteriores.",
    "outcomes": [
      "Crear tensores: torch.tensor, torch.zeros, torch.randn, device='cuda'.",
      "Aplicar autograd: x.requires_grad_(True); y = f(x); y.backward(); x.grad.",
      "Definir un MLP custom: class Net(nn.Module): def __init__(self): ...; def forward(self, x): ....",
      "Escribir el loop manual: optimizer.zero_grad(); loss.backward(); optimizer.step().",
      "Usar Dataset y DataLoader para pipelines de datos."
    ],
    "topics": [
      "Tensors vs ndarray, .to(device).",
      "Computation graph dinámico (vs estático TF1) — define-by-run.",
      "requires_grad y autograd.",
      "nn.Module, nn.Linear, nn.Sequential, nn.functional.",
      "Loss funcs: nn.CrossEntropyLoss, nn.MSELoss.",
      "Optim: torch.optim.Adam(model.parameters(), lr=...).",
      "Dataset + DataLoader(num_workers, pin_memory)."
    ],
    "materials": [
      "Fashion-MNIST vía torchvision.datasets.",
      "Librerías: torch, torchvision."
    ],
    "exercises": [
      "Tensores: crear, mover a GPU, operaciones básicas. Comparar con NumPy.",
      "Autograd: x = torch.tensor([2.0], requires_grad=True); y = x**3; y.backward(); print(x.grad) → debe ser 12.",
      "MLP custom: definir clase con 2 nn.Linear + ReLU. Verificar model.parameters().",
      "Training loop manual: Fashion-MNIST, 1 época, reportar loss.",
      "DataLoader: DataLoader(dataset, batch_size=32, shuffle=True, num_workers=2). Iterar."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/122-pytorch-fundamentos-tensores-autograd/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/123-pytorch-lightning-trainer-distribuido",
    "number": 123,
    "slug": "123-pytorch-lightning-trainer-distribuido",
    "partSlug": "parte-2-deep-learning",
    "title": "PyTorch Lightning: Trainer, callbacks, distributed",
    "description": "Aprender PyTorch Lightning — la capa de abstracción que convierte PyTorch puro (mucho boilerplate) en algo tan productivo como Keras pero conservando flexibilidad.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Aprender PyTorch Lightning — la capa de abstracción que convierte PyTorch puro (mucho boilerplate) en algo tan productivo como Keras pero conservando flexibilidad. Cubrir LightningModule, Trainer, callbacks, logging (W&B/TensorBoard), distributed training con un solo kwarg, mixed precision automática.",
    "outcomes": [
      "Subclassear LightningModule con training_step, validation_step, configure_optimizers.",
      "Usar Trainer(max_epochs, accelerator='auto', devices='auto', precision='bf16-mixed', logger=...).",
      "Aplicar callbacks: EarlyStopping, ModelCheckpoint, LearningRateMonitor.",
      "Activar distributed con strategy='ddp' o 'fsdp' para multi-GPU sin reescribir nada.",
      "Loggear a W&B / TensorBoard / MLflow vía 1 línea."
    ],
    "topics": [
      "LightningModule vs nn.Module puro.",
      "Trainer args: max_epochs, devices, precision, strategy, accumulate_grad_batches.",
      "Callbacks integrados.",
      "LightningDataModule para data pipelines.",
      "Distributed training: ddp, fsdp, deepspeed.",
      "Logging multi-backend."
    ],
    "materials": [
      "Fashion-MNIST o cualquier dataset previo.",
      "Librerías: lightning, torch, torchmetrics."
    ],
    "exercises": [
      "LightningModule básico: convertir el MLP de 108a a Lightning.",
      "Callbacks: agregar EarlyStopping(patience=5) + ModelCheckpoint(save_top_k=3).",
      "Mixed precision: Trainer(precision='bf16-mixed'). Comparar tiempo.",
      "W&B logging: Trainer(logger=WandbLogger(project='test')). Ver curvas online.",
      "DDP: si tenés 2+ GPUs, strategy='ddp', devices=2. Verificar speedup."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/123-pytorch-lightning-trainer-distribuido/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/124-tf-data-api",
    "number": 124,
    "slug": "124-tf-data-api",
    "partSlug": "parte-2-deep-learning",
    "title": "tf.data API",
    "description": "Construir pipelines de datos eficientes con tf.data.Dataset: leer desde memoria/archivos/CSV, transformar (map, filter), mezclar (shuffle), batchear (batch), prefetch (paraleliza CPU↔GPU).",
    "level": "Avanzado",
    "duration": "65 min",
    "theory": "Construir pipelines de datos eficientes con tf.data.Dataset: leer desde memoria/archivos/CSV, transformar (map, filter), mezclar (shuffle), batchear (batch), prefetch (paraleliza CPU↔GPU). Saber por qué un buen pipeline de datos es la diferencia entre \"GPU al 30 %\" y \"GPU al 95 %\".",
    "outcomes": [
      "Crear datasets desde varias fuentes: from_tensor_slices, list_files, TextLineDataset.",
      "Encadenar transformaciones: .map(fn, num_parallel_calls=tf.data.AUTOTUNE), .filter, .shuffle(buffer), .batch(N), .prefetch(tf.data.AUTOTUNE).",
      "Reconocer el orden correcto: cache → shuffle → batch → prefetch.",
      "Usar tf.data.AUTOTUNE y profilear con TensorBoard Profiler.",
      "Saber cuándo cache() vale la pena (datasets que caben en RAM)."
    ],
    "topics": [
      "Lazy evaluation: el dataset es un grafo, no datos cargados.",
      "shuffle(buffer_size): buffer chico → mal mezclado; buffer = dataset_size → perfecto pero RAM.",
      "batch(N) → cada elemento es ahora un mini-batch.",
      "prefetch: solapamiento CPU (loading) con GPU (training).",
      "interleave para leer múltiples archivos en paralelo.",
      "Métricas: tf.data.experimental.assert_cardinality."
    ],
    "materials": [
      "Fashion-MNIST cargado vía tf.data.",
      "CSV grande para testear pipelines a archivo (anticipa 110 TFRecord).",
      "Librerías: tensorflow."
    ],
    "exercises": [
      "Dataset desde NumPy: ds = tf.data.Dataset.from_tensor_slices((x_train, y_train)).shuffle(1024).batch(32).prefetch(tf.data.AUTOTUNE). Iterar y verificar shapes.",
      "Map con normalización: .map(lambda x, y: (tf.cast(x, tf.float32)/255., y), num_parallel_calls=tf.data.AUTOTUNE).",
      "Cache: comparar tiempo del 1er epoch vs 2do epoch con y sin .cache().",
      "Buffer chico: comparar shuffle con buffer_size=10 vs buffer_size=len(data). Inspeccionar el primer batch.",
      "Profilear: usar tf.profiler (vía TensorBoard) y verificar dónde está el bottleneck — data loading vs compute."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/124-tf-data-api/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/125-tfrecord",
    "number": 125,
    "slug": "125-tfrecord",
    "partSlug": "parte-2-deep-learning",
    "title": "TFRecord",
    "description": "Aprender el formato TFRecord — el formato binario nativo de TF, optimizado para datasets grandes (cientos de GB) que no caben en RAM.",
    "level": "Avanzado",
    "duration": "60 min",
    "theory": "Aprender el formato TFRecord — el formato binario nativo de TF, optimizado para datasets grandes (cientos de GB) que no caben en RAM. Saber escribirlo (tf.io.TFRecordWriter), parsearlo (tf.io.parse_single_example), y por qué es estándar en TPU/Vertex AI para training a escala.",
    "outcomes": [
      "Serializar un tf.train.Example con Features ↔ Feature (BytesList, Int64List, FloatList).",
      "Escribir TFRecord shards: with tf.io.TFRecordWriter('file.tfrecord') as w: w.write(serialized).",
      "Leer con tf.data.TFRecordDataset('file.tfrecord').map(parse_fn).",
      "Splitear datasets grandes en múltiples shards (*.tfrecord-00000-of-00010) para paralelizar reads.",
      "Reconocer cuándo TFRecord vale la pena vs alternativas modernas (Parquet, WebDataset)."
    ],
    "topics": [
      "tf.train.Example: estructura protobuf con Features (dict de strings a Feature).",
      "Feature types: BytesList, Int64List, FloatList.",
      "Serialize → escribir → leer → parse.",
      "Sharding: data.tfrecord-NNNNN-of-MMMMM.",
      "tf.data.experimental.bucket_by_sequence_length para batches eficientes por longitud (NLP)."
    ],
    "materials": [
      "Fashion-MNIST exportado a TFRecord.",
      "Librerías: tensorflow."
    ],
    "exercises": [
      "Escribir: convertir Fashion-MNIST (60 000 imágenes) a 10 shards TFRecord. Cada Example tiene image (bytes) y label (int).",
      "Leer y parsear: ds = tf.data.TFRecordDataset(glob.glob('shards/*.tfrecord')).map(parse_fn). Iterar y verificar shapes.",
      "Compresión: escribir con options=tf.io.TFRecordOptions(compression_type='GZIP'). Comparar tamaño.",
      "Reads paralelos: ds = ds.interleave(lambda f: tf.data.TFRecordDataset(f), num_parallel_calls=AUTOTUNE). Medir speedup vs lectura serial.",
      "Schema: usar tf.io.FixedLenFeature (tamaño fijo) vs VarLenFeature (variable, returns SparseTensor)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/125-tfrecord/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/126-keras-preprocessing-layers",
    "number": 126,
    "slug": "126-keras-preprocessing-layers",
    "partSlug": "parte-2-deep-learning",
    "title": "Keras preprocessing layers",
    "description": "Hacer preprocesamiento dentro del modelo con las preprocessing layers de Keras (Normalization, StringLookup, IntegerLookup, Discretization, CategoryEncoding, Hashing, TextVectorization).",
    "level": "Avanzado",
    "duration": "65 min",
    "theory": "Hacer preprocesamiento dentro del modelo con las preprocessing layers de Keras (Normalization, StringLookup, IntegerLookup, Discretization, CategoryEncoding, Hashing, TextVectorization). Beneficio: el preprocesamiento viaja con el modelo (.keras), no como código separado — elimina el clásico \"train-serve skew\" en producción.",
    "outcomes": [
      "Usar Normalization() con .adapt(data) para escalar features tabulares.",
      "Usar StringLookup para encoding de categóricas.",
      "Aplicar TextVectorization para tokenización + indexing.",
      "Construir un modelo \"todo en uno\": preprocesamiento + red en el mismo keras.Model.",
      "Reconocer la ventaja: model.predict(raw_data) funciona, sin necesidad de scaler separado."
    ],
    "topics": [
      "Normalization: substrae mean, divide por std. .adapt(data) aprende los stats.",
      "StringLookup / IntegerLookup: mapea categorías a índices enteros.",
      "CategoryEncoding: one-hot, multi-hot, count.",
      "Discretization: convierte continua en bucket (bin_boundaries=...).",
      "Hashing: mapea categorías a buckets via hash (sin necesidad de vocabulario).",
      "TextVectorization: tokeniza + lookup en una capa."
    ],
    "materials": [
      "California Housing (tabular).",
      "IMDB reviews (texto).",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "Normalization tabular: norm = Normalization(); norm.adapt(X_train); X_norm = norm(X_test). Verificar que mean ≈ 0, std ≈ 1.",
      "StringLookup: con un array de categorías, lookup = StringLookup(); lookup.adapt(categorias); lookup(['A', 'B', 'C']) → tensor de ints.",
      "Modelo end-to-end tabular: inputs = Input((n,)); x = Normalization()(inputs); x = Dense(64, ...)(x); .... Después .adapt(...) la capa norm con X_train.",
      "TextVectorization: sobre IMDB, tokenizar, entrenar un modelo de sentimiento.",
      "Hashing: con un dataset que tiene 100 000 categorías únicas, Hashing(1024) lo mapea a 1024 buckets. Comparar accuracy vs StringLookup con vocabulario truncado."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/126-keras-preprocessing-layers/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/127-tensorflow-datasets-tfds",
    "number": 127,
    "slug": "127-tensorflow-datasets-tfds",
    "partSlug": "parte-2-deep-learning",
    "title": "TensorFlow Datasets (TFDS)",
    "description": "Conocer TFDS —catálogo de datasets prearmados (CIFAR, ImageNet, IMDB, COCO, MNIST, GLUE, etc.)— y la alternativa moderna Hugging Face datasets (estándar en NLP/LLMs).",
    "level": "Avanzado",
    "duration": "40 min",
    "theory": "Conocer TFDS —catálogo de datasets prearmados (CIFAR, ImageNet, IMDB, COCO, MNIST, GLUE, etc.)— y la alternativa moderna Hugging Face datasets (estándar en NLP/LLMs). Cargar datasets de prueba, hacer splits, y entender por qué TFDS es práctico para benchmarks reproducibles.",
    "outcomes": [
      "Listar datasets disponibles con tfds.list_builders().",
      "Cargar con tfds.load('cifar10', split=['train', 'test'], as_supervised=True).",
      "Hacer splits custom con la slicing API: 'train[:80%]', 'train[80%:]'.",
      "Reconocer cuando usar tfds vs huggingface_hub.datasets."
    ],
    "topics": [
      "Catálogo TFDS: 200+ datasets, descarga automática + cache.",
      "as_supervised=True → tuplas (x, y).",
      "Splits: 'train[:80%]', 'train[-20%:]', 'all'.",
      "dataset.info con metadata (shape, num_classes, etc.).",
      "Hugging Face datasets: estándar moderno multi-framework."
    ],
    "materials": [
      "CIFAR-10 vía TFDS.",
      "IMDB vía HF datasets.",
      "Librerías: tensorflow-datasets (pip install tensorflow-datasets), opcional datasets (HF)."
    ],
    "exercises": [
      "Listar: tfds.list_builders() → primeros 20 datasets.",
      "CIFAR-10: (ds_train, ds_test), info = tfds.load('cifar10', split=['train', 'test'], as_supervised=True, with_info=True). Imprimir info.",
      "Slicing: cargar train[:90%] + train[90%:] como train/val split.",
      "Pipeline: ds_train.map(preprocess).cache().shuffle(1024).batch(32).prefetch(AUTOTUNE).",
      "HF datasets: from datasets import load_dataset; ds = load_dataset('imdb'). Inspeccionar; convertir a tf.data con ds.to_tf_dataset(...)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/127-tensorflow-datasets-tfds/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/128-capas-convolucionales-filtros-feature-maps",
    "number": 128,
    "slug": "128-capas-convolucionales-filtros-feature-maps",
    "partSlug": "parte-2-deep-learning",
    "title": "Capas convolucionales, filtros, feature maps",
    "description": "Entender la operación de convolución 2D — un filtro K×K se desliza sobre la imagen produciendo un feature map —, los hiperparámetros (filters, kernel_size, strides, padding), por qué las CNN son parameter-efficient vs M…",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Entender la operación de convolución 2D — un filtro K×K se desliza sobre la imagen produciendo un feature map —, los hiperparámetros (filters, kernel_size, strides, padding), por qué las CNN son parameter-efficient vs MLPs (sharing + locality + translation invariance) y cómo aprenden jerarquías visuales (bordes → texturas → partes → objetos).",
    "outcomes": [
      "Aplicar Conv2D(filters=32, kernel_size=3, strides=1, padding='same', activation='relu').",
      "Calcular el shape de la salida: H' = (H - K + 2P)/S + 1.",
      "Visualizar feature maps (activaciones intermedias) y filtros aprendidos.",
      "Diferenciar padding='same' (preserva tamaño) de 'valid' (reduce).",
      "Calcular el # de parámetros de una Conv2D: K K C_in * C_out + C_out (mucho menos que Dense equivalente)."
    ],
    "topics": [
      "Operación convolución 2D paso a paso.",
      "Filters / kernels como features detectables.",
      "Feature maps como representación espacial.",
      "Stride: paso del filtro.",
      "Padding: bordes; 'same' agrega zeros para preservar shape.",
      "Parameter sharing: el mismo filtro se aplica en toda la imagen."
    ],
    "materials": [
      "MNIST / Fashion-MNIST (1 canal) o CIFAR-10 (3 canales).",
      "Librerías: tensorflow, keras, matplotlib."
    ],
    "exercises": [
      "Conv básica: Conv2D(8, 3, padding='same', activation='relu')(input_28x28x1). Verificar shape de salida: (batch, 28, 28, 8).",
      "Conteo parámetros: para Conv2D(32, kernel_size=5) aplicado a entrada (28, 28, 1), calcular params (551*32 + 32 = 832).",
      "Stride 2: Conv2D(32, 3, strides=2, padding='same')(x). Shape de salida: (batch, H/2, W/2, 32).",
      "Visualizar feature maps: entrenar una mini-CNN en MNIST; tomar las activaciones intermedias para una imagen y visualizar.",
      "Filtros aprendidos: visualizar model.layers[0].kernel.numpy() para los primeros filtros. Para CIFAR, suelen verse bordes/colores básicos."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/128-capas-convolucionales-filtros-feature-maps/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/129-pooling",
    "number": 129,
    "slug": "129-pooling",
    "partSlug": "parte-2-deep-learning",
    "title": "Pooling",
    "description": "Conocer pooling — operación sin parámetros que reduce dimensiones espaciales: MaxPooling2D, AveragePooling2D, GlobalAveragePooling2D.",
    "level": "Avanzado",
    "duration": "45 min",
    "theory": "Conocer pooling — operación sin parámetros que reduce dimensiones espaciales: MaxPooling2D, AveragePooling2D, GlobalAveragePooling2D. Saber que max-pool agrega invariancia local a translación y reduce cómputo de capas posteriores. Comparar contra el approach moderno (stride > 1 en Conv).",
    "outcomes": [
      "Aplicar MaxPooling2D(2), AveragePooling2D(2), GlobalAveragePooling2D() y conocer sus shapes de salida.",
      "Diferenciar max-pool (preserva la característica más fuerte) de average-pool (promedio espacial).",
      "Aplicar GlobalAveragePooling2D antes de la cabeza Dense (estándar en CNN modernas — reemplaza Flatten).",
      "Reconocer que pooling no tiene parámetros entrenables (es solo una reducción).",
      "Saber que ResNet/ConvNeXt usan stride en lugar de pool intermedio."
    ],
    "topics": [
      "MaxPool: ventana k×k → toma el máximo. Default pool_size=2, strides=2 → halve H y W.",
      "AvgPool: promedio de la ventana. Suaviza.",
      "GlobalAvgPool: una sola activación por feature map → (batch, channels).",
      "Invariancia a translación local: si el feature se mueve 1 px, el max no cambia.",
      "Pool vs stride: equivalentes en muchos casos; tendencia moderna es eliminar pool intermedio."
    ],
    "materials": [
      "Fashion-MNIST o CIFAR-10.",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "MaxPool shape: aplicar MaxPool(2) a tensor (1, 28, 28, 32). Verificar salida (1, 14, 14, 32).",
      "MaxPool vs AvgPool: con la misma CNN, intercambiar y comparar accuracy en Fashion-MNIST. MaxPool suele ganar marginal.",
      "GlobalAvgPool reemplaza Flatten: arquitectura Conv → Conv → GlobalAvgPool → Dense(10) vs Conv → Conv → Flatten → Dense(128) → Dense(10). Comparar params y accuracy.",
      "Pool vs stride: comparar Conv(stride=1) → Pool(2) vs Conv(stride=2) (sin pool). En modelos chicos son prácticamente equivalentes.",
      "padding='same' en pool: comportamiento si H es impar. valid recorta, same agrega zeros."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/129-pooling/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/130-arquitecturas-cnn-lenet-alexnet-vgg-googlenet-resnet-xception-senet-ef",
    "number": 130,
    "slug": "130-arquitecturas-cnn-lenet-alexnet-vgg-googlenet-resnet-xception-senet-ef",
    "partSlug": "parte-2-deep-learning",
    "title": "Arquitecturas CNN: LeNet, AlexNet, VGG, GoogLeNet, ResNet, Xception, SENet, EfficientNet, ConvNeXt",
    "description": "Conocer la historia y evolución de las arquitecturas CNN desde LeNet-5 (1998) hasta ConvNeXt (2022) — qué innovación introdujo cada una, por qué importaba, y cuál usar hoy.",
    "level": "Avanzado",
    "duration": "95 min",
    "theory": "Conocer la historia y evolución de las arquitecturas CNN desde LeNet-5 (1998) hasta ConvNeXt (2022) — qué innovación introdujo cada una, por qué importaba, y cuál usar hoy. Identificar 3 patrones clave: profundidad creciente, módulos con paths múltiples, eficiencia paramétrica.",
    "outcomes": [
      "Trazar la línea temporal: LeNet → AlexNet → VGG → GoogLeNet (Inception) → ResNet → Xception → SENet → EfficientNet → ConvNeXt.",
      "Reconocer qué innovación trajo cada una: ReLU + dropout (AlexNet), kernels 3×3 (VGG), módulos Inception (GoogLeNet), skip connections (ResNet), depthwise-separable (Xception), squeeze-and-excite (SENet), compound scaling (EfficientNet), modernización con receta ConvNeXt.",
      "Implementar un mini-ResNet con Add() y skip connections.",
      "Cargar arquitecturas de keras.applications y leer sus tamaños (MobileNetV3, EfficientNetB0, ConvNeXtTiny).",
      "Elegir la arquitectura adecuada según constraint (latency, accuracy, memory)."
    ],
    "topics": [
      "LeNet-5 (1998): 7 capas, MNIST. La cuna.",
      "AlexNet (2012): GPU + ReLU + Dropout. Ganó ImageNet → revolución DL.",
      "VGG (2014): muy uniforme — solo conv 3×3 + maxpool. 138M parámetros.",
      "GoogLeNet / Inception (2014): módulos paralelos con kernels 1×1, 3×3, 5×5.",
      "ResNet (2015): skip connections → entrenamiento de redes de 152 capas posible. Cambió el juego.",
      "Xception (2017): depthwise-separable convolutions → eficiencia.",
      "SENet (2017): attention sobre canales (squeeze-and-excite).",
      "EfficientNet (2019): scaling balanceado de depth/width/resolution.",
      "ConvNeXt (2022): \"modernizar ResNet\" con trucos de ViT."
    ],
    "materials": [
      "ImageNet (vía transfer) o un dataset propio chico.",
      "Librerías: tensorflow, keras.applications."
    ],
    "exercises": [
      "Cargar varios modelos: keras.applications.{ResNet50, EfficientNetB0, ConvNeXtTiny}(weights='imagenet'). Comparar model.count_params() y model.summary().",
      "Mini-ResNet: implementar 4 bloques residuales: def res_block(x): return x + Conv(64,3,padding='same')(ReLU()(Conv(64,3,padding='same')(x))). Apilar y entrenar.",
      "Skip connection a mano: comparar entrenamiento de un \"ResNet\" sin skip vs con skip a 50 capas. Sin skip no entrena.",
      "Depthwise-separable: usar SeparableConv2D en lugar de Conv2D en el mismo modelo. Comparar params y accuracy.",
      "Squeeze-Excite: implementar un bloque SE manualmente: s = GlobalAvgPool(x); s = Dense(C//r)(s); s = Dense(C, sigmoid)(s); return x * Reshape((1,1,C))(s)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/130-arquitecturas-cnn-lenet-alexnet-vgg-googlenet-resnet-xception-senet-ef/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/131-transfer-learning-con-cnns-preentrenadas",
    "number": 131,
    "slug": "131-transfer-learning-con-cnns-preentrenadas",
    "partSlug": "parte-2-deep-learning",
    "title": "Transfer learning con CNNs preentrenadas",
    "description": "Aplicar transfer learning específicamente en visión — el caso de uso más común del campo.",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Aplicar transfer learning específicamente en visión — el caso de uso más común del campo. Profundizar la clase 101 con receta industrial: data augmentation, fine-tuning gradual, learning rate diferencial, y manejo de BatchNorm en fine-tuning (un gotcha clásico).",
    "outcomes": [
      "Construir pipeline con image_dataset_from_directory + augmentation (RandomFlip, RandomRotation, RandomZoom).",
      "Aplicar el preprocess_input específico del modelo base.",
      "Hacer fine-tuning en 2 fases con LR diferencial.",
      "Manejar correctamente BatchNorm en fine-tuning (mantenerlo en inference mode si descongelaste pocas capas).",
      "Comparar feature extraction (frozen base + nueva head) vs fine-tune (descongelar todo) según tamaño del dataset."
    ],
    "topics": [
      "Augmentation como capa: RandomFlip, RandomRotation, RandomZoom, RandomCrop, RandomContrast.",
      "preprocess_input por modelo (cada red espera su escalado).",
      "2-stage training: freeze + head warmup → unfreeze + LR bajo.",
      "BN gotcha: cuando descongelás, BN sigue actualizando moving averages → puede dañar pretraining.",
      "MixUp, CutMix, RandAugment como augmentations modernas (anticipo)."
    ],
    "materials": [
      "Dataset chico propio o tfds.load('cats_vs_dogs') o tfds.load('tf_flowers').",
      "Modelo base: EfficientNetB0 o MobileNetV3Small.",
      "Librerías: tensorflow, keras, keras.applications."
    ],
    "exercises": [
      "Pipeline con augmentation: RandomFlip + RandomRotation(0.1) + RandomZoom(0.1) como capas. Visualizar imágenes augmentadas.",
      "Modelo con base + head: base = EfficientNetB0(include_top=False, weights='imagenet'); base.trainable = False; model = Sequential([data_aug, preprocess_input, base, GlobalAvgPool, Dropout, Dense(num_classes)]).",
      "Etapa 1 (head warmup): Adam(1e-3), entrenar 5 épocas.",
      "Etapa 2 (fine-tune): base.trainable = True, recompilar con Adam(1e-5). Entrenar 10 épocas. Verificar mejora.",
      "BN gotcha: con base.trainable = True pero pasando training=False a la base durante fine-tuning → BN no se actualiza. Comparar."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/131-transfer-learning-con-cnns-preentrenadas/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/132-localizacion-deteccion-yolo-faster-r-cnn-segmentacion-semantica",
    "number": 132,
    "slug": "132-localizacion-deteccion-yolo-faster-r-cnn-segmentacion-semantica",
    "partSlug": "parte-2-deep-learning",
    "title": "Localización, detección, segmentación (+ DETR, Segment Anything, YOLOv11)",
    "description": "Saber detectar y segmentar objetos en imágenes — la tarea de visión más compleja y más comercial.",
    "level": "Avanzado",
    "duration": "90 min",
    "theory": "Saber detectar y segmentar objetos en imágenes — la tarea de visión más compleja y más comercial. Conocer la evolución: Faster R-CNN (two-stage, lento + preciso) → YOLO (one-stage, rápido) → DETR (Transformer, end-to-end) → YOLOv11 (estado del arte 2024) → Segment Anything (SAM/SAM 2) (foundation model para segmentación).",
    "outcomes": [
      "Distinguir las 4 tareas: clasificación, localización (1 objeto), detección (N objetos + cajas), segmentación (pixel-wise mask).",
      "Usar un modelo YOLOv11 preentrenado con ultralytics: model = YOLO('yolo11n.pt'); results = model('imagen.jpg').",
      "Aplicar Segment Anything (SAM 2) para segmentación promptable con puntos o cajas como input.",
      "Reconocer cuándo elegir DETR (mejor formal, lento) vs YOLO (rápido, default industrial) vs SAM (pre-entrenado universal).",
      "Métricas: IoU, mAP, COCO AP@[.5:.05:.95]."
    ],
    "topics": [
      "Localización vs detección vs instance segmentation vs semantic segmentation.",
      "IoU, mAP, COCO benchmark.",
      "Anchors vs anchor-free.",
      "One-stage (YOLO, SSD) vs two-stage (Faster R-CNN).",
      "Complemento moderno: DETR (Carion et al. 2020), SAM/SAM 2 (Meta 2023/2024), YOLOv11 (Ultralytics 2024).",
      "Pre-trained pipelines: ultralytics, transformers (DETR), segment_anything."
    ],
    "materials": [
      "COCO (detección/seg estándar): tfds.load('coco/2017').",
      "Pascal VOC: más chico, bueno para experimentos.",
      "Custom: anotaciones en YOLO format (txt por imagen) o COCO format (JSON).",
      "Librerías: ultralytics (pip install ultralytics), transformers, segment-anything."
    ],
    "exercises": [
      "YOLO inference: cargar yolo11n.pt y detectar sobre 3 imágenes propias. Visualizar boxes + labels.",
      "DETR inference: usar facebook/detr-resnet-50 desde HF. Comparar resultados con YOLO sobre las mismas imágenes.",
      "SAM segmentation: dar un punto sobre un objeto en una imagen, obtener máscara. Probar con cajas.",
      "mAP a mano: dado un set de predicciones y GT, implementar IoU y calcular AP@0.5 manualmente.",
      "YOLO fine-tune: dataset propio (≥ 100 imágenes anotadas), model.train(data='dataset.yaml', epochs=50). Reportar mAP."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/132-localizacion-deteccion-yolo-faster-r-cnn-segmentacion-semantica/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/133-segment-anything-sam-sam2",
    "number": 133,
    "slug": "133-segment-anything-sam-sam2",
    "partSlug": "parte-2-deep-learning",
    "title": "Segment Anything (SAM / SAM 2): foundation model para segmentación",
    "description": "Usar Segment Anything (Meta AI 2023) y SAM 2 (2024) — el foundation model para segmentación: entrenado en 11M imágenes + 1.1B máscaras (SAM 2 agrega video).",
    "level": "Avanzado",
    "duration": "85 min",
    "theory": "Usar Segment Anything (Meta AI 2023) y SAM 2 (2024) — el foundation model para segmentación: entrenado en 11M imágenes + 1.1B máscaras (SAM 2 agrega video). Segmenta cualquier objeto dado un prompt (punto, caja, máscara, \"todo\"). Zero-shot — no requiere training para empezar.",
    "outcomes": [
      "Instalar y cargar SAM/SAM 2 con pip install 'git+https://github.com/facebookresearch/segment-anything-2'.",
      "Aplicar prompts: punto, caja, multi-punto positivo/negativo.",
      "Generar máscaras en modo \"everything\" (segmenta cada objeto automáticamente).",
      "Tracking de máscaras en video con SAM 2 (memoria temporal).",
      "Combinar SAM con detector (YOLO) para pipeline detection → segmentation."
    ],
    "topics": [
      "Arquitectura SAM: ViT encoder + prompt encoder + mask decoder.",
      "Promptable: una sola red, múltiples interfaces.",
      "SAM 2: adds memory + tracking en video.",
      "Variants: vit_h (mejor calidad), vit_l, vit_b (más rápido).",
      "Pipeline detección + segmentación: YOLO/Grounding DINO → boxes → SAM → masks.",
      "Fine-tuning SAM (rara vez necesario, casos médicos / dominios muy específicos)."
    ],
    "materials": [
      "Imágenes propias o cualquier dataset visual.",
      "Modelos pretrained: <https://github.com/facebookresearch/segment-anything-2>.",
      "Librerías: segment-anything-2 (PyTorch)."
    ],
    "exercises": [
      "SAM setup: descargar checkpoint vit_h. Cargar con SamPredictor.",
      "Punto prompt: predictor.set_image(img); masks, scores, _ = predictor.predict(point_coords=[[x,y]], point_labels=[1]).",
      "Box prompt: pasar box=[x1,y1,x2,y2]; útil después de YOLO.",
      "Everything mode: SamAutomaticMaskGenerator(sam).generate(img) → lista de masks.",
      "SAM 2 video tracking: tomar un punto en frame 0, propagar a través del video."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/133-segment-anything-sam-sam2/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/134-yolov11-deteccion-segmentacion-practica",
    "number": 134,
    "slug": "134-yolov11-deteccion-segmentacion-practica",
    "partSlug": "parte-2-deep-learning",
    "title": "YOLOv11 práctico: detección, segmentación, pose, tracking",
    "description": "Dominar YOLOv11 (Ultralytics, 2024) — el detector default industrial 2026: inference real-time, fine-tuning sencillo, export a ONNX/TensorRT/CoreML/TFLite con un kwarg.",
    "level": "Avanzado",
    "duration": "85 min",
    "theory": "Dominar YOLOv11 (Ultralytics, 2024) — el detector default industrial 2026: inference real-time, fine-tuning sencillo, export a ONNX/TensorRT/CoreML/TFLite con un kwarg. Cubrir las 4 tareas: detection, segmentation, pose estimation, oriented bounding boxes (OBB).",
    "outcomes": [
      "Inferir con un modelo COCO-pretrained: YOLO('yolo11n.pt')(img).",
      "Fine-tunear con dataset propio en formato YOLO (txt por imagen).",
      "Aplicar las 4 tareas: detection (yolo11n.pt), segmentation (yolo11n-seg.pt), pose (yolo11n-pose.pt), OBB (yolo11n-obb.pt).",
      "Tracking de objetos en video con ByteTrack / BoT-SORT integrado.",
      "Exportar a ONNX/TensorRT para deploy."
    ],
    "topics": [
      "Modelos: n (nano), s, m, l, x. Trade-off speed vs accuracy.",
      "Formato YOLO de anotación: class cx cy w h (normalizado).",
      "dataset.yaml: paths + nombres de clases.",
      "Fine-tuning: model.train(data='dataset.yaml', epochs=100, imgsz=640).",
      "Modes: predict, val, train, export, benchmark.",
      "Tracking integrado."
    ],
    "materials": [
      "COCO pre-trained para inference.",
      "Roboflow Universe para dataset propio.",
      "Librerías: ultralytics (pip install ultralytics)."
    ],
    "exercises": [
      "Inference: model = YOLO('yolo11n.pt'); results = model('zidane.jpg'); results[0].show().",
      "Segmentation: YOLO('yolo11n-seg.pt'). Visualizar máscaras.",
      "Pose: YOLO('yolo11n-pose.pt'). Detectar keypoints en una foto.",
      "Fine-tune: dataset propio (50-100 imágenes anotadas). model.train(data='ds.yaml', epochs=50, imgsz=640).",
      "Tracking: model.track('video.mp4', tracker='botsort.yaml')."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/134-yolov11-deteccion-segmentacion-practica/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/135-rnns-neuronas-recurrentes-bptt",
    "number": 135,
    "slug": "135-rnns-neuronas-recurrentes-bptt",
    "partSlug": "parte-2-deep-learning",
    "title": "RNNs: neuronas recurrentes, BPTT",
    "description": "Entender las redes recurrentes (RNN) — la primera arquitectura para secuencias: misma celda aplicada en cada timestep, estado oculto h_t que acumula contexto, y BPTT (Backpropagation Through Time) que entrena estos mode…",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Entender las redes recurrentes (RNN) — la primera arquitectura para secuencias: misma celda aplicada en cada timestep, estado oculto h_t que acumula contexto, y BPTT (Backpropagation Through Time) que entrena estos modelos. Reconocer sus limitaciones (vanishing en secuencias largas) que motivaron LSTM (clase 120) y eventualmente Transformers.",
    "outcomes": [
      "Explicar la ecuación h_t = tanh(W_h · h_{t-1} + W_x · x_t + b).",
      "Usar keras.layers.SimpleRNN(units=N, return_sequences=False|True).",
      "Diferenciar return_sequences=False (un único output al final) vs True (output por timestep).",
      "Implementar BPTT truncado (longitud máxima de window).",
      "Reconocer cuándo una RNN simple es suficiente (secuencias cortas, < 20 pasos) y cuándo necesitás LSTM/Transformer."
    ],
    "topics": [
      "Estado oculto h_t como memoria.",
      "Unfolding: la RNN como red feedforward muy profunda en el tiempo.",
      "BPTT: gradientes a través de cada paso temporal.",
      "Vanishing/exploding en secuencias largas (compounding multiplicativo).",
      "BPTT truncado."
    ],
    "materials": [
      "Serie temporal sintética (sumas, sine).",
      "Librerías: tensorflow, keras, numpy, matplotlib."
    ],
    "exercises": [
      "SimpleRNN básico: predecir el siguiente valor de sin(t). Modelo: SimpleRNN(20) → Dense(1). Entrenar y graficar predicciones.",
      "return_sequences=True: apilar 2 RNN, primera con return_sequences=True, segunda sin. Verificar shapes.",
      "Predicción de N pasos adelante: iterar prediciendo, alimentando la predicción anterior como nuevo input.",
      "BPTT truncado: con secuencia de 200 pasos, comparar BPTT completo vs truncado a 20.",
      "Vanishing demo: usar SimpleRNN con secuencias de 100 pasos. Las primeras observaciones casi no influyen en la última predicción."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/135-rnns-neuronas-recurrentes-bptt/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/136-forecasting-de-series-con-rnn",
    "number": 136,
    "slug": "136-forecasting-de-series-con-rnn",
    "partSlug": "parte-2-deep-learning",
    "title": "Forecasting de series con RNN",
    "description": "Aplicar RNN/LSTM/GRU a un problema real de forecasting de series temporales.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Aplicar RNN/LSTM/GRU a un problema real de forecasting de series temporales. Hacer split temporal (NO aleatorio), preparar windows, comparar contra baselines (naive, MA, ARIMA), y reportar métricas estándar (MAE, MAPE, RMSE).",
    "outcomes": [
      "Hacer split temporal (train: período antiguo, val/test: período más reciente).",
      "Construir samples de longitud T con tf.keras.utils.timeseries_dataset_from_array.",
      "Comparar contra el baseline naïve (ŷ_t = y_{t-1}) y media móvil.",
      "Reportar MAE, MAPE, RMSE.",
      "Reconocer cuándo Deep Learning es mejor que ARIMA / Prophet / XGBoost para series."
    ],
    "topics": [
      "Split temporal estricto (no shuffle).",
      "Stationarity / diferenciación.",
      "Baseline naïve y por qué siempre comparar contra él.",
      "Windowing: cómo elegir tamaño de window (T) y horizonte.",
      "Forecasting multi-step: directo vs recursivo vs seq2seq."
    ],
    "materials": [
      "seaborn flights dataset o cualquier serie pública (e.g., consumo eléctrico).",
      "tfds.load('electricity_load_diagrams') o sintético.",
      "Librerías: tensorflow, keras, pandas, matplotlib."
    ],
    "exercises": [
      "Split temporal: separar primer 70 % train, 15 % val, último 15 % test. No mezclar.",
      "Baseline naïve: y_pred = y_test.shift(1). Reportar MAE.",
      "LSTM forecasting: Sequential([LSTM(32), Dense(1)]). Comparar contra naïve.",
      "GRU: igual con GRU. Comparar performance y velocidad.",
      "Multi-step: predecir 7 pasos directamente (Dense(7) al final). Comparar contra predicción recursiva."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/136-forecasting-de-series-con-rnn/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/137-lstm-gru",
    "number": 137,
    "slug": "137-lstm-gru",
    "partSlug": "parte-2-deep-learning",
    "title": "LSTM, GRU",
    "description": "Entender LSTM (Hochreiter & Schmidhuber 1997) y GRU (Cho et al.",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Entender LSTM (Hochreiter & Schmidhuber 1997) y GRU (Cho et al. 2014) — celdas recurrentes con gates que solucionan el vanishing gradient de SimpleRNN: la información puede fluir sin atenuación por la cell state, y los gates aprenden qué olvidar, recordar y emitir.",
    "outcomes": [
      "Explicar los 3 gates de LSTM: forget, input, output, y la cell state que viaja \"horizontal\".",
      "Diferenciar LSTM (3 gates + 2 estados) de GRU (2 gates + 1 estado, más simple, casi igual de bueno).",
      "Usar keras.layers.LSTM y keras.layers.GRU con return_sequences, return_state, recurrent_dropout.",
      "Aplicar Bidirectional cuando la tarea lo permite.",
      "Reconocer que con T > 100, incluso LSTM lucha — preferir Transformers."
    ],
    "topics": [
      "Cell state c_t (memoria larga) vs hidden state h_t (memoria corta).",
      "Forget gate: cuánto borrar de c_{t-1}.",
      "Input gate: cuánto agregar nuevo a c_t.",
      "Output gate: cuánto exponer en h_t.",
      "GRU: combina forget e input en una sola \"update gate\".",
      "Bidirectional + stacked LSTMs como receta clásica pre-Transformers."
    ],
    "materials": [
      "IMDB para sentimiento.",
      "Serie temporal del ejercicio anterior.",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "LSTM vs SimpleRNN: en una serie de 100 pasos con dependencia long-range, comparar accuracy.",
      "GRU vs LSTM: misma tarea, comparar. GRU ~ 25 % menos params; accuracy casi igual.",
      "Stacked: 2-3 capas LSTM apiladas con return_sequences=True en las primeras.",
      "Bidirectional: para sentimiento IMDB, comparar LSTM vs Bidirectional(LSTM).",
      "cuDNN check: medir velocidad LSTM vanilla vs con recurrent_dropout (desactiva cuDNN)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/137-lstm-gru/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/138-1d-cnns-y-wavenet",
    "number": 138,
    "slug": "138-1d-cnns-y-wavenet",
    "partSlug": "parte-2-deep-learning",
    "title": "1D CNNs y WaveNet",
    "description": "Conocer la alternativa a RNN para secuencias: Conv1D y WaveNet (dilated causal convolutions).",
    "level": "Avanzado",
    "duration": "60 min",
    "theory": "Conocer la alternativa a RNN para secuencias: Conv1D y WaveNet (dilated causal convolutions). Más rápido que LSTM (paralelizable), receptive field amplio con pocas capas (dilated convolutions). Útil para audio, series temporales y como capa de preprocesamiento.",
    "outcomes": [
      "Aplicar Conv1D(filters, kernel_size, padding='causal') sobre secuencias.",
      "Implementar dilated convolutions (kernel salta posiciones).",
      "Reconocer causal convolution: el output en t depende solo de inputs ≤ t.",
      "Construir un mini-WaveNet con dilation rates exponenciales (1, 2, 4, 8, ...).",
      "Comparar Conv1D vs LSTM en speed/accuracy."
    ],
    "topics": [
      "Conv1D fundamentos: stride, padding, dilation.",
      "Causal padding: para no ver el futuro.",
      "Dilated convolutions: receptive field grande sin más layers.",
      "WaveNet: stack de dilated causal convolutions (1, 2, 4, ..., 512).",
      "Conv1D vs LSTM: paralelización, receptive field, parameter count."
    ],
    "materials": [
      "Serie temporal del ejercicio 119.",
      "Audio simple (sintético: superposición de senos).",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "Conv1D vs LSTM: forecasting de serie. Conv1D(32, 5, padding='causal') → Conv1D(32, 5, padding='causal') → Flatten → Dense(1). Comparar con LSTM equivalente.",
      "Dilation rates: stack de 4 Conv1D con dilation_rate ∈ {1, 2, 4, 8}. Calcular receptive field.",
      "Speed test: medir tiempo de training Conv1D vs LSTM para misma data. Conv1D suele ser 5-20× más rápido en GPU.",
      "WaveNet mini: implementar stack de 10 Conv1D causal con dilations {1, 2, 4, ..., 512} para una serie larga.",
      "Visualización del receptive field: para un output [t], marcar qué inputs lo afectan."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/138-1d-cnns-y-wavenet/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/139-generacion-de-texto-char-rnn",
    "number": 139,
    "slug": "139-generacion-de-texto-char-rnn",
    "partSlug": "parte-2-deep-learning",
    "title": "Generación de texto char-RNN",
    "description": "Construir un modelo de lenguaje autoregresivo a nivel carácter — el ejercicio canónico de Karpathy 2015 sobre Shakespeare.",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Construir un modelo de lenguaje autoregresivo a nivel carácter — el ejercicio canónico de Karpathy 2015 sobre Shakespeare. Entender next-token prediction como tarea de pre-training (la base de todo LLM moderno), sampling con temperatura, y por qué char-RNN fue importante históricamente aunque hoy se hace con tokens BPE y Transformers.",
    "outcomes": [
      "Construir un vocabulario de caracteres (stoi, itos dicts).",
      "Generar samples (window, target) donde el target es el siguiente carácter.",
      "Entrenar un modelo Embedding → LSTM → Dense(vocab_size) con cross-entropy.",
      "Implementar sampling autoregresivo: softmax → multinomial → next char → feed back.",
      "Aplicar temperatura: logits / T antes de softmax — bajo T = más determinista, alto T = más random."
    ],
    "topics": [
      "Tokenización a nivel carácter vs word vs BPE.",
      "Stateful vs stateless RNN: stateful=True para mantener h entre batches.",
      "Loss: cross-entropy sobre vocab_size.",
      "Sampling: greedy vs categorical multinomial vs top-k vs nucleus.",
      "Temperatura como control de creatividad."
    ],
    "materials": [
      "Tiny Shakespeare (~1 MB de obras): https://raw.githubusercontent.com/karpathy/char-rnn/master/data/tinyshakespeare/input.txt",
      "Librerías: tensorflow, keras, numpy."
    ],
    "exercises": [
      "Vocab + encoding: tokenizar el texto a ints. Reportar vocab_size.",
      "Modelo: Embedding(vocab_size, 64) → GRU(128, return_sequences=True) → Dense(vocab_size).",
      "Train: pasar batches de longitud 100; loss = sparse_categorical_crossentropy.",
      "Sample: implementar función que genera N caracteres con T=1.0, T=0.5, T=1.5. Comparar outputs.",
      "Top-k: implementar np.argpartition(logits, -k) antes de muestrear."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/139-generacion-de-texto-char-rnn/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/140-analisis-de-sentimiento",
    "number": 140,
    "slug": "140-analisis-de-sentimiento",
    "partSlug": "parte-2-deep-learning",
    "title": "Análisis de sentimiento",
    "description": "Aplicar un modelo de clasificación de texto sobre IMDB reviews — la tarea NLP más clásica para benchmarks.",
    "level": "Avanzado",
    "duration": "65 min",
    "theory": "Aplicar un modelo de clasificación de texto sobre IMDB reviews — la tarea NLP más clásica para benchmarks. Pipeline completo: TextVectorization → Embedding → arquitectura (Dense / CNN / RNN / Transformer) → Dense(1, sigmoid). Comparar el zoo de approaches y reconocer que con Hugging Face hoy se hace en 3 líneas (clase 127).",
    "outcomes": [
      "Tokenizar y vectorizar texto con TextVectorization(max_tokens=20_000, output_sequence_length=200).",
      "Aplicar Embedding(vocab_size, dim) y entender que es una lookup table aprendible.",
      "Construir 4 arquitecturas: bag-of-embeddings (sin orden), Conv1D, LSTM, Bidirectional LSTM.",
      "Comparar accuracy de las 4 vs un baseline TfidfVectorizer + LogisticRegression.",
      "Usar Embedding(..., mask_zero=True) para manejar padding correctamente."
    ],
    "topics": [
      "TextVectorization moderno (Keras 3+).",
      "Embedding: lookup table inicializada random y entrenable.",
      "BagOfEmbeddings (mean pooling) como baseline DL.",
      "Conv1D para texto: capta n-gramas.",
      "LSTM + Bidirectional: captura contexto largo y bidireccional.",
      "Pre-trained embeddings (GloVe, Word2Vec) — históricamente importantes; hoy reemplazados por embeddings de transformers."
    ],
    "materials": [
      "keras.datasets.imdb.load_data() o tfds.load('imdb_reviews').",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "Baseline ML clásico: TfidfVectorizer + LogisticRegression. Accuracy de referencia (~0.88).",
      "Bag-of-embeddings: Embedding → GlobalAveragePooling1D → Dense(1, sigmoid). Reportar accuracy.",
      "Conv1D: Embedding → Conv1D(64, 5) → GlobalMaxPool1D → Dense(1, sigmoid).",
      "Bidirectional LSTM: Embedding → Bidirectional(LSTM(64)) → Dense(1, sigmoid).",
      "Pre-trained: cargar GloVe 100d y inicializar la matriz de Embedding con ellos. Comparar accuracy contra inicialización random."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/140-analisis-de-sentimiento/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/141-encoder-decoder-para-traduccion",
    "number": 141,
    "slug": "141-encoder-decoder-para-traduccion",
    "partSlug": "parte-2-deep-learning",
    "title": "Encoder-Decoder para traducción",
    "description": "Implementar la arquitectura seq2seq (Sutskever, Vinyals & Le 2014) — un encoder que comprime la oración fuente en un vector de contexto + un decoder que genera la oración destino token por token.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Implementar la arquitectura seq2seq (Sutskever, Vinyals & Le 2014) — un encoder que comprime la oración fuente en un vector de contexto + un decoder que genera la oración destino token por token. Conocer teacher forcing (durante training, el decoder ve los targets reales como input) vs inference autoregresiva. Esta arquitectura es la antesala de atención (clase 125) y de Transformers (clase 126).",
    "outcomes": [
      "Construir un seq2seq con dos LSTM: encoder devuelve state, decoder usa ese state como inicialización.",
      "Aplicar teacher forcing: en training, decoder input = target shifted; en inference, autoregresivo.",
      "Tokens especiales: <start>, <end>, <pad>, <unk>.",
      "Reconocer la limitación del cuello de botella (todo el meaning de la oración fuente en un vector fijo) — motivación para atención.",
      "Evaluar traducción con BLEU (nltk.translate.bleu_score)."
    ],
    "topics": [
      "Arquitectura clásica seq2seq con 2 LSTM.",
      "Teacher forcing vs scheduled sampling.",
      "Inference autoregresiva con generate loop.",
      "Beam search (mejor que greedy).",
      "BLEU como métrica.",
      "Limitación del bottleneck → motivó atención (Bahdanau 2014)."
    ],
    "materials": [
      "Tatoeba English-Spanish (small): https://www.manythings.org/anki/",
      "Librerías: tensorflow, keras, nltk (para BLEU)."
    ],
    "exercises": [
      "Preparar datos: tokenizar source y target, agregar <start> y <end> al target, padding.",
      "Encoder: Embedding → LSTM(256, return_state=True). Mantener state_h, state_c.",
      "Decoder en training: Embedding(decoder_input) → LSTM(256, initial_state=encoder_state) → Dense(target_vocab, softmax).",
      "Inference loop: feed <start>, predecir, alimentar prediction como next input, hasta <end> o max_len.",
      "BLEU: calcular sobre el test set."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/141-encoder-decoder-para-traduccion/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/142-mecanismos-de-atencion",
    "number": 142,
    "slug": "142-mecanismos-de-atencion",
    "partSlug": "parte-2-deep-learning",
    "title": "Mecanismos de atención",
    "description": "Entender la atención — el mecanismo que destrabó NLP moderno.",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Entender la atención — el mecanismo que destrabó NLP moderno. Bahdanau (2015): permite al decoder mirar todos los hidden states del encoder, ponderando dinámicamente. Luego self-attention (Vaswani 2017): tokens dentro de la misma secuencia se atienden entre sí → Transformer (clase 126).",
    "outcomes": [
      "Explicar scaled dot-product attention: softmax(QK^T / √d) V.",
      "Diferenciar cross-attention (decoder→encoder, clásico Bahdanau) de self-attention (intra-secuencia, base del Transformer).",
      "Implementar attention a mano en numpy/TF para una secuencia corta.",
      "Aplicar keras.layers.Attention o keras.layers.MultiHeadAttention.",
      "Interpretar attention weights como \"qué tokens fuente miró el decoder al generar cada token destino\"."
    ],
    "topics": [
      "Motivación: bottleneck del encoder en seq2seq.",
      "Bahdanau (additive) vs Luong (multiplicative / dot-product).",
      "Q, K, V: queries, keys, values.",
      "Scaled dot-product attention.",
      "Self-attention vs cross-attention.",
      "Multi-head: paralelizar varias attention heads con subspaces distintos.",
      "Attention weights visualizables."
    ],
    "materials": [
      "Reusar dataset de traducción de 124.",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "Attention a mano: Q, K, V random (seq, d); calcular softmax(QK^T / √d) V. Verificar shapes.",
      "Visualizar attention map: tras entrenar un seq2seq con atención, plot heatmap de los pesos (target, source) para una traducción.",
      "MultiHeadAttention: mha = MultiHeadAttention(num_heads=8, key_dim=64); output = mha(query, value).",
      "Self-attention: aplicar mha(x, x) (query = key = value). Esto es el bloque de Transformer.",
      "Causal mask: para generación autoregresiva, MultiHeadAttention(..., use_causal_mask=True)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/142-mecanismos-de-atencion/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/143-transformers-arquitectura-bert-gpt",
    "number": 143,
    "slug": "143-transformers-arquitectura-bert-gpt",
    "partSlug": "parte-2-deep-learning",
    "title": "Transformers: arquitectura, BERT, GPT (+ Flash Attention, RoPE, GQA)",
    "description": "Dominar la arquitectura Transformer —encoder, decoder, ambas variantes (BERT encoder-only, GPT decoder-only, T5 encoder-decoder)— a nivel de poder implementarla a mano.",
    "level": "Avanzado",
    "duration": "100 min",
    "theory": "Dominar la arquitectura Transformer —encoder, decoder, ambas variantes (BERT encoder-only, GPT decoder-only, T5 encoder-decoder)— a nivel de poder implementarla a mano. Conocer las mejoras clave 2022-2024 que hacen a los LLMs modernos rápidos y eficientes: Flash Attention v2/v3, RoPE (Rotary Position Embeddings), Grouped-Query Attention (GQA).",
    "outcomes": [
      "Dibujar el block de Transformer: LayerNorm → MultiHeadAttention → +residual → LayerNorm → FFN → +residual.",
      "Implementar positional encoding sinusoidal o aprendible.",
      "Reconocer 3 variantes: encoder-only (BERT), decoder-only (GPT), encoder-decoder (T5, Whisper).",
      "Saber qué hace cada mejora moderna: Flash Attention (O(N) memoria, 2-3× speedup), RoPE (mejor extrapolación a secuencias largas), GQA (compartir KV heads → menos KV cache en inference).",
      "Cargar y usar un Transformer chico con keras.layers.MultiHeadAttention o desde Hugging Face."
    ],
    "topics": [
      "Block Transformer: LN → MHA → res → LN → FFN → res.",
      "Positional encoding: por qué se necesita (attention es permutation-invariant) — sin → aprendible → RoPE.",
      "BERT: encoder-only, MLM + NSP, bidireccional.",
      "GPT: decoder-only, next-token, causal mask.",
      "T5 / BART: encoder-decoder, span-corruption / denoising.",
      "Complemento moderno: Flash Attention, RoPE, GQA, MQA."
    ],
    "materials": [
      "WikiText-2 o similar.",
      "Modelos preentrenados desde HF (clase 127).",
      "Librerías: tensorflow, keras, transformers."
    ],
    "exercises": [
      "Transformer block desde cero: implementar def transformer_block(x): x = x + mha(LN(x)); x = x + ffn(LN(x)); return x con MultiHeadAttention y FFN.",
      "Positional encoding sinusoidal: implementar la fórmula original de Vaswani; visualizar como heatmap.",
      "Mini-GPT: 4 capas Transformer con causal mask. Entrenar en next-token sobre Tiny Shakespeare. Comparar con char-RNN (122).",
      "RoPE manual: implementar la rotación. Aplicar y verificar que attention(Q_rot, K_rot) da diferencia relativa.",
      "HuggingFace check: cargar bert-base-uncased y gpt2; imprimir model.config. Identificar num_attention_heads, hidden_size, intermediate_size."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/143-transformers-arquitectura-bert-gpt/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/144-flash-attention-rope-gqa-llm-engines",
    "number": 144,
    "slug": "144-flash-attention-rope-gqa-llm-engines",
    "partSlug": "parte-2-deep-learning",
    "title": "Flash Attention v2/v3, RoPE, GQA: el motor de los LLMs modernos",
    "description": "Entender en profundidad las 3 piezas técnicas que hacen que un LLM moderno (Llama 3, Mistral, Qwen, Gemma) sea rápido y memory-efficient: Flash Attention v2/v3 (O(N) memoria + 2-3× speedup), Rotary Position Embeddings (…",
    "level": "Avanzado",
    "duration": "90 min",
    "theory": "Entender en profundidad las 3 piezas técnicas que hacen que un LLM moderno (Llama 3, Mistral, Qwen, Gemma) sea rápido y memory-efficient: Flash Attention v2/v3 (O(N) memoria + 2-3× speedup), Rotary Position Embeddings (RoPE) (mejor extrapolación), Grouped-Query Attention (GQA) (menos KV cache en inference).",
    "outcomes": [
      "Explicar por qué attention naïve es O(N²) en memoria y cómo FlashAttention lo reduce a O(N) con online softmax + tiling.",
      "Implementar RoPE: rotar pares de dimensiones de Q, K por ángulo función de posición.",
      "Diferenciar MHA, MQA, GQA — y por qué GQA es el compromiso default 2026.",
      "Aplicar torch.nn.functional.scaled_dot_product_attention(q, k, v, is_causal=True) que elige Flash auto.",
      "Reconocer combinación moderna: RMSNorm + GQA + RoPE + SwiGLU + Flash Attention."
    ],
    "topics": [
      "Attention cost: matriz (N, N) → 64 MB por head con N=8192, fp16.",
      "FlashAttention: bloques en SRAM, no materializa la matriz completa.",
      "v1 (2022), v2 (2023, 2× speedup), v3 (2024, optimizado H100).",
      "Positional encoding: sinusoidal → learnable → RoPE.",
      "RoPE: rotación bidimensional, propiedad relativa.",
      "MHA / MQA / GQA: trade-off entre calidad y memoria.",
      "KV cache: por qué crece en inference."
    ],
    "materials": [
      "HuggingFace modelos: Llama 3, Mistral 7B.",
      "Librerías: flash-attn, torch ≥ 2.0 (SDPA), transformers."
    ],
    "exercises": [
      "SDPA vs naïve: implementar attention naïve y F.scaled_dot_product_attention. Benchmark.",
      "RoPE: implementar rotation function, verificar propiedad attention(R_θ q, R_φ k) = f(θ - φ).",
      "GQA Vs MHA: con Llama config (n_heads=32, kv_heads=8), inspeccionar shapes.",
      "KV cache: medir VRAM en inference con secuencia 8192 — comparar MHA vs GQA.",
      "FlashAttention v3 en H100: si tenés H100, benchmark vs v2."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/144-flash-attention-rope-gqa-llm-engines/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/145-hugging-face-transformers-uso-practico",
    "number": 145,
    "slug": "145-hugging-face-transformers-uso-practico",
    "partSlug": "parte-2-deep-learning",
    "title": "Hugging Face Transformers (uso práctico)",
    "description": "Dominar Hugging Face Transformers — la librería estándar de la industria para usar modelos preentrenados (BERT, GPT, T5, Llama, Whisper, ViT...).",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Dominar Hugging Face Transformers — la librería estándar de la industria para usar modelos preentrenados (BERT, GPT, T5, Llama, Whisper, ViT...). Aprender el pipeline API (one-liner para 90 % de los casos), el Trainer API (fine-tuning con muy poco código) y los componentes manuales (Tokenizer + Model + DataLoader).",
    "outcomes": [
      "Usar pipeline('sentiment-analysis'), pipeline('summarization'), pipeline('zero-shot-classification'), etc. en 1 línea.",
      "Cargar manualmente: tokenizer = AutoTokenizer.from_pretrained('bert-base-uncased'), model = AutoModelForSequenceClassification.from_pretrained('...').",
      "Tokenizar con tokenizer(texts, padding=True, truncation=True, return_tensors='pt').",
      "Fine-tunear con Trainer sobre un dataset propio.",
      "Reconocer el Hub (huggingface.co/models) como catálogo de + de 500k modelos."
    ],
    "topics": [
      "pipeline API: lo más fácil. Tareas: sentiment, NER, QA, summarization, translation, fill-mask, zero-shot, etc.",
      "AutoTokenizer + AutoModel*: API manual flexible.",
      "Tokenizers: BPE, WordPiece, SentencePiece, tiktoken.",
      "Trainer + TrainingArguments: fine-tuning con 20 líneas.",
      "Hub: descubrir modelos, datasets, spaces.",
      "datasets library: cargar datasets, preprocesar."
    ],
    "materials": [
      "HuggingFace Hub: <https://huggingface.co/models>.",
      "Dataset: load_dataset('imdb'), load_dataset('squad'), etc.",
      "Librerías: transformers, datasets, accelerate, evaluate."
    ],
    "exercises": [
      "pipeline one-liner: pipe = pipeline('sentiment-analysis'); pipe('I loved this movie!'). Inspeccionar output.",
      "Zero-shot classification: pipeline('zero-shot-classification')(text, candidate_labels=['sports', 'politics', 'tech']). Sin training específico.",
      "Manual: tokenizar texto con bert-base-uncased. Inspeccionar input_ids, attention_mask, token_type_ids.",
      "Modelo + forward: outputs = model(**inputs). Inspeccionar outputs.logits.",
      "Tokenizer especiales: tokenizer.decode([101, 7592, 102]) → '[CLS] hello [SEP]'."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/145-hugging-face-transformers-uso-practico/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/146-clip-siglip-multimodal-embeddings",
    "number": 146,
    "slug": "146-clip-siglip-multimodal-embeddings",
    "partSlug": "parte-2-deep-learning",
    "title": "CLIP, SigLIP: multimodal embeddings (visión + texto)",
    "description": "Conocer CLIP (OpenAI 2021) y su evolución SigLIP (Google 2023) — los foundation models que mapean imágenes y texto al mismo espacio vectorial, entrenados con contrastive learning sobre 400M-4B pares.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Conocer CLIP (OpenAI 2021) y su evolución SigLIP (Google 2023) — los foundation models que mapean imágenes y texto al mismo espacio vectorial, entrenados con contrastive learning sobre 400M-4B pares. Aplicaciones: zero-shot classification, image search por texto, content moderation, embeddings para RAG multimodal.",
    "outcomes": [
      "Cargar CLIP/SigLIP desde HuggingFace: CLIPModel.from_pretrained('openai/clip-vit-base-patch32').",
      "Calcular embeddings de imágenes y de texto; cosine similarity entre ambos.",
      "Implementar zero-shot classification: predecir clase con la mayor similaridad a \"a photo of a [class]\".",
      "Hacer image retrieval por texto sobre un corpus de imágenes.",
      "Diferenciar CLIP (softmax contrastive) de SigLIP (sigmoid pairwise, mejor escalabilidad)."
    ],
    "topics": [
      "Contrastive Language-Image Pre-training: matchear pares correctos, separar incorrectos.",
      "Arquitectura: image encoder (ViT) + text encoder (Transformer).",
      "Cosine similarity como métrica.",
      "Zero-shot vs few-shot.",
      "Variantes modernas: SigLIP (sigmoid loss), EVA-CLIP, OpenCLIP, Apple AIM."
    ],
    "materials": [
      "Imágenes propias o tfds.load('cats_vs_dogs').",
      "HuggingFace: openai/clip-vit-base-patch32, google/siglip-base-patch16-224.",
      "Librerías: transformers, torch, PIL."
    ],
    "exercises": [
      "CLIP setup: cargar processor + model. Embed una imagen y un texto. Cosine similarity.",
      "Zero-shot classification: dada una imagen, comparar contra [\"a photo of a cat\", \"a photo of a dog\"]. Predict argmax.",
      "Image search: corpus de 100 imágenes; query texto \"a sunset over the ocean\" → top-5 más similares.",
      "SigLIP: misma tarea, comparar accuracy.",
      "Fine-tune ligero: con dataset chico custom, fine-tunear CLIP con LoRA para un dominio específico."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/146-clip-siglip-multimodal-embeddings/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/147-whisper-asr-audio-transcripcion-traduccion",
    "number": 147,
    "slug": "147-whisper-asr-audio-transcripcion-traduccion",
    "partSlug": "parte-2-deep-learning",
    "title": "Whisper: ASR, transcripción, traducción de audio",
    "description": "Usar Whisper (OpenAI 2022, open-source) — el modelo de ASR (Automatic Speech Recognition) multilenguaje que destronó a Google STT y AWS Transcribe en accuracy.",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Usar Whisper (OpenAI 2022, open-source) — el modelo de ASR (Automatic Speech Recognition) multilenguaje que destronó a Google STT y AWS Transcribe en accuracy. Cubrir transcripción, traducción a inglés, timestamps, word-level timing. Alternativas modernas: Whisper-large-v3, distil-whisper (4× más rápido), insanely-fast-whisper.",
    "outcomes": [
      "Cargar Whisper con transformers (openai/whisper-large-v3) o openai-whisper (lib oficial).",
      "Transcribir audio en cualquier idioma (99+ soportados).",
      "Aplicar task='translate' para traducir directo a inglés.",
      "Obtener timestamps a nivel palabra para subtítulos.",
      "Usar distil-whisper para inference 4-6× más rápida con calidad similar."
    ],
    "topics": [
      "Arquitectura: encoder-decoder Transformer + spectrogram input.",
      "Tamaños: tiny, base, small, medium, large-v3.",
      "Languages: detectado automático o explícito.",
      "Tareas: transcribe (en idioma origen), translate (→ inglés).",
      "Diarization (quién habla): no built-in, requiere pyannote.audio separado.",
      "Long-form audio: chunking con overlap."
    ],
    "materials": [
      "Cualquier audio: voz, podcasts, llamadas.",
      "HuggingFace: openai/whisper-large-v3, distil-whisper/distil-large-v3.",
      "Librerías: transformers, torch, librosa (procesamiento audio)."
    ],
    "exercises": [
      "Transcripción básica: cargar pipeline('asr', model='openai/whisper-base'); pasar un audio.",
      "Multilenguaje: audio en español → transcribir; verificar.",
      "Traducción: pipe(audio, task='translate') → texto en inglés.",
      "Timestamps: pipe(audio, return_timestamps='word') → palabras con start/end seconds.",
      "Distil-Whisper: comparar tiempo y WER vs full Whisper."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/147-whisper-asr-audio-transcripcion-traduccion/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/148-llms-aplicados-fine-tuning-prompting",
    "number": 148,
    "slug": "148-llms-aplicados-fine-tuning-prompting",
    "partSlug": "parte-2-deep-learning",
    "title": "LLMs aplicados: fine-tuning, prompting (+ LoRA / QLoRA, DPO, vLLM)",
    "description": "Manejar Large Language Models (Llama 3, Mistral, Qwen, etc.) en flujos reales: prompting técnico (zero-shot, few-shot, chain-of-thought), fine-tuning eficiente con LoRA / QLoRA (entrenar solo 0.1-1 % de parámetros), ali…",
    "level": "Avanzado",
    "duration": "110 min",
    "theory": "Manejar Large Language Models (Llama 3, Mistral, Qwen, etc.) en flujos reales: prompting técnico (zero-shot, few-shot, chain-of-thought), fine-tuning eficiente con LoRA / QLoRA (entrenar solo 0.1-1 % de parámetros), alineamiento con DPO (preferencias, en lugar de RLHF clásico), e inference de producción con vLLM (continuous batching, PagedAttention).",
    "outcomes": [
      "Diseñar prompts con system prompts, few-shot examples y chain-of-thought.",
      "Aplicar LoRA con peft library: agregar adapters chicos a un LLM grande, entrenar solo ~0.5 % de params.",
      "Aplicar QLoRA (cuantización 4-bit) para fine-tunear Llama 7B en una sola GPU de 24 GB.",
      "Alinear con preferencias usando DPO (trl library) — más simple y estable que RLHF.",
      "Servir un modelo con vLLM y medir throughput."
    ],
    "topics": [
      "LLM stack en 2026: base → SFT (Supervised Fine-Tuning) → DPO/RLHF → inference optimizada.",
      "Prompting técnico: structure, few-shot, chain-of-thought, function calling.",
      "PEFT (Parameter-Efficient Fine-Tuning): LoRA, QLoRA, adapters.",
      "DPO vs RLHF.",
      "vLLM: continuous batching, PagedAttention, OpenAI-compatible API.",
      "Evaluación: MMLU, HumanEval, MT-Bench, LMSys Arena."
    ],
    "materials": [
      "HuggingFace Hub para modelos.",
      "Datasets de instrucción: Alpaca, ShareGPT, OpenOrca.",
      "Datasets de preferencia: Anthropic HH-RLHF, UltraFeedback.",
      "Librerías: transformers, peft, trl, bitsandbytes, vllm."
    ],
    "exercises": [
      "Prompt engineering: para una tarea (e.g., clasificación de quejas), iterar 5 versiones de prompt (zero-shot, few-shot, CoT, etc.). Medir accuracy en un set chico.",
      "LoRA SFT: fine-tunear un Mistral 7B Instruct con LoRA sobre un dataset propio chico (1k-10k ejemplos).",
      "QLoRA: el mismo experimento pero con quantization 4-bit. Comparar memoria y velocidad.",
      "DPO: con un dataset de preferencias mínimo (e.g., 500 pairs), aplicar DPO sobre el modelo SFT.",
      "vLLM serving: levantar vLLM con el modelo + LoRA adapter, medir throughput vs HF pipeline."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/148-llms-aplicados-fine-tuning-prompting/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/149-lora-qlora-fine-tuning-eficiente",
    "number": 149,
    "slug": "149-lora-qlora-fine-tuning-eficiente",
    "partSlug": "parte-2-deep-learning",
    "title": "LoRA / QLoRA: fine-tuning eficiente de LLMs",
    "description": "Hacer fine-tuning de LLMs (Llama 3, Mistral, Qwen 2) en una GPU consumer con LoRA y QLoRA.",
    "level": "Avanzado",
    "duration": "100 min",
    "theory": "Hacer fine-tuning de LLMs (Llama 3, Mistral, Qwen 2) en una GPU consumer con LoRA y QLoRA. Cubrir hyperparámetros (r, alpha, dropout, target_modules), inspección de trainable params, merge LoRA con base, y deployment.",
    "outcomes": [
      "Aplicar LoRA con peft.LoraConfig y get_peft_model.",
      "Configurar QLoRA con bitsandbytes 4-bit + BitsAndBytesConfig(load_in_4bit=True, bnb_4bit_quant_type='nf4').",
      "Elegir rank r (típico 8-64), alpha (típico 2×r), target_modules.",
      "Mergear el LoRA adapter con el base para deploy: model.merge_and_unload().",
      "Calcular trainable params vs total: ~0.1-1 % es el ratio típico."
    ],
    "topics": [
      "LoRA matemáticamente: W' = W + (B·A)·alpha/r.",
      "QLoRA: NF4 quantization + double quant + paged optimizers.",
      "target_modules: ['q_proj', 'k_proj', 'v_proj', 'o_proj'] clásico; o all-linear.",
      "Save / load: solo el adapter (~10-50 MB) en lugar del full model.",
      "Merge + serve vs separated adapter."
    ],
    "materials": [
      "HuggingFace dataset de instrucción (Alpaca, Dolly, OpenAssistant).",
      "Modelo base: Llama 3 8B Instruct, Mistral 7B Instruct, Qwen 2 7B Instruct.",
      "Librerías: transformers, peft, bitsandbytes, accelerate, trl."
    ],
    "exercises": [
      "LoRA básico: cargar Mistral 7B Instruct sin quantization; aplicar LoRA r=16. Inspeccionar trainable params (~0.5 %).",
      "QLoRA: ahora con load_in_4bit=True. Verificar uso VRAM (~6 GB).",
      "Train con TRL: SFTTrainer sobre 500 ejemplos custom. ~30 min en GPU consumer.",
      "Inference con adapter: cargar base + LoRA y predecir.",
      "Merge: model.merge_and_unload() → save como modelo normal."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/149-lora-qlora-fine-tuning-eficiente/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/150-dpo-rlhf-alineamiento-de-llms",
    "number": 150,
    "slug": "150-dpo-rlhf-alineamiento-de-llms",
    "partSlug": "parte-2-deep-learning",
    "title": "DPO y RLHF: alineamiento de LLMs",
    "description": "Alinear LLMs con preferencias humanas (helpful, harmless, honest).",
    "level": "Avanzado",
    "duration": "95 min",
    "theory": "Alinear LLMs con preferencias humanas (helpful, harmless, honest). Cubrir RLHF clásico (SFT → Reward Model → PPO, complejo) y DPO (Direct Preference Optimization, moderno y simple). Conocer variantes 2023-2024: IPO, KTO, ORPO.",
    "outcomes": [
      "Explicar el pipeline RLHF de 3 etapas (SFT, RM, PPO).",
      "Aplicar DPO con trl.DPOTrainer sobre un dataset de preferencias.",
      "Diferenciar DPO (single-step) de KTO (no requiere pairs) y ORPO (combina SFT + alineamiento).",
      "Crear un dataset de preferencias: (prompt, chosen, rejected).",
      "Evaluar alineamiento con MT-Bench, AlpacaEval, o LLM-as-judge."
    ],
    "topics": [
      "Por qué alineamiento: LLM pretrained → genera pero no sigue instrucciones bien ni evita harm.",
      "SFT (Supervised Fine-Tuning): instruction tuning.",
      "Reward Model: regression entrenada con human preferences.",
      "PPO: optimizar el LLM contra el RM.",
      "DPO: derivación matemática que elimina el RM.",
      "IPO: variante con identity link, más estable.",
      "KTO: solo chosen o rejected (no necesita pairs).",
      "ORPO: alineamiento desde SFT directamente."
    ],
    "materials": [
      "Anthropic HH-RLHF, UltraFeedback, Argilla DPO datasets.",
      "Modelo base: SFT propio (clase 128a) o Mistral 7B Instruct.",
      "Librerías: transformers, trl, peft, bitsandbytes."
    ],
    "exercises": [
      "Dataset de preferencias: cargar Anthropic/hh-rlhf. Inspeccionar chosen y rejected.",
      "DPO con TRL: DPOTrainer(model, ref_model, ...) con LoRA encima. Train 1 época.",
      "Eval pre/post: generar respuestas a 20 prompts antes y después; comparar manualmente.",
      "β sensitivity: probar β ∈ {0.1, 0.3, 1.0}. β alto → menos cambio; β bajo → más agresivo.",
      "KTO: dataset con solo chosen (no pairs). Aplicar KTOTrainer."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/150-dpo-rlhf-alineamiento-de-llms/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/151-vllm-tgi-serving-llm-produccion",
    "number": 151,
    "slug": "151-vllm-tgi-serving-llm-produccion",
    "partSlug": "parte-2-deep-learning",
    "title": "vLLM y TGI: serving de LLMs en producción",
    "description": "Servir LLMs eficientemente en producción con vLLM (Berkeley) o TGI (HuggingFace).",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Servir LLMs eficientemente en producción con vLLM (Berkeley) o TGI (HuggingFace). Cubrir: PagedAttention, continuous batching, prefill/decode, quantization (AWQ, GPTQ, FP8), structured output (JSON, function calling), streaming, OpenAI-compatible API.",
    "outcomes": [
      "Levantar vLLM serving: python -m vllm.entrypoints.openai.api_server --model X.",
      "Hacer requests con OpenAI client apuntando a vLLM.",
      "Aplicar continuous batching y entender ganancia de throughput.",
      "Servir modelos cuantizados (AWQ, GPTQ, FP8) para reducir VRAM.",
      "Activar structured outputs con guided_json (JSON schema enforced)."
    ],
    "topics": [
      "KV cache: por qué crece con secuencia.",
      "PagedAttention (vLLM): page table como OS → no fragmentación.",
      "Continuous batching: nuevos requests entran sin esperar al batch.",
      "Prefill (compute KV) vs decode (1 token/step).",
      "Speculative decoding: predecir N tokens, verificar con modelo grande.",
      "Quantization: FP8 (H100), AWQ/GPTQ (4-bit weight-only)."
    ],
    "materials": [
      "Modelo: Mistral 7B Instruct, Llama 3 8B Instruct, o uno cuantizado AWQ.",
      "Librerías: vllm, transformers, openai (client)."
    ],
    "exercises": [
      "vLLM básico: python -m vllm.entrypoints.openai.api_server --model mistralai/Mistral-7B-Instruct-v0.2. Cliente OpenAI.",
      "Continuous batching benchmark: 100 requests paralelos vs 1 a la vez. Comparar throughput.",
      "AWQ quantization: cargar TheBloke/Mistral-7B-Instruct-v0.2-AWQ. VRAM ~5 GB vs 14 GB fp16.",
      "Structured JSON output: extra_body={'guided_json': {schema}} → forced JSON valid.",
      "TGI: docker run --gpus all ghcr.io/huggingface/text-generation-inference:latest --model-id X."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/151-vllm-tgi-serving-llm-produccion/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/152-rag-basico-y-embeddings",
    "number": 152,
    "slug": "152-rag-basico-y-embeddings",
    "partSlug": "parte-2-deep-learning",
    "title": "RAG básico y embeddings (+ hybrid search, re-ranking, MCP)",
    "description": "Construir un sistema RAG (Retrieval-Augmented Generation) — pipeline que enriquece a un LLM con conocimiento externo: documentos propios, base de datos, web.",
    "level": "Avanzado",
    "duration": "100 min",
    "theory": "Construir un sistema RAG (Retrieval-Augmented Generation) — pipeline que enriquece a un LLM con conocimiento externo: documentos propios, base de datos, web. Pipeline: embedding los docs → almacenar en vector DB → al query, hacer retrieval de los k más relevantes → inyectar como contexto al LLM → respuesta basada en docs. Conocer mejoras modernas: hybrid search (denso + sparse), cross-encoder re-ranking, y el Model Context Protocol (MCP) que estandariza la conexión LLM-herramientas.",
    "outcomes": [
      "Generar embeddings de texto con sentence-transformers o modelos HF.",
      "Almacenar y buscar embeddings con FAISS, Chroma, Pinecone, Qdrant, o pgvector.",
      "Construir el flujo query → embed → top-k → context → LLM.",
      "Aplicar hybrid search: combinar BM25 (sparse) con embeddings (dense) → mejor recall.",
      "Aplicar cross-encoder re-ranking sobre los top-100 retornados para promover los top-10 reales.",
      "Reconocer el MCP como protocolo abierto para conectar LLMs a herramientas (filesystems, DBs, APIs)."
    ],
    "topics": [
      "Por qué RAG: LLMs no saben de documentos privados; entrenar fine-tune no escala para conocimiento dinámico.",
      "Embeddings: vectores de dimensión ~768-1536.",
      "Vector DBs: FAISS (in-memory), Chroma (local), Qdrant/Weaviate (server), pgvector (Postgres extension).",
      "Chunking: dividir docs en piezas de ~200-1000 tokens.",
      "Top-k retrieval + context window.",
      "Complemento moderno: hybrid search, cross-encoder rerank, MCP."
    ],
    "materials": [
      "Cualquier corpus de docs propios (PDFs, markdown, HTML).",
      "Wikipedia dump para experimentos.",
      "Librerías: sentence-transformers, chromadb / faiss-cpu, rank_bm25, langchain / llama-index, mcp."
    ],
    "exercises": [
      "Embed + index: con sentence-transformers/all-MiniLM-L6-v2, embeber 100 párrafos y guardarlos en Chroma. Query y top-5.",
      "BM25 baseline: con rank_bm25, query y comparar resultados vs dense.",
      "Hybrid (RRF): combinar ambos. Verificar que hybrid > dense > BM25 sola en queries técnicas.",
      "Cross-encoder rerank: tomar top-50 del paso 3, rerankar con cross-encoder/ms-marco-MiniLM-L-6-v2. Comparar nDCG.",
      "RAG con LLM: top-5 → contexto + query → Claude o GPT → respuesta con citas."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/152-rag-basico-y-embeddings/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/153-mcp-model-context-protocol",
    "number": 153,
    "slug": "153-mcp-model-context-protocol",
    "partSlug": "parte-2-deep-learning",
    "title": "MCP (Model Context Protocol): herramientas y datos para LLMs",
    "description": "Aprender MCP (Model Context Protocol) — estándar abierto publicado por Anthropic en noviembre 2024 que define cómo un LLM se conecta a herramientas externas (filesystems, databases, APIs, search engines, etc.).",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Aprender MCP (Model Context Protocol) — estándar abierto publicado por Anthropic en noviembre 2024 que define cómo un LLM se conecta a herramientas externas (filesystems, databases, APIs, search engines, etc.). Antes de MCP, cada framework (LangChain, LlamaIndex, OpenAI plugins) tenía API propia. MCP unifica → portabilidad entre LLMs y clients.",
    "outcomes": [
      "Explicar la arquitectura MCP: client, server, resources, tools, prompts.",
      "Conectar MCP servers existentes a Claude Desktop, Cursor, Zed.",
      "Escribir un MCP server propio en Python (con fastmcp).",
      "Diferenciar MCP de tool use clásico de OpenAI / LangChain.",
      "Usar MCP servers populares: filesystem, postgres, git, slack, brave-search."
    ],
    "topics": [
      "Cliente (LLM app) vs Server (provee tools/resources/prompts).",
      "Transport: stdio (local) y SSE (network).",
      "Resources: read-only data (archivos, DB rows).",
      "Tools: funciones invocables (search, write).",
      "Prompts: templates reusables.",
      "Discovery: el client descubre dinámicamente qué hay disponible."
    ],
    "materials": [
      "MCP servers oficiales.",
      "Librerías: mcp (Python SDK), fastmcp."
    ],
    "exercises": [
      "Conectar server existente: instalar mcp-server-filesystem en Claude Desktop. Hacer queries sobre archivos del file system.",
      "Server propio: con fastmcp, exponer un tool search_docs(query) sobre un corpus local.",
      "Resource: exponer archivos .md como resources lectura.",
      "Prompt template: definir summarize(file_uri) como prompt reusable.",
      "Multi-server: conectar 2-3 servers simultáneos a Claude Desktop; usar conjuntamente."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/153-mcp-model-context-protocol/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/154-agentes-tool-use-react-multi-agent",
    "number": 154,
    "slug": "154-agentes-tool-use-react-multi-agent",
    "partSlug": "parte-2-deep-learning",
    "title": "Agentes: tool use, ReAct, multi-agent",
    "description": "Construir agentes con LLMs: el LLM planifica, invoca tools (funciones, MCP servers, APIs), observa los resultados y decide el siguiente paso.",
    "level": "Avanzado",
    "duration": "95 min",
    "theory": "Construir agentes con LLMs: el LLM planifica, invoca tools (funciones, MCP servers, APIs), observa los resultados y decide el siguiente paso. Cubrir el paradigma ReAct (Reasoning + Acting), tool use moderno (function calling structured), y patrones multi-agent (workflows, swarms, supervisores).",
    "outcomes": [
      "Definir tools con JSON schema; pasar a la API del LLM.",
      "Implementar loop ReAct manual: prompt → LLM → tool call → execute → observation → prompt.",
      "Usar LangGraph o AutoGen o CrewAI para orquestar multi-agent.",
      "Diseñar patrones: workflow (lineal), router (decide ruta), evaluator-optimizer (loop con auto-crítica).",
      "Reconocer cuándo NO usar agentes (tareas determinísticas → workflow simple; agentes solo si hace falta razonamiento dinámico)."
    ],
    "topics": [
      "Tool use con OpenAI/Anthropic function calling.",
      "ReAct prompt template.",
      "Loops: while LLM produces tool_call, execute and feed observation.",
      "LangGraph: state machines para agentes.",
      "AutoGen / CrewAI: multi-agent frameworks.",
      "Patrones (Anthropic 2024): prompt chaining, routing, parallelization, orchestrator-workers, evaluator-optimizer.",
      "Token cost: agentes con loops pueden gastar mucho."
    ],
    "materials": [
      "Anthropic Claude API o OpenAI API (function calling).",
      "Librerías: anthropic, openai, langgraph, crewai, autogen."
    ],
    "exercises": [
      "Tool básico: definir weather(city) y search(query) tools en Claude API. Pedirle que use ambos.",
      "ReAct loop manual: implementar el loop sin librería, en Python puro.",
      "LangGraph: definir un grafo: router → tool → evaluator → end. Compilar y ejecutar.",
      "Multi-agent (CrewAI): 3 agents (researcher, writer, editor) para producir un blog post.",
      "Evaluator-optimizer: agent que escribe + agent que critica + loop hasta approved=True."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/154-agentes-tool-use-react-multi-agent/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/155-llm-evaluation-mmlu-mtbench-llm-as-judge",
    "number": 155,
    "slug": "155-llm-evaluation-mmlu-mtbench-llm-as-judge",
    "partSlug": "parte-2-deep-learning",
    "title": "LLM Evaluation: MMLU, MT-Bench, LLM-as-judge, evals propios",
    "description": "Evaluar LLMs (propios o terceros) con rigor: benchmarks estándar (MMLU, HumanEval, GSM8K, MT-Bench, LMSys Arena), LLM-as-judge para casos open-ended, y evals propios específicos al dominio.",
    "level": "Avanzado",
    "duration": "85 min",
    "theory": "Evaluar LLMs (propios o terceros) con rigor: benchmarks estándar (MMLU, HumanEval, GSM8K, MT-Bench, LMSys Arena), LLM-as-judge para casos open-ended, y evals propios específicos al dominio. Reconocer las trampas (data contamination, reward hacking, leaderboard hacking).",
    "outcomes": [
      "Correr MMLU con lm-evaluation-harness sobre un modelo propio.",
      "Implementar LLM-as-judge con (prompt, response_A, response_B) → \"cuál es mejor\".",
      "Diseñar evals custom: cobertura por tema, casos edge, regresiones.",
      "Diferenciar classification metrics (accuracy on MCQs) de generation metrics (BLEU, ROUGE, BERTScore, LLM-judge).",
      "Reconocer data contamination (test set en pretraining) y leaderboard hacking."
    ],
    "topics": [
      "MMLU: 57 dominios, multiple choice. Standard 2020-2023.",
      "HumanEval: 164 problemas Python codegen.",
      "GSM8K: math word problems.",
      "MT-Bench: 80 multi-turn questions evaluadas por GPT-4 judge.",
      "LMSys Arena: head-to-head humanos. Standard moderno (ELO ranking).",
      "LLM-as-judge: usar GPT-4/Claude como evaluador.",
      "Custom evals: críticos para producción."
    ],
    "materials": [
      "HuggingFace: lm-eval-harness, HELM, lighteval.",
      "Modelo a evaluar: cualquier LLM open o API.",
      "Librerías: lm-evaluation-harness, inspect_ai, promptfoo."
    ],
    "exercises": [
      "MMLU con lm-eval-harness: lm_eval --model hf --model_args pretrained=mistralai/Mistral-7B-v0.1 --tasks mmlu --num_fewshot 5. Reportar score.",
      "HumanEval: code generation, pass@1.",
      "MT-Bench: usar GPT-4 / Claude como judge. Reportar score promedio.",
      "LLM-as-judge propio: 20 pairs (model_A vs model_B); judge devuelve A/B/tie + reasoning.",
      "Custom eval: 50 prompts específicos a tu use case + criterios de aceptación."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/155-llm-evaluation-mmlu-mtbench-llm-as-judge/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/156-autoencoders-undercomplete-stacked-denoising-sparse",
    "number": 156,
    "slug": "156-autoencoders-undercomplete-stacked-denoising-sparse",
    "partSlug": "parte-2-deep-learning",
    "title": "Autoencoders: undercomplete, stacked, denoising, sparse",
    "description": "Entender autoencoders — red Encoder → bottleneck → Decoder entrenada a reconstruir su input.",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Entender autoencoders — red Encoder → bottleneck → Decoder entrenada a reconstruir su input. Variantes que cubrimos: undercomplete (dim_latent < dim_input, fuerza compresión), stacked (deep), denoising (input ruidoso → output limpio), sparse (penaliza activaciones latentes). Saber qué problemas resuelven (compresión, anomaly detection, pretraining) y cuándo VAEs/GANs/Diffusion los superan en generación.",
    "outcomes": [
      "Construir un undercomplete AE con MLP/CNN y entrenarlo con MSE.",
      "Diferenciar latent_dim < input_dim (compresión real) de latent_dim >> input_dim con regularización (sparse).",
      "Implementar Denoising AE: input x + noise, target x.",
      "Aplicar AE como anomaly detector: alta reconstruction error → anomalía.",
      "Reconocer que autoencoders no son buenos generadores (latent space irregular) → motivó VAE (clase 131)."
    ],
    "topics": [
      "Encoder + Decoder simétricos.",
      "Bottleneck: latent space.",
      "Undercomplete: dimensión chica.",
      "Stacked: varias capas Dense/Conv.",
      "Denoising: robusto a ruido.",
      "Sparse: penalizar ||latent||_1 para que pocas neuronas activas.",
      "AE para anomaly detection."
    ],
    "materials": [
      "Fashion-MNIST / MNIST.",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "AE simple: Encoder: 784 → 64; Decoder: 64 → 784. Entrenar en MNIST. Visualizar reconstrucciones.",
      "Latent space 2D: latent_dim=2. Plot scatter de las representaciones de 1000 imágenes coloreadas por clase.",
      "Denoising: noise = 0.5 * rng.normal(x.shape), target = x. Mostrar que reconstruye limpio aunque input está ruidoso.",
      "Sparse: agregar keras.regularizers.l1(1e-3) sobre la capa latente. Inspeccionar activaciones.",
      "Anomaly detection: entrenar AE solo sobre clase \"normal\"; calcular reconstruction error en clase \"anomalía\"; usar como score."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/156-autoencoders-undercomplete-stacked-denoising-sparse/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/157-variational-autoencoders-vae",
    "number": 157,
    "slug": "157-variational-autoencoders-vae",
    "partSlug": "parte-2-deep-learning",
    "title": "Variational Autoencoders (VAE)",
    "description": "Construir un VAE (Variational Autoencoder, Kingma & Welling 2014) — variante probabilística del AE que aprende una distribución sobre el latent en lugar de un punto: encoder outputs μ, σ de una gaussiana; sampling + rep…",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Construir un VAE (Variational Autoencoder, Kingma & Welling 2014) — variante probabilística del AE que aprende una distribución sobre el latent en lugar de un punto: encoder outputs μ, σ de una gaussiana; sampling + reparametrization trick para mantener gradientes. Resultado: latent space continuo y estructurado → permite generación, interpolación entre samples.",
    "outcomes": [
      "Implementar encoder que devuelve (μ, log σ²); sample con z = μ + σ · ε (reparametrization).",
      "Loss = reconstruction_loss + β · KL(N(μ,σ²) || N(0,I)).",
      "Generar samples nuevos: muestrear z ~ N(0,I), pasar por el decoder.",
      "Interpolar en el latent space y verificar transiciones suaves.",
      "Reconocer que VAE produce outputs borrosos (consecuencia del MSE/BCE) — motivó GANs (132)."
    ],
    "topics": [
      "ELBO (Evidence Lower BOund): log p(x) ≥ E[log p(x|z)] - KL(q(z|x) || p(z)).",
      "Reparametrization trick: para back-propagar a través del sample.",
      "β-VAE: subir β fuerza latent más disentangled.",
      "Posterior collapse: cuando el decoder ignora z."
    ],
    "materials": [
      "Fashion-MNIST / MNIST / Celeb-A (cara).",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "VAE básico: encoder → (z_mean, z_log_var) → sample → decoder. Loss combinada. Entrenar en MNIST.",
      "Sampling: muestrear z ~ N(0,I) de tamaño (100, latent_dim). Pasar por decoder. Visualizar las 100 imágenes generadas.",
      "Interpolación: dos imágenes A y B → z_A, z_B. Generar 10 imágenes en interpolación lineal entre z_A y z_B. Visualizar.",
      "β-VAE: probar β=1, β=5, β=10. Comparar disentanglement vs blurriness.",
      "Posterior collapse: con LR alto, el encoder colapsa a μ=0, σ=1. Diagnosticar mirando z_mean.std() cerca de 0."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/157-variational-autoencoders-vae/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/158-gans-dcgan-progressive-gan-stylegan",
    "number": 158,
    "slug": "158-gans-dcgan-progressive-gan-stylegan",
    "partSlug": "parte-2-deep-learning",
    "title": "GANs: DCGAN, Progressive GAN, StyleGAN",
    "description": "Construir un GAN (Generative Adversarial Network, Goodfellow 2014) — dos redes en juego adversarial: Generador crea muestras desde noise; Discriminador distingue real de falso.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Construir un GAN (Generative Adversarial Network, Goodfellow 2014) — dos redes en juego adversarial: Generador crea muestras desde noise; Discriminador distingue real de falso. El equilibrio Nash de este juego = generador que genera muestras indistinguibles de la distribución real. Conocer las variantes principales: DCGAN, Progressive GAN, StyleGAN (caras hiperrealistas).",
    "outcomes": [
      "Implementar un DCGAN sencillo con Generator + Discriminator convolucionales sobre MNIST/Fashion.",
      "Escribir custom training loop alternando G y D updates.",
      "Diagnosticar 3 problemas clásicos: mode collapse (G produce 1 sola cosa), vanishing G gradient (D demasiado bueno), training inestable.",
      "Aplicar label smoothing (real labels = 0.9 en lugar de 1.0), noise en D inputs, y WGAN-GP (Wasserstein) para mejor estabilidad.",
      "Reconocer que GANs perdieron terreno frente a Diffusion (clase 133) en 2022+, pero StyleGAN sigue siendo competitivo para caras."
    ],
    "topics": [
      "Loss original (min-max): min_G max_D E[log D(x)] + E[log(1 - D(G(z)))].",
      "DCGAN: arquitecturas convolucionales (Radford et al. 2015).",
      "Modos de fallo: mode collapse, D demasiado fuerte/débil.",
      "WGAN, WGAN-GP, spectral norm.",
      "Progressive GAN: empezar con 4×4, ir subiendo resolución.",
      "StyleGAN: AdaIN, style mixing, latent W intermedio.",
      "Métricas: FID (Fréchet Inception Distance), IS."
    ],
    "materials": [
      "MNIST / Fashion-MNIST como playground.",
      "Celeb-A para caras (más serio).",
      "Librerías: tensorflow, keras."
    ],
    "exercises": [
      "DCGAN básico: G y D convolucionales. Custom training loop con dos tf.function (train_d, train_g).",
      "Diagnóstico: graficar D_loss y G_loss por step. Si D_loss → 0, G está perdiendo.",
      "Mode collapse: tras N épocas, generar 64 samples. Si todos son la misma cosa → collapse.",
      "WGAN-GP: implementar gradient penalty en la D loss. Comparar estabilidad vs DCGAN.",
      "FID: implementar (o usar tensorflow_gan.eval.fid) y reportar FID del modelo."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/158-gans-dcgan-progressive-gan-stylegan/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/159-modelos-de-difusion-ddpm-score-based",
    "number": 159,
    "slug": "159-modelos-de-difusion-ddpm-score-based",
    "partSlug": "parte-2-deep-learning",
    "title": "Modelos de difusión (+ Stable Diffusion XL, ControlNet, LCM)",
    "description": "Entender modelos de difusión — la familia que destronó a GANs en 2022 (DALL-E 2, Stable Diffusion, Midjourney).",
    "level": "Avanzado",
    "duration": "105 min",
    "theory": "Entender modelos de difusión — la familia que destronó a GANs en 2022 (DALL-E 2, Stable Diffusion, Midjourney). Idea: forward process agrega ruido gaussiano gradualmente; reverse process (aprendido) lo elimina paso a paso. Conocer DDPM clásico, latent diffusion (Stable Diffusion), ControlNet para condicionamiento espacial, LCM (Latent Consistency Models) para inference rápida.",
    "outcomes": [
      "Implementar un DDPM sencillo: forward q(x_t | x_0), U-Net que predice el ruido ε_θ(x_t, t).",
      "Aplicar el sampling DDPM: 1000 steps de denoising desde x_T ~ N(0,I).",
      "Reconocer latent diffusion: aplicar difusión en el espacio comprimido de un VAE (1/64 del tamaño) → 8× más rápido.",
      "Usar Stable Diffusion XL con diffusers library: prompt → imagen en 3 líneas.",
      "Aplicar ControlNet para condicionar generación en pose, edge, depth, segmentation.",
      "Acelerar inference con LCM o Turbo (1-4 steps en lugar de 50)."
    ],
    "topics": [
      "Forward process: q(x_t | x_{t-1}) = N(√(1-β_t) x_{t-1}, β_t I).",
      "Closed form: q(x_t | x_0) = N(√α̅_t · x_0, (1-α̅_t) I).",
      "Loss simple (Ho 2020): MSE(ε, ε_θ(x_t, t)) — predecir el ruido.",
      "U-Net architecture (encoder-decoder con skip connections).",
      "Sampling DDPM vs DDIM vs DPM-Solver: 1000 → 50 → 20 steps.",
      "Complemento moderno: Stable Diffusion XL, ControlNet, LCM/Turbo."
    ],
    "materials": [
      "Fashion-MNIST como playground.",
      "HF Hub para modelos pre-trained.",
      "Librerías: diffusers, transformers, accelerate, controlnet_aux."
    ],
    "exercises": [
      "DDPM en MNIST: U-Net chico + DDPM scheduler. Entrenar 50 épocas; samplear 64 imágenes.",
      "SDXL inference: cargar SDXL y generar 4 imágenes desde prompts.",
      "CFG: variar guidance_scale ∈ {1, 5, 15}. Ver cómo afecta fidelidad al prompt vs diversidad.",
      "ControlNet Canny: tomar una foto, extraer bordes con OpenCV, generar variantes condicionadas con SDXL+ControlNet.",
      "LCM: comparar SDXL base (30 steps) vs SDXL + LCM-LoRA (4 steps). Tiempo y calidad."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/159-modelos-de-difusion-ddpm-score-based/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/160-stable-diffusion-xl-controlnet",
    "number": 160,
    "slug": "160-stable-diffusion-xl-controlnet",
    "partSlug": "parte-2-deep-learning",
    "title": "Stable Diffusion XL + ControlNet en profundidad",
    "description": "Dominar Stable Diffusion XL (Stability AI 2023) en producción: pipeline completo (text encoder dual, U-Net, VAE), schedulers modernos (DPM-Solver++, Euler ancestral, UniPC), CFG (Classifier-Free Guidance), prompt weight…",
    "level": "Avanzado",
    "duration": "90 min",
    "theory": "Dominar Stable Diffusion XL (Stability AI 2023) en producción: pipeline completo (text encoder dual, U-Net, VAE), schedulers modernos (DPM-Solver++, Euler ancestral, UniPC), CFG (Classifier-Free Guidance), prompt weighting. Combinar con ControlNet para condicionamiento espacial (Canny, depth, pose, segmentation, lineart). Conocer Flux (Black Forest Labs 2024) como sucesor open-source.",
    "outcomes": [
      "Cargar SDXL: StableDiffusionXLPipeline.from_pretrained('stabilityai/stable-diffusion-xl-base-1.0').",
      "Aplicar refiner opcional para detalle final.",
      "Usar schedulers distintos y entender trade-off speed/quality.",
      "Agregar ControlNet (canny, depth, openpose) sobre SDXL.",
      "Aplicar LoRA para estilo custom (pipe.load_lora_weights('path')).",
      "Reconocer Flux y SD3 como sucesores."
    ],
    "topics": [
      "Pipeline SDXL: text_encoder_1 (CLIP-L), text_encoder_2 (CLIP-G), U-Net 2.6B params, VAE.",
      "Schedulers: DDIM (50 steps), DPM-Solver++ (20 steps), Euler ancestral (creative), UniPC (10-20 steps).",
      "CFG: guidance_scale=7.5 default; > 12 over-fitting al prompt.",
      "Negative prompts.",
      "Refiner (paso opcional adicional).",
      "ControlNet variantes: Canny, Depth, OpenPose, Scribble, Lineart, MLSD, Tile."
    ],
    "materials": [
      "HuggingFace: stabilityai/stable-diffusion-xl-base-1.0, ControlNets en diffusers/controlnet-*-sdxl-1.0.",
      "Librerías: diffusers, transformers, accelerate, controlnet_aux."
    ],
    "exercises": [
      "SDXL básico: prompt → imagen 1024². Comparar schedulers (DPM-Solver++, Euler a, UniPC).",
      "CFG sweep: guidance_scale ∈ {3, 7.5, 12, 18}. Ver trade-off creativity/fidelity.",
      "Negative prompt: agregar \"blurry, watermark, low quality\" y comparar.",
      "ControlNet Canny: extraer Canny de una foto, generar variante manteniendo estructura.",
      "LoRA estilo: cargar un LoRA de estilo (CivitAI), aplicar. Variar cross_attention_kwargs={'scale': 0.8}."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/160-stable-diffusion-xl-controlnet/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/161-rl-aprendizaje-por-recompensa-openai-gymnasium",
    "number": 161,
    "slug": "161-rl-aprendizaje-por-recompensa-openai-gymnasium",
    "partSlug": "parte-2-deep-learning",
    "title": "RL: aprendizaje por recompensa, Gymnasium (Farama)",
    "description": "Entender el paradigma de Reinforcement Learning — un agente interactúa con un environment, observa states, toma actions, recibe rewards, y aprende una policy que maximiza recompensa acumulada.",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Entender el paradigma de Reinforcement Learning — un agente interactúa con un environment, observa states, toma actions, recibe rewards, y aprende una policy que maximiza recompensa acumulada. Conocer Gymnasium (Farama Foundation, fork del antiguo OpenAI Gym que dejó de mantenerse en 2022) — la librería estándar de environments para benchmarks. > Nota: el nombre \"OpenAI Gym\" es histórico. Desde 2022, OpenAI dejó de mantenerlo y la Farama Foundation tomó el relevo creando Gymnasium — drop-in replacement con mejor mantenimiento.",
    "outcomes": [
      "Definir los 5 componentes RL: agent, environment, state, action, reward.",
      "Usar gymnasium: env = gym.make('CartPole-v1'); obs, _ = env.reset(); obs, reward, terminated, truncated, info = env.step(action).",
      "Implementar un policy random como baseline.",
      "Reconocer la diferencia entre on-policy (PPO, A2C) y off-policy (DQN, SAC).",
      "Saber dónde RL es apropiado (juegos, robótica, navegación) vs donde no (clasificación, regresión típicas)."
    ],
    "topics": [
      "Bloque básico: state → action → reward → next_state.",
      "Episodic vs continuous tasks.",
      "Discrete vs continuous action spaces.",
      "Discount factor γ: balance entre recompensa inmediata y futura.",
      "Gymnasium API estándar (reset, step).",
      "Environments populares: CartPole, MountainCar, Atari, MuJoCo, BipedalWalker."
    ],
    "materials": [
      "gymnasium library (pip install gymnasium).",
      "Environments built-in: CartPole-v1, LunarLander-v3, MountainCar-v0.",
      "Librerías: gymnasium, numpy, matplotlib."
    ],
    "exercises": [
      "Entorno básico: env = gym.make('CartPole-v1', render_mode='human'). Correr 10 episodios con acciones random; reportar duración promedio.",
      "Estructura del state: imprimir env.observation_space y env.action_space para CartPole, MountainCar, LunarLander.",
      "Policy heurística: para CartPole, action = 0 if pole_angle < 0 else 1 (push opuesto al tilt). Comparar contra random.",
      "Return discounted: calcular G_t = Σ γ^k r_{t+k} con γ=0.99 sobre un episodio.",
      "Render: usar render_mode='rgb_array' y guardar frames para crear un gif."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/161-rl-aprendizaje-por-recompensa-openai-gymnasium/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/162-policy-gradients",
    "number": 162,
    "slug": "162-policy-gradients",
    "partSlug": "parte-2-deep-learning",
    "title": "Policy gradients",
    "description": "Implementar policy gradient —REINFORCE (Williams 1992)—: parametrizar la policy con una red neuronal π_θ(a|s), optimizar directamente la expected return via gradiente.",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Implementar policy gradient —REINFORCE (Williams 1992)—: parametrizar la policy con una red neuronal π_θ(a|s), optimizar directamente la expected return via gradiente. Es el método más simple de RL que usa redes y la base conceptual de PPO/A2C/A3C (clase 138).",
    "outcomes": [
      "Definir la policy como red state → softmax(actions).",
      "Calcular el gradiente REINFORCE: ∇θ J = E[∇θ log π_θ(a|s) · G_t].",
      "Implementar el training loop: rollout → calcular returns → gradient ascent.",
      "Aplicar baseline (substraer V(s) de G_t) para reducir varianza.",
      "Reconocer la limitación: alta varianza, lento (motiva A2C/PPO)."
    ],
    "topics": [
      "Expected return J(θ) = E_π[G].",
      "Policy gradient theorem: ∇θ J = E[∇θ log π · Q].",
      "REINFORCE algorithm: rollout completo + apply gradient.",
      "Baseline para reducir varianza.",
      "Discounted returns con γ."
    ],
    "materials": [
      "CartPole-v1.",
      "Librerías: gymnasium, tensorflow, keras."
    ],
    "exercises": [
      "Policy network: Dense(32) → Dense(32) → Dense(2, softmax) para CartPole.",
      "Rollout: ejecutar 1 episodio, guardar (s, a, r) por timestep.",
      "Returns: calcular G_t para cada timestep con γ=0.99.",
      "Gradient step: loss = -Σ log π(a_t|s_t) · G_t; backward; apply.",
      "Con baseline: agregar V(s) head, restar de G antes del gradient."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/162-policy-gradients/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/163-markov-decision-processes",
    "number": 163,
    "slug": "163-markov-decision-processes",
    "partSlug": "parte-2-deep-learning",
    "title": "Markov Decision Processes",
    "description": "Formalizar el marco teórico de RL: un Markov Decision Process (MDP) = tupla (S, A, P, R, γ).",
    "level": "Avanzado",
    "duration": "60 min",
    "theory": "Formalizar el marco teórico de RL: un Markov Decision Process (MDP) = tupla (S, A, P, R, γ). Conocer la Bellman equation que define V y Q óptimos, y los algoritmos clásicos Value Iteration y Policy Iteration que los resuelven (cuando el MDP es conocido).",
    "outcomes": [
      "Definir un MDP: states, actions, transition prob, reward function, discount.",
      "Escribir la Bellman equation para V: V(s) = max_a Σ P(s'|s,a)[R + γ V*(s')].",
      "Implementar Value Iteration: actualizar iterativamente hasta convergencia.",
      "Implementar Policy Iteration: alternar policy evaluation + policy improvement.",
      "Reconocer la limitación: requiere conocer P y R (no aplicable a entornos reales) → motivó model-free (Q-learning, clase 137)."
    ],
    "topics": [
      "Propiedad de Markov: P(s_{t+1} | s_t, a_t) = P(s_{t+1} | s_t, a_t, s_{t-1}, ...).",
      "Componentes MDP.",
      "Bellman optimality equation.",
      "Value Iteration (synchronous update).",
      "Policy Iteration (alternar eval + improve).",
      "Convergencia garantizada (contractive operator)."
    ],
    "materials": [
      "MDPs sintéticos chicos (FrozenLake, Taxi de Gymnasium).",
      "Librerías: gymnasium, numpy."
    ],
    "exercises": [
      "MDP de juguete: definir un MDP de 4 estados con P, R manualmente.",
      "Value Iteration: implementar V[s] = max_a Σ P(s'|s,a)(R + γ V[s']) hasta max change < 1e-6.",
      "Policy Iteration: alternar evaluación (V^π) con mejora (π' = greedy(V)) hasta estabilidad.",
      "FrozenLake: cargar gym.make('FrozenLake-v1'), extraer env.unwrapped.P (modelo del MDP), resolver con VI.",
      "Compare: # iteraciones VI vs PI para llegar a misma policy."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/163-markov-decision-processes/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/164-td-learning-q-learning-deep-q-networks",
    "number": 164,
    "slug": "164-td-learning-q-learning-deep-q-networks",
    "partSlug": "parte-2-deep-learning",
    "title": "TD Learning, Q-Learning, Deep Q-Networks",
    "description": "Implementar Q-Learning clásico (Watkins 1989) y su versión moderna DQN (Mnih et al.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Implementar Q-Learning clásico (Watkins 1989) y su versión moderna DQN (Mnih et al. 2015, Nature paper que aprendió Atari desde pixels). Off-policy, model-free, bootstrap. Conocer los 2 trucos que hicieron a DQN funcionar: experience replay y target network.",
    "outcomes": [
      "Explicar la update Q-learning: Q(s,a) ← Q(s,a) + α[r + γ max_a' Q(s',a') - Q(s,a)].",
      "Implementar Q-learning tabular en FrozenLake.",
      "Construir un DQN: red state → Q(a) para todas las actions, MSE entre Q predicted y r + γ max_a' Q'(s',a').",
      "Implementar replay buffer (almacenar transitions, samplear batch para training).",
      "Implementar target network (copia frozen actualizada cada N steps)."
    ],
    "topics": [
      "TD (Temporal Difference) error: δ = r + γ V(s') - V(s).",
      "Q-learning: off-policy, sigue greedy de Q*.",
      "ε-greedy exploration: con prob ε explora random, sino greedy.",
      "Replay buffer: deque de (s, a, r, s', done).",
      "Target network: estabilidad (sino, target se mueve mientras estimás).",
      "DQN sobre CartPole y Atari."
    ],
    "materials": [
      "FrozenLake (tabular).",
      "CartPole (DQN).",
      "Librerías: gymnasium, tensorflow, keras, numpy."
    ],
    "exercises": [
      "Q-learning tabular: en FrozenLake, mantener Q[s, a] numpy array. Update con ε-greedy. Reportar success rate tras 5000 episodios.",
      "DQN básico: red Dense(64) → Dense(64) → Dense(2) para CartPole. Sin replay buffer ni target network → ver inestabilidad.",
      "Replay buffer: from collections import deque; buffer = deque(maxlen=10_000). Sample batch=32 random.",
      "Target network: copiar Q.weights cada 100 steps a Q_target.",
      "ε decay: empezar ε=1.0, decaer linealmente a 0.01 en 10 000 steps."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/164-td-learning-q-learning-deep-q-networks/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/165-rl-moderno-a3c-ppo-sac-vista-general",
    "number": 165,
    "slug": "165-rl-moderno-a3c-ppo-sac-vista-general",
    "partSlug": "parte-2-deep-learning",
    "title": "RL moderno: A3C, PPO, SAC (vista general)",
    "description": "Vista general (sin implementación desde cero) de los 3 algoritmos modernos de RL: A3C (Asynchronous Advantage Actor-Critic), PPO (Proximal Policy Optimization — el default industrial), y SAC (Soft Actor-Critic — off-pol…",
    "level": "Avanzado",
    "duration": "65 min",
    "theory": "Vista general (sin implementación desde cero) de los 3 algoritmos modernos de RL: A3C (Asynchronous Advantage Actor-Critic), PPO (Proximal Policy Optimization — el default industrial), y SAC (Soft Actor-Critic — off-policy, continuous actions). Saber cuál elegir y cómo usarlos con Stable-Baselines3.",
    "outcomes": [
      "Diferenciar on-policy (A3C, PPO) de off-policy (SAC, DQN).",
      "Reconocer la idea de Actor-Critic: dos redes — actor (policy) + critic (value).",
      "Entender el clipped objective de PPO: limita updates a [1-ε, 1+ε] veces el old policy → estabilidad.",
      "Usar Stable-Baselines3: PPO('MlpPolicy', env).learn(total_timesteps=100_000).",
      "Elegir: PPO para discreto/continuo, on-policy. SAC para continuo, off-policy, sample-efficient."
    ],
    "topics": [
      "Actor-Critic: actor da policy, critic da V(s). Advantage = G - V(s).",
      "A3C: async + advantage actor-critic. Paralelización con multiples workers.",
      "A2C: variante sincrónica (más simple).",
      "PPO: clipped surrogate objective.",
      "SAC: actor-critic off-policy + entropy regularization.",
      "Stable-Baselines3 como librería estándar."
    ],
    "materials": [
      "LunarLander, CartPole, Pendulum.",
      "Librerías: gymnasium, stable-baselines3 (pip install stable-baselines3[extra])."
    ],
    "exercises": [
      "PPO con SB3: from stable_baselines3 import PPO; model = PPO('MlpPolicy', 'CartPole-v1', verbose=1); model.learn(50_000). Evaluar.",
      "SAC en Pendulum: SAC('MlpPolicy', 'Pendulum-v1').learn(20_000).",
      "Comparar: PPO vs SAC en LunarLander; reportar return y sample efficiency.",
      "TensorBoard: PPO(..., tensorboard_log='./tb/') y ver curvas.",
      "Custom callback: EvalCallback para evaluar cada N steps y guardar mejor modelo."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/165-rl-moderno-a3c-ppo-sac-vista-general/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/166-tf-serving-grpc",
    "number": 166,
    "slug": "166-tf-serving-grpc",
    "partSlug": "parte-2-deep-learning",
    "title": "TF Serving + gRPC (+ ONNX, TensorRT, vLLM/TGI)",
    "description": "Servir un modelo entrenado a producción.",
    "level": "Avanzado",
    "duration": "100 min",
    "theory": "Servir un modelo entrenado a producción. Aprender TF Serving (oficial de TensorFlow, gRPC/REST, batching) y las alternativas modernas multi-framework: ONNX + ONNX Runtime (portable a cualquier framework / runtime), TensorRT (NVIDIA, máxima velocidad en GPU NVIDIA), y para LLMs: vLLM y TGI (Text Generation Inference) — específicos del caso autoregresivo con continuous batching.",
    "outcomes": [
      "Exportar un modelo Keras a SavedModel: model.save('servable/1/', save_format='tf').",
      "Levantar TF Serving con Docker: docker run -p 8501:8501 -v $PWD/servable:/models/m tensorflow/serving --model_name=m.",
      "Hacer requests REST/gRPC.",
      "Exportar a ONNX con tf2onnx / torch.onnx.export, servir con ONNX Runtime.",
      "Conocer cuándo usar TensorRT (latencia mínima en GPU NVIDIA) o vLLM/TGI (LLMs)."
    ],
    "topics": [
      "SavedModel format (TF nativo).",
      "TF Serving: configuración, versioning, model warm-up, batching.",
      "gRPC vs REST: gRPC más rápido (binary protobuf); REST más simple.",
      "Complemento moderno: ONNX/ONNX Runtime, TensorRT, vLLM/TGI."
    ],
    "materials": [
      "Un modelo ya entrenado de las clases previas (Fashion-MNIST MLP).",
      "Librerías: tensorflow, tensorflow-serving-api, tf2onnx, onnxruntime, opcional tensorrt."
    ],
    "exercises": [
      "Export SavedModel: model.export('servable/1/') (Keras 3). Inspeccionar la estructura assets, variables, saved_model.pb.",
      "TF Serving con Docker: levantar el container con el modelo montado, hacer una request REST a localhost:8501/v1/models/m:predict.",
      "ONNX export: convertir el TF model a ONNX con tf2onnx. Cargar con ONNX Runtime y verificar misma predicción.",
      "vLLM: levantar vllm con mistralai/Mistral-7B-Instruct. Cliente OpenAI-style. Medir tokens/sec.",
      "Latencia comparada: TF Serving REST vs gRPC vs ONNX Runtime CPU vs TensorRT GPU sobre el mismo modelo. Reportar latencia P50 y P99."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/166-tf-serving-grpc/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/167-onnx-onnx-runtime-portabilidad",
    "number": 167,
    "slug": "167-onnx-onnx-runtime-portabilidad",
    "partSlug": "parte-2-deep-learning",
    "title": "ONNX y ONNX Runtime: portabilidad e inference optimizada",
    "description": "Dominar ONNX (formato intermedio) y ONNX Runtime (runtime cross-platform) — la solución portable para inference: entrenás en TF/PyTorch/JAX, exportás a ONNX, corrés en cualquier hardware (CPU, GPU NVIDIA, GPU AMD, mobil…",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Dominar ONNX (formato intermedio) y ONNX Runtime (runtime cross-platform) — la solución portable para inference: entrenás en TF/PyTorch/JAX, exportás a ONNX, corrés en cualquier hardware (CPU, GPU NVIDIA, GPU AMD, mobile, browser, edge). Conocer TensorRT (NVIDIA-specific, mayor performance).",
    "outcomes": [
      "Exportar modelos: torch.onnx.export, tf2onnx.convert.",
      "Cargar e inferir con onnxruntime.InferenceSession.",
      "Elegir execution provider: CPU, CUDA, TensorRT, OpenVINO, DirectML, CoreML.",
      "Optimizar modelos: graph optimization, quantization int8/fp16.",
      "Reconocer cuándo ONNX vs TF Serving vs vLLM (LLMs)."
    ],
    "topics": [
      "ONNX como protocolo (protobuf): operator set + tensor types.",
      "Conversión: cada framework tiene su exporter.",
      "Verificación: outputs deben coincidir framework ↔ ONNX (±1e-5).",
      "Optimization: graph simplification, layer fusion.",
      "Quantization: dynamic, static (con calibration), QAT.",
      "Execution providers: priority order."
    ],
    "materials": [
      "Modelo de clases anteriores (Fashion-MNIST o ResNet preentrenado).",
      "Librerías: onnx, onnxruntime o onnxruntime-gpu, tf2onnx (TF), torch.onnx built-in."
    ],
    "exercises": [
      "PyTorch → ONNX: torch.onnx.export(model, dummy_input, 'model.onnx', opset_version=17, input_names=['input'], output_names=['output']).",
      "TF → ONNX: python -m tf2onnx.convert --saved-model dir/ --output model.onnx --opset 17.",
      "Inference: sess = ort.InferenceSession('model.onnx', providers=['CUDAExecutionProvider', 'CPUExecutionProvider']). Verificar outputs.",
      "Graph optimization: sess_options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL.",
      "Quantization: onnxruntime.quantization.quantize_dynamic('model.onnx', 'model_q.onnx', weight_type=QuantType.QUInt8)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/167-onnx-onnx-runtime-portabilidad/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/168-despliegue-en-vertex-ai",
    "number": 168,
    "slug": "168-despliegue-en-vertex-ai",
    "partSlug": "parte-2-deep-learning",
    "title": "Despliegue en Vertex AI",
    "description": "Desplegar un modelo a Vertex AI (GCP) — el servicio managed de Google para servir modelos sin maintener infrastructure.",
    "level": "Avanzado",
    "duration": "60 min",
    "theory": "Desplegar un modelo a Vertex AI (GCP) — el servicio managed de Google para servir modelos sin maintener infrastructure. Conocer alternativas: AWS SageMaker, Azure ML, Modal, Replicate, HuggingFace Inference Endpoints.",
    "outcomes": [
      "Subir un modelo a Vertex AI Model Registry.",
      "Crear un Endpoint y deployar el modelo.",
      "Hacer requests a un endpoint Vertex AI.",
      "Comparar managed (Vertex/SageMaker) vs self-hosted (TF Serving + GKE/EKS).",
      "Conocer alternativas modernas (Modal, Replicate) para deploy serverless."
    ],
    "topics": [
      "Vertex AI Model Registry.",
      "Endpoint creation + traffic split (A/B testing).",
      "gcloud CLI: gcloud ai models upload, gcloud ai endpoints deploy-model.",
      "Pricing: pay per CPU/GPU hour + requests.",
      "Alternativas: SageMaker, Azure ML, Modal, Replicate."
    ],
    "materials": [
      "Modelo de clases previas exportado.",
      "GCP account con billing habilitado (free tier limitado).",
      "Librerías: google-cloud-aiplatform."
    ],
    "exercises": [
      "Setup: gcloud init, gcloud auth application-default login. Crear bucket GCS.",
      "Upload model: gcloud ai models upload --display-name=fashion --container-image-uri=....",
      "Deploy endpoint: con n1-standard-4. Min/max replicas 1-3.",
      "Predict request: from google.cloud import aiplatform; ep = aiplatform.Endpoint(...); ep.predict(...).",
      "A/B traffic: deploy v2 con 20 % traffic, observar logs."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/168-despliegue-en-vertex-ai/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/169-tf-lite-mobile-embedded",
    "number": 169,
    "slug": "169-tf-lite-mobile-embedded",
    "partSlug": "parte-2-deep-learning",
    "title": "TF Lite (mobile/embedded)",
    "description": "Convertir y desplegar un modelo a TensorFlow Lite (LiteRT) — runtime optimizado para móviles (Android/iOS), IoT y embedded (Raspberry Pi, microcontroladores).",
    "level": "Avanzado",
    "duration": "55 min",
    "theory": "Convertir y desplegar un modelo a TensorFlow Lite (LiteRT) — runtime optimizado para móviles (Android/iOS), IoT y embedded (Raspberry Pi, microcontroladores). Aplicar quantization (int8) para reducir tamaño 4× y acelerar 2-4× en CPU móvil. > Nota: TF Lite fue renombrado a LiteRT en 2024 (mismo proyecto, nuevo branding bajo el paraguas de \"AI Edge\").",
    "outcomes": [
      "Convertir SavedModel a .tflite: converter = tf.lite.TFLiteConverter.from_saved_model('servable/1/'); tflite_model = converter.convert().",
      "Aplicar quantization post-training (dynamic range, int8 full).",
      "Cargar y ejecutar inference con tf.lite.Interpreter.",
      "Conocer alternativas modernas: ONNX Runtime Mobile, CoreML (iOS), NNAPI (Android).",
      "Reconocer trade-off accuracy vs tamaño/velocidad."
    ],
    "topics": [
      "TF Lite vs TF: subset de ops, runtime minimal.",
      "Conversión SavedModel → tflite.",
      "Quantization types: dynamic range (weights int8), int8 full (weights + activations), float16.",
      "tf.lite.Interpreter API.",
      "Mobile delegates: NNAPI, GPU, CoreML."
    ],
    "materials": [
      "Modelo Fashion-MNIST.",
      "Librerías: tensorflow."
    ],
    "exercises": [
      "Convert: TFLiteConverter.from_saved_model(...).convert() → guardar .tflite. Comparar tamaño vs SavedModel.",
      "Inference: cargar .tflite y hacer predict con Interpreter. Verificar misma predicción que el modelo original.",
      "Dynamic range quant: converter.optimizations = [tf.lite.Optimize.DEFAULT]. Tamaño 4× menor.",
      "Full int8: definir representative_dataset y converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]. Comparar tamaño y accuracy.",
      "Latencia: medir tiempo de inference en CPU laptop. Comparar versión float32 vs int8."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/169-tf-lite-mobile-embedded/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/170-tensorflow-js-navegador",
    "number": 170,
    "slug": "170-tensorflow-js-navegador",
    "partSlug": "parte-2-deep-learning",
    "title": "TensorFlow.js (navegador)",
    "description": "Servir modelos directamente en el navegador con TensorFlow.js — corre client-side (privacidad, sin server cost, sin latency network).",
    "level": "Avanzado",
    "duration": "55 min",
    "theory": "Servir modelos directamente en el navegador con TensorFlow.js — corre client-side (privacidad, sin server cost, sin latency network). Alternativas modernas: ONNX Runtime Web, WebGPU-accelerated inference, transformers.js (Hugging Face) para LLMs en el browser.",
    "outcomes": [
      "Convertir un Keras model a TF.js format con tensorflowjs_converter.",
      "Cargar y hacer inference desde JavaScript en el browser.",
      "Conocer WebGL backend (default TF.js) y WebGPU (nuevo, más rápido).",
      "Usar transformers.js para correr modelos NLP/visión en browser.",
      "Reconocer cuándo conviene client-side vs server-side."
    ],
    "topics": [
      "Conversion: tensorflowjs_converter --input_format=keras model.keras tfjs_model/.",
      "JS API: const model = await tf.loadLayersModel('tfjs_model/model.json').",
      "Backends: WebGL (default), WASM, WebGPU.",
      "transformers.js: ONNX en browser, soporta BERT, GPT-2, Whisper.",
      "Edge cases: tamaño del modelo (~5-50 MB ideal), latencia primer load."
    ],
    "materials": [
      "Modelo Fashion-MNIST.",
      "Librerías: tensorflowjs, tensorflowjs-converter."
    ],
    "exercises": [
      "Convert: tensorflowjs_converter --input_format=keras_saved_model servable/ tfjs_model/. Inspeccionar archivos.",
      "HTML page: pagina simple que carga model.json, dibuja una imagen 28×28 en canvas, predice.",
      "WebGPU: await tf.setBackend('webgpu'). Comparar velocidad vs WebGL.",
      "transformers.js: import { pipeline } from '@xenova/transformers'. Correr sentiment-analysis en browser. 1 línea.",
      "PWA: empaquetar como Progressive Web App con service worker para offline inference."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/170-tensorflow-js-navegador/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/171-aceleracion-con-gpu",
    "number": 171,
    "slug": "171-aceleracion-con-gpu",
    "partSlug": "parte-2-deep-learning",
    "title": "Aceleración con GPU",
    "description": "Configurar GPU para DL: drivers, CUDA, cuDNN, verificación.",
    "level": "Avanzado",
    "duration": "60 min",
    "theory": "Configurar GPU para DL: drivers, CUDA, cuDNN, verificación. Conocer mixed precision (bfloat16/float16) que duplica throughput en GPUs modernas (Ampere/Hopper). Profilear con TensorBoard Profiler para identificar bottlenecks (data loading vs compute vs sync).",
    "outcomes": [
      "Verificar GPU: tf.config.list_physical_devices('GPU'), torch.cuda.is_available().",
      "Activar mixed precision: keras.mixed_precision.set_global_policy('mixed_float16') (Volta+) o 'mixed_bfloat16' (Ampere+).",
      "Limitar memoria GPU: set_memory_growth(True) para no consumir toda al inicio.",
      "Multi-GPU básico con tf.distribute.MirroredStrategy (clase 144 profundiza).",
      "Profilear con TensorBoard Profiler."
    ],
    "topics": [
      "CUDA toolkit + cuDNN versions matching.",
      "nvidia-smi para monitor.",
      "Mixed precision: float16 (Volta+, 16 GB max) vs bfloat16 (Ampere+, mismo exponente que float32, más estable).",
      "Memory growth vs allocated all.",
      "Profiling con TensorBoard.",
      "GPUs típicos en 2026: H100, H200 (server); RTX 5090 (consumer)."
    ],
    "materials": [
      "Modelo + dataset cualquier de las clases previas.",
      "Librerías: tensorflow, opcional nvidia-smi."
    ],
    "exercises": [
      "GPU check: imprimir tf.config.list_physical_devices('GPU'), tf.config.list_logical_devices('GPU'), nvidia-smi.",
      "Memory growth: tf.config.experimental.set_memory_growth(gpu, True) para evitar reservar 100 % al inicio.",
      "Mixed precision: keras.mixed_precision.set_global_policy('mixed_float16'). Re-entrenar modelo. Verificar speedup (1.5-2× en V100; 2-3× en A100/H100).",
      "Profile: keras.callbacks.TensorBoard(log_dir=..., profile_batch=(5, 10)). Abrir Profiler tab.",
      "Bottleneck: si la GPU está al 30 %, el bottleneck es data loading. Optimizar pipeline (clase 109)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/171-aceleracion-con-gpu/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/172-entrenamiento-multi-dispositivo-tf-distribute",
    "number": 172,
    "slug": "172-entrenamiento-multi-dispositivo-tf-distribute",
    "partSlug": "parte-2-deep-learning",
    "title": "Entrenamiento multi-dispositivo, tf.distribute",
    "description": "Escalar el training a múltiples GPUs (y multi-nodos).",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Escalar el training a múltiples GPUs (y multi-nodos). Conocer las 3 estrategias TF: MirroredStrategy (1 nodo, varias GPUs), MultiWorkerMirroredStrategy (varios nodos), TPUStrategy. Conocer equivalentes PyTorch (DDP, FSDP) que son estándar para LLMs grandes.",
    "outcomes": [
      "Aplicar MirroredStrategy en un único nodo con N GPUs.",
      "Entender data parallelism: cada GPU procesa su mini-batch, gradients se promedian (all-reduce).",
      "Diferenciar de model parallelism (modelo dividido entre GPUs) y pipeline parallelism.",
      "Conocer FSDP (Fully Sharded Data Parallel) para modelos demasiado grandes para 1 GPU (LLMs).",
      "Saber que PyTorch Lightning abstrae todo esto cambiando un kwarg."
    ],
    "topics": [
      "Data parallelism: misma red replicada, distinto batch por GPU.",
      "Model parallelism: red dividida (tensor parallel, pipeline parallel).",
      "FSDP / DeepSpeed ZeRO: shard de parámetros, gradientes, optimizer states.",
      "TF: MirroredStrategy, MultiWorkerMirroredStrategy, TPUStrategy.",
      "PyTorch: DistributedDataParallel, FullyShardedDataParallel, DeepSpeed.",
      "Lightning / Accelerate: abstracciones de alto nivel."
    ],
    "materials": [
      "Acceso a ≥ 2 GPUs (Colab Pro+, cloud).",
      "Librerías: tensorflow, opcional torch.distributed."
    ],
    "exercises": [
      "MirroredStrategy: strategy = tf.distribute.MirroredStrategy(). with strategy.scope(): model = build_model(); model.compile(...). Entrenar.",
      "Batch effective: si tenés 4 GPUs y batch_size=32, el batch global es 128. Adjust LR (LR scales linearly with batch).",
      "Gradient accumulation: simular batch=512 acumulando 4 mini-batches de 128. Manual con custom training loop.",
      "PyTorch DDP: comando torchrun --nproc_per_node=4 train.py con DistributedDataParallel(model).",
      "PyTorch Lightning: trainer = L.Trainer(strategy='ddp', devices=4). Listo."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/172-entrenamiento-multi-dispositivo-tf-distribute/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/173-jax-flax-fundamentos",
    "number": 173,
    "slug": "173-jax-flax-fundamentos",
    "partSlug": "parte-2-deep-learning",
    "title": "JAX y Flax: el stack moderno de Google para DL",
    "description": "Aprender JAX (Google 2018) y Flax (NN library on top of JAX) — el stack que sostiene AlphaFold, Gemini, MaxText, AlphaCode y muchos modelos modernos.",
    "level": "Avanzado",
    "duration": "85 min",
    "theory": "Aprender JAX (Google 2018) y Flax (NN library on top of JAX) — el stack que sostiene AlphaFold, Gemini, MaxText, AlphaCode y muchos modelos modernos. Cubrir jit, vmap, pmap, grad, transformaciones funcionales, y Flax NNX (la nueva API 2024, similar a PyTorch).",
    "outcomes": [
      "Diferenciar JAX (NumPy + autodiff + XLA) de NumPy plano.",
      "Usar jax.jit para compilación XLA (2-10× speedup automático).",
      "Aplicar jax.vmap (vectorización automática) y jax.grad (autodiff funcional).",
      "Construir modelos con Flax NNX (API moderna similar a PyTorch).",
      "Reconocer cuándo elegir JAX sobre PyTorch (TPU, escala extrema, research)."
    ],
    "topics": [
      "Functional programming: funciones puras, no mutación.",
      "jit, grad, vmap, pmap como transformaciones.",
      "XLA: compilación a hardware específico (CPU, GPU, TPU).",
      "PRNG explícito (jax.random.PRNGKey).",
      "Flax: NN library. Antes Linen (functional), ahora NNX (stateful, más parecido a PyTorch).",
      "Optax: optimizadores."
    ],
    "materials": [
      "Fashion-MNIST.",
      "Librerías: jax, jaxlib, flax, optax."
    ],
    "exercises": [
      "JAX basic: import jax.numpy as jnp; x = jnp.array([1.,2.,3.]); jnp.sum(x**2). Comparar contra NumPy.",
      "grad: grad_f = jax.grad(lambda x: x**3); grad_f(2.) → 12.",
      "jit speedup: definir función numérica, medir tiempo con y sin @jax.jit. ≥ 5× speedup.",
      "vmap: función para una muestra → vmap para procesar batch.",
      "Flax NNX MLP: definir modelo, training step, entrenar Fashion-MNIST."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/173-jax-flax-fundamentos/notebook.ipynb"
  },
  {
    "id": "parte-2-deep-learning/174-entrenamiento-a-escala-con-vertex-ai",
    "number": 174,
    "slug": "174-entrenamiento-a-escala-con-vertex-ai",
    "partSlug": "parte-2-deep-learning",
    "title": "Entrenamiento a escala con Vertex AI",
    "description": "Cierre del bloque de despliegue: lanzar training jobs a escala en Vertex AI (GCP managed) — cluster automático, GPUs/TPUs on-demand, hyperparameter tuning distribuido.",
    "level": "Avanzado",
    "duration": "65 min",
    "theory": "Cierre del bloque de despliegue: lanzar training jobs a escala en Vertex AI (GCP managed) — cluster automático, GPUs/TPUs on-demand, hyperparameter tuning distribuido. Conocer alternativas: AWS SageMaker Training, Azure ML Jobs, y plataformas dedicadas a LLMs (Modal, Together AI).",
    "outcomes": [
      "Empaquetar un training script como Docker container.",
      "Lanzar un Custom Training Job en Vertex AI con gcloud ai custom-jobs create.",
      "Configurar HP tuning con Vertex AI Vizier.",
      "Usar TPU Pods para training distribuido extremo.",
      "Conocer alternativas cloud-agnostic (Modal, Together, RunPod)."
    ],
    "topics": [
      "Custom container vs prebuilt container en Vertex.",
      "WorkerPoolSpec: master + workers + parameter servers.",
      "TPU pods para training a escala.",
      "Hyperparameter tuning con Vizier (Bayesian search).",
      "Costos: GPU/TPU hours.",
      "Alternativas: SageMaker, Modal, Together, RunPod, Lambda Labs."
    ],
    "materials": [
      "GCP account.",
      "Librerías: google-cloud-aiplatform."
    ],
    "exercises": [
      "Dockerize: escribir Dockerfile con TF + tu training script.",
      "Lanzar job: aiplatform.CustomJob(display_name='exp1', worker_pool_specs=[...]).run().",
      "HP tuning: HyperparameterTuningJob con Vizier; 20 trials.",
      "Multi-GPU spec: machine_type='a2-highgpu-4g' (4× A100).",
      "TensorBoard integration: Vertex TB para monitor."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-2-deep-learning/174-entrenamiento-a-escala-con-vertex-ai/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/175-distribuciones-normal-binomial-poisson-exponencial",
    "number": 175,
    "slug": "175-distribuciones-normal-binomial-poisson-exponencial",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Distribuciones: normal, binomial, Poisson, exponencial",
    "description": "Reconocer las cuatro distribuciones de probabilidad que aparecen en el 90 % de los problemas reales de data science —normal, binomial, Poisson, exponencial— sabiendo qué fenómeno modela cada una, cuáles son sus parámetr…",
    "level": "Intermedio-Avanzado",
    "duration": "70 min",
    "theory": "Reconocer las cuatro distribuciones de probabilidad que aparecen en el 90 % de los problemas reales de data science —normal, binomial, Poisson, exponencial— sabiendo qué fenómeno modela cada una, cuáles son sus parámetros, cómo simularlas con scipy.stats / numpy.random, y cómo verificar empíricamente si los datos realmente siguen esa distribución antes de aplicar un test que la asuma.",
    "outcomes": [
      "Identificar la distribución apropiada para un fenómeno descrito en lenguaje natural (conteos raros → Poisson, éxitos/fracasos → binomial, tiempos entre eventos → exponencial, sumas/promedios → normal por TCL).",
      "Calcular media, varianza y cuantiles teóricos con scipy.stats.{norm, binom, poisson, expon} (.mean(), .var(), .ppf(), .pdf()/.pmf()).",
      "Simular muestras con rng = np.random.default_rng(seed) y comparar histograma vs PDF/PMF teórica.",
      "Aplicar un Q-Q plot (scipy.stats.probplot) y un Kolmogorov-Smirnov (scipy.stats.kstest) para validar normalidad.",
      "Reconocer cuándo el Teorema Central del Límite justifica usar normal aunque los datos crudos no lo sean."
    ],
    "topics": [
      "Distribución normal N(μ, σ²)",
      "Distribución binomial Bin(n, p)",
      "Distribución de Poisson Poi(λ)",
      "Distribución exponencial Exp(λ)",
      "Teorema Central del Límite (TCL)",
      "Verificación empírica: Q-Q plot + KS test"
    ],
    "materials": [
      "Conteo de llamados a un call center por hora (sintético): rng.poisson(lam=4.2, size=10_000) → Poisson.",
      "Datos reales: seaborn.load_dataset('tips') para chequear normalidad de total_bill (no es normal, asimétrico positivo — buen contraejemplo).",
      "Librerías: numpy, scipy.stats, matplotlib, seaborn."
    ],
    "exercises": [
      "Simulación y PDF/PMF: con rng = np.random.default_rng(42), generá 10 000 muestras de cada una de las 4 distribuciones con parámetros razonables. Para cada una: histograma con density=True superpuesto con la PDF/PMF teórica de scipy.stats.",
      "Cuantiles: calculá scipy.stats.norm(loc=100, scale=15).ppf([0.025, 0.5, 0.975]) (IQ test → IC 95 % poblacional) y verificá que el 2.5 % y 97.5 % muestrales de una simulación con n=100_000 se acerquen.",
      "TCL en acción: tomá Exp(λ=1) (claramente no normal). Generá 5 000 promedios de tamaños n ∈ {1, 5, 30, 100} y graficá los 4 histogramas lado a lado. Verificá cómo se va volviendo simétrico y campaniforme.",
      "Q-Q plot: scipy.stats.probplot(tips.total_bill, dist='norm', plot=plt). Anotá qué muestra el extremo derecho (asimetría positiva → cola larga arriba de la diagonal).",
      "¿Poisson o no?: con los conteos por hora del dataset sintético, calculá mean() y var(). Si var/mean ∈ [0.8, 1.2], equidispersión → Poisson plausible. Probá con lam=4.2 (deberías ver ratio ≈ 1) y con datos contaminados (mezclá con rng.poisson(20, size=200) para ver overdispersión)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/175-distribuciones-normal-binomial-poisson-exponencial/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/176-test-t-una-muestra-dos-muestras-pareado",
    "number": 176,
    "slug": "176-test-t-una-muestra-dos-muestras-pareado",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Test t (una muestra, dos muestras, pareado)",
    "description": "Que el alumno aplique correctamente las tres variantes del test t —una muestra, dos muestras independientes (Welch por default), pareado—, distinga hipótesis nula y alternativa, lea p-value e intervalo de confianza de l…",
    "level": "Intermedio-Avanzado",
    "duration": "80 min",
    "theory": "Que el alumno aplique correctamente las tres variantes del test t —una muestra, dos muestras independientes (Welch por default), pareado—, distinga hipótesis nula y alternativa, lea p-value e intervalo de confianza de la salida de scipy.stats y pingouin, y aprenda a reportar effect size (Cohen's d, Hedges' g) junto con el p-value para no caer en la trampa de \"significativo pero irrelevante\".",
    "outcomes": [
      "Formular H₀ y H₁ (bilateral / unilateral) para un problema concreto y elegir la variante correcta del test t.",
      "Ejecutar scipy.stats.ttest_1samp, ttest_ind(equal_var=False) y ttest_rel, interpretando el statistic, pvalue y el atributo .confidence_interval() (scipy ≥ 1.10).",
      "Verificar supuestos: normalidad por grupo (Shapiro / Q-Q plot) o invocar TCL si n ≥ 30.",
      "Decidir entre test bilateral vs unilateral sin caer en p-hacking (la dirección debe estar fijada antes de mirar los datos).",
      "Reportar effect size: Cohen's d, Hedges' g corregido para muestras chicas, y su interpretación cualitativa (small/medium/large)."
    ],
    "topics": [
      "H₀ / H₁, errores tipo I (α) y tipo II (β).",
      "Test t de una muestra: t = (x̄ - μ₀) / (s/√n), gl = n - 1.",
      "Test t de dos muestras independientes: Welch (varianzas distintas, default moderno) vs Student (varianzas iguales — supuesto fuerte, casi nunca correcto).",
      "Test t pareado (mismo sujeto antes/después).",
      "p-value: probabilidad bajo H₀ de observar algo al menos tan extremo. NO es P(H₀ | datos).",
      "Intervalo de confianza al 95 % como complemento del p-value.",
      "Complemento moderno: effect size (Cohen's d, Hedges' g, Cliff's δ) — la pregunta \"¿es relevante?\" que el p-value no responde."
    ],
    "materials": [
      "seaborn.load_dataset('tips'): comparar tip entre sex='Male' vs 'Female', o time='Lunch' vs 'Dinner'.",
      "Para pareado: simular un dataset antes/después con numpy.random.default_rng (presión arterial pre/post fármaco).",
      "Librerías: scipy.stats, pingouin (pip install pingouin), seaborn."
    ],
    "exercises": [
      "Una muestra: con tips.total_bill, testá H₀: μ = 20 vs H₁: μ ≠ 20 con scipy.stats.ttest_1samp(tips.total_bill, popmean=20). Reportá t, p y el IC95 % (.confidence_interval()).",
      "Dos muestras (Welch): testá si tip difiere entre sex='Male' y sex='Female' con ttest_ind(equal_var=False). Calculá Cohen's d a mano y verificá contra pingouin.ttest.",
      "Pareado: simulá presión arterial antes/después de un fármaco con rng = np.random.default_rng(0): antes = rng.normal(140, 12, 30), despues = antes - rng.normal(5, 3, 30). Aplicá ttest_rel(antes, despues) y comparalo contra hacer ttest_ind mal (verás cómo el pareado tiene mucho más poder).",
      "Bilateral vs unilateral: para el ejercicio 2, repetí con alternative='greater' y 'less'. Observá cómo el p-value se divide ≈ 2.",
      "Significativo vs relevante: generá grupo_a = rng.normal(100, 15, 10_000) y grupo_b = rng.normal(100.5, 15, 10_000). El test va a dar p < 0.001; calculá Cohen's d y discutí en 2 líneas por qué el resultado \"no importa\"."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/176-test-t-una-muestra-dos-muestras-pareado/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/177-effect-size-cohen-d-hedges-g-cliff-delta-pingouin",
    "number": 177,
    "slug": "177-effect-size-cohen-d-hedges-g-cliff-delta-pingouin",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Effect size dedicado: Cohen's d, Hedges' g, Cliff's δ con pingouin",
    "description": "Dominar effect size —la métrica que el p-value no responde: \"cuán grande es la diferencia\"—.",
    "level": "Intermedio-Avanzado",
    "duration": "75 min",
    "theory": "Dominar effect size —la métrica que el p-value no responde: \"cuán grande es la diferencia\"—. Cubrir 6 medidas: Cohen's d (means, varianzas similares), Hedges' g (bias-corrected para n chico), Glass's Δ (varianza del control como denominador), Cliff's δ (no paramétrico), r de correlación, odds ratio. Aplicar con pingouin en una sola llamada. Reportar correctamente: APA 7 lo exige.",
    "outcomes": [
      "Calcular Cohen's d a mano y con pingouin.compute_effsize.",
      "Aplicar la corrección de Hedges (recomendada cuando n < 50/grupo).",
      "Interpretar magnitudes (Cohen 1988): 0.2 / 0.5 / 0.8 = small / medium / large.",
      "Calcular Cliff's δ para datos ordinales / muy asimétricos.",
      "Reportar effect size con IC95 % bootstrap.",
      "Diseñar tabla APA-7 con mean ± SD, Cohen's d [95% CI], t, p."
    ],
    "topics": [
      "Cohen's d: (x̄₁ - x̄₂) / s_pooled.",
      "Hedges' g: d · (1 - 3/(4·gl - 1)).",
      "Glass's Δ: usar s_control como denominator. Útil cuando control y treatment tienen varianza distinta.",
      "Cliff's δ: probabilistic dominance.",
      "Effect size para correlación: r (= Pearson) o R².",
      "Effect size para chi-cuadrado: Cramér's V, phi.",
      "IC95 % de effect size: bootstrap o fórmulas paramétricas."
    ],
    "materials": [
      "seaborn.load_dataset('tips').",
      "Librerías: pingouin, scipy.stats, numpy."
    ],
    "exercises": [
      "Cohen's d a mano: para tip por sex, calcular manualmente con s_pooled.",
      "pingouin.compute_effsize: verificar contra cálculo manual. Probar eftype='cohen' | 'hedges' | 'glass' | 'CLES'.",
      "Hedges' g: con n=10 por grupo, ver diferencia entre d y g (Hedges < d).",
      "Cliff's δ: para datos Likert ordinales o muy asimétricos, calcular y interpretar.",
      "Effect size + IC: bootstrap del Cohen's d → IC95 %."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/177-effect-size-cohen-d-hedges-g-cliff-delta-pingouin/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/178-test-chi-cuadrado-de-independencia-y-bondad-de-ajuste",
    "number": 178,
    "slug": "178-test-chi-cuadrado-de-independencia-y-bondad-de-ajuste",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Test chi-cuadrado de independencia y bondad de ajuste",
    "description": "Aplicar el test chi-cuadrado de Pearson en sus dos formas: (a) independencia en una tabla de contingencia de dos variables categóricas, y (b) bondad de ajuste entre una distribución observada y una teórica.",
    "level": "Intermedio-Avanzado",
    "duration": "70 min",
    "theory": "Aplicar el test chi-cuadrado de Pearson en sus dos formas: (a) independencia en una tabla de contingencia de dos variables categóricas, y (b) bondad de ajuste entre una distribución observada y una teórica. Reconocer cuándo el test es válido (frecuencias esperadas ≥ 5 por celda) y cuándo hay que recurrir a Fisher exact o a la simulación de Monte Carlo.",
    "outcomes": [
      "Construir una tabla de contingencia con pd.crosstab y aplicar scipy.stats.chi2_contingency interpretando chi2, dof, pvalue y expected.",
      "Verificar el supuesto de frecuencias esperadas mínimas (regla de Cochran: ≥ 5 en ≥ 80 % de celdas).",
      "Decidir entre chi-cuadrado, Fisher exact (scipy.stats.fisher_exact, tablas 2×2 con conteos chicos) y chi-cuadrado con simulación (lambda_='log-likelihood' o montecarlo).",
      "Calcular Cramér's V como effect size para tablas r×c (análogo al Cohen's d categórico).",
      "Aplicar bondad de ajuste con scipy.stats.chisquare para validar dados, ruedas de roulette o conteos en bins."
    ],
    "topics": [
      "Tablas de contingencia",
      "Estadístico χ² = Σ (O - E)² / E",
      "Grados de libertad (r-1)·(c-1)",
      "Supuesto de E ≥ 5 (Cochran)",
      "Fisher exact para 2×2 con n chico",
      "Cramér's V",
      "Bondad de ajuste vs independencia"
    ],
    "materials": [
      "seaborn.load_dataset('titanic'): cruzar survived × class o survived × sex.",
      "seaborn.load_dataset('tips'): smoker × day.",
      "Bondad de ajuste: simular tiradas de un dado posiblemente cargado y testear contra distribución uniforme.",
      "Librerías: pandas, scipy.stats, pingouin (que tiene pg.chi2_independence con Cramér's V incluido)."
    ],
    "exercises": [
      "Tabla cruzada: pd.crosstab(titanic.survived, titanic['class']). Aplicá chi2, p, dof, expected = scipy.stats.chi2_contingency(tabla). Reportá los cuatro valores e interpretá.",
      "Effect size: calculá Cramér's V manualmente: V = sqrt(chi2 / (n * min(r-1, c-1))). Verificá contra pingouin.chi2_independence(titanic, x='survived', y='class').",
      "Cochran check: imprimí la matriz expected y contá cuántas celdas tienen E < 5. Si supera el 20 %, recalculá con chi2_contingency(tabla, lambda_='log-likelihood') (G-test, mejor para celdas chicas).",
      "Fisher exact (2×2): tomá la subtabla survived × sex y aplicá scipy.stats.fisher_exact(tabla_2x2). Comparalo con chi-cuadrado.",
      "Bondad de ajuste: simulá rng = np.random.default_rng(7); tiros = rng.choice([1,2,3,4,5,6], size=600, p=[0.18, 0.16, 0.17, 0.17, 0.16, 0.16]). Hipótesis: el dado es justo (p uniforme). Aplicá scipy.stats.chisquare(observado, f_exp=esperado) con esperado = [100]*6. ¿Rechazás H₀?"
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/178-test-chi-cuadrado-de-independencia-y-bondad-de-ajuste/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/179-anova-one-way-two-way",
    "number": 179,
    "slug": "179-anova-one-way-two-way",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "ANOVA (one-way, two-way)",
    "description": "Que el alumno aplique ANOVA de una vía (≥ 3 grupos, una variable categórica) y ANOVA de dos vías (dos factores categóricos + interacción), entienda por qué no se hacen \"t-tests todos contra todos\" (inflación de α) y sep…",
    "level": "Intermedio-Avanzado",
    "duration": "80 min",
    "theory": "Que el alumno aplique ANOVA de una vía (≥ 3 grupos, una variable categórica) y ANOVA de dos vías (dos factores categóricos + interacción), entienda por qué no se hacen \"t-tests todos contra todos\" (inflación de α) y sepa hacer post-hoc con Tukey HSD. Reconocer los supuestos (independencia, normalidad por grupo, homogeneidad de varianzas) y cuándo usar la alternativa robusta Welch ANOVA o el no paramétrico Kruskal-Wallis (Clase 150).",
    "outcomes": [
      "Plantear H₀: μ₁ = μ₂ = ... = μ_k vs H₁: al menos uno difiere y aplicar scipy.stats.f_oneway o pingouin.anova.",
      "Interpretar F = MS_between / MS_within y su relación con la F-distribution (F(k-1, n-k)).",
      "Aplicar Welch's ANOVA (pingouin.welch_anova) cuando se viola la homogeneidad de varianzas (Levene rechaza).",
      "Hacer Tukey HSD post-hoc con pingouin.pairwise_tukey y leer los IC ajustados.",
      "Distinguir efectos principales de interacción en ANOVA two-way y graficar interaction plots con seaborn.pointplot.",
      "Reportar η² o ω² como effect size de ANOVA."
    ],
    "topics": [
      "¿Por qué no t-tests múltiples? Si hacés 10 t-tests al α=0.05, la probabilidad de al menos un falso positivo es ≈ 40 %.",
      "Descomposición de varianza: SS_total = SS_between + SS_within.",
      "F-statistic: razón entre varianza explicada por los grupos y varianza residual.",
      "Supuestos: independencia, normalidad (Shapiro por grupo o residuos), homocedasticidad (Levene/Bartlett).",
      "Welch ANOVA — análogo a Welch's t-test para ≥ 3 grupos.",
      "Post-hoc: Tukey HSD (controla family-wise error rate), Bonferroni, Holm.",
      "Two-way ANOVA: efectos principales A, B, e interacción A×B.",
      "Effect size: η² (eta-squared), ω² (omega-squared, menos sesgado)."
    ],
    "materials": [
      "seaborn.load_dataset('tips'): total_bill por day (one-way), o por day × time (two-way).",
      "seaborn.load_dataset('penguins'): body_mass_g por species (one-way claro).",
      "Librerías: scipy.stats, pingouin, statsmodels.api as sm, statsmodels.formula.api as smf."
    ],
    "exercises": [
      "One-way: aplicá scipy.stats.f_oneway(*[grupo for grupo in penguins.groupby('species').body_mass_g]). Reportá F, p y dof_between, dof_within.",
      "Supuestos: testá normalidad por grupo (pingouin.normality(penguins, dv='body_mass_g', group='species')) y homocedasticidad (pingouin.homoscedasticity). Si Levene rechaza, repetí con pingouin.welch_anova.",
      "Post-hoc Tukey: pingouin.pairwise_tukey(data=penguins, dv='body_mass_g', between='species'). Identificá qué pares de especies difieren significativamente.",
      "Two-way con interacción: pingouin.anova(data=tips, dv='total_bill', between=['day', 'time']). Mirá las tres filas de la tabla (day, time, day×time).",
      "Interaction plot: sns.pointplot(data=tips, x='day', y='total_bill', hue='time'). Si las líneas se cruzan o no son paralelas → hay interacción visual; cruzala con el p-value del término day*time."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/179-anova-one-way-two-way/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/180-tests-no-parametricos-mann-whitney-wilcoxon-kruskal-wallis",
    "number": 180,
    "slug": "180-tests-no-parametricos-mann-whitney-wilcoxon-kruskal-wallis",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Tests no paramétricos: Mann-Whitney, Wilcoxon, Kruskal-Wallis",
    "description": "Aplicar las tres alternativas no paramétricas más usadas: Mann-Whitney U (= dos muestras independientes, análogo a Welch's t), Wilcoxon signed-rank (= pareado, análogo a ttest_rel) y Kruskal-Wallis (= ≥ 3 grupos, análog…",
    "level": "Intermedio-Avanzado",
    "duration": "70 min",
    "theory": "Aplicar las tres alternativas no paramétricas más usadas: Mann-Whitney U (= dos muestras independientes, análogo a Welch's t), Wilcoxon signed-rank (= pareado, análogo a ttest_rel) y Kruskal-Wallis (= ≥ 3 grupos, análogo a ANOVA one-way). Saber cuándo elegirlos sobre los paramétricos: muestras chicas con datos visiblemente asimétricos, datos ordinales (Likert, ranks), o presencia de outliers extremos.",
    "outcomes": [
      "Reconocer las 3 situaciones en que un test no paramétrico es preferible al paramétrico (n chico + asimetría, ordinal, outliers).",
      "Aplicar scipy.stats.mannwhitneyu, wilcoxon, kruskal con los argumentos correctos (alternative, method='exact' vs 'asymptotic').",
      "Interpretar que los no paramétricos testean distribuciones (estocásticamente iguales) o medianas, no medias.",
      "Reportar effect size no paramétrico: rank-biserial correlation (Mann-Whitney) o ε² / η²_H (Kruskal-Wallis).",
      "Hacer post-hoc no paramétrico tras Kruskal con Dunn's test (scikit-posthocs) y corrección por múltiples comparaciones."
    ],
    "topics": [
      "Mann-Whitney U (Wilcoxon rank-sum)",
      "Wilcoxon signed-rank",
      "Kruskal-Wallis H",
      "Dunn's test (post-hoc)",
      "Cliff's δ / rank-biserial r"
    ],
    "materials": [
      "seaborn.load_dataset('tips'): tip por sex o day.",
      "Datos con outliers: precios de Airbnb (Kaggle) — cola larga a la derecha por mansiones.",
      "Likert ordinal: simular respuestas 1–5 con rng.choice([1,2,3,4,5], p=...).",
      "Librerías: scipy.stats, pingouin, scikit-posthocs (pip install scikit-posthocs)."
    ],
    "exercises": [
      "Mann-Whitney: comparar tip entre sex con scipy.stats.mannwhitneyu(a, b, alternative='two-sided'). Compará el p con el del t-test del ejercicio 2 de la Clase 147. Calculá rank-biserial r.",
      "Wilcoxon signed-rank: con el dataset simulado de presión arterial antes/después de la Clase 147, aplicá scipy.stats.wilcoxon(antes, despues). Verificá supuesto de simetría con un histograma de las diferencias.",
      "Outliers: a un dataset normal rng.normal(50, 5, 100) agregale 3 outliers de valor 200. Compará Welch's t-test vs Mann-Whitney contra otro grupo normal — el Mann-Whitney es mucho más robusto.",
      "Kruskal-Wallis: aplicalo a body_mass_g por species en penguins. Comparalo con el ANOVA de la Clase 149.",
      "Post-hoc Dunn: con scikit_posthocs.posthoc_dunn(penguins, val_col='body_mass_g', group_col='species', p_adjust='holm') identificá qué pares difieren."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/180-tests-no-parametricos-mann-whitney-wilcoxon-kruskal-wallis/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/181-correccion-de-comparaciones-multiples-bonferroni-fdr",
    "number": 181,
    "slug": "181-correccion-de-comparaciones-multiples-bonferroni-fdr",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Corrección de comparaciones múltiples (Bonferroni, FDR)",
    "description": "Entender por qué hacer 100 tests al α=0.05 produce ≈ 5 falsos positivos esperados aunque todas las H₀ sean verdaderas, y aplicar las dos familias de corrección: family-wise error rate (FWER) con Bonferroni y Holm, y fal…",
    "level": "Intermedio-Avanzado",
    "duration": "70 min",
    "theory": "Entender por qué hacer 100 tests al α=0.05 produce ≈ 5 falsos positivos esperados aunque todas las H₀ sean verdaderas, y aplicar las dos familias de corrección: family-wise error rate (FWER) con Bonferroni y Holm, y false discovery rate (FDR) con Benjamini-Hochberg (BH). Saber elegir entre ambas según el contexto (medicina/seguridad → FWER; screening exploratorio → FDR).",
    "outcomes": [
      "Cuantificar la inflación de α al hacer k tests independientes: 1 - (1-α)^k.",
      "Aplicar Bonferroni: α_corregido = α / m. Conservador pero simple.",
      "Aplicar Holm-Bonferroni (statsmodels.stats.multitest.multipletests(..., method='holm')) — uniformemente más poderoso que Bonferroni.",
      "Aplicar Benjamini-Hochberg (BH/FDR) y entender que controla la proporción esperada de falsos positivos entre los rechazos, no el FWER.",
      "Distinguir FWER (P[al menos 1 falso positivo] ≤ α) de FDR (E[V/R] ≤ q, donde V son falsos positivos y R rechazos totales).",
      "Reportar p-values ajustados (q-values) y umbrales claros."
    ],
    "topics": [
      "El problema: si m=20 tests independientes con H₀ verdadera y α=0.05, P(al menos uno rechaza) = 1 - 0.95²⁰ ≈ 64 %.",
      "FWER: probabilidad de al menos 1 falso positivo en toda la familia.",
      "FDR: proporción esperada de falsos positivos entre los rechazos (no entre todos los tests).",
      "Bonferroni: rechazar si p_i ≤ α/m. Controla FWER exactamente.",
      "Holm: ordenar p-values y comparar p_(i) ≤ α/(m-i+1). Uniformemente más poderoso que Bonferroni.",
      "Benjamini-Hochberg (BH): ordenar p_(1) ≤ ... ≤ p_(m); rechazar todos los p_(i) tales que p_(i) ≤ (i/m)·q. Controla FDR a nivel q.",
      "Cuándo usar cada uno: FWER si un falso positivo es catastrófico (drug approval, security). FDR si esperás muchos descubrimientos verdaderos y querés tolerar algunos falsos (genómica, A/B testing masivo)."
    ],
    "materials": [
      "Genómica sintética: simular m=1000 tests, m₀=950 nulos verdaderos y m₁=50 alternativos. Generar p-values y mostrar comportamiento de cada método.",
      "A/B testing real: 20 métricas testeadas a la vez → controlar familia.",
      "Librerías: statsmodels.stats.multitest, pingouin.multicomp, scipy.stats."
    ],
    "exercises": [
      "Inflación de α: simulá 10 000 experimentos. En cada uno, hacé 20 tests con H₀ verdadera (scipy.stats.ttest_ind entre dos grupos N(0,1), n=30). Contá en qué % al menos 1 da p<0.05. Verificá que ≈ 64 %.",
      "Bonferroni: con un vector pvals de 20 p-values, calculá pvals_adj = np.minimum(pvals * 20, 1) y compará contra multipletests(pvals, method='bonferroni').",
      "Holm: multipletests(pvals, alpha=0.05, method='holm'). Comparar cuántos rechaza vs Bonferroni con el mismo vector.",
      "BH/FDR: genera 1000 p-values, 950 de Uniform(0,1) y 50 de Beta(0.5, 5) (concentrados cerca de 0 — alternativos). Aplicá multipletests(pvals, alpha=0.05, method='fdr_bh'). Contá cuántos rechaza y estimá el FDR empírico (rechazos del primer grupo / total rechazos).",
      "Comparación: mismo vector del ej. 4, aplicar Bonferroni, Holm y BH. Tabla con: # rechazos, % de los 50 verdaderos descubiertos (recall), FDR empírico. Verificá que BH descubre mucho más con FDR controlado."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/181-correccion-de-comparaciones-multiples-bonferroni-fdr/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/182-intervalos-de-confianza",
    "number": 182,
    "slug": "182-intervalos-de-confianza",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Intervalos de confianza",
    "description": "Construir e interpretar correctamente intervalos de confianza para media (t-based, z-based, bootstrap) y proporción (Wald, Wilson, Clopper-Pearson), entendiendo que un IC95 % NO significa \"95 % de probabilidad de que el…",
    "level": "Intermedio-Avanzado",
    "duration": "70 min",
    "theory": "Construir e interpretar correctamente intervalos de confianza para media (t-based, z-based, bootstrap) y proporción (Wald, Wilson, Clopper-Pearson), entendiendo que un IC95 % NO significa \"95 % de probabilidad de que el parámetro caiga en el intervalo\" sino \"si repitiéramos el experimento muchas veces, el 95 % de los intervalos construidos contendrían el parámetro\". Saber elegir el método según n y la métrica.",
    "outcomes": [
      "Construir un IC para la media usando la distribución t: x̄ ± t_{α/2, n-1} · (s/√n) con scipy.stats.t.interval.",
      "Construir un IC para la proporción con tres métodos y entender cuándo cada uno falla (Wald falla con p cerca de 0/1; Wilson y Clopper-Pearson son robustos).",
      "Usar scipy.stats.bootstrap (≥ 1.7) para IC sin supuestos paramétricos (anticipa Clase 153).",
      "Interpretar correctamente la frase \"intervalo de confianza al 95 %\" (es una propiedad del procedimiento, no del intervalo específico).",
      "Relacionar IC y test de hipótesis: si el IC95 % de la diferencia no incluye 0, el test bilateral al α=5 % rechaza H₀."
    ],
    "topics": [
      "IC para la media (varianza desconocida): t de Student con n-1 gl.",
      "IC para la media (varianza conocida o n grande): z.",
      "IC para proporción: Wald (p̂ ± z·√(p̂(1-p̂)/n)) vs Wilson score (recomendado por Agresti & Coull 1998) vs Clopper-Pearson (exacto, conservador).",
      "IC bootstrap percentil (anticipa Clase 153).",
      "IC del odds ratio, riesgo relativo (medicina/epidemiología).",
      "Margen de error (ME = z·SE) y cómo determina n."
    ],
    "materials": [
      "seaborn.load_dataset('tips'): IC de la propina media.",
      "Encuesta sintética: simular n=500 respuestas binarias con p=0.03 (proporción chica → Wald falla).",
      "Librerías: scipy.stats, statsmodels.stats.proportion, pingouin."
    ],
    "exercises": [
      "IC t para la media: con tips.total_bill, calculá el IC95 % con scipy.stats.t.interval(0.95, n-1, loc=mean, scale=sem). Verificá contra pingouin.compute_bootci.",
      "IC para proporción extrema: con rng.binomial(1, 0.03, 100) (proporción de eventos raros), calculá IC con statsmodels.stats.proportion.proportion_confint(count, n, method='normal') (Wald), 'wilson' y 'beta' (Clopper-Pearson). Observá cómo Wald da límite inferior negativo (¡imposible!) y los otros dos no.",
      "Cobertura empírica: simulá 5 000 muestras de tamaño 30 de N(50, 10). Para cada una, construí IC95 % t. Contá qué % contiene μ=50. Debería ser ≈ 95 %.",
      "Bootstrap IC: con tips.total_bill, aplicá scipy.stats.bootstrap((tips.total_bill,), statistic=np.mean, n_resamples=10_000, method='percentile'). Compará con el IC t.",
      "Sample size: querés estimar una proporción con margen de error de ±2 %, asumiendo p̂ ≈ 0.5 (peor caso). Calculá el n requerido para 95 % de confianza."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/182-intervalos-de-confianza/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/183-bootstrap-y-permutation-tests",
    "number": 183,
    "slug": "183-bootstrap-y-permutation-tests",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Bootstrap y permutation tests",
    "description": "Sustituir los supuestos paramétricos (normalidad, homocedasticidad, fórmulas cerradas) por resampling: el bootstrap estima la distribución muestral de cualquier estadístico re-muestreando con reemplazo, y los permutatio…",
    "level": "Intermedio-Avanzado",
    "duration": "85 min",
    "theory": "Sustituir los supuestos paramétricos (normalidad, homocedasticidad, fórmulas cerradas) por resampling: el bootstrap estima la distribución muestral de cualquier estadístico re-muestreando con reemplazo, y los permutation tests calculan un p-value re-mezclando etiquetas de tratamiento. Aprender a usar las APIs modernas de scipy (bootstrap, permutation_test, ≥ 1.9) y a interpretar las tres variantes de IC bootstrap (percentil, basic, BCa).",
    "outcomes": [
      "Implementar bootstrap a mano: B resamples con reemplazo del mismo tamaño que la muestra original, calcular el estadístico en cada uno, sacar cuantiles α/2 y 1-α/2.",
      "Usar scipy.stats.bootstrap(data, statistic, n_resamples=9_999, method='BCa') y entender por qué BCa corrige sesgo y asimetría.",
      "Diseñar un permutation test bilateral con scipy.stats.permutation_test((a, b), statistic, n_resamples=10_000, alternative='two-sided').",
      "Saber cuándo usar bootstrap (IC de estadísticos no estándar: mediana, R², AUC) vs permutación (p-value de comparación entre grupos sin supuestos).",
      "Reconocer las limitaciones del bootstrap (muestra muy chica n<20, dependencia temporal — usar block bootstrap)."
    ],
    "topics": [
      "Intuición del bootstrap: \"tratá la muestra como si fuera la población y resampleá\".",
      "Tres intervalos bootstrap: percentile, basic (reflejado), BCa (bias-corrected + accelerated).",
      "¿Cuántos resamples? B = 10_000 para IC95 % (los percentiles 2.5 y 97.5 se estabilizan).",
      "Permutation test: intercambiar etiquetas de tratamiento bajo H₀ de \"no diferencia\".",
      "Diferencia conceptual: bootstrap estima variabilidad del estadístico; permutación produce un p-value exacto condicional a los datos.",
      "Block bootstrap para series temporales (preserva autocorrelación).",
      "Complemento moderno: APIs scipy.stats.bootstrap y permutation_test desde scipy 1.9, vectorizadas y con BCa por default."
    ],
    "materials": [
      "seaborn.load_dataset('diamonds'): bootstrap del mediana del precio por cut.",
      "Modelos: AUC de un clasificador entrenado — IC bootstrap sobre la AUC en test.",
      "Librerías: scipy.stats (≥ 1.9), numpy, sklearn."
    ],
    "exercises": [
      "Bootstrap a mano: para tips.tip, hacé B=10_000 resamples con rng.choice(x, size=len(x), replace=True), calculá la media, sacá los cuantiles 2.5 y 97.5. Verificá contra scipy.stats.bootstrap(..., method='percentile').",
      "BCa vs percentile: con datos lognormales rng.lognormal(0, 1, 50), calculá IC de la mediana con method='percentile' y con method='BCa'. Comprobá que BCa es asimétrico hacia la cola derecha (refleja la asimetría real).",
      "IC para AUC: entrenar un LogisticRegression en breast cancer, calcular AUC en test. Bootstrap n_resamples=2_000 sobre (y_true_test, y_proba_test) con un statistic que devuelva roc_auc_score. Reportar IC95 % BCa.",
      "Permutation test bilateral: con tips.tip por sex, ejecutá scipy.stats.permutation_test y comparalo con el mannwhitneyu de la Clase 150.",
      "Cobertura: simulá 1 000 datasets de Exp(1) con n=25. Para cada uno, calculá IC95 % de la mediana con BCa y con percentile. Contá la cobertura empírica. BCa debería estar más cerca de 95 % que percentile."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/183-bootstrap-y-permutation-tests/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/184-bca-bootstrap-scipy-permutation-test-moderno",
    "number": 184,
    "slug": "184-bca-bootstrap-scipy-permutation-test-moderno",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "BCa bootstrap y APIs modernas de scipy",
    "description": "Profundizar el BCa (Bias-Corrected and accelerated) bootstrap —el default moderno (Efron 1987)— y las APIs modernas de scipy (scipy.stats.bootstrap ≥ 1.9, scipy.stats.permutation_test ≥ 1.8).",
    "level": "Intermedio-Avanzado",
    "duration": "75 min",
    "theory": "Profundizar el BCa (Bias-Corrected and accelerated) bootstrap —el default moderno (Efron 1987)— y las APIs modernas de scipy (scipy.stats.bootstrap ≥ 1.9, scipy.stats.permutation_test ≥ 1.8). Cubrir las correcciones que BCa hace sobre percentile clásico: bias correction (z₀) y acceleration (a) vía jackknife.",
    "outcomes": [
      "Diferenciar bootstrap percentile vs basic vs BCa.",
      "Calcular z₀ (bias correction) y a (acceleration) manualmente.",
      "Aplicar scipy.stats.bootstrap((data,), statistic, method='BCa', n_resamples=10_000).",
      "Aplicar permutation_test para p-value de comparación de 2 grupos sin paramétrica.",
      "Reconocer cuándo BCa importa: estadísticos no lineales, distribuciones asimétricas."
    ],
    "topics": [
      "Percentile bootstrap: cuantiles directos. Sub-cubre con asimetría.",
      "Basic bootstrap: reflexión 2θ̂ - q_{1-α/2}.",
      "BCa: corrige bias (z₀) y aceleración (a vía jackknife).",
      "Studentized bootstrap: estandariza con SE bootstrap del SE.",
      "Scipy.stats.bootstrap API.",
      "Permutation test exacto."
    ],
    "materials": [
      "Datos lognormales sintéticos.",
      "seaborn.load_dataset('diamonds') para mediana de price.",
      "Librerías: scipy.stats, numpy, matplotlib."
    ],
    "exercises": [
      "Tres ICs: para mediana de x = rng.lognormal(0, 1, 100), calcular IC con percentile, basic, BCa. Comparar.",
      "z₀ a mano: implementar z₀ = ppf((B_below_θ̂) / B). Verificar contra scipy.",
      "a con jackknife: implementar leave-one-out para cada θ̂_(i). Calcular a.",
      "Cobertura empírica: 1000 datasets Exp(1), n=25; cobertura percentile vs BCa. BCa más cerca de 95 %.",
      "Permutation_test: comparar dos lognormales con tamaño efecto chico. P-value exacto."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/184-bca-bootstrap-scipy-permutation-test-moderno/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/185-a-b-testing-tamano-de-muestra-poder-estadistico",
    "number": 185,
    "slug": "185-a-b-testing-tamano-de-muestra-poder-estadistico",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "A/B testing: tamaño de muestra, poder estadístico",
    "description": "Diseñar y analizar un A/B test end-to-end: definir hipótesis y métrica primaria, calcular tamaño de muestra con el poder estadístico deseado, randomizar correctamente, analizar resultados sin peeking y reportar con effe…",
    "level": "Intermedio-Avanzado",
    "duration": "90 min",
    "theory": "Diseñar y analizar un A/B test end-to-end: definir hipótesis y métrica primaria, calcular tamaño de muestra con el poder estadístico deseado, randomizar correctamente, analizar resultados sin peeking y reportar con effect size + IC. Conocer tres herramientas modernas que reducen muestra requerida o eliminan el problema de peeking: CUPED, sequential testing (always-valid p-values) y A/B bayesiano.",
    "outcomes": [
      "Calcular n requerido con statsmodels.stats.power.TTestIndPower o NormalIndPower para una MDE (minimum detectable effect) dada, α y poder.",
      "Implementar el análisis: t-test (continua) o z-test de proporciones (binaria), con effect size + IC95 %.",
      "Identificar y evitar 5 errores clásicos: peeking, p-hacking, no estratificación, SRM (sample ratio mismatch), Simpson's paradox.",
      "Aplicar CUPED para reducir varianza usando una covariable pre-experimento.",
      "Diseñar un test secuencial con always-valid p-values (Howard et al. 2021) o GST (group sequential testing) que permita parar antes sin inflar α.",
      "Comparar A/B clásico (frecuentista) con A/B bayesiano (PyMC o bayesab) y entender ventajas (interpretación directa, parar cuando alcance precisión)."
    ],
    "topics": [
      "Hipótesis nula vs alternativa en A/B; métrica primaria, guardrails (no degradar latencia, error rate).",
      "Poder estadístico: P(rechazar H₀ | H₁ verdadera). Convención: 80 %.",
      "Sample size: depende de α (0.05), poder (0.8), σ y MDE.",
      "Aleatorización a nivel correcto (usuario vs sesión vs request).",
      "Peeking problem: mirar el resultado intermedio e inflar α.",
      "SRM (Sample Ratio Mismatch): si el ratio observado A/B se aleja del esperado 50/50, hay bug de asignación.",
      "Simpson's paradox: la tendencia global se invierte al estratificar.",
      "Complemento moderno: CUPED, sequential testing, A/B bayesiano."
    ],
    "materials": [
      "Simular A/B: rng.binomial(1, 0.10, n) vs rng.binomial(1, 0.12, n) → MDE de 2 pp absoluto.",
      "Para CUPED: simular X (pre) y Y = 0.5*X + ε + δ·tratamiento.",
      "Librerías: statsmodels.stats.power, scipy.stats, confseq, pingouin."
    ],
    "exercises": [
      "Sample size: querés detectar un uplift de tasa de conversión de 10 % → 11 % con poder 0.8 y α=0.05. Usá statsmodels.stats.proportion.samplesize_proportions_2indep_onetail o power.NormalIndPower().solve_power. ¿Cuánto necesitás por grupo?",
      "Análisis clásico: simulá el experimento (n=8 000 por grupo, p_A=0.10, p_B=0.108), aplicá z-test de proporciones, reportá p, IC95 % de la diferencia y poder post-hoc.",
      "CUPED: simulá X = rng.normal(50, 10, 2000) y Y = X + ε + 2·tratamiento con ε ~ N(0,5). Calculá n requerido con y sin CUPED para detectar el efecto de 2.",
      "Peeking simulado: bajo H₀ verdadera, simulá 1 000 experimentos donde \"parás temprano\" si p < 0.05 mirando cada 100 obs hasta 5 000. Mostrá cómo el α real se infla a ≈ 0.25.",
      "A/B bayesiano: con A=(1000, 80), B=(1000, 100), calculá P(p_B > p_A) con priors Beta(1,1). Interpretá."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/185-a-b-testing-tamano-de-muestra-poder-estadistico/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/186-cuped-sequential-testing-always-valid-p-values",
    "number": 186,
    "slug": "186-cuped-sequential-testing-always-valid-p-values",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "CUPED, sequential testing, always-valid p-values",
    "description": "Aplicar las 3 técnicas modernas que la industria (Microsoft, Netflix, Booking, Spotify) usa para hacer A/B testing más eficientemente: CUPED (variance reduction con covariable pre-experiment), Sequential Testing (mirar…",
    "level": "Intermedio-Avanzado",
    "duration": "85 min",
    "theory": "Aplicar las 3 técnicas modernas que la industria (Microsoft, Netflix, Booking, Spotify) usa para hacer A/B testing más eficientemente: CUPED (variance reduction con covariable pre-experiment), Sequential Testing (mirar el resultado durante el experimento sin inflar α), y always-valid p-values / confidence sequences (Howard et al. 2021, decisión correcta en cualquier momento).",
    "outcomes": [
      "Implementar CUPED: ajustar Y_cuped = Y - θ·(X - E[X]) con θ = Cov(Y,X)/Var(X).",
      "Calcular la reducción de varianza esperada: 1 - ρ².",
      "Configurar Group Sequential Testing con O'Brien-Fleming boundaries.",
      "Aplicar always-valid CIs con la librería confseq.",
      "Decidir entre frequentist clásico, GST, y mSPRT según contexto."
    ],
    "topics": [
      "CUPED math: θ óptimo minimiza varianza.",
      "Implementación: con Y_pre (mismo usuario en período previo) o X (covariable).",
      "GST: K looks, boundaries pre-definidas.",
      "O'Brien-Fleming (gasta poco α al principio) vs Pocock (constante).",
      "mSPRT: ratio test que provee p-value válido siempre.",
      "Confidence sequences: IC válido en cualquier t."
    ],
    "materials": [
      "Simulación A/B con numpy.random.default_rng.",
      "Librerías: numpy, scipy, confseq (pip install confseq)."
    ],
    "exercises": [
      "CUPED implementation: simular X_pre, Y_post = α·X_pre + tratamiento + ε. Calcular θ. Comparar Var(Y) vs Var(Y_cuped).",
      "Variance reduction: con ρ=0.7, calcular reducción esperada (= 51 %); verificar con simulación.",
      "Peeking inflado: bajo H₀, simular 1000 experimentos con 5 looks naïve, contar % de rejects. Debería ser ≈ 18 %.",
      "O'Brien-Fleming: implementar boundaries con rpy2 + gsDesign (o aproximación). Verificar α controlled.",
      "Always-valid CI: confseq.bounds.normal_log_mixture_bound sobre stream simulado. Plotear CI a lo largo del tiempo."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/186-cuped-sequential-testing-always-valid-p-values/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/187-diseno-experimental",
    "number": 187,
    "slug": "187-diseno-experimental",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Diseño experimental",
    "description": "Pasar del A/B simple a diseños más ricos: bloques aleatorizados, factorial completo / fraccional, diseños cruzados (cross-over), switchback para experimentos con interferencia, y cluster randomization cuando la unidad d…",
    "level": "Intermedio-Avanzado",
    "duration": "80 min",
    "theory": "Pasar del A/B simple a diseños más ricos: bloques aleatorizados, factorial completo / fraccional, diseños cruzados (cross-over), switchback para experimentos con interferencia, y cluster randomization cuando la unidad de análisis no coincide con la unidad de tratamiento. Saber qué problema resuelve cada diseño y leer las consideraciones de SUTVA (Stable Unit Treatment Value Assumption).",
    "outcomes": [
      "Distinguir diseño completamente aleatorizado (CRD), bloques aleatorizados (RBD), factorial y fraccional 2^(k-p).",
      "Detectar cuándo SUTVA se viola (efectos de red, interferencia entre usuarios, fila/competencia) y aplicar el diseño correcto: cluster randomization, switchback, marketplace experiments.",
      "Diseñar un factorial 2² o 2³ con pyDOE2 / statsmodels y descomponer efectos principales + interacciones.",
      "Saber cuándo usar fraccional (2^(k-p)) para reducir corridas y qué se sacrifica (confounding de interacciones de alto orden).",
      "Aplicar cross-over para experimentos pareados dentro de sujeto, con análisis vía test pareado o modelo mixto."
    ],
    "topics": [
      "CRD: el A/B clásico. Asume SUTVA (no interferencia entre unidades).",
      "RBD (bloques): bloquear por variable nuisance (ej.: día de semana, país) para reducir varianza dentro del bloque.",
      "Factorial 2^k: testear k factores simultáneamente. Captura interacciones; mucho más eficiente que A/B por factor.",
      "Fraccional 2^(k-p): corridas reducidas. Se confunden (\"aliasing\") efectos de alto orden con principales.",
      "Cross-over: cada sujeto recibe ambos tratamientos en períodos distintos. Análisis pareado, controla variabilidad inter-sujeto. Riesgo: carry-over effect.",
      "Cluster randomization: aleatorizar grupos (clases, ciudades) en lugar de individuos cuando hay contaminación social.",
      "Switchback: alternar tratamiento global en bloques de tiempo (típico de marketplaces de dos lados — Uber, DoorDash).",
      "SUTVA: cada unidad solo recibe una versión del tratamiento; los efectos no se propagan entre unidades."
    ],
    "materials": [
      "Sintéticos para factorial 2² (e.g., A=color botón, B=texto botón → CTR).",
      "Iris / penguins para análisis ANOVA tipo factorial.",
      "Librerías: pyDOE2 (pip install pyDOE2), statsmodels.formula.api, pingouin."
    ],
    "exercises": [
      "Factorial 2²: simulá CTR con ctr = 0.10 + 0.02·A + 0.015·B + 0.005·A·B + ε. Hacé el experimento con 1 000 obs por celda. Ajustá ols('ctr ~ A * B', data).fit() y reportá los 4 coeficientes (intercepto, A, B, A:B). Verificá contra el verdadero.",
      "Bloqueo: simulá un experimento de uplift en tasa de retención por país con paises = ['AR','BR','MX'] con baselines distintos (p0 ∈ {0.5, 0.3, 0.4}). Compará: A/B sin estratificar vs bloqueado por país. Mostrá cómo el SE de δ cae con bloqueo.",
      "Fraccional 2^(4-1): usá pyDOE2.fracfact('a b c d') y discutí qué interacciones quedan aliased. ¿Cuántas corridas vs full factorial?",
      "Cluster randomization: simulá 50 escuelas con 30 alumnos c/u, ICC=0.10, efecto verdadero 0.3. Compará t-test ingenuo (n=1500) vs análisis correcto a nivel cluster (n=50). El primero infla α; el segundo es correcto.",
      "Switchback: simulá precio dinámico en una ciudad con bloques de 1 h alternando A y B durante 7 días. Análisis: comparar bloques A vs B con tests pareados por hora-del-día."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/187-diseno-experimental/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/188-inferencia-causal-dags-confounders-instrumentos",
    "number": 188,
    "slug": "188-inferencia-causal-dags-confounders-instrumentos",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Inferencia causal: DAGs, confounders, instrumentos",
    "description": "Distinguir correlación de causalidad con rigor: dibujar DAGs (Directed Acyclic Graphs), identificar confounders, colliders y mediators, aplicar el backdoor criterion para decidir qué variables controlar, y usar variable…",
    "level": "Intermedio-Avanzado",
    "duration": "95 min",
    "theory": "Distinguir correlación de causalidad con rigor: dibujar DAGs (Directed Acyclic Graphs), identificar confounders, colliders y mediators, aplicar el backdoor criterion para decidir qué variables controlar, y usar variables instrumentales (IV) cuando la randomización no es posible. Conocer la herramienta moderna Double Machine Learning (DoubleML / EconML) para estimar ATE/CATE con ML como nuisance estimator.",
    "outcomes": [
      "Dibujar un DAG para un problema de negocio e identificar los tres tipos de estructura: chain (X → M → Y), fork (X ← Z → Y, confounder), collider (X → C ← Y).",
      "Aplicar el backdoor criterion de Pearl: encontrar el conjunto mínimo de variables a controlar para identificar el efecto causal.",
      "Reconocer que controlar por un collider o un mediator introduce sesgo, NO lo elimina.",
      "Estimar ATE (Average Treatment Effect) con regresión + controles, IPW (Inverse Probability Weighting) y matching.",
      "Usar 2SLS (Two-Stage Least Squares) con linearmodels.iv cuando hay un instrumento válido.",
      "Aplicar Double Machine Learning con doubleml / econml para estimar ATE/CATE con ML como nuisance (sin asumir linealidad)."
    ],
    "topics": [
      "Correlación ≠ causalidad: el clásico ejemplo \"helado y ahogamientos\" — confounder: temperatura.",
      "DAGs: nodos = variables, flechas = relación causal.",
      "3 estructuras canónicas: chain, fork, collider.",
      "Backdoor criterion: bloquear todos los caminos no causales de X a Y; no abrir colliders.",
      "ATE = E[Y | do(T=1)] - E[Y | do(T=0)]. El \"do\" indica intervención, no observación.",
      "Identificación: ¿se puede expresar E[Y | do(T)] con datos observacionales? Si sí → estimar.",
      "IV: variable Z que afecta T pero NO a Y excepto vía T. Permite identificar el efecto cuando hay confounders no observados.",
      "Complemento moderno: Double Machine Learning (Chernozhukov et al. 2018) — usa ML para estimar las \"nuisance functions\" y separa la inferencia causal de la complejidad del fit."
    ],
    "materials": [
      "Ejemplos simulados de Pearl: smoking-cancer con tar como mediator.",
      "econml.tests.dgps para datos sintéticos con efectos heterogéneos conocidos.",
      "Lalonde 1986 (NSW job training program) — clásico de causal inference.",
      "Librerías: doubleml, econml, linearmodels, pgmpy (DAG inference), dowhy (Microsoft, framework completo)."
    ],
    "exercises": [
      "DAG en código: con pgmpy (o networkx), definí un DAG con T, Y, Z (confounder), C (collider). Identificá visualmente paths y aplicá dowhy para encontrar el adjustment set.",
      "Sesgo del collider: simulá T ~ N(0,1), Y ~ N(T, 1), C = T + Y + ε. Estimá Y ~ T sin controlar C y controlando C. Mostrá que controlar el collider destruye la relación causal.",
      "Backdoor ajustando confounder: simulá Z, T = f(Z) + ε, Y = 2T + 3Z + δ. OLS Y ~ T sesgado. OLS Y ~ T + Z recupera el 2.",
      "2SLS: simular un IV Z → T → Y con confounder no observado entre T y Y. Aplicar linearmodels.iv.IV2SLS.from_formula('Y ~ 1 + [T ~ Z]', data).fit(). Recuperar el efecto verdadero.",
      "DML con random forest: dataset sintético con confounders no lineales. Comparar OLS ingenuo vs OLS con polinomios vs DoubleMLPLR(ml_g=RF, ml_m=RF). Verificar que DML es el menos sesgado."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/188-inferencia-causal-dags-confounders-instrumentos/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/189-doubleml-econml-ml-para-causalidad",
    "number": 189,
    "slug": "189-doubleml-econml-ml-para-causalidad",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "DoubleML / EconML: Machine Learning para causalidad",
    "description": "Aplicar Double Machine Learning (Chernozhukov 2018) y EconML (Microsoft Research) para estimar ATE y CATE (Conditional ATE — heterogeneidad del efecto) usando cualquier ML como nuisance estimator (Random Forest, XGBoost…",
    "level": "Intermedio-Avanzado",
    "duration": "95 min",
    "theory": "Aplicar Double Machine Learning (Chernozhukov 2018) y EconML (Microsoft Research) para estimar ATE y CATE (Conditional ATE — heterogeneidad del efecto) usando cualquier ML como nuisance estimator (Random Forest, XGBoost, neural net). Inference válida (CI, p-value) sin asumir linearidad de los confounders.",
    "outcomes": [
      "Explicar Neyman-orthogonal score y por qué DML es doubly robust.",
      "Aplicar DoubleMLPLR para ATE con ML nuisance.",
      "Usar CausalForestDML de EconML para CATE personalizado.",
      "Cross-fitting: K-fold para evitar overfitting del nuisance.",
      "Inspeccionar policy óptimo: policy_tree para árbol de decisión de tratamiento."
    ],
    "topics": [
      "Marco PLR (Partially Linear Regression): Y = θT + g(X) + ε, T = m(X) + v.",
      "Score orthogonal: derivada respecto a nuisances = 0 en expectation.",
      "Cross-fitting: estimar nuisances en fold A, evaluar en B.",
      "CATE: efecto por subgroup.",
      "Heterogeneity tests.",
      "Policy learning: decidir a quién tratar."
    ],
    "materials": [
      "Sintético con efectos conocidos (de econml.tests.dgps).",
      "Lalonde 1986 (NSW training program) — clásico.",
      "IHDP (Infant Health and Development).",
      "Librerías: doubleml, econml, scikit-learn, xgboost."
    ],
    "exercises": [
      "Sintético: simular Y = 2·T + 3·X1 + X2² + ε, T = P(...|X). ATE verdadero = 2.",
      "DML básico: DoubleMLPLR(data, ml_g=RF, ml_m=RF, n_folds=5). Reportar θ̂.",
      "Comparar OLS vs DML: OLS lineal con Y ~ T + X1 + X2 sesgado por X2 no lineal. DML lo recupera.",
      "CausalForestDML: con dataset heterogéneo, estimar CATE. Mapa por X1.",
      "Policy tree: econml.policy.PolicyTree para decidir a quién tratar."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/189-doubleml-econml-ml-para-causalidad/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/190-uplift-modeling-did-difference-in-differences",
    "number": 190,
    "slug": "190-uplift-modeling-did-difference-in-differences",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Uplift modeling, DiD (difference-in-differences)",
    "description": "Dominar las dos técnicas causales más usadas en industria cuando hay datos panel/observacionales: DiD (Difference-in-Differences) —comparar la evolución antes/después en grupo tratado vs control— y uplift modeling —pred…",
    "level": "Intermedio-Avanzado",
    "duration": "90 min",
    "theory": "Dominar las dos técnicas causales más usadas en industria cuando hay datos panel/observacionales: DiD (Difference-in-Differences) —comparar la evolución antes/después en grupo tratado vs control— y uplift modeling —predecir a quién conviene tratar (heterogeneidad del efecto causal a nivel individuo). Conocer el complemento moderno Synthetic Control Method para cuando no hay grupo de control natural y solo se trata una unidad (una ciudad, un país).",
    "outcomes": [
      "Aplicar DiD clásico con OLS: Y = β₀ + β₁·tratado + β₂·post + β₃·(tratado×post) + ε. El coeficiente β₃ es el efecto causal bajo parallel trends.",
      "Diagnosticar la asunción de parallel trends con un gráfico antes/después y un placebo test.",
      "Construir modelos de uplift: T-learner, S-learner, X-learner (Künzel et al. 2019), Causal Forest (econml).",
      "Evaluar uplift con Qini curve y uplift@k (no con AUC clásico — uplift es individual, no global).",
      "Aplicar Synthetic Control con pysyncon o SparseSC cuando una sola unidad recibe tratamiento (estudio de caso)."
    ],
    "topics": [
      "DiD: comparación dos-por-dos en panel (2 grupos × 2 tiempos).",
      "Asunción crítica: parallel trends — sin tratamiento, ambos grupos hubieran evolucionado paralelos.",
      "Generalización: DiD con muchos tiempos, two-way fixed effects (TWFE), event study designs.",
      "Uplift = CATE individual = E[Y(1) - Y(0) | X=x].",
      "4 cuadrantes de uplift: persuadables, sure things, lost causes, do-not-disturb (no tocarlos).",
      "Métricas: Qini, uplift@k, AUUC (area under uplift curve).",
      "Complemento moderno: Synthetic Control Method (Abadie et al.) — construye un \"país sintético\" como combinación convexa de unidades no tratadas que replica la trayectoria pre-tratamiento."
    ],
    "materials": [
      "DiD clásico: Card & Krueger 1994 (mínimum wage en NJ vs PA).",
      "Uplift: Hillstrom email dataset (criteo), Lenta uplift dataset.",
      "Synthetic Control: California Prop 99 (smoking) — clásico de Abadie.",
      "Librerías: linearmodels (PanelOLS), econml, causalml (Uber), pysyncon, SparseSC."
    ],
    "exercises": [
      "DiD ingenuo: simulá panel con 2 grupos y 2 períodos. Aplicá DiD con OLS y verificá que β₃ recupera el efecto verdadero. Probá violar parallel trends y ver el sesgo.",
      "Event study: con panel 10 períodos (5 pre, 5 post), graficá coeficientes por período. Si los pre son ≈ 0 → parallel trends plausible.",
      "T-learner: en Hillstrom (binario tratamiento email), entrená dos RandomForestClassifier y predecí uplift = p₁(x) - p₀(x).",
      "Qini curve: con las predicciones del ej. 3, calculá Qini con sklift.metrics.qini_score o a mano. Compará contra \"tratar al azar\".",
      "Synthetic Control: con un dataset panel simulado (10 estados × 20 años, tratamiento en California año 11), ajustá pesos con pysyncon y graficá path_plot + gaps_plot. Aplicá placebo_test."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/190-uplift-modeling-did-difference-in-differences/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/191-synthetic-control-method-pysyncon",
    "number": 191,
    "slug": "191-synthetic-control-method-pysyncon",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Synthetic Control Method dedicado (pysyncon, SparseSC)",
    "description": "Aplicar Synthetic Control Method (Abadie et al.",
    "level": "Intermedio-Avanzado",
    "duration": "80 min",
    "theory": "Aplicar Synthetic Control Method (Abadie et al. 2010) — el estándar para evaluar políticas o intervenciones aplicadas a una única unidad (un país, un estado, una ciudad) sin grupo control natural. Construir un \"control sintético\" como combinación ponderada de donors. Conocer variantes modernas: Synthetic DiD (Arkhangelsky 2021), Generalized SC (Xu 2017), SparseSC (Microsoft Research).",
    "outcomes": [
      "Construir un Synthetic Control con pysyncon: tratado, donors, predictors, períodos pre/post.",
      "Interpretar pesos W (combinación convexa) y path plot.",
      "Aplicar placebo test (in-time y in-space) como inference informal.",
      "Conocer Synthetic DiD que combina lo mejor de DiD y SCM.",
      "Reconocer cuándo SCM no aplica (pocos donors, fit pre malo)."
    ],
    "topics": [
      "Setup: 1 tratado + N donors + features predictoras + período pre/post.",
      "Optimización: pesos minimizan ||Y_treat_pre - W·Y_donors_pre||².",
      "Constraint: w_i ≥ 0, Σ w_i = 1 (combinación convexa) — clásico.",
      "Placebo test in-space: aplicar SCM a cada donor; comparar effect real vs distribución de placebos.",
      "Placebo in-time: aplicar antes del tratamiento real → debería dar 0.",
      "Synthetic DiD: relax constraints + agregar pesos temporales."
    ],
    "materials": [
      "California Prop 99 smoking (Abadie's dataset clásico).",
      "Cualquier panel de países × años con una intervención.",
      "Librerías: pysyncon, SparseSC (Microsoft), numpy, pandas."
    ],
    "exercises": [
      "California Prop 99: cargar dataset, definir tratado California, donors otros estados, pre 1970-1988, post 1989-2000.",
      "Path plot: synth.path_plot() — California real vs sintética. Visualizar gap post-1989.",
      "Pesos: imprimir synth.weights. Verificar que solo few estados tienen peso > 0.",
      "Placebo in-space: aplicar a cada otro estado; plot de gaps. California debe destacar.",
      "Placebo in-time: tratamiento artificial en 1980 (5 años antes del real). Gap debería ser ≈ 0."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/191-synthetic-control-method-pysyncon/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/192-bayes-intro-priors-posterior-mcmc-con-pymc",
    "number": 192,
    "slug": "192-bayes-intro-priors-posterior-mcmc-con-pymc",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Bayes intro: priors, posterior, MCMC con PyMC",
    "description": "Entender la lógica bayesiana —prior + likelihood → posterior vía teorema de Bayes— y construir un modelo simple end-to-end con PyMC v5 (regresión bayesiana sobre datos reales), interpretar el posterior con ArviZ (trace…",
    "level": "Intermedio-Avanzado",
    "duration": "95 min",
    "theory": "Entender la lógica bayesiana —prior + likelihood → posterior vía teorema de Bayes— y construir un modelo simple end-to-end con PyMC v5 (regresión bayesiana sobre datos reales), interpretar el posterior con ArviZ (trace plots, posterior intervals, posterior predictive checks), y conocer el stack moderno: PyMC v5 (post-Theano, sobre PyTensor), NumPyro (sobre JAX, GPU-friendly) y ArviZ (visualización + diagnóstico backend-agnóstico).",
    "outcomes": [
      "Escribir posterior ∝ likelihood × prior y aplicarlo a un caso conjugado (Beta-Binomial para una tasa de conversión).",
      "Construir un modelo lineal bayesiano con pymc.Model() as m: ... y muestrearlo con pm.sample() (NUTS).",
      "Inspeccionar trace con arviz.plot_trace, diagnosticar convergencia (r_hat ≤ 1.01, ess_bulk ≥ 400).",
      "Interpretar HDI (Highest Density Interval) como reemplazo del IC clásico — con interpretación directa de probabilidad.",
      "Hacer posterior predictive check (pm.sample_posterior_predictive) y entender por qué es la validación bayesiana fundamental.",
      "Conocer NumPyro y cuándo elegirlo sobre PyMC (modelos grandes, GPU/JAX, optimización stocástica via SVI)."
    ],
    "topics": [
      "Teorema de Bayes: P(θ|D) = P(D|θ)·P(θ) / P(D).",
      "Conjugados: Beta–Binomial, Gamma–Poisson, Normal–Normal (intuición sin MCMC).",
      "MCMC: idea — muestrear de una distribución sin computarla analíticamente. NUTS (No U-Turn Sampler).",
      "HDI vs IC frecuentista: el HDI es interpretado directamente como P(θ ∈ HDI | datos) = 0.94.",
      "Posterior predictive: la distribución de datos futuros simulados desde el posterior. Test de modelo.",
      "Priors: no informativos (Uniform, HalfNormal con scale grande), débilmente informativos (recomendado), informativos (cuando hay expertise).",
      "Complemento moderno: PyMC v5 (PyTensor backend, ya estable post-Theano), NumPyro (JAX, GPU), ArviZ (diagnóstico estándar)."
    ],
    "materials": [
      "tips (regresión bayesiana).",
      "Tasa de conversión sintética (Beta-Binomial conjugado).",
      "McElreath's Howell1 (estatura vs peso) — el ejemplo canónico del libro.",
      "Librerías: pymc (≥ 5), arviz, numpyro, seaborn, matplotlib."
    ],
    "exercises": [
      "Conjugado a mano: 100 visitas, 8 conversiones. Prior Beta(1,1). Posterior = Beta(9, 93). Graficá prior y posterior; calculá HDI 94 % con scipy.stats.beta.ppf.",
      "Regresión bayesiana: ajustá el modelo PyMC del ejemplo sobre tips. Reportá summary y plot_trace. Verificá r_hat ≤ 1.01.",
      "Comparación: compará los coeficientes bayesianos (mean del posterior) con OLS de statsmodels sobre el mismo dataset. Con priors débiles, deberían ser casi idénticos.",
      "Posterior predictive check: ejecutá sample_posterior_predictive y az.plot_ppc. Discutí si el modelo captura la asimetría de tips (probablemente no — sugerir cambiar a likelihood Gamma o lognormal).",
      "NumPyro: traducí el modelo a NumPyro, ajustá, convertí con az.from_numpyro y verificá que los resultados son equivalentes. Comparar tiempo de ejecución."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/192-bayes-intro-priors-posterior-mcmc-con-pymc/notebook.ipynb"
  },
  {
    "id": "parte-3-estadistica-inferencial/193-pymc-v5-numpyro-arviz-stack-bayesiano",
    "number": 193,
    "slug": "193-pymc-v5-numpyro-arviz-stack-bayesiano",
    "partSlug": "parte-3-estadistica-inferencial",
    "title": "Stack bayesiano moderno: PyMC v5, NumPyro, ArviZ",
    "description": "Aprender el stack bayesiano moderno post-Theano —PyMC v5 (PyTensor), NumPyro (JAX), ArviZ (visualización backend-agnóstica)— a nivel de poder construir modelos jerárquicos serios, diagnosticar convergencia (r_hat, ess_b…",
    "level": "Intermedio-Avanzado",
    "duration": "90 min",
    "theory": "Aprender el stack bayesiano moderno post-Theano —PyMC v5 (PyTensor), NumPyro (JAX), ArviZ (visualización backend-agnóstica)— a nivel de poder construir modelos jerárquicos serios, diagnosticar convergencia (r_hat, ess_bulk, divergences), comparar modelos con LOO-CV y WAIC, y elegir backend según escala.",
    "outcomes": [
      "Construir modelo jerárquico no-centered en PyMC v5.",
      "Diagnosticar: r_hat ≤ 1.01, ess_bulk ≥ 400, divergences = 0.",
      "Aplicar non-centered parameterization para evitar funnel posteriors.",
      "Comparar modelos con az.compare([m1, m2], ic='loo').",
      "Migrar modelo de PyMC a NumPyro para 10-50× speedup en CPU.",
      "Aplicar SVI (Stochastic Variational Inference) en NumPyro como alternativa rápida a MCMC."
    ],
    "topics": [
      "PyMC v5: PyTensor backend, sintaxis estable.",
      "NumPyro: JAX backend, JIT + autograd + GPU/TPU.",
      "Centered vs non-centered parametrization.",
      "Posterior predictive check con ArviZ.",
      "LOO-CV y WAIC para comparación.",
      "SVI con AutoNormal / AutoMultivariateNormal."
    ],
    "materials": [
      "tips (regresión jerárquica por day).",
      "McElreath's Howell1 o chimpanzees (modelos clásicos).",
      "Librerías: pymc (≥ 5), numpyro, arviz, jax."
    ],
    "exercises": [
      "PyMC v5 hierarchical: tip ~ Normal(α_day + β·bill, σ); α_day ~ Normal(μα, σα).",
      "Non-centered: re-parametrizar el modelo con α_day = μα + σα · z_day, z_day ~ N(0,1). Comparar divergences.",
      "PPC: pm.sample_posterior_predictive + az.plot_ppc. Decidir si modelo razonable.",
      "NumPyro version: traducir, comparar tiempo.",
      "LOO compare: 3 modelos (intercepto solo, + slope, + jerárquico). az.compare."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-3-estadistica-inferencial/193-pymc-v5-numpyro-arviz-stack-bayesiano/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/194-versionado-de-datos-con-dvc",
    "number": 194,
    "slug": "194-versionado-de-datos-con-dvc",
    "partSlug": "parte-4-mlops",
    "title": "Versionado de datos con DVC",
    "description": "Versionar datasets pesados (>100 MB, que git rechaza) con DVC 3.x, separando qué dato se usó (puntero en git, ~200 bytes) de dónde vive el blob real (S3, GCS, Azure, disco local).",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Versionar datasets pesados (>100 MB, que git rechaza) con DVC 3.x, separando qué dato se usó (puntero en git, ~200 bytes) de dónde vive el blob real (S3, GCS, Azure, disco local). Reproducir un entrenamiento de hace 3 meses con git checkout <sha> && dvc pull y entender por qué dvc.lock es a los datos lo que package-lock.json es a npm.",
    "outcomes": [
      "Inicializar un repo con dvc init y rastrear un dataset con dvc add data/raw.csv (entiende que git solo guarda el .dvc pointer).",
      "Configurar un remote (dvc remote add -d origin s3://bucket/path) y sincronizar con dvc push / dvc pull.",
      "Construir un pipeline reproducible declarando stages en dvc.yaml (deps, outs, params, metrics) y ejecutarlo con dvc repro.",
      "Comparar experimentos con dvc exp run, dvc exp show, dvc exp diff — alternativa ligera a MLflow para casos simples.",
      "Diagnosticar ERROR: output 'X' is already tracked by SCM y otros choques DVC ↔ git."
    ],
    "topics": [
      "El problema: git LFS no escala a TB",
      "Modelo mental DVC: pointer en git + blob en remote",
      "dvc add vs dvc.yaml stages",
      "Remotes (S3, GCS, Azure, SSH, local)",
      "dvc.lock — el \"lockfile\" de tu pipeline",
      "dvc exp — branching-less experiments"
    ],
    "materials": [
      "Dataset: seaborn.load_dataset('titanic') exportado a data/raw/titanic.csv (~60 KB — pequeño a propósito para que la clase corra sin S3 real).",
      "Remote demo: directorio local /tmp/dvc-remote-demo (simula S3 sin credenciales). El comando para S3 real se muestra pero no se ejecuta.",
      "Librerías: dvc[s3] (o dvc pelado si remote local), pandas, scikit-learn."
    ],
    "exercises": [
      "Setup mínimo: inicializá un repo git + DVC (git init && dvc init). Generá data/raw/titanic.csv, hacelo trackear con dvc add data/raw/titanic.csv. Inspeccioná el .dvc resultante con cat data/raw/titanic.csv.dvc y entendé los campos md5, size, path.",
      "Remote local: configurá un remote en /tmp/dvc-remote-demo con dvc remote add -d local /tmp/dvc-remote-demo. Hacé dvc push y verificá con ls /tmp/dvc-remote-demo/files/md5/ que el blob aparece como <2-char-prefix>/<resto-del-hash>.",
      "Pipeline declarativo: creá dvc.yaml con dos stages — prepare (lee raw/titanic.csv, elimina nulos, escribe data/processed/clean.csv) y train (entrena un LogisticRegression, escribe model.pkl y metrics.json). Corré dvc repro y observá dvc.lock.",
      "Reproducción: tocá un parámetro en params.yaml (test_size: 0.2 → 0.3). Volvé a correr dvc repro y verificá que ambos stages se re-ejecutan (porque prepare no depende de params, pero train sí — y el output de train cambió). Compará con dvc repro --dry.",
      "Experimentos sin branching: dvc exp run -S 'train.C=0.1' tres veces con valores distintos de C. Listalos con dvc exp show. Aplicá el mejor con dvc exp apply <hash>."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/194-versionado-de-datos-con-dvc/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/195-versionado-de-modelos-y-experimentos-con-mlflow",
    "number": 195,
    "slug": "195-versionado-de-modelos-y-experimentos-con-mlflow",
    "partSlug": "parte-4-mlops",
    "title": "Versionado de modelos y experimentos con MLflow",
    "description": "Trackear experimentos de ML (parámetros, métricas, artefactos, código) con MLflow Tracking, registrar modelos en el Model Registry con stages (None → Staging → Production → Archived), y entender la diferencia conceptual…",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Trackear experimentos de ML (parámetros, métricas, artefactos, código) con MLflow Tracking, registrar modelos en el Model Registry con stages (None → Staging → Production → Archived), y entender la diferencia conceptual con DVC: DVC versiona el pipeline; MLflow versiona los runs.",
    "outcomes": [
      "Levantar un servidor MLflow local (mlflow ui o mlflow server) y logear runs con mlflow.start_run() + log_param/log_metric/log_artifact.",
      "Usar autolog (mlflow.sklearn.autolog()) para que params/metrics se capturen sin código boilerplate.",
      "Registrar un modelo en el Model Registry (mlflow.register_model) y transicionarlo de Staging a Production con la API o la UI.",
      "Cargar un modelo registrado en producción con mlflow.pyfunc.load_model(\"models:/MiModelo/Production\").",
      "Configurar un backend store (PostgreSQL) y un artifact store (S3) para uso en equipo."
    ],
    "topics": [
      "Tracking server: backend store + artifact store",
      "Runs, experiments, tags",
      "log_param, log_metric, log_artifact, log_model",
      "Autolog por framework (sklearn, PyTorch, XGBoost, LightGBM)",
      "Model Registry + stages",
      "MLflow Models flavor (pyfunc, sklearn, pytorch, ...)"
    ],
    "materials": [
      "Dataset: California Housing (sklearn.datasets.fetch_california_housing) — 20 640 filas, regresión, sin problemas de PII.",
      "Backend local: SQLite (mlflow server --backend-store-uri sqlite:///mlflow.db).",
      "Artifact local: ./mlruns/artifacts.",
      "Librerías: mlflow>=2.10, scikit-learn, xgboost."
    ],
    "exercises": [
      "Tracking manual: entrená un LinearRegression y un RandomForestRegressor sobre California Housing. Para cada uno, abrí un run y logueá n_estimators (si aplica), max_depth, rmse_train, rmse_test. Comparalos en la UI (mlflow ui --port 5000).",
      "Autolog: repetí el ejercicio anterior con mlflow.sklearn.autolog() y verificá que params + metrics + el modelo entero quedaron registrados sin código extra.",
      "Sweep de hiperparámetros: corré 10 runs variando max_depth ∈ {3, 5, 10, 15, 20} y n_estimators ∈ {50, 200}. Usá mlflow.search_runs() para encontrar el mejor por rmse_test.",
      "Registry: registrá el mejor modelo (mlflow.register_model(model_uri, \"housing-rf\")). Transicionalo a Staging, después a Production desde la API (MlflowClient.transition_model_version_stage).",
      "Carga en \"producción\": en una celda nueva, simulá un servicio que carga el modelo Production y predice una fila: model = mlflow.pyfunc.load_model(\"models:/housing-rf/Production\"); model.predict(X_one)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/195-versionado-de-modelos-y-experimentos-con-mlflow/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/196-feature-stores-feast",
    "number": 196,
    "slug": "196-feature-stores-feast",
    "partSlug": "parte-4-mlops",
    "title": "Feature stores (Feast)",
    "description": "Resolver el problema más caro de ML en producción —training/serving skew: que las features que ve el modelo en producción sean distintas a las que vio en training— centralizando definiciones de features en un feature st…",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Resolver el problema más caro de ML en producción —training/serving skew: que las features que ve el modelo en producción sean distintas a las que vio en training— centralizando definiciones de features en un feature store. Usar Feast para definir entidades + feature views, materializar al online store (Redis/SQLite), y servir features con get_online_features en <10 ms.",
    "outcomes": [
      "Explicar la diferencia entre offline store (parquet/BigQuery, para training) y online store (Redis/DynamoDB, para serving low-latency).",
      "Definir Entity, FeatureView, FileSource y registrar el repo con feast apply.",
      "Generar un training dataset point-in-time correct con get_historical_features (evita data leakage temporal).",
      "Materializar features (feast materialize-incremental) y consumirlas en serving con get_online_features.",
      "Reconocer cuándo NO usar feature store (ML con <5 features estables, equipo de 1, datos batch puro)."
    ],
    "topics": [
      "Training/serving skew — el bug más caro de MLOps",
      "Offline vs online store",
      "Entity + FeatureView + FileSource",
      "Point-in-time joins",
      "materialize / materialize-incremental",
      "Feast vs construir uno propio"
    ],
    "materials": [
      "Dataset: drivers de un servicio tipo Uber — driver_id, event_timestamp, conv_rate, acc_rate, avg_daily_trips. Generado sintéticamente en el notebook.",
      "Offline store: parquet local en data/.",
      "Online store: SQLite local en data/online_store.db.",
      "Librerías: feast>=0.40, pandas, pyarrow."
    ],
    "exercises": [
      "Setup mínimo: feast init driver_repo. Inspeccioná feature_store.yaml, example_repo.py. Corré feast apply y verificá feast feature-views list.",
      "Training dataset histórico: armá un entity_df con driver_id y event_timestamp para 5 momentos distintos del día. Pedile a Feast el feature driver_hourly_stats:conv_rate con get_historical_features. Confirmá manualmente que el valor devuelto es el último anterior al timestamp pedido (no el futuro).",
      "Materialización + serving: feast materialize-incremental $(date +%Y-%m-%d). Después: store.get_online_features(features=['driver_hourly_stats:conv_rate'], entity_rows=[{'driver_id': 1001}]).to_dict(). Medí latencia con %timeit (debería ser <2 ms).",
      "TTL en acción: configurá ttl=timedelta(days=1). Materializá datos viejos de 3 días atrás. Pedí features online → debería devolver None (porque expiró). Cambiá ttl=timedelta(days=7) y reintentá.",
      "Skew check: comparé el feature offline (parquet) y el online (SQLite) para el mismo driver_id. Si difieren después de materialize, hay un bug."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/196-feature-stores-feast/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/197-ci-cd-para-ml-con-github-actions",
    "number": 197,
    "slug": "197-ci-cd-para-ml-con-github-actions",
    "partSlug": "parte-4-mlops",
    "title": "CI/CD para ML con GitHub Actions",
    "description": "Automatizar el ciclo lint → test → entrenar → evaluar → comparar → desplegar con GitHub Actions.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Automatizar el ciclo lint → test → entrenar → evaluar → comparar → desplegar con GitHub Actions. Cada PR dispara entrenamiento sobre el slice actual de datos, postea métricas como comentario, y bloquea merge si la métrica empeoró >X%. Sin CI/CD, \"el modelo nuevo es mejor\" es opinión; con CI/CD, es un workflow check ✅ o ❌.",
    "outcomes": [
      "Escribir un workflow .github/workflows/ml.yml con jobs lint, test, train, evaluate.",
      "Usar CML (Continuous Machine Learning) para postear plots/metrics en el comentario del PR.",
      "Cachear dependencias (actions/setup-python con cache: pip) y pesos de modelos (actions/cache) para que el CI no tarde 20 min.",
      "Usar secrets y OIDC para deploy seguro a AWS/GCP sin claves long-lived.",
      "Configurar branch protection + required checks que bloqueen merge si las métricas degradan."
    ],
    "topics": [
      "Anatomía de un workflow: triggers, jobs, steps, runners",
      "Matrix builds (strategy.matrix)",
      "Caché de pip + datasets pesados",
      "CML: reportar métricas en PR",
      "OIDC para deploy (sin secret long-lived)",
      "Branch protection + required status checks"
    ],
    "materials": [
      "Modelo del ejemplo: RandomForestClassifier sobre Iris (corre en <5 s — ideal para CI).",
      "Repo template: estructura src/, tests/, .github/workflows/, params.yaml, metrics.json.",
      "Librerías: scikit-learn, pytest, ruff (lint), cml (npm package)."
    ],
    "exercises": [
      "Workflow mínimo (lint + test): creá .github/workflows/ci.yml con dos jobs en paralelo: lint (corre ruff check) y test (corre pytest). Push y verificá que aparecen los dos checks en el PR.",
      "Job de training: agregá un job train que corre python src/train.py, sube model.pkl y metrics.json como actions/upload-artifact. Solo en PRs (if: github.event_name == 'pull_request').",
      "Reporte CML: agregá un step que use iterative/setup-cml@v2, escribe report.md con cat metrics.json como tabla, y postea con cml comment create report.md. El comentario aparece en el PR.",
      "Comparación contra main: en el mismo job, git fetch origin main && python src/train.py desde main, guardás metrics_main.json, y agregás al reporte una tabla con Δaccuracy, Δf1.",
      "Branch protection: en Settings → Branches → Add rule → main, marcá Require status checks to pass before merging y seleccioná lint, test, train. PR con tests rotos = no podés mergear."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/197-ci-cd-para-ml-con-github-actions/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/198-docker-para-empaquetar-modelos",
    "number": 198,
    "slug": "198-docker-para-empaquetar-modelos",
    "partSlug": "parte-4-mlops",
    "title": "Docker para empaquetar modelos",
    "description": "Empaquetar un modelo entrenado + su runtime (Python, deps, código) en una imagen Docker reproducible, optimizada (multi-stage build, capas cacheadas, imagen <500 MB), y segura (non-root user, no secrets baked in).",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Empaquetar un modelo entrenado + su runtime (Python, deps, código) en una imagen Docker reproducible, optimizada (multi-stage build, capas cacheadas, imagen <500 MB), y segura (non-root user, no secrets baked in). El resultado se corre idéntico en tu laptop, en CI, y en producción.",
    "outcomes": [
      "Escribir un Dockerfile correcto para un servicio ML: base slim, multi-stage, layer caching, non-root.",
      "Diferenciar COPY de ADD, RUN de CMD de ENTRYPOINT, y cuándo usar cada uno.",
      "Reducir tamaño de imagen (de 2 GB a <500 MB) con python:3.12-slim, .dockerignore, y multi-stage builds.",
      "Versionar imágenes con tags semánticos (mymodel:1.2.3) y digests (@sha256:...) — y por qué :latest es trampa en producción.",
      "Diagnosticar image not building, image too big, slow rebuild con docker history, dive, docker scout."
    ],
    "topics": [
      "Imagen, capa, container, registry",
      "Dockerfile: FROM, COPY, RUN, CMD, ENTRYPOINT",
      "Layer caching: orden de instrucciones",
      "Multi-stage build",
      "Imágenes base: python:slim vs distroless vs alpine",
      "Security: non-root user, secrets via env/mount"
    ],
    "materials": [
      "Modelo: RandomForestClassifier entrenado en Iris, serializado con joblib.",
      "API: FastAPI sirviendo POST /predict.",
      "Herramientas: docker>=24, opcional dive, docker scout."
    ],
    "exercises": [
      "Dockerfile básico: empaquetá un script predict.py que carga model.pkl y predice una fila random. FROM python:3.12-slim, instalá deps de requirements.txt, COPY . /app, CMD [\"python\", \"predict.py\"]. Build con docker build -t miml:v1 . y corré.",
      "Layer caching: cambiá una línea en predict.py sin tocar requirements.txt. Rebuildá. Confirmá que la capa de pip install se reusa (mensaje \"CACHED\").",
      "Multi-stage: separá en dos stages: builder (FROM python:3.12 AS builder, instalá deps con compiladores) y runtime (FROM python:3.12-slim, copiá solo site-packages del builder). Compará tamaño con docker images.",
      "Non-root: agregá RUN useradd -m app && USER app antes del CMD. Verificá con docker run --rm miml:v3 whoami.",
      "Tags y digest: hacé docker push miml:v1 a Docker Hub. Obtené el digest con docker inspect miml:v1 --format '{{index .RepoDigests 0}}'. Discutí por qué deploys de producción referencian el digest."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/198-docker-para-empaquetar-modelos/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/199-apis-con-fastapi-sirviendo-modelos",
    "number": 199,
    "slug": "199-apis-con-fastapi-sirviendo-modelos",
    "partSlug": "parte-4-mlops",
    "title": "APIs con FastAPI sirviendo modelos",
    "description": "Exponer un modelo entrenado como REST API con FastAPI: validación de input con Pydantic, batching, async, healthcheck, métricas Prometheus, OpenAPI auto-generado.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Exponer un modelo entrenado como REST API con FastAPI: validación de input con Pydantic, batching, async, healthcheck, métricas Prometheus, OpenAPI auto-generado. Target: p99 latency <100 ms y throughput >500 req/s en un solo nodo CPU.",
    "outcomes": [
      "Construir un servicio FastAPI con endpoints POST /predict, POST /predict-batch, GET /health, GET /metrics.",
      "Definir schemas de input/output con pydantic.BaseModel y obtener validación + docs gratis.",
      "Usar lifespan events para cargar el modelo una sola vez (no por request).",
      "Loadtestear con locust y medir latency p50/p95/p99 + throughput.",
      "Decidir entre sync def y async def según si el predict es CPU-bound o I/O-bound."
    ],
    "topics": [
      "ASGI vs WSGI: por qué FastAPI no es Flask",
      "Pydantic v2: validación + serialización",
      "Lifespan: cargar modelo 1 vez",
      "Sync vs async para predict",
      "Batching: /predict-batch",
      "Observabilidad: /health, /metrics, logs estructurados"
    ],
    "materials": [
      "Modelo: cualquiera entrenado en clases previas — usamos sklearn por simplicidad.",
      "Librerías: fastapi, uvicorn[standard], pydantic>=2, prometheus-fastapi-instrumentator, locust (loadtest)."
    ],
    "exercises": [
      "API mínima: POST /predict con IrisInput(features: list[float]) → IrisOutput(class: int, proba: list[float]). Levantá con uvicorn app:app --reload. Abrí /docs (OpenAPI Swagger UI). Confirmá que probar desde la UI funciona.",
      "Lifespan: cargá el modelo en un lifespan y guardalo en app.state.model. Verificá que el modelo se carga UNA vez (print al inicio) aunque hagas 100 requests.",
      "Batching: agregá POST /predict-batch con BatchInput(rows: list[list[float]]). Medí latencia de 100 predicciones individuales vs 1 batch de 100.",
      "Async vs sync: simulá un predict que llama a una API externa (await httpx.AsyncClient().get(...)). Compará def (bloquea thread pool) vs async def (libera event loop). Loadtest con 200 concurrent users.",
      "Observabilidad: agregá prometheus-fastapi-instrumentator → /metrics. Healthcheck /health que devuelve {\"status\": \"ok\", \"model_loaded\": bool}. Loggeá cada request con logger.info (JSON)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/199-apis-con-fastapi-sirviendo-modelos/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/200-kubernetes-para-servir-modelos-a-escala",
    "number": 200,
    "slug": "200-kubernetes-para-servir-modelos-a-escala",
    "partSlug": "parte-4-mlops",
    "title": "Kubernetes para servir modelos a escala",
    "description": "Desplegar el contenedor de Clase 198–199 en Kubernetes con Deployment + Service + Ingress, autoescalar con HPA (CPU + custom metrics), hacer rolling updates seguros, y configurar livenessProbe/readinessProbe/resources c…",
    "level": "Avanzado",
    "duration": "90 min",
    "theory": "Desplegar el contenedor de Clase 198–199 en Kubernetes con Deployment + Service + Ingress, autoescalar con HPA (CPU + custom metrics), hacer rolling updates seguros, y configurar livenessProbe/readinessProbe/resources correctamente. Aprender los 5 manifests mínimos que necesita cualquier servicio de inferencia.",
    "outcomes": [
      "Escribir manifests YAML para Deployment, Service, ConfigMap, Secret, HPA, Ingress.",
      "Diferenciar livenessProbe (reinicia pod) de readinessProbe (saca del LB) de startupProbe (gracia inicial para modelos lentos).",
      "Configurar resources.requests/limits y entender por qué un pod sin requests es OOM-killable y sin limits es noisy-neighbor.",
      "Hacer kubectl rollout/rollback y entender los maxSurge/maxUnavailable del rolling update.",
      "Diagnosticar CrashLoopBackOff, ImagePullBackOff, Pending, Evicted con kubectl describe y kubectl logs."
    ],
    "topics": [
      "Pod, Deployment, ReplicaSet, Service",
      "Probes (liveness, readiness, startup)",
      "Resources: requests vs limits",
      "HPA: CPU + custom metrics (latency, queue depth)",
      "Rolling update + rollback",
      "Ingress + service mesh (mention)"
    ],
    "materials": [
      "Cluster: minikube, kind, o k3d para local. Equivalente en cloud: GKE/EKS/AKS.",
      "Imagen: la de Clase 198 (iris-api:v1).",
      "Herramientas: kubectl, kustomize (built-in) o helm."
    ],
    "exercises": [
      "Cluster local: kind create cluster --name ml. Pusheá la imagen local con kind load docker-image iris-api:v1 --name ml. Verificá con kubectl get nodes.",
      "Deployment + Service: aplicá los YAML del notebook. kubectl get pods -w mientras los 3 pods arrancan. kubectl port-forward svc/iris-api 8000:80 y pegale con curl localhost:8000/predict.",
      "Probes: cambiá livenessProbe a apuntar a /wrong-endpoint. Observá con kubectl get pods -w cómo entra en CrashLoopBackOff. Revertí.",
      "HPA: kubectl apply -f hpa.yaml con targetCPUUtilizationPercentage: 50. Generá carga con kubectl run loadtester --image=busybox -it --rm -- /bin/sh -c \"while true; do wget -q -O- iris-api/predict; done\". Observá kubectl get hpa -w escalar de 3 → 10.",
      "Rolling update + rollback: cambiá la imagen a iris-api:v2 (versión rota a propósito). kubectl rollout status deployment/iris-api debería timeoutear. kubectl rollout undo deployment/iris-api y verificá recuperación."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/200-kubernetes-para-servir-modelos-a-escala/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/201-serverless-ml-aws-lambda-gcp-cloud-functions",
    "number": 201,
    "slug": "201-serverless-ml-aws-lambda-gcp-cloud-functions",
    "partSlug": "parte-4-mlops",
    "title": "Serverless ML: AWS Lambda, GCP Cloud Functions",
    "description": "Desplegar un modelo como función serverless que escala de 0 a N sin gestionar servidores.",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Desplegar un modelo como función serverless que escala de 0 a N sin gestionar servidores. Decidir cuándo serverless gana (tráfico bursty, batch chico, no podés mantener infra) y cuándo pierde (cold start crítico, modelo >1 GB, latencia <50 ms requerida).",
    "outcomes": [
      "Empaquetar un modelo sklearn/XGBoost como Lambda Container Image (hasta 10 GB) o Cloud Function 2nd gen (build automático con Buildpacks).",
      "Mitigar cold starts con: provisioned concurrency (Lambda), min-instances=1 (Cloud Functions), o snapshot-based init (SnapStart).",
      "Configurar API Gateway o HTTP trigger para exponer la función como REST.",
      "Calcular costo: $/M invocations × duration × memory, vs un pod K8s 24/7.",
      "Reconocer límites: timeout 15 min (Lambda), payload 6 MB sync / 256 KB async, disco efímero 512 MB /tmp (10 GB con ephemeral-storage)."
    ],
    "topics": [
      "Modelo de ejecución: scale-to-zero, request-per-instance",
      "Cold start vs warm",
      "Package formats: ZIP (≤250 MB) vs Container (≤10 GB)",
      "Cost model: invocations + GB-seconds",
      "Provisioned concurrency / min-instances",
      "Cuándo NO usar serverless"
    ],
    "materials": [
      "Modelo: LogisticRegression sobre Iris (chico — buen fit serverless).",
      "Tools: AWS CLI + SAM (Serverless Application Model), o gcloud functions deploy.",
      "Imagen base Lambda: public.ecr.aws/lambda/python:3.12."
    ],
    "exercises": [
      "Lambda con container: buildeá un Dockerfile basado en public.ecr.aws/lambda/python:3.12, copiá app.py con lambda_handler(event, context), y model.pkl. Push a ECR. aws lambda create-function con --package-type Image.",
      "API Gateway: creá una API HTTP y conectala a la Lambda. curl <api-url>/predict -d '{\"features\":[5.1,3.5,1.4,0.2]}'. Medí latencia primera vs segunda llamada (cold vs warm).",
      "Provisioned Concurrency: configurá provisioned-concurrency=1 en la Lambda. Vuelve a medir — debería eliminar el cold start.",
      "Cloud Functions equivalent: gcloud functions deploy iris --gen2 --runtime=python312 --trigger-http --source=. --entry-point=predict --memory=512Mi --min-instances=1. Compará cold start con Lambda.",
      "Cost calc: asumí 100 req/s sostenido, modelo en RAM 512 MB, 80 ms p99. Calculá $/mes en Lambda vs un pod K8s con 4 vCPU 24/7. Encontrá el punto de cruce."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/201-serverless-ml-aws-lambda-gcp-cloud-functions/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/202-monitoreo-data-drift-model-drift-alertas",
    "number": 202,
    "slug": "202-monitoreo-data-drift-model-drift-alertas",
    "partSlug": "parte-4-mlops",
    "title": "Monitoreo: data drift, model drift, alertas",
    "description": "Detectar antes que el negocio: (a) data drift (la distribución de features cambió), (b) prediction drift (la distribución de predicciones cambió), (c) concept drift (la relación X→y cambió).",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Detectar antes que el negocio: (a) data drift (la distribución de features cambió), (b) prediction drift (la distribución de predicciones cambió), (c) concept drift (la relación X→y cambió). Configurar alertas que avisen antes de que la métrica de negocio caiga, no después.",
    "outcomes": [
      "Distinguir data drift (P(X) cambia), prediction drift (P(ŷ) cambia), concept drift (P(y|X) cambia) y elegir el test correcto para cada uno.",
      "Detectar drift con tests estadísticos: PSI (Population Stability Index), K-S (continuas), chi-cuadrado (categóricas), Wasserstein (más sensible que K-S en colas).",
      "Usar Evidently AI para generar reportes HTML con todos los tests + visualizaciones, y NannyML para estimar performance sin labels en producción (CBPE).",
      "Configurar alertas en Grafana / CloudWatch / Slack vía webhook cuando el drift score supera el umbral.",
      "Reconocer cuándo el \"drift\" es ruido (re-test con bonferroni) vs señal (acción)."
    ],
    "topics": [
      "3 tipos de drift y por qué importan distinto",
      "PSI: umbral 0.1 / 0.2",
      "K-S, chi-cuadrado, Wasserstein",
      "Performance estimation sin labels (CBPE)",
      "Reference window vs current window",
      "Alertas: umbral + cooldown + canal"
    ],
    "materials": [
      "Dataset training: California Housing — usado como reference.",
      "Dataset \"producción\": California Housing con shift sintético (escalar MedInc × 1.5 para simular inflación, o filtrar HouseAge > 30 para simular nuevo segmento).",
      "Librerías: evidently, scipy, nannyml, scikit-learn."
    ],
    "exercises": [
      "PSI manual: bineá MedInc en 10 deciles (con bordes del reference). Calculá p_ref, p_cur y aplicá la fórmula PSI. Verificá que sin shift PSI < 0.05; con shift × 1.5 PSI > 0.5.",
      "K-S vs Wasserstein: agregale outliers a 5% de la muestra de producción (multiplicá esos por 100). K-S podría no detectar (la mediana no cambió mucho); Wasserstein sí. Reproducí ambos casos.",
      "Reporte Evidently: Report(metrics=[DataDriftPreset()]) sobre reference vs current. Guardalo como HTML, abrilo, identificá qué features driftearon y con qué test.",
      "Concept drift sin labels (CBPE): con NannyML, fit el estimador sobre reference + predicciones. Aplicalo a current. Compará estimated_accuracy vs actual_accuracy (calculable porque tenés y en este ejercicio).",
      "Alerta: escribí un script que (a) calcule PSI por feature, (b) si alguna >0.2 emite un POST a un webhook Slack/Discord, (c) usá cooldown de 4 h con un archivo last_alert.txt para evitar spamming."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/202-monitoreo-data-drift-model-drift-alertas/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/203-reentrenamiento-programado",
    "number": 203,
    "slug": "203-reentrenamiento-programado",
    "partSlug": "parte-4-mlops",
    "title": "Reentrenamiento programado",
    "description": "Convertir el reentrenamiento en un proceso programado, auditado y reversible: DAG que cada N horas/días corre pull-data → validate → train → evaluate → promote-if-better → notify, con shadow/canary (Clase 204) antes del…",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Convertir el reentrenamiento en un proceso programado, auditado y reversible: DAG que cada N horas/días corre pull-data → validate → train → evaluate → promote-if-better → notify, con shadow/canary (Clase 204) antes del rollout pleno. Decidir entre schedule fijo, trigger por drift y trigger por degradación según el caso.",
    "outcomes": [
      "Diseñar un DAG (Airflow/Prefect/Dagster) que orqueste el reentrenamiento completo.",
      "Implementar el patrón champion-challenger: el modelo Production sigue sirviendo hasta que el challenger demuestra ser mejor en métricas de validación + en shadow.",
      "Configurar tres estrategias de trigger: cron(0 2 MON), on_drift > threshold, on_performance_degraded.",
      "Garantizar idempotencia (re-runs no duplican datos) y observabilidad (logs estructurados, alertas en fallas).",
      "Diferenciar online learning (modelo actualiza con cada nueva muestra) de continual training (re-trainings periódicos)."
    ],
    "topics": [
      "Triggers: schedule vs drift vs degradation",
      "DAG = grafo de tareas con deps",
      "Champion-challenger",
      "Idempotencia",
      "Online vs continual training",
      "Catastrophic forgetting"
    ],
    "materials": [
      "Pipeline target: Airflow local (Docker), o Prefect Cloud free tier, o GitHub Actions schedule.",
      "Librerías: apache-airflow>=2.9, prefect>=3, mlflow, evidently."
    ],
    "exercises": [
      "DAG mínimo (Airflow o Prefect): 5 tareas: pull_data → validate_data → train → evaluate → promote. Cada tarea es una función Python. Schedule diario.",
      "Champion-challenger: en promote, comparar challenger.f1 vs champion.f1 (leídos de MLflow). Promover solo si challenger.f1 > champion.f1 + 0.005. Sino, logear [skipped] challenger no es significativamente mejor y dejar champion intacto.",
      "Idempotencia: ejecutá el DAG dos veces seguidas para la misma fecha. Verificá que no se duplican filas en data/processed/, ni se crean dos registros en MLflow con el mismo execution_date.",
      "Trigger por drift: agregá una tarea inicial check_drift que (a) si PSI > 0.2 continúa el DAG, (b) si no, hace raise AirflowSkipException (skipea el resto). Resultado: solo se entrena si hay drift.",
      "Backfill: simulá un bug en la tarea validate_data que ya corrió bien por una semana. Fixeá el bug, airflow dags backfill --start-date X --end-date Y. Verificá que se re-procesan los días afectados sin duplicar registros downstream."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/203-reentrenamiento-programado/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/204-shadow-deployment-y-canary-releases",
    "number": 204,
    "slug": "204-shadow-deployment-y-canary-releases",
    "partSlug": "parte-4-mlops",
    "title": "Shadow deployment y canary releases",
    "description": "Desplegar un modelo nuevo sin arriesgar producción: primero en shadow (recibe tráfico real pero sus predicciones no se devuelven al usuario), después canary (1% → 5% → 25% → 100% del tráfico).",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Desplegar un modelo nuevo sin arriesgar producción: primero en shadow (recibe tráfico real pero sus predicciones no se devuelven al usuario), después canary (1% → 5% → 25% → 100% del tráfico). Convertir \"creo que esto es mejor\" en \"lo medí en producción real\".",
    "outcomes": [
      "Implementar shadow mode: doble call (champion + challenger), respuesta del champion al user, log de ambas para análisis offline.",
      "Configurar canary release progresivo (1% → 5% → 25% → 100%) con K8s + Istio, o con feature flag a nivel app (LaunchDarkly, Unleash).",
      "Definir rollback automático: si la métrica del canary degrada >X%, volver al 100% champion en <5 min.",
      "Implementar A/B test correcto: muestra del mismo segmento, métrica primaria pre-registrada, poder estadístico calculado.",
      "Diferenciar shadow (sin riesgo, costo doble) de canary (riesgo limitado, costo nuevo solo)."
    ],
    "topics": [
      "Shadow vs canary vs blue-green vs A/B",
      "Implementación: app-level vs infra-level",
      "Métrica de \"salud\" del canary",
      "Rollback automático",
      "Análisis de shadow data",
      "A/B test riguroso"
    ],
    "materials": [
      "Stack ejemplo: FastAPI + Istio (canary) o feature flag in-process (shadow simple).",
      "Librerías: scipy.stats (A/B test), numpy."
    ],
    "exercises": [
      "Shadow en proceso: en el FastAPI de Clase 199, agregá la lógica: cargá model_champion y model_challenger. En /predict, predeci con ambos, devolvé solo champion, log los dos en JSON. Después de 1000 requests, analizá la distribución de diferencias.",
      "Canary con feature flag: implementá un toggle CANARY_PERCENT (env var). Si random.random() < CANARY_PERCENT/100, usá challenger. Sticky: hash por user_id para que el mismo user vea siempre lo mismo dentro del test.",
      "Canary con Istio: VirtualService con weight: 95 / 5. kubectl apply y verificá distribución de tráfico con kubectl logs.",
      "Rollback automático: agregá un sidecar (Python script) que cada 60 s consulta Prometheus: si latency_p99{model=challenger} > 200ms, cambia el weight a 100 / 0 automáticamente.",
      "A/B test riguroso: calculá tamaño de muestra para detectar δ = 0.02 en accuracy con α=0.05, power=0.8. Corré el A/B test el tiempo necesario para acumular ese N. Reportá p-value + CI de la diferencia."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/204-shadow-deployment-y-canary-releases/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/205-interpretabilidad-shap-lime-pdp-ice",
    "number": 205,
    "slug": "205-interpretabilidad-shap-lime-pdp-ice",
    "partSlug": "parte-4-mlops",
    "title": "Interpretabilidad: SHAP, LIME, PDP, ICE",
    "description": "Hacer interpretabilidad deployable: exponer un endpoint /explain que devuelva la atribución por feature de una predicción individual (SHAP/LIME), generar reportes globales (PDP/ICE) al promover un modelo, y entender los…",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Hacer interpretabilidad deployable: exponer un endpoint /explain que devuelva la atribución por feature de una predicción individual (SHAP/LIME), generar reportes globales (PDP/ICE) al promover un modelo, y entender los tres trade-offs: fidelidad vs simplicidad, global vs local, exacto vs aproximado.",
    "outcomes": [
      "Diferenciar local (esta predicción) vs global (modelo en general) y model-agnostic vs model-specific.",
      "Usar SHAP con TreeExplainer (rápido, exacto, árboles), KernelExplainer (lento, model-agnostic), DeepExplainer (redes neuronales) y Partition (recientes).",
      "Usar LIME para explicaciones model-agnostic en texto/imágenes/tabular.",
      "Generar PDP (Partial Dependence Plot) e ICE (Individual Conditional Expectation) con sklearn.inspection.",
      "Decidir cuándo SHAP es lo correcto y cuándo es overkill (ej. modelo lineal: usar coeficientes directamente)."
    ],
    "topics": [
      "Local vs global, model-agnostic vs specific",
      "SHAP: TreeExplainer vs KernelExplainer",
      "LIME para texto/imágenes",
      "PDP + ICE: efecto marginal vs heterogeneidad",
      "Endpoint /explain en producción",
      "Comunicar a stakeholders no técnicos"
    ],
    "materials": [
      "Dataset: California Housing.",
      "Modelos: XGBRegressor (TreeSHAP) y MLPRegressor (KernelSHAP/DeepSHAP).",
      "Librerías: shap>=0.45, lime, sklearn>=1.5, matplotlib."
    ],
    "exercises": [
      "TreeSHAP: entrená XGB sobre California. explainer = shap.TreeExplainer(model). shap_values = explainer(X_test[:100]). shap.plots.waterfall(shap_values[0]) (local) y shap.plots.beeswarm(shap_values) (global).",
      "KernelSHAP vs TreeSHAP: corré KernelExplainer con 100 background samples sobre el mismo XGB. Compará SHAP values con TreeSHAP. ¿Son iguales? ¿Cuánto tardó cada uno?",
      "LIME tabular: LimeTabularExplainer sobre el mismo modelo. Explicá la misma instancia que en SHAP. Compará las features importantes.",
      "PDP + ICE: sklearn.inspection.PartialDependenceDisplay.from_estimator(model, X, features=['MedInc', 'HouseAge'], kind='both'). Identificá si hay no-linealidad y/o heterogeneidad.",
      "Endpoint /explain: extendé el FastAPI (Clase 199) con POST /explain que devuelve top-5 features + SHAP values + base value, para una instancia. Medí latencia — TreeSHAP debería ser <50 ms."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/205-interpretabilidad-shap-lime-pdp-ice/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/206-testing-de-datos-great-expectations-deequ",
    "number": 206,
    "slug": "206-testing-de-datos-great-expectations-deequ",
    "partSlug": "parte-4-mlops",
    "title": "Testing de datos: Great Expectations, Deequ",
    "description": "Aplicar testing como código a los datos: definir \"expectations\" (assertions sobre el dataset) y validarlas en cada corrida del pipeline.",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Aplicar testing como código a los datos: definir \"expectations\" (assertions sobre el dataset) y validarlas en cada corrida del pipeline. Detectar schema drift, outliers extremos, nulos inesperados antes de que lleguen al entrenamiento o a la predicción. Bug típico: no es que el modelo se rompe — es que la data está rota y nadie se entera.",
    "outcomes": [
      "Definir un Expectation Suite con Great Expectations 1.x: schema, ranges, uniqueness, null rates, regex.",
      "Generar un Data Docs HTML que documenta el dataset + resultados de validación (auditoría para regulador).",
      "Integrar GE en un pipeline DVC/Airflow: si validación falla, abortar el pipeline.",
      "Usar Deequ (Scala/Python via PyDeequ) para datasets grandes en Spark.",
      "Diferenciar data tests (sobre el dataset) de unit tests (sobre el código) — son ortogonales."
    ],
    "topics": [
      "Por qué unit tests no alcanzan en data pipelines",
      "Expectation Suite: schema + business rules",
      "Profiling automático",
      "Data Docs: docs ejecutables",
      "Checkpoints e integración con pipelines",
      "Deequ para Spark scale"
    ],
    "materials": [
      "Dataset: California Housing (sin shift) como reference, después con shift sintético para ver fallas.",
      "Librerías: great-expectations>=1.0, opcional pandera, pydeequ."
    ],
    "exercises": [
      "Bootstrap de un suite: gx init para crear el proyecto. gx datasource new apuntando a CSV. Profileá el dataset para suite inicial. Revisalo a mano: descomentá las expectations razonables, borrá las absurdas.",
      "Custom expectations: agregá: expect_column_values_to_be_between('MedInc', 0, 20), expect_table_row_count_to_be_between(1000, 100000), expect_column_pair_values_A_to_be_greater_than_B('AveRooms', 'AveBedrms') (más rooms que bedrooms).",
      "Checkpoint: configurá un checkpoint que (a) corre el suite, (b) si falla, abre un Slack alert. Corré con gx checkpoint run my_checkpoint.",
      "Data Docs: gx docs build. Abrí el HTML. Mostrá a un PM/regulador hipotético: la suite + el último validation result.",
      "Pandera alternative: el mismo schema con pandera: class HousingSchema(pa.DataFrameModel): MedInc: Series[float] = pa.Field(in_range={\"min_value\": 0, \"max_value\": 20}). Compará verbosidad y velocidad."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/206-testing-de-datos-great-expectations-deequ/notebook.ipynb"
  },
  {
    "id": "parte-4-mlops/207-testing-de-modelos-invariance-behavioral-tests",
    "number": 207,
    "slug": "207-testing-de-modelos-invariance-behavioral-tests",
    "partSlug": "parte-4-mlops",
    "title": "Testing de modelos: invariance + behavioral tests",
    "description": "Ir más allá de \"accuracy en hold-out\": tests que verifican que el modelo se comporta como debería en casos específicos.",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Ir más allá de \"accuracy en hold-out\": tests que verifican que el modelo se comporta como debería en casos específicos. Tres familias: invariance tests (\"misma predicción si reemplazo Juan por María\"), directional tests (\"si subo el ingreso, la proba de aprobar el préstamo no debe bajar\"), minimum functionality tests (\"predicción correcta sobre casos canónicos hand-crafted\"). Cierra la Parte 4: con esto, el modelo en producción tiene 6 capas de protección (data tests, model tests, monitoring, shadow, canary, rollback).",
    "outcomes": [
      "Implementar invariance tests (perturbaciones que NO deben cambiar la predicción): swap de nombres protegidos, sinónimos, ruido pequeño.",
      "Implementar directional tests (perturbaciones que deben cambiar la predicción en una dirección esperada): subir ingreso → menos riesgo crediticio.",
      "Crear minimum functionality test sets (MFT): casos hand-crafted que cubren cada feature/segmento crítico.",
      "Integrar tests de modelo en pytest y correrlos en CI antes de promover (gate de Clase 197).",
      "Usar Deepchecks o CheckList para suites pre-armados (especialmente NLP)."
    ],
    "topics": [
      "Accuracy ≠ corrección — los 3 tipos de test",
      "Invariance tests",
      "Directional tests",
      "MFT (Minimum Functionality)",
      "Slice-based testing",
      "Integración con CI"
    ],
    "materials": [
      "Tabular: Adult Income (UCI) con gender como atributo sensible.",
      "NLP: subset de IMDb reviews para sentiment.",
      "Librerías: deepchecks>=0.18, checklist, pytest, pandas."
    ],
    "exercises": [
      "MFT tabular: para un modelo de crédito sobre Adult, hand-craft 20 casos: 10 obvios \"should approve\" (alto ingreso, educación alta, sin debts) y 10 obvios \"should reject\" (ingreso bajo, edad joven, sin historial). Asseré con pytest que el modelo acierta los 20.",
      "Invariance — gender swap: tomá 500 registros, cambiá gender M ↔ F, dejá el resto igual. Mediá accuracy(predictions_original == predictions_swapped). Si <99%: el modelo está usando gender (probablemente vía proxy).",
      "Directional — income up: para los mismos 500, multiplicá income × 1.5. La proba predicha de >50K debería subir (o quedar igual) en >95% de los casos. Si baja en muchos: bug.",
      "Slice-based: calculá accuracy por slice (gender × race × age_bucket). Reportá top 5 worst slices. Si el peor slice tiene accuracy 0.55 y el promedio 0.85: tenés un problema de fairness invisible en métricas agregadas.",
      "Pytest gate: empaquetá los 4 tests anteriores en tests/test_model_behavior.py. Hacelo correr en GitHub Actions (Clase 197) como required check. Si tests rojos: PR no se mergea."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-4-mlops/207-testing-de-modelos-invariance-behavioral-tests/notebook.ipynb"
  },
  {
    "id": "parte-5-ingenieria-de-datos/208-pipelines-etl-elt-con-airflow",
    "number": 208,
    "slug": "208-pipelines-etl-elt-con-airflow",
    "partSlug": "parte-5-ingenieria-de-datos",
    "title": "Pipelines ETL/ELT con Airflow",
    "description": "Escribir DAGs de Airflow 2.x con la API moderna (TaskFlow + @dag/@task decorators), entender la diferencia entre ETL (transform antes de cargar) y ELT (cargar al warehouse y transformar ahí), y orquestar un pipeline ext…",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Escribir DAGs de Airflow 2.x con la API moderna (TaskFlow + @dag/@task decorators), entender la diferencia entre ETL (transform antes de cargar) y ELT (cargar al warehouse y transformar ahí), y orquestar un pipeline extract → load → transform → notify con retries, SLAs y backfill.",
    "outcomes": [
      "Escribir un DAG con TaskFlow API (@dag, @task) y entender el grafo resultante.",
      "Diferenciar ETL (clásico) de ELT (moderno, warehouse-first) y elegir según contexto.",
      "Configurar retries, SLAs, trigger rules (all_success, one_failed, none_failed), y XComs.",
      "Hacer backfill (airflow dags backfill) para reprocesar fechas históricas sin duplicar.",
      "Diagnosticar Task stuck in queued, Worker died, DAG not appearing con airflow dags list, logs, y airflow.cfg."
    ],
    "topics": [
      "ETL vs ELT — cuándo cada uno",
      "DAG = grafo dirigido acíclico",
      "TaskFlow API vs Operators clásicos",
      "XComs — pasar data entre tasks",
      "Schedule + catchup + backfill",
      "Sensors, hooks, providers"
    ],
    "materials": [
      "Stack ejemplo: Airflow 2.10+ con docker-compose oficial.",
      "Pipeline target: extrae CSV → carga a DuckDB → transforma con SQL → publica métricas a Slack.",
      "Librerías: apache-airflow>=2.10, duckdb, pandas."
    ],
    "exercises": [
      "DAG mínimo TaskFlow: 3 tasks: extract (descarga CSV), transform (limpia con pandas), load (escribe a DuckDB). Ver el grafo en /graph.",
      "Schedule + catchup: schedule='@daily', start_date=days_ago(7), catchup=True. Verificá que Airflow crea 7 runs históricos. Cambiar a catchup=False y observar diferencia.",
      "Retries + SLA: agregá retries=3, retry_delay=timedelta(minutes=2), sla=timedelta(minutes=10) al transform. Simulá falla con raise Exception(\"flaky\") y observá reintento.",
      "XCom: extract devuelve un dict pequeño (filename + row count). transform lo recibe como argumento (TaskFlow autoinjecta). Verificá en la UI tab \"XCom\".",
      "Backfill: airflow dags backfill --start-date 2026-06-01 --end-date 2026-06-05 my_dag. Confirmá que se ejecutan los 5 días sin duplicar (gracias a idempotencia con execution_date como key)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-5-ingenieria-de-datos/208-pipelines-etl-elt-con-airflow/notebook.ipynb"
  },
  {
    "id": "parte-5-ingenieria-de-datos/209-pipelines-con-prefect-o-dagster",
    "number": 209,
    "slug": "209-pipelines-con-prefect-o-dagster",
    "partSlug": "parte-5-ingenieria-de-datos",
    "title": "Pipelines con Prefect o Dagster",
    "description": "Construir el mismo pipeline de Clase 208 con Prefect 3 (API Python moderna, hybrid execution) y con Dagster (asset-oriented, mejor lineage).",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Construir el mismo pipeline de Clase 208 con Prefect 3 (API Python moderna, hybrid execution) y con Dagster (asset-oriented, mejor lineage). Entender qué problemas resuelven mejor que Airflow y cuándo elegir cada uno.",
    "outcomes": [
      "Escribir un flow Prefect con @flow/@task, deployments, work pools y workers.",
      "Definir assets Dagster (@asset) y entender la diferencia entre \"task-oriented\" (Airflow/Prefect) y \"asset-oriented\" (Dagster).",
      "Configurar hybrid execution Prefect: control plane en cloud, workers en tu infra (sin enviar data sensible).",
      "Usar Dagster's UI para ver lineage automático: qué asset depende de qué, cuándo se materializó cada uno.",
      "Decidir Airflow vs Prefect vs Dagster según contexto (equipo, escala, tipo de pipeline)."
    ],
    "topics": [
      "Prefect 3: flows, tasks, deployments",
      "Work pools + workers",
      "Dagster: asset-oriented vs task-oriented",
      "Software-defined assets (SDA)",
      "Scheduling: cron, interval, event-driven",
      "Cuándo migrar de Airflow"
    ],
    "materials": [
      "Mismo pipeline de Clase 208 (BTC price), implementado dos veces.",
      "Librerías: prefect>=3, dagster>=1.7, duckdb, pandas, requests."
    ],
    "exercises": [
      "Prefect flow: copiá la lógica del DAG Airflow al patrón Prefect: @flow def btc_pipeline(): notify(transform(load(extract()))). Corré python btc.py directo (no necesita scheduler).",
      "Deployment Prefect: flow.serve(name=\"btc-hourly\", cron=\"0 \"). Dejá corriendo, observá ejecuciones programadas en localhost:4200.",
      "Dagster assets: convertí las funciones a @asset def btc_price(), @asset def daily_avg(btc_price). Dagster infiere daily_avg depende de btc_price. UI muestra el grafo.",
      "Materializar: en Dagster UI, click \"Materialize\" sobre btc_price. Solo se ejecuta ese asset; daily_avg queda \"stale\" hasta que se materialice también.",
      "Comparativa: mismo pipeline en Airflow + Prefect + Dagster. Compará LOC, claridad, UI, velocidad de feedback dev."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-5-ingenieria-de-datos/209-pipelines-con-prefect-o-dagster/notebook.ipynb"
  },
  {
    "id": "parte-5-ingenieria-de-datos/210-pyspark-para-datasets-grandes",
    "number": 210,
    "slug": "210-pyspark-para-datasets-grandes",
    "partSlug": "parte-5-ingenieria-de-datos",
    "title": "PySpark para datasets grandes",
    "description": "Procesar datasets que no entran en RAM con PySpark 3.5+: DataFrames con lazy evaluation, Spark SQL, particionado, joins eficientes (broadcast vs shuffle), y entender cuándo Spark gana vs pandas/Polars (>10 GB) y cuándo…",
    "level": "Avanzado",
    "duration": "90 min",
    "theory": "Procesar datasets que no entran en RAM con PySpark 3.5+: DataFrames con lazy evaluation, Spark SQL, particionado, joins eficientes (broadcast vs shuffle), y entender cuándo Spark gana vs pandas/Polars (>10 GB) y cuándo pierde (<1 GB, dev local).",
    "outcomes": [
      "Crear una SparkSession (local o cluster) y leer Parquet/CSV/JSON con schema inference o explícito.",
      "Diferenciar transformations (lazy: select, filter, groupBy) de actions (eager: count, collect, show, write).",
      "Optimizar joins: broadcast join (tabla chica × tabla grande) vs sort-merge join (dos tablas grandes).",
      "Particionar correctamente (partitionBy(\"date\") al escribir, evitar partitionBy con cardinalidad alta).",
      "Diagnosticar performance con Spark UI: stages, shuffle data, skew."
    ],
    "topics": [
      "RDD vs DataFrame vs SQL — 3 APIs",
      "Lazy evaluation + DAG de ejecución",
      "Particionado: al leer, al escribir, en memoria",
      "Joins: broadcast vs shuffle vs sort-merge",
      "Caching / persist",
      "Spark UI: stages, shuffle, skew"
    ],
    "materials": [
      "Local mode: pyspark.SparkSession.builder.master(\"local[*]\") — usa todos los cores.",
      "Dataset: NYC TLC Yellow Taxi 2024 (parquet, ~10 GB) — clásico para Spark demos.",
      "Librerías: pyspark>=3.5, pyarrow."
    ],
    "exercises": [
      "Spark session local: spark = SparkSession.builder.master(\"local[4]\").appName(\"demo\").getOrCreate(). Cargá un parquet, mostrá schema con df.printSchema().",
      "Lazy vs eager: df2 = df.filter(...).select(...) (rápido, no ejecuta). df2.count() (lento, ejecuta). Mirá en Spark UI (localhost:4040) los stages.",
      "Broadcast join: cargá taxi (10 GB) y zones (1 KB). Hacé taxi.join(broadcast(zones), \"zone_id\"). Compará con taxi.join(zones, \"zone_id\") sin hint — debería ser igual gracias a AQE auto-broadcast.",
      "Particionado al escribir: df.write.partitionBy(\"date\").parquet(\"out/\"). Verificá estructura out/date=2024-01-01/part-*.parquet. Lecturas con filtro WHERE date='2024-01-01' solo leen ese subdirectorio.",
      "Skew: simulá una key skewed (90% rows con user_id=1). Hacé groupBy → observá UI: 1 task tarda 90% del tiempo. Mitigá con salting: agregar columna random salt = (rand() * 10).cast(\"int\"), group por (user_id, salt), después sumar."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-5-ingenieria-de-datos/210-pyspark-para-datasets-grandes/notebook.ipynb"
  },
  {
    "id": "parte-5-ingenieria-de-datos/211-polars-como-alternativa-moderna",
    "number": 211,
    "slug": "211-polars-como-alternativa-moderna",
    "partSlug": "parte-5-ingenieria-de-datos",
    "title": "Polars como alternativa moderna",
    "description": "Reemplazar pandas en pipelines productivos por Polars 1.x: 5-30× más rápido, multi-threaded por default, lazy API que optimiza la query antes de ejecutar, y streaming engine que procesa datasets mayores que RAM.",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Reemplazar pandas en pipelines productivos por Polars 1.x: 5-30× más rápido, multi-threaded por default, lazy API que optimiza la query antes de ejecutar, y streaming engine que procesa datasets mayores que RAM. Identificar los pocos casos donde pandas sigue ganando (ecosistema, statsmodels, sklearn pre-Arrow).",
    "outcomes": [
      "Convertir scripts pandas a Polars (eager API: pl.DataFrame) y medir speedup.",
      "Usar lazy API (pl.scan_parquet + .collect()) para que el optimizador haga predicate pushdown + column pruning.",
      "Procesar archivos mayores que RAM con .collect(engine=\"streaming\") (1.x rename de streaming=True).",
      "Hacer zero-copy interop con Arrow/DuckDB/pandas.",
      "Decidir Polars vs DuckDB vs pandas vs PySpark según tamaño + caso de uso."
    ],
    "topics": [
      "Eager vs Lazy API",
      "Expressions: paralelización implícita",
      "scan_parquet/scan_csv + predicate pushdown",
      "Streaming engine para datasets > RAM",
      "Arrow interop con DuckDB/pandas",
      "when().then().otherwise() y over()"
    ],
    "materials": [
      "Mismo NYC Yellow Taxi de Clase 210 (parquet, ~150 MB/mes, ~10 GB/año).",
      "Librerías: polars>=1.5, pyarrow, opcional duckdb para integración."
    ],
    "exercises": [
      "Eager vs Lazy benchmark: misma agregación con pl.read_parquet(...) (eager) y pl.scan_parquet(...).collect() (lazy). Compará tiempos. La diferencia es chica con dataset chico; aumenta dramáticamente con datasets >GB.",
      "Pandas → Polars: tomá un script pandas existente, traducí a Polars. Medí speedup. Casos comunes: groupby().agg() → group_by().agg(), .apply → expressions.",
      "Streaming: con un parquet de 5 GB (descargar 12 meses NYC Taxi), correr una agregación con .collect() y luego con .collect(engine=\"streaming\"). Comparar RAM peak (memory_profiler).",
      "Predicate pushdown explícito: pl.scan_parquet(\"data/\").filter(pl.col(\"date\") == \"2024-01-15\").select(\"fare\").collect() vs pl.read_parquet(\"data/\").filter(...).select(...). Mirá el plan con .explain().",
      "Polars + DuckDB: hacer la query principal en Polars; pasar el resultado a DuckDB con con.from_arrow(df.to_arrow()) para hacer una consulta SQL compleja."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-5-ingenieria-de-datos/211-polars-como-alternativa-moderna/notebook.ipynb"
  },
  {
    "id": "parte-5-ingenieria-de-datos/212-data-warehouses-bigquery-snowflake-duckdb",
    "number": 212,
    "slug": "212-data-warehouses-bigquery-snowflake-duckdb",
    "partSlug": "parte-5-ingenieria-de-datos",
    "title": "Data warehouses: BigQuery, Snowflake, DuckDB",
    "description": "Consultar y operar 3 data warehouses modernos desde Python: BigQuery (GCP, serverless, separación compute/storage), Snowflake (multi-cloud, virtual warehouses, time travel), DuckDB (embedded, OLAP local, no requiere ser…",
    "level": "Avanzado",
    "duration": "80 min",
    "theory": "Consultar y operar 3 data warehouses modernos desde Python: BigQuery (GCP, serverless, separación compute/storage), Snowflake (multi-cloud, virtual warehouses, time travel), DuckDB (embedded, OLAP local, no requiere server). Decidir cuál usar según escala, presupuesto y latencia.",
    "outcomes": [
      "Conectar a BigQuery (google-cloud-bigquery), Snowflake (snowflake-connector-python), DuckDB (duckdb) y ejecutar queries.",
      "Diseñar tablas con particionado (BigQuery: PARTITION BY date_field) y clustering (BigQuery, Snowflake) para reducir costos y latencia.",
      "Usar COPY INTO (Snowflake) y LOAD DATA (BigQuery) para bulk ingest desde S3/GCS.",
      "Aprovechar time travel (SELECT ... AT(TIMESTAMP => ...) Snowflake) para auditar / recuperar.",
      "Decidir DW: BigQuery (serverless, GCP-first), Snowflake (multi-cloud, separation, sharing), DuckDB (local/embedded), Redshift (legacy AWS)."
    ],
    "topics": [
      "Compute/storage separation",
      "Particionado vs clustering",
      "BigQuery: SQL standard + UDF + ML",
      "Snowflake: virtual warehouses, time travel, data sharing",
      "DuckDB: el DW que entra en pip install",
      "Costo: cómo NO gastar miles"
    ],
    "materials": [
      "BigQuery: bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2018 (GB-scale, gratis para query con free tier).",
      "DuckDB: local con parquets de NYC Taxi.",
      "Snowflake: trial 30 días con $400 de crédito.",
      "Librerías: duckdb>=1.0, google-cloud-bigquery, snowflake-connector-python."
    ],
    "exercises": [
      "DuckDB local: con = duckdb.connect(\"warehouse.duckdb\"). Cargá un parquet con CREATE TABLE trips AS SELECT FROM 'trips.parquet'. Hacé SELECT COUNT(), AVG(fare) FROM trips. Compará tiempo vs Polars (Clase 211).",
      "BigQuery query: from google.cloud import bigquery; client = bigquery.Client(project=\"...\"). client.query(\"SELECT borough, COUNT(*) FROM bigquery-public-data.new_york_taxi_trips.tlc_yellow_trips_2018 GROUP BY borough\"). Crítico: usar LIMIT en exploración, no escanear 100 GB sin querer.",
      "Particionado en BQ: crear tabla mi_proyecto.dataset.trips_partitioned con PARTITION BY DATE(pickup_datetime). Query con WHERE DATE(pickup_datetime) = '2018-01-15' → mostrá \"bytes processed\" con/sin partition filter.",
      "Snowflake time travel: CREATE TABLE x AS SELECT .... Insertá data. DELETE FROM x WHERE .... SELECT * FROM x AT(OFFSET => -60) (60s atrás) — los datos vuelven.",
      "DuckDB queryando S3 directo: con.execute(\"SELECT FROM 's3://bucket/path/.parquet' LIMIT 10\") sin descargar nada — DuckDB lee remoto con HTTPFS."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-5-ingenieria-de-datos/212-data-warehouses-bigquery-snowflake-duckdb/notebook.ipynb"
  },
  {
    "id": "parte-5-ingenieria-de-datos/213-streaming-intro-kafka-kinesis",
    "number": 213,
    "slug": "213-streaming-intro-kafka-kinesis",
    "partSlug": "parte-5-ingenieria-de-datos",
    "title": "Streaming intro: Kafka, Kinesis",
    "description": "Entender el modelo streaming vs batch (Clase 208), producir y consumir mensajes en Kafka (con confluent-kafka o kafka-python), comparar contra AWS Kinesis Data Streams (managed equivalent), y reconocer los 3 problemas c…",
    "level": "Avanzado",
    "duration": "85 min",
    "theory": "Entender el modelo streaming vs batch (Clase 208), producir y consumir mensajes en Kafka (con confluent-kafka o kafka-python), comparar contra AWS Kinesis Data Streams (managed equivalent), y reconocer los 3 problemas clásicos de streaming: exactly-once, out-of-order events, backpressure.",
    "outcomes": [
      "Diferenciar batch (datos llegan en bloques) de streaming (datos llegan continuos, baja latencia).",
      "Producir mensajes a un topic Kafka con keys (garantiza orden por key, distribuye load).",
      "Consumir con consumer groups: partitions distribuidas entre consumers, offset management.",
      "Diseñar para at-least-once (default razonable) y entender qué requiere exactly-once (transactional API).",
      "Decidir Kafka (self-hosted o Confluent Cloud) vs Kinesis (AWS) vs Pub/Sub (GCP) vs Event Hubs (Azure)."
    ],
    "topics": [
      "Batch vs streaming — el espectro real",
      "Kafka model: topic, partition, offset",
      "Producer: keys, acks, idempotence",
      "Consumer groups + rebalancing",
      "Delivery semantics: at-most/at-least/exactly-once",
      "Kinesis comparison"
    ],
    "materials": [
      "Kafka local: docker-compose con Kafka (KRaft mode, sin Zookeeper) + Kafka UI.",
      "Stream sintético: producer genera \"click events\" cada 100 ms.",
      "Librerías: confluent-kafka>=2.5 (más robusta) o kafka-python>=2.0 (más simple), faker para data sintética."
    ],
    "exercises": [
      "Setup local: docker-compose con Kafka + Kafka UI. Crear topic clicks con 4 partitions. Verificar con docker exec kafka kafka-topics --list ....",
      "Producer: script Python que produce 1000 mensajes con key=user_id, value={\"page\":\"/foo\",\"ts\":...}. Verificar en Kafka UI que mensajes con mismo user_id caen en la misma partition.",
      "Consumer 1 instancia: consumer.subscribe(['clicks']) + loop for msg in consumer. Procesar = print(msg.value()). Commitear offset cada 100 mensajes.",
      "Consumer group, 2 instancias: levantar 2 consumers con mismo group.id. Confirmar que se reparten las 4 partitions (2-2). Matar uno, observar rebalancing — el otro toma las 4.",
      "At-least-once explícito: enable.auto.commit=False, procesar mensaje, consumer.commit(). Si crash entre procesar y commit → duplicate al reiniciar."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-5-ingenieria-de-datos/213-streaming-intro-kafka-kinesis/notebook.ipynb"
  },
  {
    "id": "parte-5-ingenieria-de-datos/214-formatos-columnares-parquet-avro",
    "number": 214,
    "slug": "214-formatos-columnares-parquet-avro",
    "partSlug": "parte-5-ingenieria-de-datos",
    "title": "Formatos columnares: Parquet, Avro",
    "description": "Elegir formato de almacenamiento según el patrón de lectura: Parquet (columnar, OLAP, queries analíticas), Avro (row-based, OLTP/streaming, schema evolution), ORC (columnar, Hive ecosystem).",
    "level": "Avanzado",
    "duration": "70 min",
    "theory": "Elegir formato de almacenamiento según el patrón de lectura: Parquet (columnar, OLAP, queries analíticas), Avro (row-based, OLTP/streaming, schema evolution), ORC (columnar, Hive ecosystem). Entender por qué Parquet es 5-100× más rápido que CSV para queries analíticas, y por qué Avro domina en Kafka.",
    "outcomes": [
      "Convertir CSV → Parquet con pandas.to_parquet / polars.write_parquet / pyarrow.",
      "Diferenciar row-based (CSV, JSON, Avro) de columnar (Parquet, ORC) y elegir según query pattern.",
      "Aprovechar column pruning + predicate pushdown + row group pruning de Parquet (Polars/DuckDB/Spark lo hacen automático).",
      "Aplicar compresión (snappy default, zstd mejor ratio, gzip mejor compat) y entender trade-off CPU vs tamaño.",
      "Definir un schema Avro y usarlo en Kafka con Schema Registry (concept)."
    ],
    "topics": [
      "Row vs columnar",
      "Parquet anatomy: file > row group > column chunk > page",
      "Compresión: snappy, zstd, gzip, lz4",
      "Dictionary encoding, RLE",
      "Avro: schema-first, row-based, compact binary",
      "Schema evolution: forward/backward/full compat"
    ],
    "materials": [
      "Dataset: NYC Taxi (CSV ~2 GB/mes) — convertir a Parquet (~150 MB/mes).",
      "Librerías: pyarrow>=15, polars, duckdb, fastavro (Avro)."
    ],
    "exercises": [
      "CSV → Parquet: descargá NYC Taxi 1 mes en CSV. Cargá con pandas, escribí Parquet snappy. Comparar tamaños (CSV vs Parquet) y tiempo de query (COUNT WHERE borough='Manhattan').",
      "Compresión benchmark: mismo dataset, escribir con snappy, zstd, gzip, lz4. Reportar tamaño + tiempo de lectura. (Hint: zstd suele ganar en ratio; snappy en speed).",
      "Predicate pushdown: en DuckDB, EXPLAIN ANALYZE SELECT FROM parquet WHERE pickup_date='2024-01-15'. Compará \"rows read\" vs SELECT FROM parquet sin WHERE.",
      "Row groups y stats: con pyarrow.parquet.ParquetFile(path).metadata, inspeccioná min/max/null_count por columna por row group.",
      "Avro schema + roundtrip: definí schema Avro para evento de click. Serializá 1000 eventos con fastavro, deserializá. Compará tamaño con JSON puro."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-5-ingenieria-de-datos/214-formatos-columnares-parquet-avro/notebook.ipynb"
  },
  {
    "id": "parte-5-ingenieria-de-datos/215-modelado-dimensional-star-snowflake-schemas",
    "number": 215,
    "slug": "215-modelado-dimensional-star-snowflake-schemas",
    "partSlug": "parte-5-ingenieria-de-datos",
    "title": "Modelado dimensional: star/snowflake schemas",
    "description": "Diseñar el esquema de un data warehouse usando modelado dimensional (Kimball): una fact table central + dimension tables alrededor (star schema), o dimensiones normalizadas (snowflake schema).",
    "level": "Avanzado",
    "duration": "75 min",
    "theory": "Diseñar el esquema de un data warehouse usando modelado dimensional (Kimball): una fact table central + dimension tables alrededor (star schema), o dimensiones normalizadas (snowflake schema). Es el modelo que han usado los data warehouses serios desde los 90s y sigue vigente en BigQuery/Snowflake/dbt en 2026.",
    "outcomes": [
      "Identificar fact tables (eventos medibles: sale, click, payment) vs dimension tables (entidades descriptivas: customer, product, date).",
      "Diseñar un star schema con fact + dimensions desnormalizadas.",
      "Manejar slowly changing dimensions (SCD): Tipo 1 (overwrite), Tipo 2 (history con valid_from/valid_to), Tipo 3 (current + previous).",
      "Crear una date dimension completa (con feriados, fiscal year, etc.) — la dimensión más reutilizada.",
      "Diferenciar OLAP (modelado dimensional, query analíticas) de 3NF (modelado normalizado, OLTP)."
    ],
    "topics": [
      "Star schema: fact + dims",
      "Snowflake schema: dims normalizadas",
      "Surrogate keys vs natural keys",
      "Slowly Changing Dimensions (SCD 1/2/3)",
      "Date dimension",
      "Granularidad de la fact"
    ],
    "materials": [
      "Caso ejemplo: e-commerce con tablas operacionales orders, order_items, products, customers. Transformar a star schema.",
      "Librerías: DuckDB/SQL puro (las tablas son SQL, no Python)."
    ],
    "exercises": [
      "Identificar grain: dado un dataset de pedidos de e-commerce, decidí el grain de tu fact. ¿\"1 row per order\"? ¿\"1 row per order line\"? Elegí, justificá.",
      "Date dimension: SQL que genera dim_date con 5 años de días, columnas year, quarter, month, day_of_week_iso, is_weekend, is_holiday_us, fiscal_year. (generate_series de Postgres/DuckDB).",
      "Star schema: del e-commerce, diseñá fact_sales(date_key, product_key, customer_key, store_key, qty, revenue, discount), dim_product, dim_customer, dim_store, dim_date. SQL completo.",
      "SCD Tipo 2 en dim_customer: cliente cambia de ciudad. Tu pipeline detecta el cambio → UPDATE la fila vigente con valid_to=NOW(), is_current=FALSE → INSERT nueva fila con valid_from=NOW(), is_current=TRUE. Toda venta del cliente queda asociada a su ciudad al momento de la compra.",
      "Query típica: \"Revenue por brand × month × is_weekend\" — escribíla con JOINs entre fact + dims + dim_date. Comparala con la equivalente en tablas no-modeladas (más JOINs, más subqueries)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-5-ingenieria-de-datos/215-modelado-dimensional-star-snowflake-schemas/notebook.ipynb"
  },
  {
    "id": "parte-6-sistemas-de-recomendacion/216-filtrado-colaborativo-user-based-e-item-based",
    "number": 216,
    "slug": "216-filtrado-colaborativo-user-based-e-item-based",
    "partSlug": "parte-6-sistemas-de-recomendacion",
    "title": "Filtrado colaborativo: user-based e item-based",
    "description": "Construir el recomendador más antiguo y todavía usado: filtrado colaborativo basado en vecinos (kNN).",
    "level": "Intermedio-Avanzado",
    "duration": "75 min",
    "theory": "Construir el recomendador más antiguo y todavía usado: filtrado colaborativo basado en vecinos (kNN). Calcular similitudes user-user e item-item sobre una matriz usuario-item dispersa, generar top-N recomendaciones, y entender por qué Amazon publicó en 2003 que item-based gana a user-based en escala (computar similitudes item-item es offline y estable).",
    "outcomes": [
      "Representar las interacciones usuario-item en una scipy.sparse.csr_matrix (típicamente >99% sparse).",
      "Calcular similitud coseno, Pearson y Jaccard entre filas (users) o columnas (items).",
      "Generar top-N recomendaciones user-based: predicted_rating = Σ sim(u, v) * rating(v, i) / Σ sim(u, v).",
      "Generar top-N recomendaciones item-based: score(u, i) = Σ sim(i, j) * interaction(u, j).",
      "Reconocer límites: sparsity → similitudes ruidosas; cold-start → items/users nuevos sin recomendaciones (Clase 221)."
    ],
    "topics": [
      "Matriz usuario-item: dense vs sparse",
      "Similitud coseno, Pearson, Jaccard",
      "User-based kNN",
      "Item-based kNN",
      "Implicit vs explicit feedback",
      "Mean centering"
    ],
    "materials": [
      "Dataset: MovieLens 100K (ml-100k, ~1 MB, ~100K ratings de 943 users × 1682 movies). El clásico para empezar.",
      "Librerías: scipy.sparse, numpy, pandas, scikit-learn (para cosine_similarity)."
    ],
    "exercises": [
      "Sparse matrix: cargar MovieLens 100K. Construir R como csr_matrix shape (n_users, n_items). Verificar sparsity: (1 - R.nnz / np.prod(R.shape)).",
      "User similarity: sim_users = cosine_similarity(R) — devuelve (n_users, n_users). Encontrar los 5 más similares a user_id=42.",
      "User-based top-10: para user_id=42, predecir score para items no vistos como R.T @ sim_users[42] (broadcasting). Recomendar top-10 que aún no vio.",
      "Item-based top-10: sim_items = cosine_similarity(R.T) (ahora (n_items, n_items)). Para user_id=42, score = R[42] @ sim_items. Mostrar top-10.",
      "Pearson + mean centering: R_centered = R - user_means.reshape(-1, 1) (cuidado con sparse — usar sklearn). Comparar recomendaciones con coseno vanilla."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-6-sistemas-de-recomendacion/216-filtrado-colaborativo-user-based-e-item-based/notebook.ipynb"
  },
  {
    "id": "parte-6-sistemas-de-recomendacion/217-factorizacion-de-matrices-svd-als",
    "number": 217,
    "slug": "217-factorizacion-de-matrices-svd-als",
    "partSlug": "parte-6-sistemas-de-recomendacion",
    "title": "Factorización de matrices: SVD, ALS",
    "description": "Reemplazar la matriz usuario-item dispersa por dos matrices densas de baja dimensión: R ≈ P × Q^T donde P (n_users × k) y Q (n_items × k).",
    "level": "Intermedio-Avanzado",
    "duration": "80 min",
    "theory": "Reemplazar la matriz usuario-item dispersa por dos matrices densas de baja dimensión: R ≈ P × Q^T donde P (n_users × k) y Q (n_items × k). Aprender los embeddings k-dimensionales que capturan los factores latentes (género de película, gusto del usuario). Usar SVD (cuando hay datos completos) y ALS (Alternating Least Squares — robusto a sparse). Implicit-feedback ALS (Hu et al. 2008) es el algoritmo que ganó la mayoría de los Netflix Prize spin-offs en producción.",
    "outcomes": [
      "Explicar el modelo r̂(u, i) = p_u · q_i + b_u + b_i + μ (con biases).",
      "Aplicar SVD truncado sobre matriz densa (poco realista, pero base teórica).",
      "Implementar ALS explicit (rating predicho) y ALS implicit (con confidence weighting c_ui = 1 + α × r_ui).",
      "Elegir hiperparámetros: factors (típicamente 20-200), regularization (λ para evitar overfitting), iterations (10-30).",
      "Usar implicit.AlternatingLeastSquares (Cython, multi-thread, rápido)."
    ],
    "topics": [
      "Modelo latente: factores escondidos",
      "SVD vs SVD truncado vs ALS",
      "Biases: μ, b_u, b_i",
      "Implicit feedback + confidence",
      "Regularización L2",
      "Cold-start parcial: con biases"
    ],
    "materials": [
      "Explicit: MovieLens 1M con ratings 1-5.",
      "Implicit: Last.fm \"lastfm-360K\" o convertir MovieLens (rating ≥ 4 = \"le gustó\" = 1).",
      "Librerías: implicit>=0.7 (ALS rápido en Cython), scipy.sparse.linalg.svds, opcional surprise."
    ],
    "exercises": [
      "SVD truncado: tomar matriz R densa imputando 0. U, sigma, Vt = svds(R, k=20). Reconstruir R̂ = U × diag(sigma) × Vt. Verificar que R̂ predice valores no-cero similares y \"rellena\" los ceros con guesses.",
      "ALS explicit con Surprise: from surprise import SVD; algo = SVD(n_factors=50, n_epochs=20). algo.fit(trainset). Predict algo.predict(user, item). RMSE sobre test split.",
      "ALS implicit con implicit: model = implicit.als.AlternatingLeastSquares(factors=64, regularization=0.05, iterations=15). model.fit(R_train * 40) (multiplicar por α=40). model.recommend(user_id, R_train[user_id], N=10).",
      "Inspeccionar embeddings: PCA de model.item_factors a 2D y plot. Items \"parecidos\" deben caer cerca.",
      "Biases analysis: imprimir top 10 movies por b_i (las que todos aman / odian) y top 10 usuarios por b_u."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-6-sistemas-de-recomendacion/217-factorizacion-de-matrices-svd-als/notebook.ipynb"
  },
  {
    "id": "parte-6-sistemas-de-recomendacion/218-content-based-filtering",
    "number": 218,
    "slug": "218-content-based-filtering",
    "partSlug": "parte-6-sistemas-de-recomendacion",
    "title": "Content-based filtering",
    "description": "Recomendar items basándose en sus atributos (texto, género, categoría) en vez de interacciones — útil cuando hay cold-start de items (Clase 221) o cuando los items tienen rica metadata.",
    "level": "Intermedio-Avanzado",
    "duration": "70 min",
    "theory": "Recomendar items basándose en sus atributos (texto, género, categoría) en vez de interacciones — útil cuando hay cold-start de items (Clase 221) o cuando los items tienen rica metadata. Combinar TF-IDF / embeddings sobre descripciones + scoring por similitud al perfil del usuario.",
    "outcomes": [
      "Construir un item profile desde texto + features categóricas con TF-IDF / one-hot.",
      "Construir un user profile como agregado ponderado de items que le gustaron.",
      "Calcular score(u, i) = cos(user_profile, item_profile) y rankear.",
      "Reemplazar TF-IDF por embeddings modernos (sentence-transformers) para entender semántica.",
      "Reconocer límites: serendipia baja (recomienda variantes de lo conocido); sobreespecialización."
    ],
    "topics": [
      "TF-IDF + cosine similarity",
      "One-hot vs multi-hot features categóricas",
      "User profile como media ponderada",
      "Embeddings semánticos (sentence-transformers)",
      "FAISS para top-N rápido",
      "Hybrid con CF (Clase 219)"
    ],
    "materials": [
      "Dataset: MovieLens + sinopsis (de TMDB API) o kaggle/the-movies-dataset.",
      "Librerías: scikit-learn (TfidfVectorizer), sentence-transformers, opcional faiss-cpu."
    ],
    "exercises": [
      "TF-IDF base: cargar movies con title + overview + genres. TfidfVectorizer(max_features=10000, ngram_range=(1,2)). Matrix shape (n_items, 10000).",
      "Item-item similarity: cosine_similarity(tfidf_matrix). Para Toy Story, mostrar top-10 más similares — deberían ser otras animaciones.",
      "User profile: para user_id=42, tomar items rateados ≥4. user_profile = mean(item_profiles) (ponderado por rating). Recomendar top-10.",
      "Embeddings modernos: model = SentenceTransformer('all-MiniLM-L6-v2'). Generar embeddings de cada movie. Comparar top-10 de TF-IDF vs embeddings — los embeddings entienden semántica.",
      "FAISS rápido: index = faiss.IndexFlatIP(384); index.add(embeddings). index.search(user_profile, k=10) → top-10 en <1 ms aunque haya 1M items."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-6-sistemas-de-recomendacion/218-content-based-filtering/notebook.ipynb"
  },
  {
    "id": "parte-6-sistemas-de-recomendacion/219-recomendadores-hibridos",
    "number": 219,
    "slug": "219-recomendadores-hibridos",
    "partSlug": "parte-6-sistemas-de-recomendacion",
    "title": "Recomendadores híbridos",
    "description": "Combinar CF (filtrado colaborativo, Clase 216-217) + content-based (Clase 218) para conseguir lo mejor de ambos: serendipia + cold-start + explicabilidad.",
    "level": "Intermedio-Avanzado",
    "duration": "75 min",
    "theory": "Combinar CF (filtrado colaborativo, Clase 216-217) + content-based (Clase 218) para conseguir lo mejor de ambos: serendipia + cold-start + explicabilidad. Aplicar los 7 patrones de hybrid de Burke (2002) y usar LightFM (que aprende un modelo único con CF + features).",
    "outcomes": [
      "Diferenciar los 7 patrones de hybrid: weighted, switching, mixed, feature combination, cascade, feature augmentation, meta-level.",
      "Implementar un hybrid weighted: score = α × score_cf + (1-α) × score_content.",
      "Implementar un hybrid switching: usar content para users con <N interactions, CF para el resto.",
      "Usar LightFM como hybrid built-in: el modelo aprende embeddings que combinan CF + content features.",
      "Tunear α con validation y entender por qué α óptimo varía por user/item segment."
    ],
    "topics": [
      "7 patrones de Burke (2002)",
      "Weighted hybrid: α × CF + (1-α) × CB",
      "Switching: cold-start triage",
      "LightFM: hybrid aprendido",
      "Tuning α por segmento",
      "Two-tower modelo (concept)"
    ],
    "materials": [
      "Dataset: MovieLens 100K con u.item que tiene géneros (19 binarios).",
      "Librerías: lightfm>=1.17, scipy.sparse, pandas."
    ],
    "exercises": [
      "Weighted hybrid manual: tomar scores de Clase 217 (ALS) y Clase 218 (content-based). Combinar score = α × cf + (1-α) × cb para α ∈ {0, 0.25, 0.5, 0.75, 1}. Reportar NDCG@10 para cada α.",
      "Switching por user: si interactions(u) < 5: usar content; si no: usar CF. Comparar contra weighted para users en distintos segmentos (new/mature).",
      "LightFM hybrid: entrenar LightFM(loss='warp') con item_features (géneros) y user_features (demographics). Comparar NDCG vs pure CF (sin features).",
      "Cold-start eval: held-out incluye items nuevos (no en train) y users nuevos (sin ratings). Comparar pure CF (~0%), pure content (~OK), LightFM hybrid (~mejor).",
      "Cascade: top-100 con CF, re-rankear top-10 con content (boost a items con descripción similar al historial del user)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-6-sistemas-de-recomendacion/219-recomendadores-hibridos/notebook.ipynb"
  },
  {
    "id": "parte-6-sistemas-de-recomendacion/220-metricas-map-k-ndcg-recall-k",
    "number": 220,
    "slug": "220-metricas-map-k-ndcg-recall-k",
    "partSlug": "parte-6-sistemas-de-recomendacion",
    "title": "Métricas: MAP@k, NDCG, recall@k",
    "description": "Evaluar recomendadores con las métricas correctas: NO accuracy ni RMSE de rating (irrelevante para top-N).",
    "level": "Intermedio-Avanzado",
    "duration": "70 min",
    "theory": "Evaluar recomendadores con las métricas correctas: NO accuracy ni RMSE de rating (irrelevante para top-N). Sí recall@k (¿cuántos relevantes recuperaste en top-k?), precision@k (¿qué % del top-k es relevante?), MAP@k (precision promedio sensible al ranking), NDCG@k (gain descontado por posición). Decidir qué métrica reportar según objetivo de negocio.",
    "outcomes": [
      "Calcular precision@k, recall@k, F1@k, hit rate desde cero.",
      "Calcular MAP@k (Mean Average Precision) y entender por qué sensible al ranking dentro del top-k.",
      "Calcular NDCG@k (Normalized Discounted Cumulative Gain) y entender el descuento logarítmico.",
      "Diseñar el split correcto: leave-one-out por user vs temporal split vs random.",
      "Decidir métrica según objetivo: recall (catálogo grande, descubrimiento) vs NDCG (orden importa) vs MAP (búsqueda)."
    ],
    "topics": [
      "Por qué NO usar RMSE de rating",
      "Precision@k vs recall@k",
      "MAP@k: precision promediada por posición",
      "NDCG@k con descuento log2(i+1)",
      "Leave-one-out vs temporal split",
      "Coverage + diversity (beyond accuracy)"
    ],
    "materials": [
      "Dataset: MovieLens 100K.",
      "Librerías: numpy puro (las métricas son fáciles), opcional recmetrics."
    ],
    "exercises": [
      "Implementar precision@k, recall@k: dadas listas [1, 0, 0, 1, 0] (relevancia) y k=5, calcular. Verificar contra recmetrics u otra librería.",
      "MAP@k: implementar AP@k. Mostrar diferencia con precision@k: AP penaliza tener los relevantes al final.",
      "NDCG@k: implementar DCG y iDCG. Mostrar caso donde recall@k es igual pero NDCG distinto porque el orden cambia.",
      "Leave-one-out por user: para cada user con ≥5 ratings, dejar el último (cronológico o random) para test, resto para train. Evaluar.",
      "Coverage y diversity: para 1000 users, ¿qué % del catálogo fue recomendado? Diversidad media intra-list (cosine entre items recomendados)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-6-sistemas-de-recomendacion/220-metricas-map-k-ndcg-recall-k/notebook.ipynb"
  },
  {
    "id": "parte-6-sistemas-de-recomendacion/221-cold-start-problem",
    "number": 221,
    "slug": "221-cold-start-problem",
    "partSlug": "parte-6-sistemas-de-recomendacion",
    "title": "Cold-start problem",
    "description": "Cuándo un user o item es \"nuevo\" (0 interacciones), CF (Clase 216-217) no funciona.",
    "level": "Intermedio-Avanzado",
    "duration": "70 min",
    "theory": "Cuándo un user o item es \"nuevo\" (0 interacciones), CF (Clase 216-217) no funciona. Estrategias concretas para los 3 tipos de cold-start: user cold-start (onboarding), item cold-start (catalog launch), system cold-start (lanzamiento del producto). Las estrategias correctas son la diferencia entre un recomendador útil desde el día 1 vs uno inútil hasta el mes 6.",
    "outcomes": [
      "Diferenciar user cold-start (usuario nuevo), item cold-start (item nuevo), system cold-start (todo nuevo).",
      "Aplicar popularity fallback con shrinkage Bayesiano ((c + m × C) / (n + m)) para users sin historia.",
      "Diseñar onboarding explícito (pedir N preferencias antes de personalizar).",
      "Usar content features (Clase 218) para items nuevos.",
      "Aplicar exploration-exploitation con bandits (epsilon-greedy, Thompson sampling) para users mid-cold-start."
    ],
    "topics": [
      "3 tipos de cold-start",
      "Popularity fallback",
      "Bayesian shrinkage para popularity",
      "Onboarding: preguntar al user",
      "Content-based para item cold-start",
      "Bandits para explorar"
    ],
    "materials": [
      "Dataset: MovieLens 100K + new users / new items simulados.",
      "Librerías: numpy, opcional vowpalwabbit (bandits), scikit-learn."
    ],
    "exercises": [
      "Popularity baseline: rankear items por n_ratings. Top-10 son siempre los mismos. Evaluar recall@10 para users cold-start (con 0 interactions).",
      "Bayesian shrinkage: implementar (sum + m × C) / (n + m) con m=10, C=mean_rating. Comparar top-10 con popularity vanilla. Items con pocos ratings caen al promedio.",
      "Onboarding 3 géneros: simular que user nuevo elige [\"Action\", \"Sci-Fi\", \"Comedy\"]. Recomendar top-10 movies de esos géneros (content-based + popularity tiebreaker).",
      "Item cold-start: agregar 10 movies nuevas con descripción pero 0 ratings. Content-based (Clase 218) las puede ranquear; CF no. Demostrar.",
      "Epsilon-greedy: en cada slot del top-10, con prob ε=0.1 recomendar item random (explore), con prob 0.9 recomendar el \"best\" del modelo (exploit). Medir coverage en N usuarios."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-6-sistemas-de-recomendacion/221-cold-start-problem/notebook.ipynb"
  },
  {
    "id": "parte-6-sistemas-de-recomendacion/222-librerias-lightfm-implicit-surprise",
    "number": 222,
    "slug": "222-librerias-lightfm-implicit-surprise",
    "partSlug": "parte-6-sistemas-de-recomendacion",
    "title": "Librerías: LightFM, Implicit, Surprise",
    "description": "Conocer las librerías de recomendación que vas a usar en la vida real sin tener que reimplementar lo de Clases 216-221.",
    "level": "Intermedio-Avanzado",
    "duration": "70 min",
    "theory": "Conocer las librerías de recomendación que vas a usar en la vida real sin tener que reimplementar lo de Clases 216-221. Decidir cuál usar según: tipo de feedback (explicit/implicit), tamaño del dataset, features disponibles, integración con stack.",
    "outcomes": [
      "Usar Surprise para algoritmos clásicos explicit (KNNBasic, SVD, SVD++, NMF, Co-Clustering) con API tipo sklearn.",
      "Usar Implicit para ALS implicit, BPR, Logistic MF — la opción más rápida en Python para datasets grandes.",
      "Usar LightFM cuando tenés features (Clase 219 hybrid).",
      "Conocer TensorFlow Recommenders y Spotlight (PyTorch) para arquitecturas deep (two-tower, sequential).",
      "Decidir librería según: explicit vs implicit, escala, features, deployment target."
    ],
    "topics": [
      "Surprise: explicit, didáctica",
      "Implicit: ALS/BPR Cython",
      "LightFM: CF + features",
      "TF Recommenders + Spotlight",
      "Spark pyspark.ml.recommendation.ALS",
      "Vector DBs (FAISS, Milvus, Pinecone)"
    ],
    "materials": [
      "Dataset: MovieLens 100K y 1M.",
      "Librerías: scikit-surprise, implicit>=0.7, lightfm>=1.17, opcional tensorflow-recommenders."
    ],
    "exercises": [
      "Surprise SVD: from surprise import SVD, Dataset; data = Dataset.load_builtin('ml-100k'); algo = SVD(); cross_validate(algo, data, measures=['RMSE','MAE'], cv=5). Reportar RMSE.",
      "Implicit ALS: model = implicit.als.AlternatingLeastSquares(factors=64, regularization=0.05, iterations=20). model.fit(R_sparse * 40). recommend(user_id, R[user_id], N=10).",
      "Implicit BPR: mismo modelo pero implicit.bpr.BayesianPersonalizedRanking(factors=64). Comparar NDCG vs ALS.",
      "LightFM: LightFM(loss='warp', no_components=32). Con item features (géneros). Comparar pure CF vs hybrid.",
      "Benchmarking: mismo dataset, mismo split, las 4 librerías. Tabla con NDCG@10, recall@10, tiempo entrenamiento, tiempo predict."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-6-sistemas-de-recomendacion/222-librerias-lightfm-implicit-surprise/notebook.ipynb"
  },
  {
    "id": "parte-7-etica-fairness-privacidad/223-tipos-de-sesgo-algoritmico-y-origenes",
    "number": 223,
    "slug": "223-tipos-de-sesgo-algoritmico-y-origenes",
    "partSlug": "parte-7-etica-fairness-privacidad",
    "title": "Tipos de sesgo algorítmico y orígenes",
    "description": "Aprender a nombrar y diagnosticar el origen del sesgo en un sistema ML antes de intentar mitigarlo.",
    "level": "Intermedio",
    "duration": "75 min",
    "theory": "Aprender a nombrar y diagnosticar el origen del sesgo en un sistema ML antes de intentar mitigarlo. Un modelo \"sesgado\" no es un bug: es el resultado de decisiones tomadas en cada fase del life cycle (recolección, medición, modelado, evaluación, despliegue). Si no sabemos dónde entró el sesgo, no podemos elegir la mitigación correcta (Clases 225-227).",
    "outcomes": [
      "Distinguir los 6 tipos del framework Suresh-Guttag: histórico, representación, medición, agregación, evaluación, despliegue.",
      "Identificar el origen probable de un sesgo dado evidencia empírica (gap de accuracy entre subgrupos, drift, proxy-target gap).",
      "Reproducir el patrón de Gender Shades (Buolamwini & Gebru 2018): accuracy alta global, accuracy baja en subgrupo minoritario.",
      "Reconocer Simpson's paradox y por qué un modelo único puede ser peor que un modelo por subgrupo.",
      "Justificar por qué fairness no es solo un problema del modelo — empieza en la definición de la tarea."
    ],
    "topics": [
      "Sesgo histórico",
      "Sesgo de representación",
      "Sesgo de medición",
      "Sesgo de agregación",
      "Sesgo de evaluación",
      "Sesgo de despliegue"
    ],
    "materials": [
      "Dataset: sintético (préstamos con sesgo histórico inyectado). Auto-generado en el notebook con numpy seed 42.",
      "Librerías: numpy, pandas, scikit-learn. Sin descargas externas."
    ],
    "exercises": [
      "Sesgo histórico: generar un dataset de préstamos donde P(aprobado | grupo=A) = 0.70 y P(aprobado | grupo=B) = 0.30 por razones históricas (no por capacidad de pago). Entrenar LogisticRegression sin la feature grupo y mostrar que el modelo igual reproduce el gap vía proxies (código postal, ingreso, etc.).",
      "Selection rate disparity: calcular P(ŷ=1 | grupo=A) vs P(ŷ=1 | grupo=B) — la métrica más simple de demographic parity (Clase 224).",
      "Sesgo de representación (Gender Shades): re-muestrear el dataset al 10% del grupo B. Reportar accuracy global vs accuracy por subgrupo. Mostrar el patrón \"97% global, 60% en B\".",
      "Sesgo de medición: definir y_proxy = y_true XOR ruido_correlacionado_con_grupo. Entrenar sobre y_proxy. Mostrar que el modelo aprende el patrón del ruido, no del target real.",
      "Sesgo de agregación (Simpson): comparar AUC de un modelo único vs un modelo por subgrupo. Mostrar que el modelo único es subóptimo en ambos subgrupos."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-7-etica-fairness-privacidad/223-tipos-de-sesgo-algoritmico-y-origenes/notebook.ipynb"
  },
  {
    "id": "parte-7-etica-fairness-privacidad/224-metricas-de-fairness-demographic-parity-equalized-odds-calibration",
    "number": 224,
    "slug": "224-metricas-de-fairness-demographic-parity-equalized-odds-calibration",
    "partSlug": "parte-7-etica-fairness-privacidad",
    "title": "Métricas de fairness: demographic parity, equalized odds, calibration",
    "description": "Pasar de \"el modelo es injusto\" a medirlo con un número.",
    "level": "Intermedio",
    "duration": "75 min",
    "theory": "Pasar de \"el modelo es injusto\" a medirlo con un número. Implementar las tres familias de métricas grupales que dominan la literatura — demographic parity, equalized odds, calibration — sobre un dataset binario con atributo protegido, y demostrar numéricamente el teorema de imposibilidad de Kleinberg-Mullainathan-Raghavan / Chouldechova (2017): salvo casos triviales, no se pueden satisfacer las tres a la vez.",
    "outcomes": [
      "Calcular demographic parity gap = |P(Ŷ=1|A=0) − P(Ŷ=1|A=1)| sobre predicciones de cualquier clasificador binario.",
      "Calcular equal opportunity (TPR por grupo) y equalized odds (TPR y FPR por grupo) — Hardt, Price, Srebro 2016.",
      "Verificar calibración por grupo con reliability curves: P(Y=1|Ŝ=s, A=a) debe ser igual entre grupos para un mismo score s.",
      "Demostrar el teorema de imposibilidad: ajustar threshold por grupo para forzar demographic parity rompe calibración.",
      "Aplicar mitigación post-processing con thresholds por grupo (Hardt 2016) y reportar el trade-off accuracy vs fairness gap."
    ],
    "topics": [
      "Atributo protegido A y notación Y / Ŷ / Ŝ",
      "Demographic parity (statistical parity)",
      "Equal opportunity y equalized odds (Hardt 2016)",
      "Calibration por grupo (Chouldechova 2017)",
      "Teorema de imposibilidad (KMR / Chouldechova 2017)",
      "Post-processing: threshold por grupo"
    ],
    "materials": [
      "Dataset notebook: sintético binario con un atributo protegido A∈{0,1} y base rates diferentes (60% vs 40%) — necesario para que el teorema de imposibilidad se active.",
      "Dataset real recomendado para tarea: Adult / Census Income (UCI) con sex como atributo protegido, o COMPAS (ProPublica) con race.",
      "Librerías: numpy, pandas, scikit-learn. Opcional: fairlearn."
    ],
    "exercises": [
      "Selection rate por grupo: entrenar LogisticRegression baseline. Calcular P(Ŷ=1|A=0) y P(Ŷ=1|A=1) y el DP_gap. ¿Cumple regla del 80%?",
      "TPR y FPR por grupo: armar confusion_matrix separada por grupo. Calcular equal_opportunity_gap = |TPR_0 − TPR_1| y equalized_odds_gap = max(|TPR_diff|, |FPR_diff|).",
      "Calibration curves por grupo: binning de scores en 10 bins. Para cada bin y cada grupo, graficar mean(y_true) vs mean(y_score). ¿Las curvas coinciden?",
      "Romper calibración: ajustar threshold por grupo (t_0, t_1) tal que se cumpla DP exacta. Recalcular calibración — debe degradarse. (Demostración numérica del teorema.)",
      "Post-processing Hardt: buscar (t_0, t_1) que minimicen equalized_odds_gap y reportar el costo en accuracy global. Tabla: baseline vs DP-fixed vs EO-fixed."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-7-etica-fairness-privacidad/224-metricas-de-fairness-demographic-parity-equalized-odds-calibration/notebook.ipynb"
  },
  {
    "id": "parte-7-etica-fairness-privacidad/225-privacidad-diferencial-intro",
    "number": 225,
    "slug": "225-privacidad-diferencial-intro",
    "partSlug": "parte-7-etica-fairness-privacidad",
    "title": "Privacidad diferencial: intro",
    "description": "Entender privacidad diferencial (DP) como la única definición formal de privacidad con garantías matemáticas — no \"anonimización\" heurística que se rompe con un join.",
    "level": "Intermedio",
    "duration": "75 min",
    "theory": "Entender privacidad diferencial (DP) como la única definición formal de privacidad con garantías matemáticas — no \"anonimización\" heurística que se rompe con un join. Implementar el mecanismo de Laplace desde cero, observar el trade-off privacy-utility vía el presupuesto ε (epsilon), y mirar conceptualmente DP-SGD (Abadi et al. 2016): cómo se entrena un modelo sin que un atacante pueda inferir si tu registro estuvo en el training set.",
    "outcomes": [
      "Enunciar la definición de (ε, δ)-DP: P[M(D) ∈ S] ≤ e^ε · P[M(D') ∈ S] + δ para datasets vecinos D, D'.",
      "Calcular la sensibilidad Δf de funciones típicas (conteos, sumas acotadas, medias) y elegir ruido Laplace o Gaussiano calibrado.",
      "Implementar laplace_mechanism(value, sensitivity, epsilon) y verificar que ε chico → más ruido → menos utilidad.",
      "Aplicar composición básica: k consultas con ε cada una gastan k·ε del presupuesto total.",
      "Reconocer la idea de DP-SGD: per-sample gradient clipping + ruido gaussiano → entrenamiento DP (Opacus, TF-Privacy)."
    ],
    "topics": [
      "Anonimización falla (Netflix Prize, AOL search logs)",
      "Definición (ε, δ)-DP y datasets vecinos",
      "Sensibilidad Δf",
      "Mecanismos Laplace y Gaussiano",
      "Composición y post-processing",
      "DP-SGD (Abadi 2016)"
    ],
    "materials": [
      "Dataset: sintético — un dataframe de salarios n=10_000 con valores en [0, 200_000]. Suficiente para Laplace, mean privado, histograma y DP-SGD demo. Sin descarga externa.",
      "Librerías: numpy, pandas, scikit-learn. En producción real: opacus (PyTorch), tensorflow-privacy, diffprivlib (IBM)."
    ],
    "exercises": [
      "Laplace básico: implementar laplace_mechanism(value, sensitivity, epsilon) y verificar empíricamente sobre 10_000 corridas que la varianza es 2·(Δf/ε)².",
      "Conteo privado: contar empleados con salario > 100k con ε ∈ {0.1, 1.0, 10.0}. Reportar error medio absoluto y discutir el trade-off.",
      "Mean privado con clipping: clip salarios a [0, B], sumar con Laplace (Δf=B/n, ε=1), dividir por n. Mostrar bias vs varianza al variar B.",
      "Histograma privado: 10 bins de salario, ruido Laplace independiente por bin (sensibilidad = 1 por bin). Comparar con histograma no privado.",
      "Composición: hacer 10 conteos con ε=0.1 cada uno → presupuesto total ε=1.0. Mostrar acumulación empírica del ruido."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-7-etica-fairness-privacidad/225-privacidad-diferencial-intro/notebook.ipynb"
  },
  {
    "id": "parte-7-etica-fairness-privacidad/226-federated-learning-intro",
    "number": 226,
    "slug": "226-federated-learning-intro",
    "partSlug": "parte-7-etica-fairness-privacidad",
    "title": "Federated learning: intro",
    "description": "Entrenar un modelo central sin centralizar los datos.",
    "level": "Intermedio",
    "duration": "75 min",
    "theory": "Entrenar un modelo central sin centralizar los datos. Cada cliente (móvil, hospital, banco) entrena local sobre su data, sube solo pesos o gradientes al servidor, que agrega vía FedAvg. Implementar FedAvg manual sobre regresión logística, ver cómo degrada con datos non-IID, y demostrar el ataque básico de gradient leakage (los gradientes filtran data).",
    "outcomes": [
      "Explicar el setup FL: server + K clientes, rondas, partial participation, comunicación de pesos en vez de data.",
      "Implementar el algoritmo FedAvg (McMahan 2017): w_{t+1} = Σ_k (n_k / n) * w_k^t.",
      "Distinguir cross-device (millones de móviles, intermitentes) vs cross-silo (decenas de hospitales, estables).",
      "Reconocer el efecto de datos non-IID: FedAvg degrada cuando cada cliente ve una distribución distinta.",
      "Identificar los riesgos: model poisoning, gradient leakage (Zhu 2019), y las defensas (secure aggregation, DP-FedAvg, Krum)."
    ],
    "topics": [
      "Setup FL: server + clientes + rondas",
      "FedAvg: muestreo, local epochs, agregación ponderada",
      "Cross-device vs cross-silo",
      "Heterogeneidad: non-IID + system + partial",
      "Ataques: model poisoning, gradient leakage (DLG)",
      "Defensas: secure aggregation, DP, Krum/Median"
    ],
    "materials": [
      "Dataset: sintético tabular (clasificación binaria, 2000 muestras × 10 features), split en K=10 clientes. Self-contained, sin descargas.",
      "Librerías: numpy, scikit-learn. Implementamos FedAvg manualmente — sin flower, PySyft ni TensorFlow Federated, para que el algoritmo quede claro."
    ],
    "exercises": [
      "Particionado IID: generar 2000 muestras, split aleatorio uniforme en K=10 clientes. Verificar que cada cliente tiene ~200 muestras con clases balanceadas.",
      "Local training: implementar local_train(X, y, w, epochs=5, lr=0.05) — regresión logística con SGD manual. Devuelve nuevos pesos w_k.",
      "FedAvg loop: 20 rondas. En cada ronda, samplear 5 de 10 clientes; entrenar local; agregar vía fedavg(weights, sizes). Trackear loss global.",
      "Centralizado vs federado: entrenar la misma logística sobre todo el data junto. Verificar que FL converge a una accuracy comparable (gap < 0.03 en setting IID).",
      "Non-IID: re-partir asignando a cada cliente solo 1-2 clases (cliente 0 ve mayoritariamente clase 0, etc.). Correr FedAvg. Mostrar que la accuracy global degrada y oscila más."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-7-etica-fairness-privacidad/226-federated-learning-intro/notebook.ipynb"
  },
  {
    "id": "parte-7-etica-fairness-privacidad/227-gdpr-y-ai-act-eu",
    "number": 227,
    "slug": "227-gdpr-y-ai-act-eu",
    "partSlug": "parte-7-etica-fairness-privacidad",
    "title": "GDPR y AI Act (EU)",
    "description": "Entender qué exige la regulación europea a un sistema de ML que toca datos personales o decisiones automatizadas.",
    "level": "Intermedio",
    "duration": "75 min",
    "theory": "Entender qué exige la regulación europea a un sistema de ML que toca datos personales o decisiones automatizadas. GDPR (en vigor desde 25-may-2018) regula el dato: bases legales, derechos del titular, DPIA. AI Act (Reglamento UE 2024/1689, escalonado 2024-2027) regula el sistema de IA por nivel de riesgo: prohibido / alto / limitado / mínimo. Aterrizamos ambas normas en un mini-toolkit programático que un equipo de datos puede ejecutar antes de poner un modelo en producción.",
    "outcomes": [
      "Identificar la base legal del Art. 6 GDPR aplicable a un tratamiento (consentimiento, contrato, interés legítimo, etc.) y distinguir las categorías especiales del Art. 9 (salud, biometría, raza).",
      "Implementar los derechos del titular más comunes: acceso, rectificación, supresión (Art. 17 — derecho al olvido) y portabilidad.",
      "Reconocer cuándo el Art. 22 GDPR (decisiones automatizadas con efectos significativos) exige supervisión humana y combinarlo con el Art. 14 del AI Act.",
      "Clasificar un caso de uso de IA en el nivel de riesgo del AI Act (prohibido, alto — Anexo III, limitado, mínimo) y listar las obligaciones que aplican.",
      "Generar una model card mínima y un checklist DPIA programático como artefactos de compliance."
    ],
    "topics": [
      "Bases legales (Art. 6) y categorías especiales (Art. 9) GDPR",
      "Derechos del titular (acceso, supresión, portabilidad, Art. 22)",
      "DPIA (Art. 35) — Data Protection Impact Assessment",
      "AI Act: pirámide de riesgo",
      "Sistemas de alto riesgo (Anexo III)",
      "GPAI y modelos fundacionales"
    ],
    "materials": [
      "Dataset sintético de decisiones de crédito (1000 filas) con campos personales (email, dni, age, salary, score, is_minority) generado en el notebook con np.random.default_rng(42) — sin datos reales.",
      "Librerías: numpy, pandas, scikit-learn, re (regex para PII)."
    ],
    "exercises": [
      "Clasificador de riesgo AI Act: is_high_risk_use_case(\"CV screening\") → \"alto\"; \"juego móvil de match-3\" → \"mínimo\". Cubrir los 4 niveles con lookup table basada en Anexo III.",
      "DPIA checklist: dado {\"sensitive_categories\": True, \"automated_decisions\": True, \"scale\": \"large\"}, listar las obligaciones GDPR aplicables (DPIA, DPO, consentimiento reforzado, etc.).",
      "Right to be forgotten: implementar right_to_be_forgotten(df, user_id) que elimine al usuario y devuelva un registro de auditoría con timestamp + columnas afectadas.",
      "Data minimization audit: detectar columnas que parecen email (r\"[\\w\\.-]+@[\\w\\.-]+\") o DNI (r\"\\d{8}[A-Z]\"); sugerir hash o remoción.",
      "Compliance report: pipeline de scoring de crédito que ejecuta los 7 chequeos del notebook (clasificación de riesgo, DPIA, model card, supervisión humana, minimización, auditoría de PII, registro de borrado) e imprime un reporte único."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-7-etica-fairness-privacidad/227-gdpr-y-ai-act-eu/notebook.ipynb"
  },
  {
    "id": "parte-7-etica-fairness-privacidad/228-reproducibilidad-seeds-lock-files-versionado-de-datasets",
    "number": 228,
    "slug": "228-reproducibilidad-seeds-lock-files-versionado-de-datasets",
    "partSlug": "parte-7-etica-fairness-privacidad",
    "title": "Reproducibilidad: seeds, lock files, versionado de datasets",
    "description": "Cerrar la Parte 7 con el problema que atraviesa todo lo anterior: si un experimento no es reproducible, no es auditable, no es comparable y no es ciencia.",
    "level": "Intermedio",
    "duration": "75 min",
    "theory": "Cerrar la Parte 7 con el problema que atraviesa todo lo anterior: si un experimento no es reproducible, no es auditable, no es comparable y no es ciencia. Aprender a controlar las tres fuentes de no-determinismo (código, datos, ambiente) con seeds, lock files, hashes de datasets, model cards y manifiestos de pipeline. Entender por qué Hutson (Science, 2018) habló de \"crisis de reproducibilidad\" en ML y qué piden hoy NeurIPS/JMLR como mínimo.",
    "outcomes": [
      "Sembrar correctamente random, numpy, sklearn (y comentar torch) con una función seed_everything() y PYTHONHASHSEED.",
      "Distinguir requirements.txt (top-level) de un lock file (uv.lock, poetry.lock, conda-lock) que pinea toda la transitive tree.",
      "Calcular un hash estable de un DataFrame (sha256_of_df) que sobreviva a reorden de columnas e índice y sirva como dataset_id.",
      "Producir un manifest JSON con {data_hash, code_hash, seed, package_versions} y validar reproducibilidad antes de re-entrenar.",
      "Redactar una model card mínima (intended use, training data hash, metrics, limitations) según Mitchell et al. 2019."
    ],
    "topics": [
      "Fuentes de no-determinismo",
      "Seeds en stack Python",
      "Lock files vs requirements",
      "Ambiente reproducible",
      "Versionado de datasets",
      "Documentación: datasheets + model cards"
    ],
    "materials": [
      "Dataset sintético generado in-notebook (no externo) — la clase es sobre el proceso, no sobre el dato.",
      "Librerías: stdlib (hashlib, json, importlib.metadata, os, random), numpy, pandas, scikit-learn.",
      "Opcional para homework: DVC, uv."
    ],
    "exercises": [
      "Seed everything: implementar seed_everything(seed=42) que cubra random, numpy y PYTHONHASHSEED. Verificar que np.random.rand(5) da el mismo vector en dos corridas consecutivas.",
      "Hash de DataFrame: escribir sha256_of_df(df) que ordene columnas alfabéticamente, resetee el índice y serialice a CSV bytes antes de hashear. Mostrar que dos df con columnas en distinto orden dan el mismo hash.",
      "Manifest de experimento: dict con {data_hash, code_hash, seed, sklearn_version, numpy_version, pandas_version, python_version} serializado a experiment.json.",
      "Validación de reproducibilidad: dado un manifest guardado, re-leer el dataset, recomputar su hash, comparar — abortar con RuntimeError si difiere.",
      "Model card mínima: función build_model_card(model, X, y, intended_use, limitations, date_trained) que devuelve dict con campos de Mitchell et al. y lo dumpea a JSON."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-7-etica-fairness-privacidad/228-reproducibilidad-seeds-lock-files-versionado-de-datasets/notebook.ipynb"
  },
  {
    "id": "parte-8-capstones/229-capstone-1-problema-tabular-end-to-end-eda-modelo-api-dashboard",
    "number": 229,
    "slug": "229-capstone-1-problema-tabular-end-to-end-eda-modelo-api-dashboard",
    "partSlug": "parte-8-capstones",
    "title": "Capstone 1: problema tabular end-to-end (EDA, modelo, API, dashboard)",
    "description": "Integrar en un único proyecto entregable todo lo aprendido en Partes 0-7: cargar un dataset tabular real, hacer EDA, construir un pipeline ColumnTransformer reproducible, entrenar y tunear un modelo gradient-boosting co…",
    "level": "Integrador",
    "duration": "180 min",
    "theory": "Integrar en un único proyecto entregable todo lo aprendido en Partes 0-7: cargar un dataset tabular real, hacer EDA, construir un pipeline ColumnTransformer reproducible, entrenar y tunear un modelo gradient-boosting con MLflow tracking, serializar el modelo, exponerlo vía FastAPI con Pydantic v2, construir un dashboard Streamlit con SHAP, y dejar todo bajo CI con GitHub Actions. La entrega debe poder reproducirse desde un clon limpio con uv sync y un docker compose up.",
    "outcomes": [
      "Diseñar un pipeline ML end-to-end siguiendo el flujo de Huyen (Designing ML Systems): data → features → modelo → tracking → serving → monitoring.",
      "Tunear un gradient-boosting con Optuna (≥50 trials) y loguear cada run en MLflow con parámetros, métricas y artefactos.",
      "Exponer el modelo en FastAPI con schemas Pydantic v2 validados y latencia P95 < 200 ms.",
      "Construir un dashboard Streamlit con explicaciones SHAP por predicción + drift monitor (Evidently).",
      "Publicar una Model Card (Mitchell et al. 2019) con uso intencionado, métricas por subgrupo y limitaciones conocidas."
    ],
    "topics": [
      "EDA",
      "Feature engineering",
      "Modelo + tuning",
      "Tracking + Model Card",
      "API FastAPI",
      "Dashboard + CI"
    ],
    "materials": [
      "Dataset sugerido (elegí uno): UCI Adult (clasificación binaria, 48K filas, mix num+cat), Telco Customer Churn (Kaggle, 7K filas, churn binario), o Ames House Prices (Kaggle, 1.5K filas, regresión).",
      "Librerías: pandas o polars, scikit-learn, xgboost/lightgbm, optuna, mlflow, fastapi, uvicorn, pydantic, streamlit, shap, evidently, joblib, pytest, httpx.",
      "Infra local: Docker + compose.yml con 3 servicios (mlflow, api, streamlit)."
    ],
    "exercises": [
      "EDA: cargar dataset, generar ydata-profiling HTML, identificar missing, outliers, balance de clases. Documentar 5 hallazgos en notebooks/01_eda.ipynb.",
      "Pipeline FE: armar ColumnTransformer con OneHotEncoder(handle_unknown='ignore') para cat, StandardScaler para num, SimpleImputer para missing. Persistir el preprocessor.",
      "Modelo + Optuna: entrenar baseline (LogisticRegression) y challenger (XGBClassifier/LGBMClassifier). Tunear con Optuna 50 trials maximizando ROC-AUC sobre validación. Loguear cada trial en MLflow.",
      "API: en src/api/main.py, definir PredictRequest(BaseModel) con todas las features tipadas y PredictResponse(BaseModel) con probability y prediction. Cargar modelo en lifespan. Endpoint /predict + /health.",
      "Dashboard: app.py Streamlit con (a) form input → llama a la API y muestra predicción, (b) plot SHAP waterfall de la última predicción, (c) Evidently report comparando producción vs training data."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-8-capstones/229-capstone-1-problema-tabular-end-to-end-eda-modelo-api-dashboard/notebook.ipynb"
  },
  {
    "id": "parte-8-capstones/230-capstone-2-nlp-o-series-de-tiempo-end-to-end",
    "number": 230,
    "slug": "230-capstone-2-nlp-o-series-de-tiempo-end-to-end",
    "partSlug": "parte-8-capstones",
    "title": "Capstone 2: NLP o series de tiempo end-to-end",
    "description": "Entregar un segundo capstone end-to-end eligiendo una de dos ramas: (A) NLP — clasificación de texto / NER / RAG con transformers y endpoint FastAPI, o (B) series de tiempo — forecasting con baselines + modelos modernos…",
    "level": "Integrador",
    "duration": "180 min",
    "theory": "Entregar un segundo capstone end-to-end eligiendo una de dos ramas: (A) NLP — clasificación de texto / NER / RAG con transformers y endpoint FastAPI, o (B) series de tiempo — forecasting con baselines + modelos modernos, backtesting honesto e intervalos de predicción. En ambas ramas: tracking con MLflow, contenedorización con Docker, reproducibilidad con uv lock + seeds, Model Card, y discusión de drift (texto o forecast).",
    "outcomes": [
      "Elegir entre NLP o series de tiempo según interés/dominio y justificar la decisión en el README del proyecto.",
      "Construir un pipeline reproducible con split honesto (estratificado en NLP, temporal sin shuffle en series).",
      "Reportar métricas del dominio: F1/accuracy + slice analysis (NLP) o sMAPE/MASE + pinball loss (series).",
      "Servir el modelo en un endpoint FastAPI dockerizado, con MLflow tracking del entrenamiento.",
      "Detectar drift (Evidently text drift en NLP; KS sobre residuos en series) y documentarlo en la Model Card."
    ],
    "topics": [
      "Definición + dataset + Model Card v0",
      "EDA específico del dominio",
      "Split honesto + baselines",
      "Modelo moderno + MLflow tracking",
      "Backtesting + intervalos",
      "Empaquetado + endpoint + drift"
    ],
    "materials": [
      "Rama A — NLP: IMDB reviews (50K, binario), AG News (120K, 4 clases), o reseñas de Yelp en español. Para RAG: Wikipedia dump pequeño o docs internos.",
      "Rama B — Series: M5 (Walmart, jerárquica), electricity load (UCI), o clima diario (NOAA). Mínimo 2 años con estacionalidad clara.",
      "Stack común: uv (Parte 7), Docker, MLflow, FastAPI, Evidently. NLP extra: transformers, datasets, sentence-transformers, faiss-cpu. Series extra: statsmodels, statsforecast, darts o neuralprophet."
    ],
    "exercises": [
      "Definición: escribir el problema en 5 líneas (qué se predice, para qué, métrica primaria, baseline aceptable, costo de errar). Elegir rama A o B.",
      "EDA del dominio: rama A → distribuciones de longitud y balance de clases por idioma; rama B → STL + ACF/PACF + test de estacionariedad ADF.",
      "Baselines: rama A → TF-IDF + LogisticRegression; rama B → naive + seasonal naive + ETS. Loggear todo a MLflow.",
      "Modelo moderno: rama A → fine-tune DistilBERT 2 epochs con transformers.Trainer; rama B → SARIMA o NeuralProphet con backtesting expanding window 5 folds.",
      "Endpoint + drift: FastAPI con /predict (NLP) o /forecast?horizon=14 (series), dockerizado. Reporte de drift entre primera y segunda mitad del test (Evidently o KS test manual)."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-8-capstones/230-capstone-2-nlp-o-series-de-tiempo-end-to-end/notebook.ipynb"
  },
  {
    "id": "parte-8-capstones/231-capstone-3-vision-por-computadora-con-transfer-learning",
    "number": 231,
    "slug": "231-capstone-3-vision-por-computadora-con-transfer-learning",
    "partSlug": "parte-8-capstones",
    "title": "Capstone 3: visión por computadora con transfer learning",
    "description": "Construir un clasificador de imágenes de calidad producción usando transfer learning sobre un backbone moderno (ConvNeXt-tiny / EfficientNetV2-S / ViT-Base/16).",
    "level": "Integrador",
    "duration": "180 min",
    "theory": "Construir un clasificador de imágenes de calidad producción usando transfer learning sobre un backbone moderno (ConvNeXt-tiny / EfficientNetV2-S / ViT-Base/16). Entrenar en dos fases (feature extraction → fine-tuning progresivo), aplicar augmentation moderna (RandAugment, MixUp, CutMix), evaluar con métricas per-clase + slice analysis, y servir vía ONNX + FastAPI con endpoint /predict que recibe imagen en base64. Cerrar el capstone con un fairness check si aplica.",
    "outcomes": [
      "Diseñar un pipeline de transfer learning completo: backbone preentrenado en ImageNet → head custom → fine-tuning progresivo con LR diferencial por grupo.",
      "Aplicar augmentation moderna con Albumentations (RandAugment, MixUp, CutMix, RandomErasing) y verificar invariancia de label.",
      "Entrenar con PyTorch Lightning + AMP (mixed precision) + torch.compile + grad accumulation, con seed_everything y deterministic algorithms.",
      "Reportar accuracy + per-class F1 + confusion matrix + slice analysis (Clase 169) y un fairness check (Clase 224) si el dataset tiene atributos sensibles.",
      "Exportar el modelo a ONNX o TorchScript y servirlo en un endpoint FastAPI /predict que reciba imagen base64."
    ],
    "topics": [
      "Dataset + EDA",
      "Augmentation",
      "Backbone preentrenado",
      "Fine-tuning progresivo",
      "Evaluación",
      "Serving"
    ],
    "materials": [
      "Opciones de dataset (elegí una):",
      "Stack: torch 2.x · torchvision · timm · pytorch-lightning · albumentations · onnx · onnxruntime · fastapi · uvicorn · wandb o mlflow."
    ],
    "exercises": [
      "Baseline tonto: entrenar una CNN de 2 capas conv from scratch (sin transfer). Reportar accuracy de validation. Esperá <60% en multiclase — establece el piso.",
      "Feature extraction: cargar timm.create_model('convnext_tiny', pretrained=True, num_classes=N). Congelar backbone (for p in model.parameters(): p.requires_grad = False), entrenar solo head 5 epochs. Esperá +20-30 puntos sobre el baseline.",
      "Fine-tuning progresivo: unfreeze último bloque → 5 epochs con LR 1e-4 → unfreeze full → 10 epochs con LR diferencial (1e-5 backbone, 1e-3 head). Loggear con W&B/MLflow.",
      "Augmentation ablation: comparar (a) sin aug, (b) flip + crop, (c) RandAugment, (d) RandAugment + MixUp + CutMix. Reportar curva val_acc.",
      "Serving end-to-end: exportar a ONNX (torch.onnx.export), validar con onnxruntime que la inferencia da la misma probabilidad ±1e-4, levantar FastAPI con endpoint POST /predict que reciba {\"image_b64\": \"...\"} y devuelva {\"class\": \"...\", \"prob\": 0.94}. Probar con curl."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-8-capstones/231-capstone-3-vision-por-computadora-con-transfer-learning/notebook.ipynb"
  },
  {
    "id": "parte-8-capstones/232-portafolio-publico-en-github-pages-y-presentacion",
    "number": 232,
    "slug": "232-portafolio-publico-en-github-pages-y-presentacion",
    "partSlug": "parte-8-capstones",
    "title": "Portafolio público en GitHub Pages y presentación",
    "description": "Empaquetar los tres capstones (229, 230, 231) en un portafolio público que un reclutador entienda en 30 segundos: sitio en GitHub Pages, demos hosted, blog técnico, deck de presentación y CV.",
    "level": "Integrador",
    "duration": "150 min",
    "theory": "Empaquetar los tres capstones (229, 230, 231) en un portafolio público que un reclutador entienda en 30 segundos: sitio en GitHub Pages, demos hosted, blog técnico, deck de presentación y CV. La regla es calidad > cantidad: 3 proyectos terminados con métricas honestas valen más que 10 a medias.",
    "outcomes": [
      "Estructurar un sitio de portafolio con MkDocs Material o Quarto desplegado en GitHub Pages.",
      "Escribir un README de proyecto que comunica problema, approach, métricas y limitaciones sin marketing vacío.",
      "Publicar demos hosted (Streamlit Community Cloud, HuggingFace Spaces) y un blog técnico por capstone.",
      "Armar un deck de 10-15 slides que cuenta cada proyecto en formato problema → datos → enfoque → resultado → trade-offs.",
      "Detectar y evitar los antipatterns clásicos (10 proyectos a medias, README sin números, demo rota)."
    ],
    "topics": [
      "README pulido por proyecto",
      "Demos hosted (Streamlit/HF Spaces)",
      "Blog técnico (1 post por capstone)",
      "Presentación (deck 10-15 slides)",
      "Video demo (2-3 min)",
      "CV técnico (1 página)"
    ],
    "materials": [
      "Herramientas: MkDocs Material, Quarto, Streamlit Community Cloud, HuggingFace Spaces, Render, Vercel.",
      "Templates: mkdocs-material starter, Quarto blog template.",
      "Inspiración: portfolios de Eugene Yan, Chip Huyen, Vicki Boykis, Hamel Husain — todos en eugeneyan.com, huyenchip.com, etc."
    ],
    "exercises": [
      "MkDocs Material setup: pip install mkdocs-material, mkdocs new portfolio, editar mkdocs.yml con tema material y deployar a gh-pages con mkdocs gh-deploy. Verificar que el sitio carga en https://<user>.github.io/portfolio.",
      "README de capstone: tomar el capstone 229 (NLP) y reescribir el README con hero image, badges (CI, license, Python version), quick start de 30 seg, sección \"decisiones técnicas\" (3 bullets) y \"limitaciones\" (3 bullets).",
      "Demo hosted: subir el capstone 230 (CV) a HuggingFace Spaces con Gradio. URL pública compartible.",
      "Blog post técnico: escribir 1 post de 800-1500 palabras sobre el capstone 231 (tabular) siguiendo el outline problema → datos → approach → resultado con un plot → trade-offs → próximos pasos.",
      "Deck: armar 10-15 slides (Google Slides, Marp o reveal.js) presentando los 3 capstones con la regla de \"1 idea por slide\"."
    ],
    "codeExamples": [],
    "colabUrl": "https://colab.research.google.com/github/vladimiracunadev-create/python-data-science-program/blob/main/classes/parte-8-capstones/232-portafolio-publico-en-github-pages-y-presentacion/notebook.ipynb"
  }
];

export const CLASS_IDS_BY_PART = {
  "parte-0-prerrequisitos": [
    "parte-0-prerrequisitos/001-instalacion-de-python-3-12-y-entornos-virtuales-venv-uv-conda",
    "parte-0-prerrequisitos/002-jupyter-y-jupyterlab-kernels-magics-debugging-profiling",
    "parte-0-prerrequisitos/003-git-y-github-para-data-scientists",
    "parte-0-prerrequisitos/004-estructura-reproducible-de-proyecto-cookiecutter-data-science",
    "parte-0-prerrequisitos/005-vs-code-cursor-para-python-y-jupyter",
    "parte-0-prerrequisitos/006-python-tipos-estructuras-control-de-flujo",
    "parte-0-prerrequisitos/007-comprehensions-y-generadores",
    "parte-0-prerrequisitos/008-funciones-args-kwargs-lambdas-closures",
    "parte-0-prerrequisitos/009-manejo-de-excepciones-y-context-managers",
    "parte-0-prerrequisitos/010-oop-basico-dataclasses-herencia",
    "parte-0-prerrequisitos/011-pathlib-lectura-y-escritura-de-archivos",
    "parte-0-prerrequisitos/012-logging",
    "parte-0-prerrequisitos/013-type-hints-y-mypy",
    "parte-0-prerrequisitos/014-numpy-tipos-creacion-atributos",
    "parte-0-prerrequisitos/015-numpy-ufuncs-y-vectorizacion",
    "parte-0-prerrequisitos/016-numpy-agregaciones",
    "parte-0-prerrequisitos/017-numpy-broadcasting",
    "parte-0-prerrequisitos/018-numpy-boolean-masks-y-fancy-indexing",
    "parte-0-prerrequisitos/019-numpy-ordenamiento-y-busqueda",
    "parte-0-prerrequisitos/020-numpy-algebra-lineal-con-numpy-linalg",
    "parte-0-prerrequisitos/021-numpy-aleatoriedad-y-semillas",
    "parte-0-prerrequisitos/022-pandas-series-y-dataframe",
    "parte-0-prerrequisitos/023-pandas-indexacion-loc-iloc-at-iat",
    "parte-0-prerrequisitos/024-pandas-operaciones-y-alineacion",
    "parte-0-prerrequisitos/025-pandas-datos-faltantes",
    "parte-0-prerrequisitos/026-pandas-multiindex",
    "parte-0-prerrequisitos/027-pandas-concat-merge-join",
    "parte-0-prerrequisitos/028-pandas-groupby-split-apply-combine",
    "parte-0-prerrequisitos/029-pandas-pivot-tables-y-crosstab",
    "parte-0-prerrequisitos/030-pandas-operaciones-vectorizadas-sobre-strings",
    "parte-0-prerrequisitos/031-pandas-series-de-tiempo-resampling-rolling",
    "parte-0-prerrequisitos/032-pandas-eval-y-query",
    "parte-0-prerrequisitos/033-polars-dataframes-modernos",
    "parte-0-prerrequisitos/034-parquet-arrow-pyarrow-duckdb",
    "parte-0-prerrequisitos/035-matplotlib-anatomia-figura-axes",
    "parte-0-prerrequisitos/036-matplotlib-line-scatter-bar-histogram-boxplot",
    "parte-0-prerrequisitos/037-matplotlib-subplots-y-gridspec",
    "parte-0-prerrequisitos/038-matplotlib-legends-colorbars-ticks-anotaciones",
    "parte-0-prerrequisitos/039-matplotlib-stylesheets",
    "parte-0-prerrequisitos/040-matplotlib-3d-plotting",
    "parte-0-prerrequisitos/041-seaborn-distribuciones-relaciones-categoricas-facetas",
    "parte-0-prerrequisitos/042-visualizacion-geografica-plotly-folium",
    "parte-0-prerrequisitos/043-sql-fundamental-select-where-join-group-by-having",
    "parte-0-prerrequisitos/044-sql-avanzado-ctes-window-functions-subqueries-correlacionadas",
    "parte-0-prerrequisitos/045-sql-desde-python-sqlite3-sqlalchemy-duckdb",
    "parte-0-prerrequisitos/046-nosql-mongodb-con-pymongo",
    "parte-0-prerrequisitos/047-apis-rest-con-requests",
    "parte-0-prerrequisitos/048-web-scraping-con-beautifulsoup",
    "parte-0-prerrequisitos/049-async-httpx-aiohttp-para-data-scientists"
  ],
  "parte-1-machine-learning-clasico": [
    "parte-1-machine-learning-clasico/050-panorama-del-ml-tipos-batch-vs-online-instance-vs-model-based",
    "parte-1-machine-learning-clasico/051-desafios-del-ml-overfitting-underfitting-datos-insuficientes",
    "parte-1-machine-learning-clasico/052-testing-validacion-hyperparameter-tuning-no-free-lunch-theorem",
    "parte-1-machine-learning-clasico/053-validacion-temporal-timeseries-walk-forward",
    "parte-1-machine-learning-clasico/054-proyecto-end-to-end-vision-datos-exploracion-preparacion",
    "parte-1-machine-learning-clasico/055-feature-engineering-avanzado-target-encoding-mice",
    "parte-1-machine-learning-clasico/056-seleccion-y-entrenamiento-de-modelo",
    "parte-1-machine-learning-clasico/057-fine-tuning-grid-search-randomized-search",
    "parte-1-machine-learning-clasico/058-optuna-bayesian-hpo-dedicado",
    "parte-1-machine-learning-clasico/059-launch-monitoreo-y-mantenimiento",
    "parte-1-machine-learning-clasico/060-model-cards-y-responsible-ml",
    "parte-1-machine-learning-clasico/061-crisp-dm-como-framework-metodologico",
    "parte-1-machine-learning-clasico/062-clasificacion-binaria-con-mnist",
    "parte-1-machine-learning-clasico/063-metricas-confusion-matrix-precision-recall-f1",
    "parte-1-machine-learning-clasico/064-class-imbalance-smote-adasyn-class-weight",
    "parte-1-machine-learning-clasico/065-precision-recall-tradeoff",
    "parte-1-machine-learning-clasico/066-curva-roc-y-auc",
    "parte-1-machine-learning-clasico/067-clasificacion-multiclase-multilabel-multioutput",
    "parte-1-machine-learning-clasico/068-analisis-de-errores",
    "parte-1-machine-learning-clasico/069-regresion-lineal-ecuacion-normal-vs-gradient-descent",
    "parte-1-machine-learning-clasico/070-gradient-descent-batch-stochastic-mini-batch",
    "parte-1-machine-learning-clasico/071-regresion-polinomial",
    "parte-1-machine-learning-clasico/072-curvas-de-aprendizaje-bias-variance",
    "parte-1-machine-learning-clasico/073-regularizacion-ridge-lasso-elastic-net",
    "parte-1-machine-learning-clasico/074-early-stopping",
    "parte-1-machine-learning-clasico/075-regresion-logistica-binaria-y-softmax",
    "parte-1-machine-learning-clasico/076-calibracion-de-probabilidades-platt-isotonic",
    "parte-1-machine-learning-clasico/077-svm-lineal",
    "parte-1-machine-learning-clasico/078-svm-no-lineal-kernel-polinomial-rbf",
    "parte-1-machine-learning-clasico/079-svm-para-regresion",
    "parte-1-machine-learning-clasico/080-arboles-de-decision-entrenamiento-visualizacion-cart",
    "parte-1-machine-learning-clasico/081-regularizacion-de-arboles",
    "parte-1-machine-learning-clasico/082-regresion-con-arboles",
    "parte-1-machine-learning-clasico/083-voting-classifiers-hard-soft",
    "parte-1-machine-learning-clasico/084-bagging-y-pasting",
    "parte-1-machine-learning-clasico/085-random-forests-y-extra-trees",
    "parte-1-machine-learning-clasico/086-feature-importance",
    "parte-1-machine-learning-clasico/087-shap-en-profundidad-treeexplainer-deepexplainer",
    "parte-1-machine-learning-clasico/088-boosting-adaboost-gradient-boosting",
    "parte-1-machine-learning-clasico/089-xgboost-lightgbm-catboost",
    "parte-1-machine-learning-clasico/090-stacking",
    "parte-1-machine-learning-clasico/091-maldicion-de-la-dimensionalidad",
    "parte-1-machine-learning-clasico/092-pca-proyeccion-varianza-explicada-incremental-randomized-kernel",
    "parte-1-machine-learning-clasico/093-lle",
    "parte-1-machine-learning-clasico/094-mds-isomap-t-sne-umap-lda",
    "parte-1-machine-learning-clasico/095-clustering-k-means-seleccion-de-k-mini-batch",
    "parte-1-machine-learning-clasico/096-dbscan",
    "parte-1-machine-learning-clasico/097-clustering-agglomerative-birch-mean-shift-affinity-propagation-spectra",
    "parte-1-machine-learning-clasico/098-gaussian-mixture-models",
    "parte-1-machine-learning-clasico/099-deteccion-de-anomalias-isolation-forest-lof-one-class-svm"
  ],
  "parte-2-deep-learning": [
    "parte-2-deep-learning/100-perceptron-mlp-y-backpropagation",
    "parte-2-deep-learning/101-regresion-y-clasificacion-con-mlp",
    "parte-2-deep-learning/102-keras-sequential-api",
    "parte-2-deep-learning/103-keras-functional-api-y-subclassing",
    "parte-2-deep-learning/104-callbacks-tensorboard-guardar-restaurar-modelos",
    "parte-2-deep-learning/105-keras-tuner",
    "parte-2-deep-learning/106-ray-tune-hpo-distribuido",
    "parte-2-deep-learning/107-vanishing-exploding-gradients",
    "parte-2-deep-learning/108-inicializacion-glorot-he",
    "parte-2-deep-learning/109-activaciones-relu-elu-gelu-swish-mish",
    "parte-2-deep-learning/110-batch-normalization-layer-normalization",
    "parte-2-deep-learning/111-gradient-clipping",
    "parte-2-deep-learning/112-transfer-learning-unsupervised-pretraining",
    "parte-2-deep-learning/113-optimizadores-momentum-nesterov-adagrad-rmsprop-adam-adamw",
    "parte-2-deep-learning/114-optimizadores-modernos-lion-sophia",
    "parte-2-deep-learning/115-learning-rate-scheduling",
    "parte-2-deep-learning/116-regularizacion-l1-l2-dropout-max-norm-mc-dropout",
    "parte-2-deep-learning/117-stochastic-depth-droppath-layerdrop",
    "parte-2-deep-learning/118-tensorflow-tensores-variables-operaciones",
    "parte-2-deep-learning/119-losses-metricas-capas-modelos-custom",
    "parte-2-deep-learning/120-funciones-y-grafos-autograph",
    "parte-2-deep-learning/121-custom-training-loops",
    "parte-2-deep-learning/122-pytorch-fundamentos-tensores-autograd",
    "parte-2-deep-learning/123-pytorch-lightning-trainer-distribuido",
    "parte-2-deep-learning/124-tf-data-api",
    "parte-2-deep-learning/125-tfrecord",
    "parte-2-deep-learning/126-keras-preprocessing-layers",
    "parte-2-deep-learning/127-tensorflow-datasets-tfds",
    "parte-2-deep-learning/128-capas-convolucionales-filtros-feature-maps",
    "parte-2-deep-learning/129-pooling",
    "parte-2-deep-learning/130-arquitecturas-cnn-lenet-alexnet-vgg-googlenet-resnet-xception-senet-ef",
    "parte-2-deep-learning/131-transfer-learning-con-cnns-preentrenadas",
    "parte-2-deep-learning/132-localizacion-deteccion-yolo-faster-r-cnn-segmentacion-semantica",
    "parte-2-deep-learning/133-segment-anything-sam-sam2",
    "parte-2-deep-learning/134-yolov11-deteccion-segmentacion-practica",
    "parte-2-deep-learning/135-rnns-neuronas-recurrentes-bptt",
    "parte-2-deep-learning/136-forecasting-de-series-con-rnn",
    "parte-2-deep-learning/137-lstm-gru",
    "parte-2-deep-learning/138-1d-cnns-y-wavenet",
    "parte-2-deep-learning/139-generacion-de-texto-char-rnn",
    "parte-2-deep-learning/140-analisis-de-sentimiento",
    "parte-2-deep-learning/141-encoder-decoder-para-traduccion",
    "parte-2-deep-learning/142-mecanismos-de-atencion",
    "parte-2-deep-learning/143-transformers-arquitectura-bert-gpt",
    "parte-2-deep-learning/144-flash-attention-rope-gqa-llm-engines",
    "parte-2-deep-learning/145-hugging-face-transformers-uso-practico",
    "parte-2-deep-learning/146-clip-siglip-multimodal-embeddings",
    "parte-2-deep-learning/147-whisper-asr-audio-transcripcion-traduccion",
    "parte-2-deep-learning/148-llms-aplicados-fine-tuning-prompting",
    "parte-2-deep-learning/149-lora-qlora-fine-tuning-eficiente",
    "parte-2-deep-learning/150-dpo-rlhf-alineamiento-de-llms",
    "parte-2-deep-learning/151-vllm-tgi-serving-llm-produccion",
    "parte-2-deep-learning/152-rag-basico-y-embeddings",
    "parte-2-deep-learning/153-mcp-model-context-protocol",
    "parte-2-deep-learning/154-agentes-tool-use-react-multi-agent",
    "parte-2-deep-learning/155-llm-evaluation-mmlu-mtbench-llm-as-judge",
    "parte-2-deep-learning/156-autoencoders-undercomplete-stacked-denoising-sparse",
    "parte-2-deep-learning/157-variational-autoencoders-vae",
    "parte-2-deep-learning/158-gans-dcgan-progressive-gan-stylegan",
    "parte-2-deep-learning/159-modelos-de-difusion-ddpm-score-based",
    "parte-2-deep-learning/160-stable-diffusion-xl-controlnet",
    "parte-2-deep-learning/161-rl-aprendizaje-por-recompensa-openai-gymnasium",
    "parte-2-deep-learning/162-policy-gradients",
    "parte-2-deep-learning/163-markov-decision-processes",
    "parte-2-deep-learning/164-td-learning-q-learning-deep-q-networks",
    "parte-2-deep-learning/165-rl-moderno-a3c-ppo-sac-vista-general",
    "parte-2-deep-learning/166-tf-serving-grpc",
    "parte-2-deep-learning/167-onnx-onnx-runtime-portabilidad",
    "parte-2-deep-learning/168-despliegue-en-vertex-ai",
    "parte-2-deep-learning/169-tf-lite-mobile-embedded",
    "parte-2-deep-learning/170-tensorflow-js-navegador",
    "parte-2-deep-learning/171-aceleracion-con-gpu",
    "parte-2-deep-learning/172-entrenamiento-multi-dispositivo-tf-distribute",
    "parte-2-deep-learning/173-jax-flax-fundamentos",
    "parte-2-deep-learning/174-entrenamiento-a-escala-con-vertex-ai"
  ],
  "parte-3-estadistica-inferencial": [
    "parte-3-estadistica-inferencial/175-distribuciones-normal-binomial-poisson-exponencial",
    "parte-3-estadistica-inferencial/176-test-t-una-muestra-dos-muestras-pareado",
    "parte-3-estadistica-inferencial/177-effect-size-cohen-d-hedges-g-cliff-delta-pingouin",
    "parte-3-estadistica-inferencial/178-test-chi-cuadrado-de-independencia-y-bondad-de-ajuste",
    "parte-3-estadistica-inferencial/179-anova-one-way-two-way",
    "parte-3-estadistica-inferencial/180-tests-no-parametricos-mann-whitney-wilcoxon-kruskal-wallis",
    "parte-3-estadistica-inferencial/181-correccion-de-comparaciones-multiples-bonferroni-fdr",
    "parte-3-estadistica-inferencial/182-intervalos-de-confianza",
    "parte-3-estadistica-inferencial/183-bootstrap-y-permutation-tests",
    "parte-3-estadistica-inferencial/184-bca-bootstrap-scipy-permutation-test-moderno",
    "parte-3-estadistica-inferencial/185-a-b-testing-tamano-de-muestra-poder-estadistico",
    "parte-3-estadistica-inferencial/186-cuped-sequential-testing-always-valid-p-values",
    "parte-3-estadistica-inferencial/187-diseno-experimental",
    "parte-3-estadistica-inferencial/188-inferencia-causal-dags-confounders-instrumentos",
    "parte-3-estadistica-inferencial/189-doubleml-econml-ml-para-causalidad",
    "parte-3-estadistica-inferencial/190-uplift-modeling-did-difference-in-differences",
    "parte-3-estadistica-inferencial/191-synthetic-control-method-pysyncon",
    "parte-3-estadistica-inferencial/192-bayes-intro-priors-posterior-mcmc-con-pymc",
    "parte-3-estadistica-inferencial/193-pymc-v5-numpyro-arviz-stack-bayesiano"
  ],
  "parte-4-mlops": [
    "parte-4-mlops/194-versionado-de-datos-con-dvc",
    "parte-4-mlops/195-versionado-de-modelos-y-experimentos-con-mlflow",
    "parte-4-mlops/196-feature-stores-feast",
    "parte-4-mlops/197-ci-cd-para-ml-con-github-actions",
    "parte-4-mlops/198-docker-para-empaquetar-modelos",
    "parte-4-mlops/199-apis-con-fastapi-sirviendo-modelos",
    "parte-4-mlops/200-kubernetes-para-servir-modelos-a-escala",
    "parte-4-mlops/201-serverless-ml-aws-lambda-gcp-cloud-functions",
    "parte-4-mlops/202-monitoreo-data-drift-model-drift-alertas",
    "parte-4-mlops/203-reentrenamiento-programado",
    "parte-4-mlops/204-shadow-deployment-y-canary-releases",
    "parte-4-mlops/205-interpretabilidad-shap-lime-pdp-ice",
    "parte-4-mlops/206-testing-de-datos-great-expectations-deequ",
    "parte-4-mlops/207-testing-de-modelos-invariance-behavioral-tests"
  ],
  "parte-5-ingenieria-de-datos": [
    "parte-5-ingenieria-de-datos/208-pipelines-etl-elt-con-airflow",
    "parte-5-ingenieria-de-datos/209-pipelines-con-prefect-o-dagster",
    "parte-5-ingenieria-de-datos/210-pyspark-para-datasets-grandes",
    "parte-5-ingenieria-de-datos/211-polars-como-alternativa-moderna",
    "parte-5-ingenieria-de-datos/212-data-warehouses-bigquery-snowflake-duckdb",
    "parte-5-ingenieria-de-datos/213-streaming-intro-kafka-kinesis",
    "parte-5-ingenieria-de-datos/214-formatos-columnares-parquet-avro",
    "parte-5-ingenieria-de-datos/215-modelado-dimensional-star-snowflake-schemas"
  ],
  "parte-6-sistemas-de-recomendacion": [
    "parte-6-sistemas-de-recomendacion/216-filtrado-colaborativo-user-based-e-item-based",
    "parte-6-sistemas-de-recomendacion/217-factorizacion-de-matrices-svd-als",
    "parte-6-sistemas-de-recomendacion/218-content-based-filtering",
    "parte-6-sistemas-de-recomendacion/219-recomendadores-hibridos",
    "parte-6-sistemas-de-recomendacion/220-metricas-map-k-ndcg-recall-k",
    "parte-6-sistemas-de-recomendacion/221-cold-start-problem",
    "parte-6-sistemas-de-recomendacion/222-librerias-lightfm-implicit-surprise"
  ],
  "parte-7-etica-fairness-privacidad": [
    "parte-7-etica-fairness-privacidad/223-tipos-de-sesgo-algoritmico-y-origenes",
    "parte-7-etica-fairness-privacidad/224-metricas-de-fairness-demographic-parity-equalized-odds-calibration",
    "parte-7-etica-fairness-privacidad/225-privacidad-diferencial-intro",
    "parte-7-etica-fairness-privacidad/226-federated-learning-intro",
    "parte-7-etica-fairness-privacidad/227-gdpr-y-ai-act-eu",
    "parte-7-etica-fairness-privacidad/228-reproducibilidad-seeds-lock-files-versionado-de-datasets"
  ],
  "parte-8-capstones": [
    "parte-8-capstones/229-capstone-1-problema-tabular-end-to-end-eda-modelo-api-dashboard",
    "parte-8-capstones/230-capstone-2-nlp-o-series-de-tiempo-end-to-end",
    "parte-8-capstones/231-capstone-3-vision-por-computadora-con-transfer-learning",
    "parte-8-capstones/232-portafolio-publico-en-github-pages-y-presentacion"
  ]
};

/** Devuelve las clases de una parte, en orden de numeración. */
export const classesForPart = (partId) =>
  CLASSES.filter((item) => item.partSlug === partId);

/** Busca una clase por su id (`parte-N-slug/NNN-slug`). */
export const classById = (id) => CLASSES.find((item) => item.id === id);

export const TOTAL_CLASSES = 232;
export const TOTAL_PARTS = 9;
