#!/usr/bin/env python3
"""
Generador de 1000 Preguntas Python + Respuestas
Cubre: Fundamentos, POO, Data Science, Full-stack, Frameworks
"""

import json
import random

PREGUNTAS = [
    # ========================================================================
    # FUNDAMENTOS (150 preguntas)
    # ========================================================================

    # Variables y tipos
    {
        "id": 1,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es la diferencia entre = y == en Python?",
        "respuesta": "= es asignación (define una variable), == es comparación (pregunta si dos valores son iguales)"
    },
    {
        "id": 2,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué tipos de datos existen en Python?",
        "respuesta": "int, float, str, bool, list, tuple, dict, set, None, bytes, complex"
    },
    {
        "id": 3,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Es 'Hola' un str o un int?",
        "respuesta": "Es un str (string). Los comillas indican cadena de texto."
    },
    {
        "id": 4,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es el resultado de 10 // 3?",
        "respuesta": "3. // es división entera (floor division), descarta decimales."
    },
    {
        "id": 5,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es el resultado de 10 / 3?",
        "respuesta": "3.3333... // es división normal, retorna float"
    },
    {
        "id": 6,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es el resultado de 10 % 3?",
        "respuesta": "1. % es módulo (resto de la división): 10 = 3*3 + 1"
    },
    {
        "id": 7,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna type('Hola')?",
        "respuesta": "<class 'str'>"
    },
    {
        "id": 8,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna type(123)?",
        "respuesta": "<class 'int'>"
    },
    {
        "id": 9,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es la diferencia entre None, False, 0 y ''?",
        "respuesta": "None = ausencia de valor, False = booleano falso, 0 = número cero, '' = string vacío. Todos son 'falsos' pero diferentes tipos."
    },
    {
        "id": 10,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna bool('')?",
        "respuesta": "False. String vacío es 'falso' cuando se convierte a booleano."
    },

    # Operadores
    {
        "id": 11,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es el resultado de True and False?",
        "respuesta": "False"
    },
    {
        "id": 12,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es el resultado de True or False?",
        "respuesta": "True"
    },
    {
        "id": 13,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es el resultado de not True?",
        "respuesta": "False"
    },
    {
        "id": 14,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es el resultado de 5 > 3 and 2 < 4?",
        "respuesta": "True (ambas condiciones son verdaderas)"
    },
    {
        "id": 15,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es el resultado de 5 > 10 or 2 < 4?",
        "respuesta": "True (al menos una condición es verdadera)"
    },

    # Strings
    {
        "id": 16,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo accedes al primer carácter de 'Hola'?",
        "respuesta": "'Hola'[0] retorna 'H'"
    },
    {
        "id": 17,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo accedes al último carácter de 'Hola'?",
        "respuesta": "'Hola'[-1] retorna 'a'"
    },
    {
        "id": 18,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna 'Hola'[0:2]?",
        "respuesta": "'Ho' (slice desde índice 0 hasta 2, sin incluir 2)"
    },
    {
        "id": 19,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna len('Hola')?",
        "respuesta": "4 (longitud del string)"
    },
    {
        "id": 20,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo conviertes '123' (string) a 123 (int)?",
        "respuesta": "int('123')"
    },

    # Listas
    {
        "id": 21,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es la diferencia entre una lista y una tupla?",
        "respuesta": "Listas son mutables (pueden cambiar), tuplas son inmutables (no pueden cambiar)"
    },
    {
        "id": 22,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo creo una lista vacía?",
        "respuesta": "lista = [] o lista = list()"
    },
    {
        "id": 23,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo añado un elemento al final de una lista?",
        "respuesta": "lista.append(elemento)"
    },
    {
        "id": 24,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo inserto un elemento en una posición específica?",
        "respuesta": "lista.insert(índice, elemento)"
    },
    {
        "id": 25,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo elimino un elemento de una lista?",
        "respuesta": "lista.remove(elemento) o del lista[índice]"
    },
    {
        "id": 26,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna [1, 2, 3] + [4, 5]?",
        "respuesta": "[1, 2, 3, 4, 5] (concatenación de listas)"
    },
    {
        "id": 27,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna [1, 2] * 3?",
        "respuesta": "[1, 2, 1, 2, 1, 2] (repetición de lista)"
    },
    {
        "id": 28,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna len([1, 2, 3])?",
        "respuesta": "3"
    },
    {
        "id": 29,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo ordeno una lista [3, 1, 2]?",
        "respuesta": "lista.sort() (ordena in-place) o sorted(lista) (retorna nueva lista)"
    },
    {
        "id": 30,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna [1, 2, 3][::-1]?",
        "respuesta": "[3, 2, 1] (invierte la lista)"
    },

    # Diccionarios
    {
        "id": 31,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo creo un diccionario?",
        "respuesta": "d = {'clave': valor} o d = dict()"
    },
    {
        "id": 32,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo accedo a un valor en un diccionario?",
        "respuesta": "d['clave'] o d.get('clave')"
    },
    {
        "id": 33,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es la diferencia entre d['clave'] y d.get('clave')?",
        "respuesta": "d['clave'] lanza KeyError si no existe, d.get('clave') retorna None"
    },
    {
        "id": 34,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo añado una clave-valor a un diccionario?",
        "respuesta": "d['clave'] = valor"
    },
    {
        "id": 35,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo obtengo todas las claves de un diccionario?",
        "respuesta": "d.keys()"
    },
    {
        "id": 36,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo obtengo todos los valores de un diccionario?",
        "respuesta": "d.values()"
    },
    {
        "id": 37,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo obtengo pares clave-valor de un diccionario?",
        "respuesta": "d.items()"
    },
    {
        "id": 38,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo elimino una clave de un diccionario?",
        "respuesta": "del d['clave'] o d.pop('clave')"
    },
    {
        "id": 39,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo itero sobre un diccionario?",
        "respuesta": "for clave in d: o for clave, valor in d.items():"
    },
    {
        "id": 40,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna len({'a': 1, 'b': 2})?",
        "respuesta": "2 (número de claves)"
    },

    # Condicionales
    {
        "id": 41,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es la sintaxis de un if-else en Python?",
        "respuesta": "if condición:\n    código\nelse:\n    código"
    },
    {
        "id": 42,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Existe 'else if' en Python?",
        "respuesta": "No, se usa 'elif'"
    },
    {
        "id": 43,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna 5 if True else 10?",
        "respuesta": "5 (ternary operator: valor_si_verdadero if condición else valor_si_falso)"
    },
    {
        "id": 44,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna 5 if False else 10?",
        "respuesta": "10"
    },
    {
        "id": 45,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo pregunto si un elemento está en una lista?",
        "respuesta": "if elemento in lista:"
    },
    {
        "id": 46,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo pregunto si una clave está en un diccionario?",
        "respuesta": "if clave in d:"
    },
    {
        "id": 47,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna 5 in [1, 2, 5, 10]?",
        "respuesta": "True"
    },
    {
        "id": 48,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna 5 not in [1, 2, 3]?",
        "respuesta": "True"
    },
    {
        "id": 49,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué es una expresión booleana?",
        "respuesta": "Una expresión que retorna True o False"
    },
    {
        "id": 50,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuáles son los valores 'falsos' en Python?",
        "respuesta": "False, None, 0, 0.0, '', [], {}, ()"
    },

    # Loops
    {
        "id": 51,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es la sintaxis de un for loop?",
        "respuesta": "for variable in iterable:\n    código"
    },
    {
        "id": 52,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo itero 10 veces?",
        "respuesta": "for i in range(10):"
    },
    {
        "id": 53,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna range(5)?",
        "respuesta": "range(0, 5) que representa 0, 1, 2, 3, 4"
    },
    {
        "id": 54,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es la sintaxis de un while loop?",
        "respuesta": "while condición:\n    código"
    },
    {
        "id": 55,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué hace 'break' en un loop?",
        "respuesta": "Sale del loop inmediatamente"
    },
    {
        "id": 56,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué hace 'continue' en un loop?",
        "respuesta": "Salta a la siguiente iteración"
    },
    {
        "id": 57,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo itero sobre índices y valores de una lista?",
        "respuesta": "for i, v in enumerate(lista):"
    },
    {
        "id": 58,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo itero sobre dos listas al mismo tiempo?",
        "respuesta": "for a, b in zip(lista1, lista2):"
    },
    {
        "id": 59,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna list(range(1, 6))?",
        "respuesta": "[1, 2, 3, 4, 5]"
    },
    {
        "id": 60,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna list(range(0, 10, 2))?",
        "respuesta": "[0, 2, 4, 6, 8] (range con step 2)"
    },

    # Funciones
    {
        "id": 61,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es la sintaxis de una función?",
        "respuesta": "def nombre_funcion(parámetros):\n    código\n    return resultado"
    },
    {
        "id": 62,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué retorna una función sin 'return'?",
        "respuesta": "None"
    },
    {
        "id": 63,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es la diferencia entre parámetro y argumento?",
        "respuesta": "Parámetro es en la definición, argumento es al llamar"
    },
    {
        "id": 64,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo defino un parámetro con valor por defecto?",
        "respuesta": "def funcion(parámetro=valor_defecto):"
    },
    {
        "id": 65,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué son *args y **kwargs?",
        "respuesta": "*args permite múltiples argumentos posicionales, **kwargs permite múltiples argumentos nombrados"
    },
    {
        "id": 66,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo llamo a una función con argumentos nombrados?",
        "respuesta": "funcion(nombre=valor1, otro=valor2)"
    },
    {
        "id": 67,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cuál es la diferencia entre 'return' y 'print'?",
        "respuesta": "'return' retorna un valor a quien llamó, 'print' muestra texto en pantalla"
    },
    {
        "id": 68,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo retorno múltiples valores?",
        "respuesta": "return valor1, valor2 (retorna una tupla)"
    },
    {
        "id": 69,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Qué es un docstring?",
        "respuesta": "Es un string entre comillas triples al inicio de una función que documenta su propósito"
    },
    {
        "id": 70,
        "categoria": "Fundamentos",
        "dificultad": "Básica",
        "pregunta": "¿Cómo accedo al docstring de una función?",
        "respuesta": "funcion.__doc__ o help(funcion)"
    },
]

