from solver.funcionesaux import * #arreglo en la importacion
import numpy as np
import scipy
import scipy.linalg
import math

"""Capitulo 1"""
#Busquedas Incrementables
def hallarRaiz(funcionX,xi,deltax,maxIteracion):
    xini=xi
    fi=evaluar(funcionX,xi)
    if fi==0:
        return str(xi) + " es una raíz\n"
    else:
        xn = xi+deltax
        fn = evaluar(funcionX,xn)
        iteraciones=1
        while((fn*fi > 0) and (iteraciones < maxIteracion)):
            xi=xn
            fi=fn
            xn=xi+deltax
            fn=evaluar(funcionX,xn)
            print(fn)
            if(fn==0):
                return str(xn) + " es una raíz"
            iteraciones+=1
    if float(fn)*float(fi)==0:
        return str(xn) + " es una raíz"
    elif float(fn)*float(fi) < 0:
        return "entre " + str(xi) + " y " + str(xn) +" existe raíz"
    else:
        return "no existe raíz entre " + str(xini) + " y " + str(xn)+", intente un deltaX menor o grafique la funcion y asegure que la funcion cruce por el eje x"
    
#Bisección
def hallarRaizBiseccion(xi,xf,funcionX,tol):
    fi=evaluar(funcionX,xi)
    ff=evaluar(funcionX,xf)
    if fi==0:
        return str(fi)+" es una raíz"
    elif ff==0:
        return (ff)+ " es una raíz"
    elif ff*fi>0:
        return "el intervalo es incorrecto"
    else:
        xm=(xi+xf)/2
        fm=evaluar(funcionX,xm)
        error=abs(xm-xi)
        while error>=tol and fm!=0:
            if(fi*fm<0):
                xf=xm
                ff=fm
            else:
                xi=xm
                fi=fm
            xm=(xi+xf)/2
            fm=evaluar(funcionX,xm)
            error=abs(xm-xi)
    if fm==0:
        return str(xm)+" es raíz"
    else:
        return str(xm)+" es una raiz con una tolerancia de error de"+str(tol)
                
#Regla Falsa
def hallarRaizReglaFalsa(xi,xf,funcionX,tol):
    fi=evaluar(funcionX,xi)
    ff=evaluar(funcionX,xf)
    if fi==0:
        return str(fi) + " es una raíz"
    elif ff==0:
        return str(ff)+ " es una raíz"
    elif ff*fi>0:
        return "el intervalo es incorrecto"
    else:
        xm= (ff*xi-fi*xf)/(ff-fi)
        fm=evaluar(funcionX,xm)
        error=abs(xm-xi)
        while error>=tol and fm!=0:
            if(fi*fm<0):
                xf=xm
                ff=fm
            else:
                xi=xm
                fi=fm
            xm= (ff*xi-fi*xf)/(ff-fi)  #(f(b)*a-f(a)*b)/(f(b)-f(a))
            fm=evaluar(funcionX,xm)
            error=abs(xm-xi)
    if fm==0:
        return str(xm)+" es raíz"
    else:
        return str(xm)+" es una raiz con una tolerancia de error"
    
#Newton
def hallarRaizNewton(funcionX, derivadaX, x0, tol, maxIter):
    fx = evaluar(funcionX,x0)
    dfx= evaluar(derivadaX,x0)
    if(dfx==0):
        return "la derivada de la funcion es 0, por tanto no se puede usar este metodo"
    xn= x0-(fx/dfx)
    error = abs(x0-xn)
    iter = 1
    while(error >= tol and iter <= maxIter):
      x0 = xn
      fx = evaluar(funcionX,x0)
      xn = x0-(fx/dfx)
      error = abs(x0-xn)
      iter += 1
    if error <= tol:
        return str(xn)+" es raiz con un tolerancia de "+ str(tol)
    else:
        return "no se encontro raiz"
    
#Punto Fijo
def hallarRaizPuntoFijo(funcionGX,x0,tol,maxIter):
    xn=evaluar(funcionGX,x0)
    Error=abs(xn-x0)
    ite = 1
    while(tol < Error and ite <= maxIter):
        x0=xn
        xn=evaluar(funcionGX,x0)
        Error=abs(xn-x0)
        ite=+1
    if Error <= tol:
        return str(xn)+"es raiz con un tolerancia de "+str(tol)
    else:
        return "no se encontro raiz"
    
