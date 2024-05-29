import numpy as np


def evaluar(funcion, valor):
    """
    Evalúa una función matemática dada una cadena y un valor.

    Args:
    funcion (str): La función matemática en forma de cadena.
    valor (float): El valor en el cual se evaluará la función.

    Returns:
    float: El resultado de la función evaluada.
    """
    import math
    from math import sqrt, sin, cos, tan, exp, log

    # Definir un contexto seguro para eval
    contexto = {
        'sqrt': math.sqrt,
        'sin': math.sin,
        'cos': math.cos,
        'tan': math.tan,
        'exp': math.exp,
        'log': math.log,
        'x': float(valor)
    }

    try:
        return eval(funcion, {"__builtins__": None}, contexto)
    except Exception as e:
        raise ValueError(f"Error al evaluar la función: {e}")


def leerMatriz(matriz):
    """
    Convierte una cadena de texto en una matriz.

    Args:
    matriz (str): La matriz en forma de cadena.

    Returns:
    list: La matriz convertida en una lista de listas.
    """
    A = []
    filas = matriz.split(';')
    for fila in filas:
        columnas = fila.split(',')
        A.append([float(col) for col in columnas])
    return A


def leerVector(vector):
    """
    Convierte una cadena de texto en un vector.

    Args:
    vector (str): El vector en forma de cadena.

    Returns:
    list: El vector convertido en una lista.
    """
    return [float(col) for col in vector.split(',')]


def cambiarFilas(matriz, fila1, fila2):
    """
    Intercambia dos filas de una matriz.

    Args:
    matriz (numpy.ndarray): La matriz en la que se intercambiarán las filas.
    fila1 (int): El índice de la primera fila.
    fila2 (int): El índice de la segunda fila.

    Returns:
    numpy.ndarray: La matriz con las filas intercambiadas.
    """
    matriz[[fila1, fila2]] = matriz[[fila2, fila1]]
    return matriz


def cambiarColumnas(matriz, col1, col2):
    """
    Intercambia dos columnas de una matriz.

    Args:
    matriz (numpy.ndarray): La matriz en la que se intercambiarán las columnas.
    col1 (int): El índice de la primera columna.
    col2 (int): El índice de la segunda columna.

    Returns:
    numpy.ndarray: La matriz con las columnas intercambiadas.
    """
    matriz[:, [col1, col2]] = matriz[:, [col2, col1]]
    return matriz


def luDecomposicion(A, n):
    """
    Realiza la descomposición LU de una matriz.

    Args:
    A (numpy.ndarray): La matriz a descomponer.
    n (int): El tamaño de la matriz.

    Returns:
    tuple: Las matrices L y U resultantes de la descomposición.
    """
    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for k in range(n):
        for i in range(k, n):
            sum1 = sum(L[i][p] * U[p][k] for p in range(k))
            L[i][k] = A[i][k] - sum1
        for i in range(k + 1, n):
            if L[k][k] == 0:
                raise ValueError("Debe usar el pivoteo parcial")
            sum2 = sum(L[k][p] * U[p][i] for p in range(k))
            U[k][i] = (A[k][i] - sum2) / L[k][k]

    U += np.eye(n, dtype=float)
    return L, U


def susprog(L, b):
    """
    Realiza la sustitución progresiva en una matriz triangular inferior.

    Args:
    L (numpy.ndarray): La matriz triangular inferior.
    b (numpy.ndarray): El vector de términos independientes.

    Returns:
    numpy.ndarray: El vector solución.
    """
    n = L.shape[0]
    y = np.zeros(n)
    for i in range(n):
        suma = sum(L[i][j] * y[j] for j in range(i))
        y[i] = (b[i] - suma) / L[i][i]
    return y


def susReg(U, y):
    """
    Realiza la sustitución regresiva en una matriz triangular superior.

    Args:
    U (numpy.ndarray): La matriz triangular superior.
    y (numpy.ndarray): El vector de términos independientes.

    Returns:
    numpy.ndarray: El vector solución.
    """
    n = U.shape[0]
    x = np.zeros(n)
    for i in range(n - 1, -1, -1):
        suma = sum(U[i][j] * x[j] for j in range(i + 1, n))
        x[i] = (y[i] - suma) / U[i][i]
    return x


def lu(A):
    """
    Realiza la descomposición LU simple de una matriz.

    Args:
    A (numpy.ndarray): La matriz a descomponer.

    Returns:
    tuple: Las matrices L y U resultantes de la descomposición.
    """
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)

    for i in range(n):
        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]

    return L, U


def plu(A):
    """
    Realiza la descomposición PLU de una matriz.

    Args:
    A (numpy.ndarray): La matriz a descomponer.

    Returns:
    tuple: Las matrices P, L y U resultantes de la descomposición.
    """
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)

    for i in range(n):
        # Pivoteo parcial
        max_index = np.argmax(np.abs(U[i:, i])) + i
        if i != max_index:
            U[[i, max_index]] = U[[max_index, i]]
            P[[i, max_index]] = P[[max_index, i]]
            if i > 0:
                L[[i, max_index], :i] = L[[max_index, i], :i]

        if np.isclose(U[i, i], 0.0):
            raise ValueError("La matriz es singular y no se puede descomponer.")

        factor = U[i + 1:, i] / U[i, i]
        L[i + 1:, i] = factor
        U[i + 1:] -= factor[:, np.newaxis] * U[i]

    return P, L, U



  
  