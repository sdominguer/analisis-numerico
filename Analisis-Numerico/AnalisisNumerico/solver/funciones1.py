from solver.funcionesaux import * #arreglo en la importacion
import solver
import solver.funcionesaux
import numpy as np
import scipy
import scipy.linalg
import math

"""Capitulo 1"""
#Busquedas Incrementables
def hallarRaiz(funcionX, xi, deltax, maxIteracion):
    """
    Encuentra una raíz de la función usando el método de búsquedas incrementales.

    Args:
    funcionX (str): La función matemática en forma de cadena.
    xi (float): El valor inicial.
    deltax (float): El incremento de x.
    maxIteracion (int): El número máximo de iteraciones.

    Returns:
    str: El resultado indicando la raíz encontrada o el intervalo donde existe una raíz.
    """
    xini = xi
    fi = evaluar(funcionX, xi)

    if fi == 0:
        return f"{xi} es una raíz\n"

    xn = xi + deltax
    fn = evaluar(funcionX, xn)
    iteraciones = 1

    while (fn * fi > 0) and (iteraciones < maxIteracion):
        xi = xn
        fi = fn
        xn = xi + deltax
        fn = evaluar(funcionX, xn)
        if fn == 0:
            return f"{xn} es una raíz"
        iteraciones += 1

    if fn * fi == 0:
        return f"{xn} es una raíz"
    elif fn * fi < 0:
        return f"entre {xi} y {xn} existe raíz"
    else:
        return f"no existe raíz entre {xini} y {xn}, intente un deltaX menor o grafique la función y asegure que la función cruce por el eje x"


#Bisección
def hallarRaizBiseccion(xi, xf, funcionX, tol):
    """
    Encuentra una raíz de la función usando el método de bisección.

    Args:
    xi (float): El valor inicial inferior del intervalo.
    xf (float): El valor inicial superior del intervalo.
    funcionX (str): La función matemática en forma de cadena.
    tol (float): La tolerancia de error aceptable.

    Returns:
    str: El resultado indicando la raíz encontrada o un mensaje de error.
    """
    fi = evaluar(funcionX, xi)
    ff = evaluar(funcionX, xf)

    if fi == 0:
        return f"{xi} es una raíz"
    elif ff == 0:
        return f"{xf} es una raíz"
    elif fi * ff > 0:
        return "El intervalo es incorrecto. No se puede aplicar el método de bisección."

    xm = (xi + xf) / 2
    fm = evaluar(funcionX, xm)
    error = abs(xf - xi)

    while error >= tol and fm != 0:
        if fi * fm < 0:
            xf = xm
            ff = fm
        else:
            xi = xm
            fi = fm
        xm = (xi + xf) / 2
        fm = evaluar(funcionX, xm)
        error = abs(xf - xi)

    if fm == 0:
        return f"{xm} es raíz"
    else:
        return f"{xm} es una raíz con una tolerancia de error de {tol}"


#Regla Falsa
def hallarRaizReglaFalsa(xi, xf, funcionX, tol):
    """
    Encuentra una raíz de la función usando el método de la regla falsa.

    Args:
    xi (float): El valor inicial inferior del intervalo.
    xf (float): El valor inicial superior del intervalo.
    funcionX (str): La función matemática en forma de cadena.
    tol (float): La tolerancia de error aceptable.

    Returns:
    str: El resultado indicando la raíz encontrada o un mensaje de error.
    """
    fi = evaluar(funcionX, xi)
    ff = evaluar(funcionX, xf)

    if fi == 0:
        return f"{xi} es una raíz"
    elif ff == 0:
        return f"{xf} es una raíz"
    elif fi * ff > 0:
        return "El intervalo es incorrecto. No se puede aplicar el método de la regla falsa."

    xm = (ff * xi - fi * xf) / (ff - fi)
    fm = evaluar(funcionX, xm)
    error = abs(xf - xi)

    while error >= tol and fm != 0:
        if fi * fm < 0:
            xf = xm
            ff = fm
        else:
            xi = xm
            fi = fm
        xm = (ff * xi - fi * xf) / (ff - fi)
        fm = evaluar(funcionX, xm)
        error = abs(xf - xi)

    if fm == 0:
        return f"{xm} es raíz"
    else:
        return f"{xm} es una raíz con una tolerancia de error de {tol}"


