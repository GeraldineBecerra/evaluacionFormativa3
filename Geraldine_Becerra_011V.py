import os
import csv
from random import *


def inicio():
    inicio = True
    while inicio:
        menu=("1. Registrar pedido","2. Listar todos los pedidos","3. Imprimir hoja de ruta","4. Salir del programa")
        for i in menu:
            print(i)
        try:
            opcion = int(input("Ingrese una opciòn"))
            if opcion == 1:
                registrar()
            elif opcion == 2:
                listar()
            elif opcion == 3:
                imprimir()
            elif opcion == 4:
                inicio = False
            else:
                print("Debes ingresar un valor entre el 1-4")
        except  ValueError:
            print("Debes ingresar un nùmero valido")


def registrar():
    archivo = "registrar.csv"
    archivoExiste = os.path.isfile(archivo)
    if not archivoExiste:
        with open("registrar.csv", "w", newline="") as registro:
            registros = csv.writer(registro)
            registros.writerow(["Nro.Pedido","Cliente","Direcciòn","Sector","Saco 5kg","Saco 10kg","Saco 20kg"])

    num = randint(1,1000)
    numPedido = num +1
    cliente = input("ingrese su nombre")
    direccion = input("Ingrese direcciòn")
    sector = sectores()
    try:
        saco5kg = int(input("¿Cuantos sacos de 5kg desea?"))
    except ValueError:
            print("Solo se aceptan numeros")
    try:                   
        saco10kg = int(input("¿Cuantos sacos de 10kg desea?"))
    except ValueError:
        print("Solo se aceptan numeros")
    try:
        saco20kg = int(input("¿Cuantos sacos de 20kg desea?"))
    except ValueError:
        print("Solo se aceptan numeros")

    with open("registrar.csv", "a",newline="") as registro:
            registros = csv.writer(registro)
            registros.writerow([numPedido,cliente,direccion,sector,saco5kg,saco10kg,saco20kg])
            print("Cliente agreado con exito")

def listar():
    with open("registrar.csv", "r",newline="") as registro:
        registros = csv.reader(registro)
        for  registro in registros:
            print(registro)

def imprimir():
    with open("registrar.csv","r",newline="") as registro:
        registros = csv.DictReader(registro)
        sector = sectores()
        for i in registros:
            if  i["Sector"] == sector:
                print(i)
      
def sectores():
    print("1. San Bernardo")
    print("2. Calera de Tango")
    print("3. Buin")
    try:
        sectores = int(input("ingrese el sector"))
        if  sectores  == 1:
            sectores = "San Bernardo"
        elif  sectores == 2:
            sectores = "Calera de Tango"
        elif sectores ==3:
            sectores = "Buin"
        elif sectores > 3:
            print("Debes ingresar un numero entre el 1-3")
    except ValueError:
        print("Solo se aceptan nùmeros")
    return sectores
inicio()
