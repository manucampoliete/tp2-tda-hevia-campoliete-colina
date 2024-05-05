from pd import *
from lector_archivos import *
from verificacion import *
from sys import argv
from time import time

IDX_ARCHIVO = 1
RED = '\033[91m'
BOLD = '\033[1m'
END = '\033[0m'

def main():
    
    x_i, f = leer_archivo(argv[IDX_ARCHIVO])
    inicio = time()
    maximo, solucion = pd(x_i, f)
    fin = time()

    print(RED + BOLD + "Solución: " + END + f"{solucion}")
    print(RED + BOLD + "Máximo: " + END + f"{maximo}")
    print(RED + BOLD + "Tiempo de ejecución: " + END + f"{(fin-inicio) * 1000} milisegundos")
    
    correcta = verificacion(x_i, f, solucion, maximo)
    print(RED + BOLD + "La reconstrucción de la solución es: " + END + ("correcta :)" if correcta else "incorrecta :("))

main()