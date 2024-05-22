"""AnalisisNumerico URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from solver.views import busquedasIncrementales, biseccion, index, reglaFalsa,newton,puntoFijo,raicesMultiples,secante,Jaccobi,GaussSeidel,Vandermonde
from solver.views import gauss, gaussParcial, gaussTotal,LU,LUPar,Crout,Doolittle,Cholesky
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('busquedas-incrementales/', busquedasIncrementales, name='busquedas-incrementales'),
    path('biseccion/',biseccion, name='biseccion'),
    path('reglaFalsa/',reglaFalsa, name='reglaFalsa'),
    path('newton/',newton, name="newton"),
    path('puntoFijo/',puntoFijo,name="puntoFijo"),
    path('secante/',secante, name='secante'),
    path('raicesMultiples/',raicesMultiples,name='raicesMultiples'),
    path('eliminacionGaussiana/',gauss, name='gauss'),
    path('eliminacionGaussianaParcial',gaussParcial,name='gaussParcial'),
    path('eliminacionGaussianaTotal',gaussTotal,name='gaussTotal'),
    path('factorizacionLU/',LU, name='factorizacionLU'),
    path('factorizacionLUPar/',LUPar, name='factorizacionLUPar'),
    path('factorizacionCrout/',Crout,name='factorizacionCrout'),
    path('factorizacionDoolittle/',Doolittle,name='factorizacionDoolittle'),
    path('factorizacionCholesky/',Cholesky,name='factorizacionCholesky'),
    path('jaccobi/',Jaccobi,name='jaccobi'),
    path('gaussSeidel/',GaussSeidel,name='gaussSeidel'),
    path('vandermonde/',Vandermonde, name='vandermonde'),
]