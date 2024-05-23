# Manual de Usuario de los Métodos

## Prerrequisitos

## Capítulo 1

### 1. Búsquedas Incrementales

#### a. Entradas
- **FuncionX**: función continua a evaluar
- **Xi**: punto de valor numérico donde inicia la búsqueda
- **DeltaX**: incremento en cada iteración
- **MaxIteracion**: la máxima cantidad de iteraciones que puede realizar

#### b. Condiciones
- La función debe estar escrita en sintaxis de operaciones de Python sin librerías
- Xi debe ser un valor entero
- DeltaX en caso de no ser entero, el decimal debe ser separado con “.”
- MaxIteracion solo puede ser un valor entero positivo

#### c. Salida
- Entrega la raíz o un rango donde está la raíz o un mensaje de que no existe una raíz

### 2. Bisección y Regla Falsa

#### a. Entrada
- **Xi**: el límite inferior del intervalo en el que se busca la raíz
- **Xf**: el límite superior del intervalo en el que se busca la raíz
- **FuncionX**: función a evaluar
- **Tol**: margen de error permitido del valor de la raíz

#### b. Condiciones
- Tanto Xi como Xf deben ser un valor entero
- La función debe estar escrita en sintaxis de operaciones de Python sin librerías
- Tol en caso de no ser entero, el decimal debe ser separado con “.”

#### c. Salida
- El valor de la raíz exacta o el valor de la raíz con un margen de error o un mensaje informando que el intervalo es incorrecto

### 3. Newton

#### a. Entrada
- **FuncionX**: función continua a evaluar
- **DerivadaX**: derivada de la función a evaluar
- **X0**: valor inicial en que se realizará el método
- **Tol**: margen de error permitido del valor de la raíz
- **MaxIter**: la máxima cantidad de iteraciones que puede realizar

#### b. Condiciones
- Tanto funcionX continua como derivadaX deben estar escritas en sintaxis de operaciones de Python sin librerías
- X0 debe ser un valor entero
- Tol en caso de no ser entero, el decimal debe ser separado con “.”
- MaxIteracion solo puede ser un valor entero positivo

#### c. Salida
- Valor de la raíz con un margen de error o un mensaje de que la derivada es cero o debido a que superó la cantidad de iteraciones y el error es menor a la tolerancia entrega mensaje de que no encontró raíz

### 4. Punto Fijo

#### a. Entrada
- **FuncionGX**: función después de despejar X que se usará para evaluar escrita en sintaxis de operaciones de Python sin librerías
- **X0**: valor inicial en que se realizará el método
- **Tol**: margen de error permitido del valor de la raíz
- **MaxIter**: la máxima cantidad de iteraciones que puede realizar

#### b. Condiciones
- funcionGX debe estar escrita en sintaxis de operaciones de Python sin librerías
- X0 debe ser un valor entero
- Tol en caso de no ser entero, el decimal debe ser separado con “.”
- MaxIteracion solo puede ser un valor entero positivo

#### c. Salida
- Valor de la raíz con una tolerancia especificada en las entradas o un mensaje de que no se encuentra una raíz debido a que el error es mayor que la tolerancia

### 5. Secante

#### a. Entrada
- **FuncionX**: función continua a evaluar
- **X0**: valor inicial a evaluar la función
- **X1**: valor siguiente del valor inicial para evaluar la función
- **Tol**: margen de error permitido del valor de la raíz
- **MaxIter**: la máxima cantidad de iteraciones que puede realizar

#### b. Condiciones
- La función debe estar escrita en sintaxis de operaciones de Python sin librerías
- X0 y X1 deben ser un valor entero
- Tol en caso de no ser entero, el decimal debe ser separado con “.”
- MaxIter solo puede ser un valor entero positivo

#### c. Salida
- Valor de la raíz con un margen de error o un mensaje de que no se encontró raíz

### 6. Raíces Múltiples

