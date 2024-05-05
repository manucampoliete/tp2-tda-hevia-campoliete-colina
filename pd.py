import sys

sys.setrecursionlimit(10000)

CARGAR = 'Cargar'
ATACAR = 'Atacar'

def reconstruir_solucion(n, x_i, f, OPT, solucion):
    if n == 0:
        return solucion

    solucion[n-1] = ATACAR

    maximo = 0
    pos_ultimo_ataque = n-1

    for j in range(1, n + 1):
        if OPT[n-j] + min(x_i[n], f[j]) > maximo:
            maximo = OPT[n-j] + min(x_i[n], f[j])
            pos_ultimo_ataque = n-j

    return reconstruir_solucion(pos_ultimo_ataque, x_i, f, OPT, solucion)

""" 
ECUACIÓN DE RECURRENCIA:

OPT[n] = max( ∀ j∈[1,n] : OPT[n-j] + min(x_n, f(j)) )
"""

def pd(x_i, f):

    n = len(x_i) - 1

    OPT = [0] * (n + 1)
    OPT[1] = min(x_i[1], f[1])

    for i in range(2, n + 1):
        maximo = 0
        for j in range(1, i + 1):
            if OPT[i-j] + min(x_i[i], f[j]) > maximo:
                maximo = OPT[i-j] + min(x_i[i], f[j])
        OPT[i] = maximo

    solucion = [CARGAR] * n
    return OPT[n], reconstruir_solucion(n, x_i, f, OPT, solucion)