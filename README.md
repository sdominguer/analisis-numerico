# Manual de Usuario de los Métodos

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

#### a. Entradas
- **FuncionX**: Función continua a evaluar.
- **Xi**: Punto de valor numérico donde inicia la búsqueda.
- **DeltaX**: Incremento en cada iteración.
- **MaxIteracion**: La máxima cantidad de iteraciones que puede realizar.

#### b. Condiciones
- La función debe estar escrita en sintaxis de operaciones de Python sin librerías.
- Xi debe ser un valor entero.
- DeltaX, en caso de no ser entero, debe tener el decimal separado con “.”.
- MaxIteracion solo puede ser un valor entero positivo.

#### c. Salida
- Entrega la raíz, un rango donde está la raíz, o un mensaje indicando que no existe una raíz.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaiz("x**2 - 4", 0, 0.1, 100)

### 2. Bisección y Regla Falsa

#### a. Entradas
- **Xi**: Límite inferior del intervalo en el que se busca la raíz.
- **Xf**: Límite superior del intervalo en el que se busca la raíz.
- **FuncionX**: Función a evaluar.
- **Tol**: Margen de error permitido del valor de la raíz.

#### b. Condiciones
- Xi y Xf deben ser valores enteros.
- La función debe estar escrita en sintaxis de operaciones de Python sin librerías.
- Tol, en caso de no ser entero, debe tener el decimal separado con “.”.

#### c. Salida
- Valor de la raíz exacta, valor de la raíz con un margen de error, o un mensaje informando que el intervalo es incorrecto.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaizBiseccion(0, 5, "x**2 - 4", 0.01)
- **Ejemplo de Uso**: hallarRaizReglaFalsa(0, 5, "x**2 - 4", 0.01)

### 3. Newton

#### a. Entradas
- **FuncionX**: Función continua a evaluar.
- **DerivadaX**: Derivada de la función a evaluar.
- **X0**: Valor inicial en que se realizará el método.
- **Tol**: Margen de error permitido del valor de la raíz.
- **MaxIter**: La máxima cantidad de iteraciones que puede realizar.

#### b. Condiciones
- FuncionX y derivadaX deben estar escritas en sintaxis de operaciones de Python sin librerías.
- X0 debe ser un valor entero.
- Tol, en caso de no ser entero, debe tener el decimal separado con “.”.
- MaxIteracion solo puede ser un valor entero positivo.

#### c. Salida
- Valor de la raíz con un margen de error, o un mensaje indicando que la derivada es cero, o que se superó la cantidad de iteraciones sin encontrar una raíz.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaizNewton("x**2 - 4", "2*x", 1, 0.01, 100)

### 4. Punto Fijo

#### a. Entradas
- **FuncionGX**: Función después de despejar X, escrita en sintaxis de operaciones de Python sin librerías.
- **X0**: Valor inicial en que se realizará el método.
- **Tol**: Margen de error permitido del valor de la raíz.
- **MaxIter**: La máxima cantidad de iteraciones que puede realizar.

#### b. Condiciones
- FuncionGX debe estar escrita en sintaxis de operaciones de Python sin librerías.
- X0 debe ser un valor entero.
- Tol, en caso de no ser entero, debe tener el decimal separado con “.”.
- MaxIteracion solo puede ser un valor entero positivo.

#### c. Salida
- Valor de la raíz con una tolerancia especificada, o un mensaje indicando que no se encuentra una raíz debido a que el error es mayor que la tolerancia.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaizPuntoFijo("x**2 - 4", 1, 0.01, 100)

### 5. Secante

#### a. Entradas
- **FuncionX**: Función continua a evaluar.
- **X0**: Valor inicial a evaluar la función.
- **X1**: Valor siguiente del valor inicial para evaluar la función.
- **Tol**: Margen de error permitido del valor de la raíz.
- **MaxIter**: La máxima cantidad de iteraciones que puede realizar.

