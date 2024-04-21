def leer_archivo(nombre_archivo):
    archivo = open(nombre_archivo)

    archivo.readline()
    
    n = int(archivo.readline().strip())

    x_i = [0]
    f = [0]

    for i in range(n):
        x_i.append(int(archivo.readline().strip()))

    for i in range(n):
        f.append(int(archivo.readline().strip()))

    archivo.close()

    return x_i, f