#### a. Entrada
- **FuncionX**: función continua a evaluar
- **DerivateX**: derivada de la función a evaluar
- **Derivate2X**: segunda derivada de la función a evaluar
- **X0**: valor inicial en que se realizará el método
- **Tol**: margen de error permitido del valor de la raíz
- **MaxIter**: la máxima cantidad de iteraciones que puede realizar

#### b. Condiciones
- Tanto funcionX, derivateX y derivate2X deben estar escritas en sintaxis de operaciones de Python sin librerías
- X0 y X1 deben ser un valor entero
- Tol en caso de no ser entero, el decimal debe ser separado con “.”
- MaxIter solo puede ser un valor entero positivo

#### c. Salida
- Valor de la raíz con un margen de error especificado con en las entradas

## Capítulo 2

### 1. Eliminación Gaussiana Simple

#### a. Entradas
- **A**: Matriz Aumentada de una matriz invertible y un vector constante
- **N**: número de Incógnitas

#### b. Condiciones
- En la diagonal no debe haber algún valor cero
- El número de incógnitas debe ser correcto, de lo contrario el método fallará
- La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. No debe tener espacios ni otros caracteres, de lo contrario el algoritmo no podrá leer la matriz. Un ejemplo puede ser: `2,2;2,2`

#### c. Salida
- Solución del sistema de ecuaciones

### 2. Eliminación Gaussiana con Pivoteo Parcial

#### a. Entradas
- **A**: Matriz Aumentada de una matriz invertible y un vector constante
- **N**: número de Incógnitas

#### b. Condiciones
- En cada columna debajo del pivote debe haber al menos un elemento diferente de cero, incluyendo al pivote
- El número de incógnitas debe ser correcto, de lo contrario el método fallará
- La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. No debe tener espacios ni otros caracteres, de lo contrario el algoritmo no podrá leer la matriz. Un ejemplo puede ser: `2,2;2,2`

#### c. Salida
- Solución del sistema de ecuaciones

### 3. Eliminación Gaussiana con Pivoteo Total

#### a. Entradas
- **A**: Matriz Aumentada de una matriz invertible y un vector constante
- **N**: número de Incógnitas

#### b. Condiciones
- Debe ser posible solucionarlo con pivoteo Total
- El número de incógnitas debe ser correcto, de lo contrario el método fallará
- La notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. No debe tener espacios ni otros caracteres, de lo contrario el algoritmo no podrá leer la matriz. Un ejemplo puede ser: `2,2;2,2`

#### c. Salida
- Solución del sistema de ecuaciones

### 4. Factorización LU

#### a. Entradas
- **A**: Matriz Invertible
- **_b**: Vector constante

#### b. Condiciones
- La matriz debe ser cuadrada, la notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. No debe tener espacios ni otros caracteres, de lo contrario el algoritmo no podrá leer la matriz. Un ejemplo puede ser: `2,2;2,2`
- El vector debe ser escrito de forma traspuesta, por ejemplo: en vez de `2;2;2;2` se debe escribir `2,2,2,2`. De lo contrario, puede que falle el método

#### c. Salida
- Solución del sistema de ecuaciones

### 5. Factorización LU con Pivoteo Parcial

#### a. Entradas
- **A**: Matriz Invertible
- **_b**: Vector Constante

#### b. Condiciones
- La matriz debe ser cuadrada, la notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. No debe tener espacios ni otros caracteres, de lo contrario el algoritmo no podrá leer la matriz. Un ejemplo puede ser: `2,2;2,2`
- El vector debe ser escrito de forma traspuesta, por ejemplo: en vez de `2;2;2;2` se debe escribir `2,2,2,2`. De lo contrario, puede que falle el método

#### c. Salida
- Solución del sistema de ecuaciones

### 6. Método de Doolittle

#### a. Entradas
- **A**: Matriz Invertible
- **_b**: Vector constante
- **_n**: Tamaño de la Matriz A

#### b. Condiciones
- La matriz debe ser cuadrada, la notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. No debe tener espacios ni otros caracteres, de lo contrario el algoritmo no podrá leer la matriz. Un ejemplo puede ser: `2,2;2,2`
- El vector debe ser escrito de forma traspuesta, por ejemplo: en vez de `2;2;2;2` se debe escribir `2,2,2,2`. De lo contrario, puede que falle el método
- _n debe ser el tamaño correcto de la matriz, de lo contrario, el método fallará y generará error

