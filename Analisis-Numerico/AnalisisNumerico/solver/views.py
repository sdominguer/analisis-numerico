from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from solver.funciones1 import *

# Create your views here.
"""Capitulo 1"""
def index(request):
    return render(request, 'solver/index.html')
#Busquedas Incrementables
def busquedasIncrementales(request):
    hsolucion = False
    if request.method == 'POST':
        funcionX = request.POST['funcionX']
        xi = float(request.POST['xi'])
        deltax = float(request.POST['deltax'])
        maxIteracion = int(request.POST['maxIteracion'])
        solucion = hallarRaiz(funcionX, xi, deltax, maxIteracion)
        hsolucion = True
    
    if hsolucion:
        context = {"hsolucion":hsolucion,"solucion":solucion}
    else:
        context = {"hsolucion":hsolucion}
    return render(request, 'solver/busquedaIncremental.html', context)

#Regla Falsa
def reglaFalsa(request):
    bSolucion=False
    biseccion=False
    if request.method == 'POST':
        Fx=request.POST['funcion']
        xi = float(request.POST['xi'])
        xf = float(request.POST['xf'])
        tol = float(request.POST['tol'])
        solucion=hallarRaizReglaFalsa(xi,xf,Fx,tol)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"biseccion":biseccion,"solucion":solucion}
    else:
        context={"bSolucion":bSolucion,"biseccion":biseccion}
    return render(request,'solver/ByRF.html',context)

#Biseccion
def biseccion(request):
    bSolucion=False
    biseccion=True
    if request.method == 'POST':
        Fx=request.POST['funcion']
        xi = float(request.POST['xi'])
        xf = float(request.POST['xf'])
        tol = float(request.POST['tol'])
        solucion=hallarRaizBiseccion(xi,xf,Fx,tol)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"biseccion":biseccion,"solucion":solucion}
    else:
        context={"bSolucion":bSolucion,"biseccion":biseccion}
    return render(request,'solver/ByRF.html',context)

#Newton
def newton(request):
    bSolucion=False
    if request.method == 'POST':
        Fx=request.POST['funcion']
        DFx=request.POST['derivada']
        x0=float(request.POST['x0'])
        tol=float(request.POST['tol'])
        maxIte=int(request.POST['maxIte'])
        solucion=hallarRaizNewton(Fx,DFx,x0,tol,maxIte)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion}
    else:
        context={"bSolucion":bSolucion}
    return render(request,'solver/newton.html',context)

#Punto Fijo
def puntoFijo(request):
    bSolucion=False
    if request.method == 'POST':
        fGx=request.POST['funcionGX']
        x0=float(request.POST['x0'])
        tol=float(request.POST['tol'])
        maxIte=int(request.POST['maxIte'])
        solucion=hallarRaizPuntoFijo(fGx,x0,tol,maxIte)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion}
    else:
        context={"bSolucion":bSolucion}
    return render(request,'solver/puntoFijo.html',context)

#Secante
def secante(request):
    bSolucion = False
    solucion = ""

    if request.method == 'POST':
        functionX = request.POST.get('funcionX')
        x0 = request.POST.get('x0')
        x1 = request.POST.get('x1')
        tol = request.POST.get('tol')
        maxIte = request.POST.get('maxIte')

        solucion = hallarRaizSecante(functionX, x0, x1, tol, maxIte)
        bSolucion = True

    context = {"bSolucion": bSolucion, "solucion": solucion}
    return render(request, 'solver/secante.html', context)
    
#Raices Multiples
def raicesMultiples(request):
    bSolucion = False
    if request.method == 'POST':
        functionX=request.POST['funcionX']
        derivateX=request.POST['derivateX']
        derivate2X=request.POST['derivate2X']
        x0=float(request.POST['x0'])
        tol=float(request.POST['tol'])
        maxIte=int(request.POST['maxIte'])
        solucion=hallarRaizRaicesMultiples(functionX,derivateX,derivate2X,x0,tol,maxIte)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion}
    else:
        context={"bSolucion":bSolucion}
    return render(request,"solver/raicesMultiples.html",context)

"""Capitulo 2"""
#Eliminacion Gaussiana
def gauss(request):
    simple=True
    parcial=False
    bSolucion=False
    if request.method== 'POST':
        a1=request.POST['matriz']
        A=leerMatriz(a1)
        n=int(request.POST['numeroIncognitas'])
        solucion=eliminacionGaussiana(n,A)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion,"simple":simple,"parcial":parcial}
    else:
        context={"bSolucion":bSolucion,"simple":simple,"parcial":parcial}
    return render(request,"solver/gauss.html",context)
        
#Eliminiacion Gaussiana con pivoteo Parcial
def gaussParcial(request):
    simple=False
    parcial=True
    bSolucion=False
    if request.method== 'POST':
        a1=request.POST['matriz']
        A=leerMatriz(a1)
        A = np.array(A, float)
        n=int(request.POST['numeroIncognitas'])
        solucion=pivoteoParcial(n,A)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion,"simple":simple,"parcial":parcial}
    else:
        context={"bSolucion":bSolucion,"simple":simple,"parcial":parcial}
    return render(request,"solver/gauss.html",context)

