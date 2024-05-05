import sys
sys.path.append("../")
from lector_archivos import *
from pd import *

def generar_archivo_resultados():
    nombre_archivo_resultados = "Resultados Esperados.txt"
    archivo_resultados = open(nombre_archivo_resultados, 'w')

    for n in range(100, 5001, 50):
        nombre_archivo = str(n) + ".txt"
        archivo_resultados.write(nombre_archivo + "\n")
        x_i, f = leer_archivo(nombre_archivo)
        maximo, solucion = pd(x_i, f)
        archivo_resultados.write("Estrategia: " + ", ".join(solucion) + "\n")
        archivo_resultados.write("Cantidad de tropas eliminadas: " + str(maximo) + "\n\n")

    archivo_resultados.close()

generar_archivo_resultados()