#### b. Condiciones
- La función debe estar escrita en sintaxis de operaciones de Python sin librerías.
- X0 y X1 deben ser valores enteros.
- Tol, en caso de no ser entero, debe tener el decimal separado con “.”.
- MaxIter solo puede ser un valor entero positivo.

#### c. Salida
- Valor de la raíz con un margen de error, o un mensaje indicando que no se encontró raíz.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaizSecante("x**2 - 4", 1, 2, 0.01, 100)

### 6. Raíces Múltiples

#### a. Entradas
- **FuncionX**: Función continua a evaluar.
- **DerivadaX**: Derivada de la función a evaluar.
- **Derivada2X**: Segunda derivada de la función a evaluar.
- **X0**: Valor inicial en que se realizará el método.
- **Tol**: Margen de error permitido del valor de la raíz.
- **MaxIter**: La máxima cantidad de iteraciones que puede realizar.

#### b. Condiciones
- FuncionX, derivadaX, y derivada2X deben estar escritas en sintaxis de operaciones de Python sin librerías.
- X0 debe ser un valor entero.
- Tol, en caso de no ser entero, debe tener el decimal separado con “.”.
- MaxIter solo puede ser un valor entero positivo.

#### c. Salida
- Valor de la raíz con un margen de error especificado en las entradas.

#### d. Ejemplo
- **Ejemplo de Uso**: hallarRaizMultiples("x**3 - 6*x**2 + 11*x - 6", "3*x**2 - 12*x + 11", "6*x - 12", 1, 0.01, 100)

## Capítulo 2: Métodos de Eliminación

### 1. Eliminación Gaussiana Simple

#### a. Entradas
- **A**: Matriz Aumentada de una matriz invertible y un vector constante.
- **N**: Número de incógnitas.

#### b. Condiciones
- En la diagonal no debe haber algún valor cero.
- El número de incógnitas debe ser correcto, de lo contrario el método fallará.
- La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. Ejemplo: `2,2;2,2`.

#### c. Salida
- Solución del sistema de ecuaciones.

#### d. Ejemplo
- **Ejemplo de Uso**: eliminacionGaussianaSimple("2,1,-1,8; -3,-1,2,-11; -2,1,2,-3", 3)

### 2. Eliminación Gaussiana con Pivoteo Parcial

#### a. Entradas
- **A**: Matriz Aumentada de una matriz invertible y un vector constante.
- **N**: Número de incógnitas.

#### b. Condiciones
- En cada columna debajo del pivote debe haber al menos un elemento diferente de cero, incluyendo al pivote.
- El número de incógnitas debe ser correcto, de lo contrario el método fallará.
- La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. Ejemplo: `2,2;2,2`.

#### c. Salida
- Solución del sistema de ecuaciones.

#### d. Ejemplo
- **Ejemplo de Uso**: eliminacionGaussianaPivoteoParcial("2,1,-1,8; -3,-1,2,-11; -2,1,2,-3", 3)

### 3. Eliminación Gaussiana con Pivoteo Total

#### a. Entradas
- **A**: Matriz Aumentada de una matriz invertible y un vector constante.
- **N**: Número de incógnitas.

#### b. Condiciones
- Debe ser posible solucionarlo con pivoteo total.
- El número de incógnitas debe ser correcto, de lo contrario el método fallará.
- La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. Ejemplo: `2,2;2,2`.

#### c. Salida
- Solución del sistema de ecuaciones.

#### d. Ejemplo
- **Ejemplo de Uso**: eliminacionGaussianaPivoteoTotal("2,1,-1,8; -3,-1,2,-11; -2,1,2,-3", 3)

### 4. Factorización LU

#### a. Entradas
- **A**: Matriz invertible.
- **_b**: Vector constante.

#### b. Condiciones
- La matriz debe ser cuadrada. La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. Ejemplo: `2,2;2,2`.
- El vector debe ser escrito de forma traspuesta. Ejemplo: `2,2,2,2`.

