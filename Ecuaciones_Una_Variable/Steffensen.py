def metodo_steffensen(g, p0, TOL, N0):
    """
    Método de Steffensen para encontrar una solución aproximada p = g(p).

    Args:
    g (callable): Función g que define la iteración.
    p0 (float): Aproximación inicial.
    TOL (float): Tolerancia para el criterio de parada.
    N0 (int): Número máximo de iteraciones.

    Returns:
    float: La solución aproximada p o None si el método falla.
    """
    i = 1  # Inicia el contador de iteraciones
    while i <= N0:  # Itera hasta un número máximo de iteraciones
        p1 = g(p0)  # Calcula p1 = g(p0)
        p2 = g(p1)  # Calcula p2 = g(p1)
        # Calcula la nueva aproximación usando la fórmula de Steffensen
        p = p0 - (p1 - p0)**2 / (p2 - 2*p1 + p0)
        print(f"Iteración {i}: p = {p}") # Imprime el valor de p en cada iteración
        if abs(p - p0) < TOL:  # Verifica si se ha alcanzado la tolerancia deseada
            
            return p  # Retorna la aproximación si la condición de parada se cumple
        p0 = p  # Actualiza p0 para la próxima iteración
        i += 1  # Incrementa el contador de iteraciones
    
    return None  # Retorna None si el método no logra converger dentro de las iteraciones máximas

# Ejemplo de uso del método de Steffensen
def g(x):
    return x**2 - 2  # Una función g(x) que definimos para encontrar la raíz cuadrada de 2

# Parámetros iniciales
p0 = 1.5  # Aproximación inicial cercana a la raíz cuadrada de 2
TOL = 1e-7  # Tolerancia pequeña para una precisión alta
N0 = 10  # Número máximo de iteraciones

# Llamada al método
resultado = metodo_steffensen(g, p0, TOL, N0)
if resultado is not None:
    print(f"La solución aproximada encontrada es: {resultado}")
else:
    print("El método de Steffensen no convergió.")
