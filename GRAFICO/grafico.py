import matplotlib.pyplot as plt
import csv
import numpy
from scipy.optimize import curve_fit

def leerMediciones(x,y):
    with open("Mediciones.txt","r") as file:
        lector=csv.reader(file,delimiter=",")
        file.readline()
        for linea in lector:
            x.append(int(linea[0]))
            y.append(float(linea[1]))

def funcionCuadratica(x, a, b, c):
    return (a*x**2) + (b*x) + c

def graficar():

    x=[]
    y=[]

    leerMediciones(x,y)

    res , _ = curve_fit(funcionCuadratica,x,y)
    
    x2 = numpy.linspace(0,5000,500)
    
    _ , ax = plt.subplots()
    ax.plot(x,y,color="blue",label="Pd")
    ax.plot(x2,funcionCuadratica(x2,res[0],res[1],res[2]),color="red",label="Ajuste cuadratico")
    ax.legend(loc='upper left')

    plt.title('Algoritmo de Maximas kills')
    plt.xlabel('Cantidad de elementos en C/arreglo')
    plt.ylabel('Tiempo [ms]')
    plt.grid(True)
    plt.show()

graficar()