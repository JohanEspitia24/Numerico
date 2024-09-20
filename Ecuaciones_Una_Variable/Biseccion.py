def biseccion(f, a, b, TOL, N0):
    """
    Implementa el método de bisección para encontrar una raíz de la función f en el intervalo [a, b].
    
    Parámetros:
    f (callable): Función para la cual queremos encontrar una raíz.
    a (float): Límite inferior del intervalo inicial.
    b (float): Límite superior del intervalo inicial.
    TOL (float): Tolerancia, el criterio de parada que determina la precisión deseada.
    N0 (int): Número máximo de iteraciones permitidas.
    
    Retorna:
    float o None: La raíz aproximada de la función o None si el método fracasa o no se cumple Bolzano.
    """
    
    i = 1
    FA = f(a)
    
    # Verificar el teorema de Bolzano para asegurar que hay una raíz en el intervalo
    if FA * f(b) >= 0:
        print("El teorema de Bolzano no se cumple en el intervalo dado, es decir, f(a) y f(b) no tienen signos opuestos.")
        return None
    
    while i <= N0:
        # Calcular el punto medio del intervalo
        p = a + (b - a) / 2
        FP = f(p)
        
        # Verificar si hemos encontrado la raíz o si hemos alcanzado la tolerancia deseada
        if FP == 0 or (b - a) / 2 < TOL:
            print(f"La raíz aproximada es: {p} después de {i} iteraciones.")
            return p
        
        # Incrementar el contador de iteraciones
        i += 1
        
        # Decidir si continuar la búsqueda en el intervalo [a, p] o [p, b]
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
            
    # Si se alcanza el número máximo de iteraciones sin encontrar una raíz
    print(f'El método fracasó después de {N0} iteraciones.')
    return None

# Función específica para la cual queremos encontrar una raíz
def funcion(x):
    return x**3 + 4*x**2 - 10

# Parámetros iniciales
a = 1
b = 2
TOL = 1e-4
N0 = 100

# Ejecutar el método de bisección
raiz = biseccion(funcion, a, b, TOL, N0)