#secante
def hallarRaizSecante(funcionX,x0,x1,tol,maxIter):
    f0=evaluar(funcionX,x0)
    f1=evaluar(funcionX,x1)
    error = 1000000000000
    iter = 1
    while(error>tol and iter<maxIter):
        xn = x1-((f1*(x1-x0))/(f1-f0))
        fn = evaluar(funcionX,xn)
        error = abs(x1-xn)
        iter =+ 1
        x0=x1
        f0=f1
        x1=xn
        f1=fn
    if error <= tol:
        return str(xn)+" es raiz con una tolerancia de "+str(tol)
    else:
        return "no se encontro raiz"

#Raices Multiples
def hallarRaizRaicesMultiples(funcionX,derivateX,derivate2X,X0,tol,maxIte):
  xact=X0
  fact=evaluar(funcionX,xact)
  E=10000
  cont=0
  while E>tol and cont<maxIte :
     dfact=evaluar(derivateX,xact)
     d2act=evaluar(derivate2X,xact)
     xnew=xact - ((fact*dfact)/((dfact**2)-fact*d2act))
     fnew=evaluar(funcionX,xnew)
     E=abs(xnew-xact)
     cont+=1
     xact=xnew
     fact=fnew
  return str(xact)+" es una raiz con una tolerancia de "+str(tol)

"""Capitulo 2"""
#Eliminacion Gaussiana
def eliminacionGaussiana(n, a):
    # Vector pa soluciones
    x = np.zeros(n)
    # Gauss
    for i in range(n):
        if a[i][i] == 0.0:
            return "sistema no compatible, probar otro método"     
        for j in range(i+1, n):
            multiplicador = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - multiplicador * a[i][k]
    # Sustitucion
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i]/a[i][i]
    solucion = ""
    for i in range(n):
        solucion = solucion + 'X'+str(i+1)+' = ' + str(x[i]) + " "
    return solucion

#Eliminiacion Gaussiana con pivoteo Parcial
def pivoteoParcial(n, a):
    if n == 0:
        x = np.zeros(1)
    # Solucion
    x = np.zeros(n)
    # pivoteo
    for i in range(n):
        for j in range (i, n):
            if abs(a[i][i]) < abs(a[j][i]):
                a = cambiarFilas(a,i,j)
        if a[i][i] == 0.0:
            return 'Sistema de ecuaciones no compatible'
        # Gauss
        for j in range(i+1, n):
            multiplicador = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - multiplicador * a[i][k]
    # Sustitucion
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i]/a[i][i]
    # solucion
    solucion = ""
    for i in range(n):
        solucion = solucion + 'X'+str(i+1)+' = ' + str(x[i])+ " "
    return solucion

#Eliminacion Gaussiana con pivoteo Total
def pivoteoTotal(n, a):
    if n == 0:
        x = np.zeros(1)
    # Solucion
    x = np.zeros(n)
    # pivoteo
    for i in range(n):
        for j in range (1, n):
            if abs(a[i][i]) < abs(a[i][j]):
                a = cambiarColumnas(a,i,j)
            if abs(a[i][i]) < abs(a[j][i]):
                a = cambiarFilas(a,i,j)
        if a[i][i] == 0.0:
            return 'Sistema de ecuaciones no compatible'
        # Gauss
        for j in range(i+1, n):
            multiplicador = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] = a[j][k] - multiplicador * a[i][k]
    # Sustitucion
    x[n-1] = a[n-1][n]/a[n-1][n-1]
    for i in range(n-2,-1,-1):
        x[i] = a[i][n]
        for j in range(i+1,n):
            x[i] = x[i] - a[i][j]*x[j]
        x[i] = x[i]/a[i][i]

    # solucion
    solucion = ""
    for i in range(n):
        solucion = solucion + 'X'+str(i+1)+' = ' + str(x[i])+" "
    return solucion