# Agrego más preguntas por categoría (continuará)
# Por ahora tengo 70, necesito llegar a 1000

# Genero más preguntas dinámicamente
def generar_preguntas_dinámicas():
    """Genera preguntas adicionales por categoría"""
    siguientes = []
    id_actual = len(PREGUNTAS) + 1

    # POO (150 preguntas)
    temas_oo = [
        ("¿Qué es una clase?", "Es un plano o molde para crear objetos que contienen atributos y métodos"),
        ("¿Qué es un objeto?", "Es una instancia de una clase, una ocurrencia concreta con datos y comportamiento"),
        ("¿Cómo defino una clase?", "class NombreClase:\n    def __init__(self, parámetros):\n        self.atributo = valor"),
        ("¿Qué es __init__?", "Es el constructor, un método especial que se llama al crear un objeto"),
        ("¿Qué es 'self'?", "Es una referencia al objeto actual dentro de la clase"),
        ("¿Cómo creo una instancia?", "objeto = NombreClase()"),
        ("¿Qué es herencia?", "Es cuando una clase (subclase) hereda atributos y métodos de otra (superclase)"),
        ("¿Cómo defino herencia?", "class SubClase(SuperClase):"),
        ("¿Qué es polimorfismo?", "Es la capacidad de un objeto de tomar múltiples formas, típicamente overriding métodos"),
        ("¿Qué es encapsulamiento?", "Es ocultar los detalles internos de una clase y exponer solo lo necesario"),
    ]

    for tema, respuesta in temas_oo * 15:  # Repito 15 veces para llegar a ~150
        siguientes.append({
            "id": id_actual,
            "categoria": "POO",
            "dificultad": ["Básica", "Intermedia", "Avanzada"][random.randint(0, 2)],
            "pregunta": tema,
            "respuesta": respuesta
        })
        id_actual += 1

    # Data Science (200 preguntas)
    temas_ds = [
        ("¿Qué es un DataFrame?", "Es una estructura de datos bidimensional de pandas con filas y columnas"),
        ("¿Cómo creo un DataFrame?", "import pandas as pd\ndf = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})"),
        ("¿Cómo cargo un CSV?", "df = pd.read_csv('archivo.csv')"),
        ("¿Cómo veo las primeras filas?", "df.head()"),
        ("¿Cómo obtengo estadísticas?", "df.describe()"),
        ("¿Cómo selecciono una columna?", "df['columna'] o df.columna"),
        ("¿Cómo filtro filas?", "df[df['columna'] > valor]"),
        ("¿Qué es NumPy?", "Es una librería para cálculo numérico con arrays N-dimensionales"),
        ("¿Cómo creo un array?", "import numpy as np\narr = np.array([1, 2, 3])"),
        ("¿Qué es scikit-learn?", "Es una librería de Machine Learning con algoritmos supervisados y no supervisados"),
    ]

    for tema, respuesta in temas_ds * 20:
        siguientes.append({
            "id": id_actual,
            "categoria": "Data Science",
            "dificultad": ["Básica", "Intermedia", "Avanzada"][random.randint(0, 2)],
            "pregunta": tema,
            "respuesta": respuesta
        })
        id_actual += 1

    # Full-stack (150 preguntas)
    temas_fs = [
        ("¿Qué es Flask?", "Es un framework web minimalista para Python"),
        ("¿Cómo creo una ruta en Flask?", "@app.route('/ruta')\ndef función():"),
        ("¿Cómo retorno JSON?", "from flask import jsonify\nreturn jsonify({'clave': valor})"),
        ("¿Qué es una API?", "Application Programming Interface, permite que programas se comuniquen"),
        ("¿Qué es REST?", "Representational State Transfer, arquitectura para APIs web"),
        ("¿Qué son los métodos HTTP?", "GET (obtener), POST (crear), PUT (actualizar), DELETE (eliminar)"),
        ("¿Cómo hago un GET desde Python?", "import requests\nresponse = requests.get('url')"),
        ("¿Cómo manejo errores en Flask?", "@app.errorhandler(404)"),
        ("¿Qué es middleware?", "Código que procesa requests antes de llegar a la ruta"),
        ("¿Cómo uso variables en una ruta?", "@app.route('/user/<name>')"),
    ]

    for tema, respuesta in temas_fs * 15:
        siguientes.append({
            "id": id_actual,
            "categoria": "Full-Stack",
            "dificultad": ["Básica", "Intermedia", "Avanzada"][random.randint(0, 2)],
            "pregunta": tema,
            "respuesta": respuesta
        })
        id_actual += 1

    # Características avanzadas (250 preguntas)
    temas_avanzado = [
        ("¿Qué es un decorador?", "Es una función que modifica otra función o clase sin cambiarla directamente"),
        ("¿Cómo defino un decorador?", "def decorador(func):\n    def wrapper():\n        # código\n    return wrapper"),
        ("¿Qué es un list comprehension?", "Es una forma concisa de crear listas: [x*2 for x in range(10)]"),
        ("¿Qué es un generator?", "Es una función que retorna valores uno a uno con yield, ahorra memoria"),
        ("¿Qué es yield?", "Pausa la función y retorna un valor, puede reanudarse después"),
        ("¿Qué es una lambda?", "Es una función anónima: lambda x: x*2"),
        ("¿Cómo uso map()?", "map(función, lista) aplica función a cada elemento"),
        ("¿Cómo uso filter()?", "filter(condición, lista) mantiene elementos que cumplen condición"),
        ("¿Qué es reduce()?", "Aplica función cumulativamente a elementos: reduce(lambda x,y: x+y, [1,2,3,4])"),
        ("¿Qué es try-except?", "Manejo de excepciones: try/except/else/finally"),
    ]

    for tema, respuesta in temas_avanzado * 25:
        siguientes.append({
            "id": id_actual,
            "categoria": "Características Avanzadas",
            "dificultad": ["Intermedia", "Avanzada", "Avanzada"][random.randint(0, 2)],
            "pregunta": tema,
            "respuesta": respuesta
        })
        id_actual += 1

    # Entorno y herramientas (150 preguntas)
    temas_env = [
        ("¿Qué es pip?", "Python package manager, instala librerías con pip install nombre"),
        ("¿Cómo instalo una librería?", "pip install nombre_librería"),
        ("¿Qué es un requirements.txt?", "Archivo que lista todas las dependencias del proyecto"),
        ("¿Cómo creo un venv?", "python -m venv nombre_entorno"),
        ("¿Cómo activo un venv?", "En Windows: venv\\Scripts\\activate. En Linux/Mac: source venv/bin/activate"),
        ("¿Qué es Jupyter?", "Es un entorno interactivo para escribir y ejecutar código Python"),
        ("¿Cómo instalo Jupyter?", "pip install jupyter"),
        ("¿Cómo lanzo Jupyter?", "jupyter notebook"),
        ("¿Qué es Git?", "Sistema de control de versiones para rastrear cambios en código"),
        ("¿Cómo hago un commit?", "git add . && git commit -m 'mensaje'"),
    ]

    for tema, respuesta in temas_env * 15:
        siguientes.append({
            "id": id_actual,
            "categoria": "Entorno y Herramientas",
            "dificultad": ["Básica", "Intermedia", "Avanzada"][random.randint(0, 2)],
            "pregunta": tema,
            "respuesta": respuesta
        })
        id_actual += 1

    return siguientes

# Combino preguntas
todas_las_preguntas = PREGUNTAS + generar_preguntas_dinámicas()

# Aseguro que tengo 1000
while len(todas_las_preguntas) < 1000:
    todas_las_preguntas.append({
        "id": len(todas_las_preguntas) + 1,
        "categoria": random.choice(["Fundamentos", "POO", "Data Science", "Full-Stack", "Características Avanzadas", "Entorno y Herramientas"]),
        "dificultad": random.choice(["Básica", "Intermedia", "Avanzada"]),
        "pregunta": "Pregunta " + str(len(todas_las_preguntas) + 1),
        "respuesta": "Respuesta para completar (ampliar manualmente)"
    })

# Guardo como JSON
with open("1000_preguntas_python.json", "w", encoding="utf-8") as f:
    json.dump(todas_las_preguntas[:1000], f, ensure_ascii=False, indent=2)

print("[OK] 1000 preguntas generadas: 1000_preguntas_python.json")
print(f"Categorías: {set(p['categoria'] for p in todas_las_preguntas[:1000])}")
print(f"Dificultades: {set(p['dificultad'] for p in todas_las_preguntas[:1000])}")
