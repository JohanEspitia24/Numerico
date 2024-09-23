import math

def metodo_steffensen(g, p0, TOL, N0):
    """
    Método de Steffensen para encontrar una solución aproximada de la ecuación g(p) = p.

    Args:
    g (callable): La función g definida para la iteración de punto fijo.
    p0 (float): Aproximación inicial.
    TOL (float): Tolerancia para determinar la convergencia.
    N0 (int): Número máximo de iteraciones permitidas.

    Returns:
    float: La solución aproximada, p, o None si el método falla.
    """
    i = 1  # Contador de iteraciones inicializado en 1
    while i <= N0:
        p1 = g(p0)  # Calcula g en la aproximación inicial
        p2 = g(p1)  # Calcula g en el resultado anterior
        # Fórmula de Steffensen para acelerar la convergencia
        p = p0 - (p1 - p0)**2 / (p2 - 2*p1 + p0)
        if abs(p - p0) < TOL:  # Chequea si la diferencia es menor que la tolerancia
            return p  # Retorna la solución aproximada
        p0 = p  # Actualiza p0 para la siguiente iteración
        i += 1  # Incrementa el contador de iteraciones
    return None  # Retorna None si no se alcanza convergencia en N0 iteraciones

def g(x):
    """
    Define la función g(x) para el método de Steffensen basado en la ecuación dada.
    """
    try:
        return math.pow(10 - 4*x**2, 1/3)  # Calcula la raíz cúbica
    except ValueError:
        return None  # Retorna None si el argumento de la raíz cúbica es negativo

# Parámetros iniciales
p0 = 1.5  # Aproximación inicial
TOL = 1e-7  # Tolerancia para la convergencia
N0 = 20  # Número máximo de iteraciones

# Ejecución del método de Steffensen
resultado = metodo_steffensen(g, p0, TOL, N0)
if resultado is not None:
    print(f"La solución aproximada encontrada es: {resultado}")
else:
    print("El método de Steffensen no convergió o la función g retornó un valor no válido.")

