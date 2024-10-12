import cmath  # Para manejo de números complejos si es necesario
from data import cuerpos  # Importamos los datos de cuerpos desde data.py

# Función f(E) = E - e*sin(E) - M
def f(E, M, e):
    return E - e * cmath.sin(E) - M

# Método de Muller
def muller(M, e, p0, p1, p2, tol, max_iter):
    i = 3  # Comienza en la tercera iteración según el pseudocódigo

    while i <= max_iter:
        h1 = p1 - p0
        h2 = p2 - p1
        δ1 = (f(p1, M, e) - f(p0, M, e)) / h1
        δ2 = (f(p2, M, e) - f(p1, M, e)) / h2
        d = (δ2 - δ1) / (h2 + h1)

        b = δ2 + h2 * d
        D = cmath.sqrt(b**2 - 4 * f(p2, M, e) * d)  # Puede requerir aritmética compleja

        # Determinar E
        if abs(b - D) < abs(b + D):
            E = b + D
        else:
            E = b - D

        h = -2 * f(p2, M, e) / E
        p = p2 + h

        # Verificar criterio de parada
        if abs(h) < tol:
            return p.real, i, abs(h)  # Retornamos la solución, número de iteraciones y la tolerancia
        
        # Preparar la siguiente iteración
        p0 = p1
        p1 = p2
        p2 = p
        i += 1

    return None, max_iter, None  # Si el método no converge después de las iteraciones permitidas

def main():

    tol = 1e-8  # Tolerancia para la convergencia
    max_iter = 100  # Número máximo de iteraciones
    p0, p1, p2 = 0.0, 1.0, 2.0  # Valores iniciales del método de Muller
    tols = 0  # Acumulador de tolerancias
    iteraciones_total = 0  # Acumulador de iteraciones
    cuerpos_convergidos = 0  # Contador de cuerpos que han convergido

    for cuerpo, valores in cuerpos.items():
        M = valores["M"]
        e = valores["e"]
        
        # Ejecutar el método de Muller
        E_solution, it, given_tol = muller(M, e, p0, p1, p2, tol, max_iter)

        # Si el método ha convergido, sumamos la tolerancia y el número de iteraciones
        if given_tol is not None:
            tols += given_tol
            iteraciones_total += it
            cuerpos_convergidos += 1

    # Calcular la tolerancia promedio
    if cuerpos_convergidos > 0:
        tolerancia_promedio = tols / cuerpos_convergidos
        iteraciones_promedio = iteraciones_total / cuerpos_convergidos
        print(f"Tolerancia promedio: {tolerancia_promedio:.8e}")  # Notación científica
        print(f"Promedio de iteraciones: {iteraciones_promedio:.2f}")
    else:
        print("No se pudo calcular la tolerancia promedio ni el promedio de iteraciones, ya que no hubo convergencia en ningún cuerpo.")

if __name__ == "__main__":
    main()