#Eliminacion Gaussiana con pivoteo Total
def gaussTotal(request):
    simple=False
    parcial=False
    bSolucion=False
    if request.method== 'POST':
        a1=request.POST['matriz']
        A=leerMatriz(a1)
        A = np.array(A, float)
        n=int(request.POST['numeroIncognitas'])
        solucion=pivoteoTotal(n,A)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion,"simple":simple,"parcial":parcial}
    else:
        context={"bSolucion":bSolucion,"simple":simple,"parcial":parcial}
    return render(request,"solver/gauss.html",context)

#Factorizacion LU
def LU(request):
    bSolucion=False
    if request.method == 'POST':
        a=request.POST['A']
        B=request.POST['b']
        A=leerMatriz(a)
        b=leerVector(B)
        A=np.array(A)
        solucion=luSimple(A,b)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion}
    else:
        context={"bSolucion":bSolucion}
    return render(request,"solver/LU.html",context)

#Factorizacion LU con pivoteo Parcial
def LUPar(request):
    bSolucion=False
    if request.method == 'POST':
        a=request.POST['A']
        B=request.POST['b']
        A=leerMatriz(a)
        A=np.array(A)
        b=leerVector(B)
        solucion=luPivote(A,b)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion}
    else:
        context={"bSolucion":bSolucion}
    return render(request,"solver/LUPar.html",context)

#Factotizacion de Doolittle
def Doolittle(request):
    doolittle=True
    crout=False
    bSolucion=False
    if request.method == 'POST':
        A1=request.POST['A']
        A=leerMatriz(A1)
        b1=request.POST['b']
        b=leerVector(b1)
        n=int(request.POST['n'])
        solucion=luDescomposicionDoolittle(A,b,n)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion,"doolittle":doolittle,"crout":crout}
    else:
        context={"bSolucion":bSolucion,"doolittle":doolittle,"crout":crout}
    return render(request,"solver/Crout_Doolittle_Cholesky.html",context)
        
#Factorizacion de Crout
def Crout(request):
    doolittle=False
    crout=True
    bSolucion=False
    if request.method == 'POST':
        A1=request.POST['A']
        A=leerMatriz(A1)
        b1=request.POST['b']
        b=leerVector(b1)
        n=int(request.POST['n'])
        solucion=factorizacionLUCrout(A,b,n)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion,"doolittle":doolittle,"crout":crout}
    else:
        context={"bSolucion":bSolucion,"doolittle":doolittle,"crout":crout}
    return render(request,"solver/Crout_Doolittle_Cholesky.html",context)

#Factotizacion de Cholesky
def Cholesky(request):
    doolittle=False
    crout=False
    bSolucion=False
    if request.method == 'POST':
        A1=request.POST['A']
        A=leerMatriz(A1)
        b1=request.POST['b']
        b=leerVector(b1)
        n=int(request.POST['n'])
        solucion=cholesky(A,b,n)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion,"doolittle":doolittle,"crout":crout}
    else:
        context={"bSolucion":bSolucion,"doolittle":doolittle,"crout":crout}
    return render(request,"solver/Crout_Doolittle_Cholesky.html",context)

#Metodo de Jaccobi
def Jaccobi(request):
    jaccobi=True
    bSolucion=False
    if request.method == 'POST':
        A1=request.POST['A']
        A=leerMatriz(A1)
        b1=request.POST['b']
        b=leerVector(b1)
        x01=request.POST['x0']
        x0=leerVector(x01)
        tol=float(request.POST['tol'])
        maxIte=int(request.POST['maxIte'])
        solucion=jaccobii(A,b,x0,tol,maxIte)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"jaccobi":jaccobi,"solucion":solucion}
    else:
        context={"bSolucion":bSolucion,"jaccobi":jaccobi}
    return render(request,"solver/JyGS.html",context)
        
#Metodo de Gauss-Seidel
def GaussSeidel(request):
    jaccobi=False
    bSolucion=False
    if request.method == 'POST':
        A1=request.POST['A']
        A=leerMatriz(A1)
        b1=request.POST['b']
        b=leerVector(b1)
        x01=request.POST['x0']
        x0=leerVector(x01)
        tol=request.POST['tol']
        maxIte=request.POST['maxIte']
        solucion=gaussSeidel(A,b,x0,tol,maxIte)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"jaccobi":jaccobi,"solucion":solucion}
    else:
        context={"bSolucion":bSolucion,"jaccobi":jaccobi}
    return render(request,"solver/JyGS.html",context)

"""Capitulo 3"""

#Metodo de Vandermonde
def Vandermonde(request):
    bSolucion=False
    if request.method == 'POST':
        x1=request.POST['x']
        x=leerVector(str(x1))
        y1=request.POST['y']
        y=leerVector(str(y1))
        solucion = vandermonde(x,y)
        bSolucion=True
    if bSolucion:
        context={"bSolucion":bSolucion,"solucion":solucion}
    else:
        context={"bSolucion":bSolucion}
    return render(request,"solver/vandermonde.html",context)