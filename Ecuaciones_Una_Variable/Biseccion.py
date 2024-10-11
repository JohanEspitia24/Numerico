import numpy as np

# Parámetros dados
M = 3050  # Anomalía media
e = 0.2056  # Excentricidad
tol = 1e-8  # Tolerancia para la convergencia
max_iter = 100  # Número máximo de iteraciones

# Función f(E) = E - e*sin(E) - M
def f(E, M, e):
    return E - e * np.sin(E) - M

# Método de Bisección
def biseccion(f, a, b, M, e, tol, max_iter):
    FA = f(a, M, e)
    
    # Verificar el teorema de Bolzano para asegurar que hay una raíz en el intervalo
    if FA * f(b, M, e) >= 0:
        print("El teorema de Bolzano no se cumple en el intervalo dado.")
        return None
    
    for i in range(max_iter):
        # Calcular el punto medio
        p = a + (b - a) / 2
        FP = f(p, M, e)
        
        # Verificar si hemos encontrado la raíz o alcanzado la tolerancia deseada
        if abs(FP) < tol or (b - a) / 2 < tol:
            print(f"La raíz aproximada es: {p} después de {i+1} iteraciones.")
            return p
        
        # Decidir si continuar en el intervalo [a, p] o [p, b]
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
            
    print(f'El método fracasó después de {max_iter} iteraciones.')
    return None

# Definir el intervalo inicial para E
a = 0
b = 2 * np.pi

# Ejecutar el método de bisección para encontrar E
E_solution = biseccion(f, a, b, M, e, tol, max_iter)
print(E_solution)
