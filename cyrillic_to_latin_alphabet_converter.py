##### Imports
import pandas as pd

##### Creando los diccionarios necesarios para realizar la conversión
df = pd.read_csv("cyrillic2.csv")
df2 = df.set_index("cyrillic1")
dic1 = df2.to_dict()

# dict 1
d1 = dic1["latin"]
# dict 2
# NOTA: Por varios problemas de codificación al cargar el alfabeto cirílico en minúscula,
# varios de estos no eran reconocidos, la forma mas sencilla de solucionar esto es simplemente convirtiendo a minúsculas las keys del d1

def modifyString(s):
    """
    Devuelve string en minúscula.
    """
    return s.lower()

d2 = {}

for key in d1:
    d2[modifyString(key)] = d1[key]  #Añadiendo las keys en minúscula al d2

#### Conversor de alfabeto cirílico a alfabeto latin:

# String en ruso Alfabeto cirílico:
# s = "системой письменности"
s = input("Введите текст - Ingrese Texto: ")

def find_replace(string, d1, d2):
    """
    Función que recorre el string en alfabeto cirílico ingresado y devuelve el mismo en alfabeto latin.
    :param string:
    :param d1: Diccionario en cirílico mayúsculas
    :param d2: Diccionario en cirílico minúsculas
    """
    # iterando para cada carácter del string:
    for item in string:
        if item in d1.keys():
            # Chequeando y reemplazando
            string = string.replace(item, d1[item])
        elif item in d2.keys():
            # Chequeando y reemplazando
            string = string.replace(item, d2[item])
    # Devolviendo el string convertido
    return string

# llamando la función

print("кириллица - Original cirílico: " + s)
print("латинский - Convesión latin: " + (find_replace(s,d1,d2)))