#Newton
def hallarRaizNewton(funcionX, derivadaX, x0, tol, maxIter):
    """
    Encuentra una raíz de la función usando el método de Newton.

    Args:
    funcionX (str): La función matemática en forma de cadena.
    derivadaX (str): La derivada de la función matemática en forma de cadena.
    x0 (float): El valor inicial.
    tol (float): La tolerancia de error aceptable.
    maxIter (int): El número máximo de iteraciones.

    Returns:
    str: El resultado indicando la raíz encontrada o un mensaje de error.
    """
    fx = evaluar(funcionX, x0)
    dfx = evaluar(derivadaX, x0)

    if dfx == 0:
        return "La derivada de la función es 0, por tanto no se puede usar este método."

    xn = x0 - (fx / dfx)
    error = abs(x0 - xn)
    iteraciones = 1

    while error >= tol and iteraciones <= maxIter:
        x0 = xn
        fx = evaluar(funcionX, x0)
        dfx = evaluar(derivadaX, x0)

        if dfx == 0:
            return "La derivada de la función es 0, por tanto no se puede usar este método."

        xn = x0 - (fx / dfx)
        error = abs(x0 - xn)
        iteraciones += 1

    if error <= tol:
        return f"{xn} es raíz con una tolerancia de {tol}"
    else:
        return "No se encontró raíz en el número máximo de iteraciones."


#Punto Fijo
def hallarRaizPuntoFijo(funcionGX, x0, tol, maxIter):
    """
    Encuentra una raíz de la función usando el método del punto fijo.

    Args:
    funcionGX (str): La función G(x) en forma de cadena.
    x0 (float): El valor inicial.
    tol (float): La tolerancia de error aceptable.
    maxIter (int): El número máximo de iteraciones.

    Returns:
    str: El resultado indicando la raíz encontrada o un mensaje de error.
    """
    xn = evaluar(funcionGX, x0)
    error = abs(xn - x0)
    iteraciones = 1

    while error >= tol and iteraciones <= maxIter:
        x0 = xn
        xn = evaluar(funcionGX, x0)
        error = abs(xn - x0)
        iteraciones += 1

    if error <= tol:
        return f"{xn} es raíz con una tolerancia de {tol}"
    else:
        return "No se encontró raíz en el número máximo de iteraciones."


#secante
def hallarRaizSecante(funcionX, x0, x1, tol, maxIter):
    """
    Encuentra una raíz de la función usando el método de la secante.

    Args:
    funcionX (str): La función matemática en forma de cadena.
    x0 (float or str): El primer valor inicial.
    x1 (float or str): El segundo valor inicial.
    tol (float or str): La tolerancia de error aceptable.
    maxIter (int or str): El número máximo de iteraciones.

    Returns:
    str: El resultado indicando la raíz encontrada o un mensaje de error.
    """
    # Convertir los valores a los tipos adecuados
    x0 = float(x0)
    x1 = float(x1)
    tol = float(tol)
    maxIter = int(maxIter)

    f0 = evaluar(funcionX, x0)
    f1 = evaluar(funcionX, x1)
    error = float('inf')
    iteraciones = 1

    while error > tol and iteraciones < maxIter:
        if f1 == f0:
            return "No se puede continuar porque f1 y f0 son iguales, lo que causaría una división por cero."

        xn = x1 - (f1 * (x1 - x0)) / (f1 - f0)
        fn = evaluar(funcionX, float(xn))
        error = abs(x1 - xn)
        iteraciones += 1

        x0, f0 = x1, f1
        x1, f1 = xn, fn

    if error <= tol:
        return f"{xn} es raíz con una tolerancia de {tol}"
    else:
        return "No se encontró raíz en el número máximo de iteraciones."


