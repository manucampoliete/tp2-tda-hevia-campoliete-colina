from random import randint

MIN_X_I = 10
MAX_X_I = 2000

MIN_F = 0
MAX_F = 10000

def generador(n):
    nombre_archivo = str(n) + ".txt"
    archivo = open(nombre_archivo, "w")

    archivo.write("# La primera línea indica la cantidad de minutos a considerar (n). Luego vienen n líneas que corresponden a los x_i, y luego los n valores que corresponden a la función f(.):\n")
    
    archivo.write(str(n) + "\n")

    for _ in range(n):
        archivo.write(str(randint(MIN_X_I, MAX_X_I)) + "\n")

    margen_de_aumento = MAX_F // n
    ultimo = MIN_F
    for _ in range(n):
        f = ultimo + randint(0, margen_de_aumento)
        archivo.write(str(f) + "\n")
        ultimo = f + 1

    archivo.close()

def generar_archivos():
    for i in range(100,5001,50):
        generador(i)

generar_archivos()
    