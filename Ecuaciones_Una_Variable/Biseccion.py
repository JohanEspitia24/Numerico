def biseccion(f, a, b, TOL, N0):
    i = 1
    FA = f(a)
    if FA * f(b) >= 0:
        print("El teorema de Bolzano no se cumple en el intervalo dado.")
        return None
    while i <= N0:
        p = a + (b - a) / 2
        FP = f(p)
        if FP == 0 or (b - a) / 2 < TOL:
            print(f"La raíz aproximada es: {p} después de {i} iteraciones.")
            return p
        i += 1
        if FA * FP > 0:
            a = p
            FA = FP
        else:
            b = p
    print(f'El método fracasó después de {N0} iteraciones.')
    return None

def funcion(x):
    return x**3 + 4*x**2 - 10

a = 1
b = 2
TOL = 1e-4
N0 = 100

raiz = biseccion(funcion, a, b, TOL, N0)
