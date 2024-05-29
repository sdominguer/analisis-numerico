
## Prerrequisitos

## Introducción
Con este manual se busca proporcionarle las instrucciones detalladas a los usuarios del programa sobre cómo pueden y deben usar los métodos númericos implementados. 
Estos servirán como elementos o herramientas de gran importancia en el análisis numérico y con ellos se buscará encontrar las raíces de algunas funciones matemáticas 
proporcionadas, al igual que la o las soluciones para sistemas de ecuaciones lineales. Cada uno de los métodos que componen los dos capítulos del programa cuenta con 
una breve descripción de cuáles son las entradas que deben ingresársele, las condiciones de uso del método y la descripción de cuál será su salida; buscando con esto
que cualquier persona que use el programa, y cuente con los conocimientos matemáticos y de programación básicos necesarios, pueda aplicar adecuadamente
estas funciones para resolver sus problemas o casos específicos.

Como se podrá apreciar a continuación, el manual, al igual que el programa, se encuentra dividido en dos capítulos principales:
  - **Capítulo 1**: métodos de Búsqueda de Raíces, con técnicas como búsquedas incrementales, bisección, regla falsa, Newton, punto fijo, secante y métodos para raíces múltiples.
  - **Capítulo 2**: métodos de Eliminación, con la eliminación gaussiana (simple y con pivoteo), factorización LU y otros métodos de factorización como Doolittle, Crout, Cholesky, así como los métodos iterativos de Jacobi y Gauss-Seidel.

## Capítulo 1: Métodos de Búsqueda de Raíces

### 1. Búsquedas Incrementales
@@ -21,6 +33,9 @@
#### c. Salida
- Entrega la raíz, un rango donde está la raíz, o un mensaje indicando que no existe una raíz.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaiz("x**2 - 4", 0, 0.1, 100)

### 2. Bisección y Regla Falsa

#### a. Entradas
@@ -37,6 +52,10 @@
#### c. Salida
- Valor de la raíz exacta, valor de la raíz con un margen de error, o un mensaje informando que el intervalo es incorrecto.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaizBiseccion(0, 5, "x**2 - 4", 0.01)
- **Ejemplo de Uso**: hallarRaizReglaFalsa(0, 5, "x**2 - 4", 0.01)

### 3. Newton

#### a. Entradas
@@ -55,6 +74,9 @@
#### c. Salida
- Valor de la raíz con un margen de error, o un mensaje indicando que la derivada es cero, o que se superó la cantidad de iteraciones sin encontrar una raíz.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaizNewton("x**2 - 4", "2*x", 1, 0.01, 100)

### 4. Punto Fijo

#### a. Entradas
@@ -72,6 +94,9 @@
#### c. Salida
- Valor de la raíz con una tolerancia especificada, o un mensaje indicando que no se encuentra una raíz debido a que el error es mayor que la tolerancia.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaizPuntoFijo("x**2 - 4", 1, 0.01, 100)

### 5. Secante

#### a. Entradas
@@ -90,6 +115,9 @@
#### c. Salida
- Valor de la raíz con un margen de error, o un mensaje indicando que no se encontró raíz.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaizSecante("x**2 - 4", 1, 2, 0.01, 100)

### 6. Raíces Múltiples

#### a. Entradas
@@ -109,6 +137,9 @@
#### c. Salida
- Valor de la raíz con un margen de error especificado en las entradas.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaizMultiples("x**3 - 6*x**2 + 11*x - 6", "3*x**2 - 12*x + 11", "6*x - 12", 1, 0.01, 100)

## Capítulo 2: Métodos de Eliminación

### 1. Eliminación Gaussiana Simple
@@ -125,6 +156,9 @@
#### c. Salida
- Solución del sistema de ecuaciones.

#### d. Ejemplo
- **Ejemplo de Uso**: eliminacionGaussianaSimple("2,1,-1,8; -3,-1,2,-11; -2,1,2,-3", 3)

### 2. Eliminación Gaussiana con Pivoteo Parcial

#### a. Entradas
@@ -139,6 +173,9 @@
#### c. Salida
- Solución del sistema de ecuaciones.

#### d. Ejemplo
- **Ejemplo de Uso**: eliminacionGaussianaPivoteoParcial("2,1,-1,8; -3,-1,2,-11; -2,1,2,-3", 3)

### 3. Eliminación Gaussiana con Pivoteo Total

#### a. Entradas
@@ -153,6 +190,9 @@
#### c. Salida
- Solución del sistema de ecuaciones.

#### d. Ejemplo
- **Ejemplo de Uso**: eliminacionGaussianaPivoteoTotal("2,1,-1,8; -3,-1,2,-11; -2,1,2,-3", 3)

### 4. Factorización LU

#### a. Entradas
@@ -166,7 +206,10 @@
#### c. Salida
- Solución del sistema de ecuaciones.

### 6. Método de Doolittle
#### d. Ejemplo
- **Ejemplo de Uso**: factorizacionLU("4,3;6,3", "5,9")

### 5. Método de Doolittle

#### a. Entradas
- **A**: Matriz invertible.
@@ -181,7 +224,10 @@
#### c. Salida
- Solución del sistema de ecuaciones.

### 7. Método de Crout
#### d. Ejemplo
- **Ejemplo de Uso**: metodoDoolittle("4,3;6,3", "5,9", 2)

### 6. Método de Crout

#### a. Entradas
- **A**: Matriz invertible.
@@ -196,7 +242,10 @@
#### c. Salida
- Solución del sistema de ecuaciones.

### 8. Método de Cholesky
#### d. Ejemplo
- **Ejemplo de Uso**: metodoCrout("4,3;6,3", "5,9", 2)

### 7. Método de Cholesky

#### a. Entradas
- **A**: Matriz invertible.
@@ -211,7 +260,10 @@
#### c. Salida
- Solución del sistema de ecuaciones.

### 9. Método de Jacobi
#### d. Ejemplo
- **Ejemplo de Uso**: metodoCholesky("4,3;6,3", "5,9", 2)

### 8. Método de Jacobi

#### a. Entradas
- **A**: Matriz invertible.
@@ -229,7 +281,10 @@
#### c. Salida
- Solución del sistema de forma iterativa.

### 10. Método de Gauss-Seidel
#### d. Ejemplo
- **Ejemplo de Uso**: metodoJacobi("4,3;6,3", "5,9", "0,0", 0.01, 100)

### 9. Método de Gauss-Seidel

#### a. Entradas
- **A**: Matriz invertible.
@@ -246,3 +301,6 @@

#### c. Salida
- Solución del sistema de forma iterativa.

#### d. Ejemplo
- **Ejemplo de Uso**: metodoGaussSeidel("4,3;6,3", "5,9", "0,0", 0.01, 100)
