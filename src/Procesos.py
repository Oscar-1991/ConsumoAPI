'''
Created on 5 jul. 2022

@author: oscar.vidal
'''
import requests
from pip._vendor.urllib3.util import response



def lecturaTxt():
    try:
        archivo = open("Clientes.txt", "r+")
    except:
        print(f"Error al abrir el archivo.")
    else:
        contenido = archivo.readlines()
        newCont = formateo(contenido)  
        return newCont

def formateo(contenido):
    aux = []
    for c in contenido:
        aux.append(c.rstrip("\n"))
    return aux  

def separarDatos(contenido):
    for c in contenido:
        if(c != ''):
            print(str(c))
            

def altaEmployee(surname, firstname, country, language):
    try:
        url = 'http://localhost:8080/apiv1/employees/add'
        requests.post(url)
        data = {"surname": surname, "firstname": firstname, "country": country, "language": language}
        response = requests.post(url, json=data)
        resultado = response.json()        
    except:
        print("Error al guardar.")
    else:
        print(str(resultado))

def altaCountry(code, name, airport):
    try:
        url = 'http://localhost:8080/apiv1/countries/add'
        requests.post(url)
        data = {"code": code, "name": name, "airport": airport}
        response = requests.post(url, json=data)
        resultado = response.json()        
    except:
        print("Error al guardar.")
    else:
        print(str(resultado))
        

def altaLanguage(code, name):
    try:
        url = 'http://localhost:8080/apiv1/languages/add'
        requests.post(url)
        data = {"code": code, "name": name}
        response = requests.post(url, json=data)
        resultado = response.json()        
    except:
        print("Error al guardar.")
    else:
        print(str(resultado))

def altaAirport(name):
    try:
        url = 'http://localhost:8080/apiv1/airports/add'
        requests.post(url)
        data = {"name": name}
        response = requests.post(url, json=data)
        resultado = response.json()        
    except:
        print("Error al guardar.")
    else:
        print(str(resultado))        