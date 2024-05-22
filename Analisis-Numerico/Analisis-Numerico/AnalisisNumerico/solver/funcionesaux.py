import numpy as np

def evaluar(funcion,valor):
  x=valor
  return eval(funcion)




def leerMatriz(matriz):
    A=[]
    filas=matriz.split(';')
    for i in range(len(filas)):
        columnas=filas[i].split(',')
        A.append([])
        for j in range(len(columnas)):
            A[i].append(float(columnas[j]))
    return A
  
def leerVector(vector):
    A=[]
    columnas=vector.split(',')
    for j in range(len(columnas)):
        A.append(float(columnas[j]))
    return A
    
            
def cambiarFilas(matriz, fila1, fila2):
    matriz[[fila1, fila2]] = matriz[[fila2, fila1]]
    return matriz

def cambiarColumnas(matriz, _a, _b):
    matriz[:,[_a, _b]] = matriz[:,[_b, _a]]
    return matriz
  
def luDecomposicion(A, n): 
    L = np.zeros((n, n))  
    U = np.zeros((n, n))
    for k in range (n):
        for i in range(k,n):
            sum1=0
            for p in range (k):
                sum1+=L[i][p]*U[p][k]
            L[i][k]=(A[i][k]-sum1)
        for i in range(k+1,n):
            if L[k][k] == 0:
                return "Debe usar el pivoteo parcial"
            sum2=0
            for p in range(k):
                sum2+=L[k][p]*U[p][i]
            U[k][i]=(A[k][i]-sum2)/L[k][k]
    U = U + np.eye(n, dtype=float)
    return L,U
  
def susprog(L, b):
    n = L.shape[0]
    y = np.zeros_like(b, dtype=np.double)
    y[0] = b[0] / L[0, 0]
    for i in range(1, n):
        y[i] = (b[i] - np.dot(L[i,:i], y[:i])) / L[i,i]
        
    return y

def susReg(U, y):
    n = U.shape[0]
    x = np.zeros_like(y, dtype=np.double)
    x[-1] = y[-1] / U[-1, -1]
    for i in range(n-2, -1, -1):
        x[i] = (y[i] - np.dot(U[i,i:], x[i:])) / U[i,i]
        
    return x

def lu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    for i in range(n):
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
    return L, U
  
def plu(A):
    n = A.shape[0]
    U = A.copy()
    L = np.eye(n, dtype=np.double)
    P = np.eye(n, dtype=np.double)
    
    for i in range(n):
        for k in range(i, n): 
            if ~np.isclose(U[i, i], 0.0):
                break
            U[[k, k+1]] = U[[k+1, k]]
            P[[k, k+1]] = P[[k+1, k]]
        factor = U[i+1:, i] / U[i, i]
        L[i+1:, i] = factor
        U[i+1:] -= factor[:, np.newaxis] * U[i]
        
    return P, L, U
  
  
  