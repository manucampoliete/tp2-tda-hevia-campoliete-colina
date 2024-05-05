import sys
sys.path.append("../")
from pd import *
from lector_archivos import leer_archivo
from time import time

def generar_mediciones():
    with open('Mediciones.txt','a') as file:
        file.write("Cantidad_de_elementos,Media_de_tiempo_de_ejecucion\n")
        for i in range(100,5001,50):
            xi,f=leer_archivo("../MAS_TESTS/"+str(i)+".txt")
            suma_de_tiempos=0
            for j in range(5):
                inicio=time()
                _,_ = pd(xi,f)
                fin=time()
                suma_de_tiempos+=(fin-inicio)*1000
            file.write(str(i)+","+str(suma_de_tiempos/5)+"\n")


generar_mediciones()