#Raices Multiples
def hallarRaizRaicesMultiples(funcionX, derivadaX, derivada2X, X0, tol, maxIter):
    """
    Encuentra una raíz de la función usando el método de raíces múltiples.

    Args:
    funcionX (str): La función matemática en forma de cadena.
    derivadaX (str): La derivada de la función en forma de cadena.
    derivada2X (str): La segunda derivada de la función en forma de cadena.
    X0 (float): El valor inicial.
    tol (float): La tolerancia de error aceptable.
    maxIter (int): El número máximo de iteraciones.

    Returns:
    str: El resultado indicando la raíz encontrada o un mensaje de error.
    """
    xact = X0
    fact = evaluar(funcionX, xact)
    error = float('inf')
    iteraciones = 0

    while error > tol and iteraciones < maxIter:
        dfact = evaluar(derivadaX, xact)
        d2fact = evaluar(derivada2X, xact)

        if (dfact ** 2 - fact * d2fact) == 0:
            return "División por cero en el cálculo. No se puede continuar."

        xnew = xact - (fact * dfact) / (dfact ** 2 - fact * d2fact)
        fnew = evaluar(funcionX, xnew)
        error = abs(xnew - xact)

        iteraciones += 1
        xact = xnew
        fact = fnew

    if error <= tol:
        return f"{xact} es una raíz con una tolerancia de {tol}"
    else:
        return "No se encontró raíz en el número máximo de iteraciones."


