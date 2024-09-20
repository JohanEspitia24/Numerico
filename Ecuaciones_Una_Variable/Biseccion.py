# Definimos la función del problema
def funcion(x):
    # Esta es la función f(x) = x^3 + 4x^2 - 10
    # Es continua en el intervalo [1, 2] y es donde buscaremos la raíz
    return x**3 + 4*x**2 - 10

# Implementamos el método de bisección
def biseccion(f, a, b, TOL, N0):
    """
    Método de bisección para encontrar una raíz de la ecuación f(x) = 0
    en el intervalo [a, b] con una tolerancia TOL y un número máximo de iteraciones N0.
    
    Parámetros:
    f   : función continua en [a, b]
    a   : extremo izquierdo del intervalo
    b   : extremo derecho del intervalo
    TOL : tolerancia para el criterio de convergencia
    N0  : número máximo de iteraciones
    
    Retorna:
    p : aproximación de la raíz o None si el método falla
    """
    
    # Paso 1: Inicialización
    i = 1  # Inicializamos el contador de iteraciones
    FA = f(a)  # Calculamos f(a)
    
    # Verificación inicial del Teorema del Valor Intermedio (Teorema de Bolzano)
    # Es necesario para asegurar que hay al menos una raíz en [a, b]
    if FA * f(b) >= 0:
        # Si f(a) * f(b) >= 0, el método no puede garantizar una raíz en el intervalo
        print("El teorema de Bolzano no se cumple en el intervalo dado.")
        return None  # Salimos de la función ya que no podemos aplicar el método

    # Paso 2: Iteración
    while i <= N0:
        # Paso 3: Calcular p = a + (b - a) / 2
        # Este es el punto medio del intervalo actual
        p = a + (b - a) / 2
        FP = f(p)  # Evaluamos la función en el punto medio
        
        # Paso 4: Verificar si hemos encontrado la raíz o si el intervalo es suficientemente pequeño
        if FP == 0 or (b - a) / 2 < TOL:
            # Si f(p) == 0, hemos encontrado la raíz exacta
            # Si el tamaño del intervalo es menor que la tolerancia, aceptamos p como aproximación
            print(f"La raíz aproximada es: {p} después de {i} iteraciones.")
            return p  # Procedimiento completado exitosamente
        
        # Paso 5: Incrementar el contador de iteraciones
        i += 1  # Avanzamos a la siguiente iteración
        
        # Paso 6: Actualizar los extremos del intervalo
        if FA * FP > 0:
            # Si f(a) * f(p) > 0, la raíz está en el subintervalo [p, b]
            a = p     # Actualizamos el extremo izquierdo del intervalo
            FA = FP   # Actualizamos f(a) para el nuevo extremo
        else:
            # Si f(a) * f(p) < 0, la raíz está en el subintervalo [a, p]
            b = p     # Actualizamos el extremo derecho del intervalo
            # FA no cambia ya que el extremo izquierdo permanece igual

        # **Aspecto de implementación en análisis numérico:**
        # En este paso, utilizamos el Teorema del Valor Intermedio repetidamente
        # para reducir el intervalo donde se encuentra la raíz. Este proceso es esencial
        # en métodos numéricos para aproximar soluciones con un margen de error controlado.

    # Paso 7: Si se alcanza el número máximo de iteraciones sin converger
    print(f'El método fracasó después de {N0} iteraciones.')
    return None  # No se encontró una solución dentro del número máximo de iteraciones

# Parámetros del método
a = 1          # Extremo izquierdo del intervalo inicial
b = 2          # Extremo derecho del intervalo inicial
TOL = 1e-4     # Tolerancia de 10^-4 para la precisión deseada
N0 = 100       # Número máximo de iteraciones permitidas

# Llamamos al método de bisección
raiz = biseccion(funcion, a, b, TOL, N0)

# Verificamos si se encontró una raíz y mostramos el resultado
if raiz is not None:
    print(f"Una aproximación de la raíz es: {raiz}")
    # Podemos verificar qué tan cerca está de cero al evaluar la función en la raíz aproximada
    print(f"f({raiz}) = {funcion(raiz)}")
