import math

def punto_fijo(g, p0, TOL, N0):
    """
    Método de punto fijo para encontrar una solución aproximada de p = g(p).

    Parámetros:
    g (callable): La función g(p) que define la iteración.
    p0 (float): Valor inicial para empezar las iteraciones.
    TOL (float): Tolerancia que determina la precisión deseada.
    N0 (int): Número máximo de iteraciones permitidas.

    Retorna:
    float o None: Retorna el punto fijo aproximado o None si el método falla.
    """
    i = 1  # Inicializa el contador de iteraciones
    while i <= N0:  # Bucle que permite un máximo de N0 iteraciones
        p = g(p0)  # Calcula el nuevo valor de p usando g
        if abs(p - p0) < TOL:  # Comprueba si la diferencia es menor que la tolerancia
            return p  # Retorna el valor de p si se cumple la condición de parada
        p0 = p  # Actualiza p0 para la siguiente iteración
        i += 1  # Incrementa el contador de iteraciones
    return None  # Retorna None si no se encontró un punto fijo después de N0 iteraciones

def g(x):
    """
    Función g derivada de la ecuación original x^3 + 4x^2 - 10 = 0.
    Se ha manipulado algebraicamente para aislar x en un lado.
    """
    try:
        return math.sqrt((10 - x**3) / 4)
    except ValueError:
        return None  # Retorna None si la raíz cuadrada es negativa

# Parámetros iniciales
p0 = 1.5  # Valor inicial
TOL = 0.0001  # Tolerancia
N0 = 20  # Máximo número de iteraciones

# Ejecución del método
resultado = punto_fijo(g, p0, TOL, N0)
if resultado is not None:
    print(f"El punto fijo encontrado es: {resultado}")
else:
    print("El método de punto fijo no convergió o g(x) produjo un valor inválido")
