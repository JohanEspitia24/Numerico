import math

def punto_fijo(g, p0, TOL, N0):
    """
    Método de punto fijo para encontrar una raíz aproximada de la ecuación x = g(x).
    
    Args:
    g (callable): Función transformada g(x).
    p0 (float): Valor inicial para la iteración.
    TOL (float): Tolerancia para el criterio de parada.
    N0 (int): Número máximo de iteraciones.
    
    Returns:
    float: Punto fijo aproximado o informa que no se encontró.
    """
    i = 0
    while i < N0:
        p = g(p0)
        if abs(p - p0) < TOL:
            return p
        p0 = p
        i += 1
    return None  # Retorno None si no se encuentra un punto fijo en N0 iteraciones

def metodo_newton(f, df, p0, TOL, N0):
    """
    Método de Newton para encontrar una raíz de la función f.
    
    Args:
    f (callable): La función para la cual se busca la raíz.
    df (callable): La derivada de la función f.
    p0 (float): Valor inicial.
    TOL (float): Tolerancia.
    N0 (int): Número máximo de iteraciones.
    
    Returns:
    float: La raíz aproximada o None si el método no converge.
    """
    i = 0
    while i < N0:
        p = p0 - f(p0) / df(p0)
        if abs(p - p0) < TOL:
            return p
        p0 = p
        i += 1
    return None  # Si el método falla en converger

def g(x):
    return math.cos(x)

def f(x):
    return math.cos(x) - x

def df(x):
    return -math.sin(x) - 1

# Parámetros iniciales
p0 = 1.0  # Estimación inicial
TOL = 1e-7  # Tolerancia
N0 = 100   # Máximo número de iteraciones

# Llamadas a las funciones
punto_fijo_result = punto_fijo(g, p0, TOL, N0)
newton_result = metodo_newton(f, df, p0, TOL, N0)

print(f"Resultado del método de punto fijo: {punto_fijo_result}")
print(f"Resultado del método de Newton: {newton_result}")
