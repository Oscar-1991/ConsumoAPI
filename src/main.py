'''
Created on 5 jul. 2022

@author: oscar.vidal
'''
# import requests
# print("SOLICITANDO")
# url = 'http://localhost:8080/employees'
# data = requests.get(url)
# data = data.json()
# for d in data:
#     id = d['id']
#     surname = d['surname']
#     print(str(id) +  str(surname))
from re import match
from Procesos import lecturaTxt, separarDatos

menu = [
    ['MENU'],
    ['[1].-Dar de alta Employees desde el archivo "Clientes.txt".'],
    ['[0].-Salir.']
]
salir = False
while(salir !=True):
    for i in range(len(menu)):
        print(menu[i][0])
    try:
        opc = int(input("Seleccione una opción válida del 0 al 1:\n"))
    except ValueError:
        print("Solo se acepta numeros para realizar una accion.") 
    else:
        match opc:
            case 1:
                contenido = lecturaTxt()
                separarDatos(contenido)
            case 0:
                salir = True
                print("Hasta luego...")
            case _:
                print("Favor de agregar una opcion valida.")        