"""Capitulo 2"""
#Eliminacion Gaussiana
def eliminacionGaussiana(n, a):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de eliminación gaussiana.

    Args:
    n (int): El número de ecuaciones (y variables).
    a (list of list of float): La matriz aumentada del sistema de ecuaciones.

    Returns:
    str: El resultado indicando las soluciones encontradas o un mensaje de error.
    """
    A = np.array(a, dtype=float)  # Convertir la matriz a un array de numpy para facilitar el manejo
    x = np.zeros(n)  # Vector para soluciones

    # Gauss
    for i in range(n):
        if A[i][i] == 0.0:
            return "Sistema no compatible, probar otro método"
        for j in range(i + 1, n):
            multiplicador = A[j][i] / A[i][i]
            A[j][i:] -= multiplicador * A[i][i:]

    # Sustitución hacia atrás
    x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += A[i][j] * x[j]
        x[i] = (A[i][n] - suma) / A[i][i]

    solucion = ""
    for i in range(n):
        solucion += f'X{i + 1} = {x[i]} '
    return solucion


#Eliminiacion Gaussiana con pivoteo Parcial
def pivoteoParcial(n, a):
    """
    Resuelve un sistema de ecuaciones usando eliminación gaussiana con pivoteo parcial.

    Args:
    n (int): El número de ecuaciones.
    a (numpy.ndarray): La matriz aumentada del sistema.

    Returns:
    str: El resultado indicando las soluciones del sistema o un mensaje de error.
    """
    x = np.zeros(n)

    for i in range(n):
        max_index = i + np.argmax(np.abs(a[i:n, i]))
        if a[max_index, i] == 0:
            return "Sistema de ecuaciones no compatible"

        if max_index != i:
            a[[i, max_index]] = a[[max_index, i]]

        for j in range(i + 1, n):
            multiplicador = a[j][i] / a[i][i]
            a[j][i:] -= multiplicador * a[i][i:]

    x[n - 1] = a[n - 1][n] / a[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        x[i] = (a[i][n] - np.dot(a[i][i + 1:], x[i + 1:])) / a[i][i]

    solucion = " ".join([f"X{i + 1} = {x[i]}" for i in range(n)])
    return solucion


#Eliminacion Gaussiana con pivoteo Total
def pivoteoTotal(n, a):
    """
    Resuelve un sistema de ecuaciones lineales usando el método de eliminación gaussiana con pivoteo total.

    Args:
    n (int): El número de ecuaciones (y variables).
    a (list of list of float): La matriz aumentada del sistema de ecuaciones.

    Returns:
    str: El resultado indicando las soluciones encontradas o un mensaje de error.
    """
    A = np.array(a, dtype=float)  # Convertir la matriz a un array de numpy para facilitar el manejo
    x = np.zeros(n)  # Vector para soluciones
    indices = np.arange(n)

    # Pivoteo total y eliminación Gaussiana
    for i in range(n):
        # Pivoteo total
        sub_matriz = np.abs(A[i:, i:n])  # Submatriz para encontrar el pivote
        max_index = np.unravel_index(np.argmax(sub_matriz), sub_matriz.shape)
        max_index = (max_index[0] + i, max_index[1] + i)

        if A[max_index[0], max_index[1]] == 0:
            return 'Sistema de ecuaciones no compatible'

        # Cambiar filas
        if max_index[0] != i:
            A = cambiarFilas(A, i, max_index[0])

        # Cambiar columnas
        if max_index[1] != i:
            A = cambiarColumnas(A, i, max_index[1])
            indices[i], indices[max_index[1]] = indices[max_index[1]], indices[i]

        # Gauss
        for j in range(i + 1, n):
            multiplicador = A[j][i] / A[i][i]
            A[j][i:] -= multiplicador * A[i][i:]

    # Sustitución hacia atrás
    x[n - 1] = A[n - 1][n] / A[n - 1][n - 1]
    for i in range(n - 2, -1, -1):
        suma = 0
        for j in range(i + 1, n):
            suma += A[i][j] * x[j]
        x[i] = (A[i][n] - suma) / A[i][i]

    # Reordenar las soluciones de acuerdo con los intercambios de columnas
    x_final = np.zeros(n)
    for i in range(n):
        x_final[indices[i]] = x[i]

    # Construcción de la solución
    solucion = ""
    for i in range(n):
        solucion += f'X{i + 1} = {x_final[i]} '
    return solucion

#Factorizacion LU
def luSimple(A, b):
    """
    Resuelve un sistema de ecuaciones usando factorización LU simple.

    Args:
    A (numpy.ndarray): La matriz del sistema.
    b (numpy.ndarray): El vector de términos independientes.

    Returns:
    str: El resultado indicando las soluciones del sistema.
    """
    L, U = lu(A)
    y = susprog(L, b)
    x = susReg(U, y)

    solucion = " ".join([f"X{i + 1} = {x[i]}" for i in range(len(x))])
    return solucion


#Factorizacion LU con pivoteo Parcial Temporal
"""def metodoLUPar(A,b):
    P,L,U = scipy.linalg.lu(A)
    A=np.array(A,float)
    P = np.array(P,float)
    L = np.array(L,float)
    U = np.array(U,float)
    L = np.dot(P,L)
    z = np.linalg.solve(L,b)
    x = np.linalg.solve(U,z)
    return str(x)"""


def luPivote(A, b):
    """
    Resuelve un sistema de ecuaciones usando factorización LU con pivoteo parcial.

    Args:
    A (numpy.ndarray): La matriz del sistema.
    b (numpy.ndarray): El vector de términos independientes.

    Returns:
    str: El resultado indicando las soluciones del sistema.
    """
    P, L, U = plu(A)
    y = susprog(L, np.dot(P, b))
    x = susReg(U, y)

    solucion = " ".join([f"X{i + 1} = {x[i]}" for i in range(len(x))])
    return solucion


#Factotizacion de Doolittle
def luDescomposicionDoolittle(A, b, n):
    """
    Resuelve un sistema de ecuaciones usando factorización LU de Doolittle.

    Args:
    A (numpy.ndarray): La matriz del sistema.
    b (numpy.ndarray): El vector de términos independientes.
    n (int): El tamaño de la matriz.

    Returns:
    str: El resultado indicando las soluciones del sistema.
    """
    L = np.zeros((n, n), float)
    U = np.zeros((n, n), float)

    for i in range(n):
        for k in range(i, n):
            suma = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - suma
        for k in range(i, n):
            if i == k:
                L[i][i] = 1
            else:
                suma = sum(L[k][j] * U[j][i] for j in range(i))
                L[k][i] = (A[k][i] - suma) / U[i][i]

    y = susprog(L, b)
    x = susReg(U, y)

    solucion = " ".join([f"X{i + 1} = {x[i]}" for i in range(len(x))])
    return solucion


#Factorizacion de Crout
def factorizacionLUCrout(A, b, n):
    """
    Resuelve un sistema de ecuaciones usando factorización LU de Crout.

    Args:
    A (numpy.ndarray): La matriz del sistema.
    b (numpy.ndarray): El vector de términos independientes.
    n (int): El tamaño de la matriz.

    Returns:
    str: El resultado indicando las soluciones del sistema.
    """
    L, U = luDecomposicion(A, n)
    y = np.linalg.solve(L, b)
    x = np.linalg.solve(U, y)

    solucion = " ".join([f"X{i + 1} = {x[i]}" for i in range(n)])
    return solucion


#Factotizacion de Cholesky
def cholesky(A, b, n):
    """
    Resuelve un sistema de ecuaciones usando factorización de Cholesky.

    Args:
    A (numpy.ndarray): La matriz del sistema.
    b (numpy.ndarray): El vector de términos independientes.
    n (int): El tamaño de la matriz.

    Returns:
    str: El resultado indicando las soluciones del sistema.
    """
    L = np.zeros((n, n), float)

    for i in range(n):
        for j in range(i + 1):
            if j == i:  # Elementos de la diagonal
                sum1 = sum(L[i][k] ** 2 for k in range(j))
                value = A[i][i] - sum1
                if value < 0:
                    return "Error: La matriz no es definida positiva."
                L[i][j] = math.sqrt(value)
            else:
                sum1 = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (A[i][j] - sum1) / L[j][j]

    U = np.transpose(L)
    y = susprog(L, b)
    x = susReg(U, y)

    solucion = " ".join([f"X{i + 1} = {x[i]}" for i in range(len(x))])
    return solucion



#Metodo de Jaccobi
def jacobi(A, b, x0, tol, nmax):
    """
    Resuelve un sistema de ecuaciones usando el método de Jacobi.

    Args:
    A (numpy.ndarray): La matriz del sistema.
    b (numpy.ndarray): El vector de términos independientes.
    x0 (numpy.ndarray): El vector inicial.
    tol (float): La tolerancia de error aceptable.
    nmax (int): El número máximo de iteraciones.

    Returns:
    str: El resultado indicando las soluciones del sistema.
    """
    A, b, x0 = np.array(A), np.array(b), np.array(x0)
    L, U = -np.tril(A, -1), -np.triu(A, 1)
    D_inv = np.linalg.inv(np.diag(np.diag(A)))

    T = np.dot(D_inv, L + U)
    C = np.dot(D_inv, b)

    x = np.dot(T, x0) + C
    error = np.linalg.norm(x - x0, ord=np.inf)
    iteraciones = 0

    while error > tol and iteraciones < nmax:
        x0 = x
        x = np.dot(T, x0) + C
        error = np.linalg.norm(x - x0, ord=np.inf)
        iteraciones += 1

    solucion = " ".join([f"X{i + 1} = {x[i]}" for i in range(len(x))])
    return solucion


#Metodo de Gauss-Seidel
def gaussSeidel(A, b, x0, tol, nmax):
    """
    Resuelve un sistema de ecuaciones usando el método de Gauss-Seidel.

    Args:
    A (numpy.ndarray): La matriz del sistema.
    b (numpy.ndarray): El vector de términos independientes.
    x0 (numpy.ndarray): El vector inicial.
    tol (float): La tolerancia de error aceptable.
    nmax (int): El número máximo de iteraciones.

    Returns:
    str: El resultado indicando las soluciones del sistema.
    """
    A, b, x0 = np.array(A), np.array(b), np.array(x0)
    n = len(b)
    x = np.copy(x0)

    iteraciones = 0
    error = float('inf')

    while error > tol and iteraciones < nmax:
        x_old = np.copy(x)

        for i in range(n):
            sum1 = sum(A[i, j] * x[j] for j in range(i))
            sum2 = sum(A[i, j] * x_old[j] for j in range(i + 1, n))
            x[i] = (b[i] - sum1 - sum2) / A[i, i]

        error = np.linalg.norm(x - x_old, ord=np.inf)
        iteraciones += 1

    solucion = " ".join([f"X{i + 1} = {x[i]}" for i in range(len(x))])
    return solucion


"""Capitulo 3"""
#Metodo de Vandermonde
def vandermonde(x,y):
    cont=len(x)-1
    A = []
    for i in range(len(x)):
        A.append([])
        for j in range(len(x)):
            A[i].append(x[i]**cont)
            cont-=1
        cont=len(x)-1   
    A=np.array(A)
    b=np.array(y)
    Ainv=np.linalg.inv(A)
#b=np.transpose(b)
    res=[]
    total=0
    for i in range(len(Ainv)):
        for j in range(len(b)):
            total+=Ainv[i][j]*b[j]
        res.append(total)
        total=0
    return(res)