#### c. Salida
- Solución del sistema de ecuaciones.

#### d. Ejemplo
- **Ejemplo de Uso**: factorizacionLU("4,3;6,3", "5,9")

### 5. Método de Doolittle

#### a. Entradas
- **A**: Matriz invertible.
- **_b**: Vector constante.
- **_n**: Tamaño de la matriz A.

#### b. Condiciones
- La matriz debe ser cuadrada. La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. Ejemplo: `2,2;2,2`.
- El vector debe ser escrito de forma traspuesta. Ejemplo: `2,2,2,2`.
- _n debe ser el tamaño correcto de la matriz, de lo contrario el método fallará.

#### c. Salida
- Solución del sistema de ecuaciones.

#### d. Ejemplo
- **Ejemplo de Uso**: metodoDoolittle("4,3;6,3", "5,9", 2)

### 6. Método de Crout

#### a. Entradas
- **A**: Matriz invertible.
- **_b**: Vector constante.
- **_n**: Tamaño de la matriz A.

#### b. Condiciones
- La matriz debe ser cuadrada. La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. Ejemplo: `2,2;2,2`.
- El vector debe ser escrito de forma traspuesta. Ejemplo: `2,2,2,2`.
- _n debe ser el tamaño correcto de la matriz, de lo contrario el método fallará.

#### c. Salida
- Solución del sistema de ecuaciones.

#### d. Ejemplo
- **Ejemplo de Uso**: metodoCrout("4,3;6,3", "5,9", 2)

### 7. Método de Cholesky

#### a. Entradas
- **A**: Matriz invertible.
- **_b**: Vector constante.
- **_n**: Tamaño de la matriz A.

#### b. Condiciones
- La matriz debe ser cuadrada. La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. Ejemplo: `2,2;2,2`.
- El vector debe ser escrito de forma traspuesta. Ejemplo: `2,2,2,2`.
- _n debe ser el tamaño correcto de la matriz, de lo contrario el método fallará.

#### c. Salida
- Solución del sistema de ecuaciones.

#### d. Ejemplo
- **Ejemplo de Uso**: metodoCholesky("4,3;6,3", "5,9", 2)

### 8. Método de Jacobi

#### a. Entradas
- **A**: Matriz invertible.
- **_b**: Vector constante.
- **X0**: Vector de la aproximación inicial.
- **Tol**: Tolerancia.
- **Nmax**: Número máximo de iteraciones.

#### b. Condiciones
- La matriz debe ser cuadrada. La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. Ejemplo: `2,2;2,2`.
- El vector “b” y “X0” deben ser escritos de forma traspuesta. Ejemplo: `2,2,2,2`.
- Tol, en caso de no ser entero, debe tener el decimal separado con “.”.
- MaxIteracion solo puede ser un valor entero positivo.

#### c. Salida
- Solución del sistema de forma iterativa.

#### d. Ejemplo
- **Ejemplo de Uso**: metodoJacobi("4,3;6,3", "5,9", "0,0", 0.01, 100)

### 9. Método de Gauss-Seidel

#### a. Entradas
- **A**: Matriz invertible.
- **_b**: Vector constante.
- **X0**: Vector de la aproximación inicial.
- **Tol**: Tolerancia.
- **Nmax**: Número máximo de iteraciones.

#### b. Condiciones
- La matriz debe ser cuadrada. La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. Ejemplo: `2,2;2,2`.
- El vector “b” y “X0” deben ser escritos de forma traspuesta. Ejemplo: `2,2,2,2`.
- Tol, en caso de no ser entero, debe tener el decimal separado con “.”.
- MaxIteracion solo puede ser un valor entero positivo.

#### c. Salida
- Solución del sistema de forma iterativa.

#### d. Ejemplo
- **Ejemplo de Uso**: metodoGaussSeidel("4,3;6,3", "5,9", "0,0", 0.01, 100)