#### c. Salida
- Solución al sistema de ecuaciones

### 7. Método de Crout

#### a. Entradas
- **A**: Matriz Invertible
- **_b**: Vector constante
- **_n**: Tamaño de la Matriz A

#### b. Condiciones
- La matriz debe ser cuadrada, la notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. No debe tener espacios ni otros caracteres, de lo contrario el algoritmo no podrá leer la matriz. Un ejemplo puede ser: `2,2;2,2`
- El vector debe ser escrito de forma traspuesta, por ejemplo: en vez de `2;2;2;2` se debe escribir `2,2,2,2`. De lo contrario, puede que falle el método
- _n debe ser el tamaño correcto de la matriz, de lo contrario, el método fallará y generará error

#### c. Salida
- Solución al sistema de ecuaciones

### 8. Método de Cholesky

#### a. Entradas
- **A**: Matriz Invertible
- **_b**: Vector constante
- **_n**: Tamaño de la Matriz A

#### b. Condiciones
- La matriz debe ser cuadrada, la notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. No debe tener espacios ni otros caracteres, de lo contrario el algoritmo no podrá leer la matriz. Un ejemplo puede ser: `2,2;2,2`
- El vector debe ser escrito de forma traspuesta, por ejemplo: en vez de `2;2;2;2` se debe escribir `2,2,2,2`. De lo contrario, puede que falle el método
- _n debe ser el tamaño correcto de la matriz, de lo contrario, el método fallará y generará error

#### c. Salida
- Solución al sistema de ecuaciones

### 9. Método de Jacobi

#### a. Entradas
- **A**: Matriz Invertible
- **_b**: Vector Constante
- **X0**: Vector de la aproximación inicial
- **Tol**: Tolerancia
- **Nmax**: número máximo de iteraciones

#### b. Condiciones
- La matriz debe ser cuadrada, la notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. No debe tener espacios ni otros caracteres, de lo contrario el algoritmo no podrá leer la matriz. Un ejemplo puede ser: `2,2;2,2`
- El vector “b” y “x0” deben ser escritos de forma traspuesta, por ejemplo: en vez de `2;2;2;2` se debe escribir `2,2,2,2`. De lo contrario, puede que falle el método
- Tol en caso de no ser entero, el decimal debe ser separado con “.”
- MaxIteracion solo puede ser un valor entero positivo

#### c. Salida
- Solución al sistema de forma iterativa

### 10. Método de Gauss-Seidel

#### a. Entradas
- **A**: Matriz Invertible
- **_b**: Vector Constante
- **X0**: Vector de la aproximación inicial
- **Tol**: Tolerancia
- **Nmax**: número máximo de iteraciones

#### b. Condiciones
- La matriz debe ser cuadrada, la notación de la matriz debe ser escrita diferenciando las filas con “;” y las columnas con “,”. No debe tener espacios ni otros caracteres, de lo contrario el algoritmo no podrá leer la matriz. Un ejemplo puede ser: `2,2;2,2`
- El vector “b” y “x0” deben ser escritos de forma traspuesta, por ejemplo: en vez de `2;2;2;2` se debe escribir `2,2,2,2`. De lo contrario, puede que falle el método
- Tol en caso de no ser entero, el decimal debe ser separado con “.”
- MaxIteracion solo puede ser un valor entero positivo

#### c. Salida
- Solución al sistema de forma iterativa

## Capítulo 3

### 1. Vandermonde

#### a. Entrada
- **X**: Vector constante con los puntos x
- **Y**: Vector constante con los puntos y

#### b. Condiciones
- El vector “x” y “y” deben ser escritos de forma traspuesta, por ejemplo: en vez de `2;2;2;2` se debe escribir `2,2,2,2`. De lo contrario, puede que falle el método

#### c. Salida
- Solución del método con un pequeño margen de error
