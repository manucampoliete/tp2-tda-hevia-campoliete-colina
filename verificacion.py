from pd import ATACAR

def verificacion(x_i, f, solucion_obtenida, maximo_obtenido):

    maximo = 0
    j = 1

    for i in range(len(solucion_obtenida)):
        if solucion_obtenida[i] == ATACAR:
            maximo += min(x_i[i+1], f[j])
            j = 0
        j += 1

    return maximo == maximo_obtenido