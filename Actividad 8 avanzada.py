"""Actividad: Avanzada

Asigna un número aleatorio a tu compañero. Los guardarás en un diccionario, junto con el nombre de tu compañero.
Luego imprimirán los valores del diccionario (nombre de la persona y número que dijo) (Usando un bucle for)
 Al final imprimirán dos mensajes, mostrando el número más grande, y el número más pequeño que dijeron, sin el nombre del socio, sólo el número."""

import random

dic = {}
idn = 1

# Paso 1
alum = int(input("Indica por favor cuantos alumnos van a ingresar valores:  "))

while idn <= alum:
    nombre = input("Indica tu nombre:  ")
    numero = random.randint(1,1000000)
    dic[nombre] = numero
    idn += 1

# Paso 2
print("\n\nListado del Diccionario\n")
for i,j in dic.items():
    print(f"{i} dió el numero {j}".format(i,j))

#Paso 3

valores = list(dic.values())

print(f"\n\1El numero mas grande que se dió es {max(valores)}")
print(f"El numero mas chico que se dió es {min(valores)}")