#Factorizacion LU
def luSimple(A,b):
    L,U = lu(A)
    y = susprog(L,b)
    x = susReg(U,y)
    solucion = ""
    for i in range(len(x)):
        solucion = solucion+"X"+str(i+1)+" = "+str(x[i])+ " "
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
    P, L, U = plu(A)
    y = susprog(L, np.dot(P, b))
    x = susReg(U, y)
    return str(x)

#Factotizacion de Doolittle
def luDescomposicionDoolittle(A,b,n):
    L=np.zeros((n,n),float)
    U=np.zeros((n,n),float)
    for i in range(n):
        for k in range(i,n):
            sum=0
            for j in range(i):
                sum+= (L[i][j]*U[j][k])
            U[i][k]=A[i][k]-sum
        for k in range(i,n):
            if i==k:
                L[i][i]=1
            else:
                sum=0
                for j in range(i):
                    sum+=(L[k][j]*U[j][i])
                L[k][i]=float((A[k][i]-sum)/U[i][i])
    z=susprog(L,b)
    x=susReg(U,z)
    return x

#Factorizacion de Crout
def factorizacionLUCrout(A, b, n):
    L, U = luDecomposicion(A, n)
    A = np.array(A, float)
    L = np.array(L, float)
    U = np.array(U, float)
    y = np.linalg.solve(L,b)
    x = np.linalg.solve(U,y)
    solucion = ""
    for i in range(n):
        solucion = solucion + 'X'+str(i)+' = ' + str(x[i])+ " "
    return solucion

#Factotizacion de Cholesky
def cholesky(A,b,n):
    L=np.zeros((n,n),float)
    for i in range(n):
        for j in range(i+1):
            sum1=0
            if j==i:
                for k in range(j):
                    sum1+=pow(L[j][k],2)
                L[j][j]=float(math.sqrt(A[j][j]-sum1))
            else:
                for k in range(j):
                    sum1 += (L[i][k]*L[j][k])
                if L[j][j]>0:
                    L[i][j]= float((A[i][j]-sum1)/L[j][j])
    U=np.transpose(L)
    z=susprog(L,b)
    x=susReg(U,z)
    return(x)

#Metodo de Jaccobi
def jaccobii(A,b,x0,tol,nmax):
    A=np.array(A)
    b=np.array(b)
    L=-(np.tril(A,-1))
    U=-(np.triu(A,1))
    D=A+L+U
    T=(np.linalg.inv(D))*(L+U)
    C1=(np.linalg.inv(D))
    #C1*b
    C=[]
    suma=0
    for i in range(len(C1)):
        for j in range(len(C1[i])):
            suma+=C1[i][j]*b[j]
        C.append(suma)
        suma=0
    C=np.array(C)
    xn=[]
    for i in range(len(T)):
        for j in range(len(T[i])):
            suma+=T[i][j]*x0[j]
        xn.append(suma+C[i])
        suma=0
    xn=np.array(xn)
    E=1000
    cont=0
    while E>tol and cont<nmax:
        xn1=[]
        for i in range(len(T)):
            for j in range(len(T[i])):
                suma+=T[i][j]*xn[j]
            xn1.append(suma+C[i])
            suma=0
        xn1=np.array(xn1)
        xn=xn1
        cont+=1
    return xn

#Metodo de Gauss-Seidel
def gaussSeidel(A,b,x0,tol,nmax):
    A=np.array(A)
    b=np.array(b)
    x0=np.array(x0)
    U=np.triu(A,1)
    L=np.tril(A,-1)
    D=A+U+L
    T=(np.linalg.inv(D-L))*U
    C1=(np.linalg.inv(D-L))
    suma=0
    C=[]
    for i in range(len(C1)):
        for j in range(len(C1[i])):
            suma+=C1[i][j]*b[j]
        C.append(suma)
        suma=0
    C=np.array(C)
    xn=[]
    for i in range(len(T)):
        for j in range(len(T[i])):
            suma+=T[i][j]*x0[j]
        xn.append(suma+C[i])
        suma=0
    xn=np.array(xn)
    E=1000
    cont=0
    while(E>tol and cont<nmax):
        xn1=[]
        for i in range(len(T)):
            for j in range(len(T[i])):
                suma+=T[i][j]*xn[j]
            xn1.append(suma+C[i])
            suma=0
        xn1=np.array(xn1)
        xn=xn1
        cont+=1
    return xn

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