import cmath  # Para manejo de números complejos si es necesario

# Definir la función para la cual queremos encontrar una raíz
def f(x):
    # Aquí puedes definir la función que desees. 
    # Ejemplo: x^3 + 2*x^2 + 10*x - 20
    return x**3 + 2*x**2 + 10*x - 20

# Método de Muller
def muller(p0, p1, p2, tol, max_iter):
    i = 3  # Comienza en la tercera iteración según el pseudocódigo

    while i <= max_iter:
        h1 = p1 - p0
        h2 = p2 - p1
        δ1 = (f(p1) - f(p0)) / h1
        δ2 = (f(p2) - f(p1)) / h2
        d = (δ2 - δ1) / (h2 + h1)

        b = δ2 + h2 * d
        D = cmath.sqrt(b**2 - 4 * f(p2) * d)  # Puede requerir aritmética compleja

        # Determinar E
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D

        h = -2 * f(p2) / E
        p = p2 + h

        # Verificar criterio de parada
        if abs(h) < tol:
            print(f"La solución aproximada es: {p} después de {i} iteraciones.")
            return p
        
        # Preparar la siguiente iteración
        p0 = p1
        p1 = p2
        p2 = p
        i += 1

    # Si el método no converge después de las iteraciones permitidas
    print(f"El método falló después de {max_iter} iteraciones.")
    return None

# Parámetros iniciales
p0 = 0.0  # Punto inicial
p1 = 1.0  # Segundo punto
p2 = 2.0  # Tercer punto
tol = 1e-5  # Tolerancia
max_iter = 100  # Número máximo de iteraciones

# Ejecutar el método de Muller
solucion = muller(p0, p1, p2, tol, max_iter)
print("Raíz aproximada:", solucion)
