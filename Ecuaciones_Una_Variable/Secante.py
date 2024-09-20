import math

def metodo_secante(f, p0, p1, TOL, N0):
    """
    Método de la secante para encontrar una raíz de la función f.

    Args:
    f (callable): Función objetivo cuya raíz se busca.
    p0, p1 (float): Valores iniciales para iniciar la secante.
    TOL (float): Tolerancia que determina el criterio de parada.
    N0 (int): Número máximo de iteraciones permitido.

    Returns:
    float: La raíz aproximada encontrada o None si no se logra convergencia.
    """
    q0 = f(p0)
    q1 = f(p1)
    for i in range(2, N0 + 1):
        if q1 == q0:  # Prevenir división por cero
            print("División por cero en la secante.")
            return None
        p = p1 - q1 * (p1 - p0) / (q1 - q0)
        if abs(p - p1) < TOL:
            return p
        p0, p1 = p1, p
        q0, q1 = q1, f(p1)
    return None

def metodo_newton(f, df, p0, TOL, N0):
    """
    Método de Newton para encontrar la raíz de la función f.

    Args:
    f (callable): Función objetivo cuya raíz se busca.
    df (callable): Derivada de la función f.
    p0 (float): Valor inicial para iniciar Newton.
    TOL (float): Tolerancia para el criterio de parada.
    N0 (int): Número máximo de iteraciones permitido.

    Returns:
    float: La raíz aproximada encontrada o None si no se logra convergencia.
    """
    for i in range(1, N0 + 1):
        f_p0 = f(p0)
        df_p0 = df(p0)
        if df_p0 == 0:  # Prevenir división por cero
            print("Derivada cero encontrada.")
            return None
        p = p0 - f_p0 / df_p0
        if abs(p - p0) < TOL:
            return p
        p0 = p
    return None

def f(x):
    return math.cos(x) - x  # La función f(x) = cos(x) - x

def df(x):
    return -math.sin(x) - 1  # Derivada de f, f'(x) = -sin(x) - 1

# Parámetros iniciales
p0 = 0.5  # Estimación inicial para Newton y primer punto para la secante
p1 = 1.0  # Segundo punto inicial para la secante
TOL = 1e-7  # Tolerancia
N0 = 20    # Número máximo de iteraciones

# Llamadas a las funciones
raiz_secante = metodo_secante(f, p0, p1, TOL, N0)
raiz_newton = metodo_newton(f, df, p0, TOL, N0)

print(f"Raíz encontrada por el método de la secante: {raiz_secante}")
print(f"Raíz encontrada por el método de Newton: {raiz_newton}")
