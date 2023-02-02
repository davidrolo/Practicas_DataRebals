"""Actividad: Avanzada

Hagamos un programa que le pida al usuario que ingrese dos nombres con su respectivas edades y muestre quién de ellos es mayor. Para dicha actividad, el usuario debe ingresar dos nombres y dos edades distintas, para que después el programa identifique quién de ellos es mayor e imprima el nombre del mayor, su edad y si es mayor o menor de edad."""

dir = {}
i = 1
print("A continuación debe ingresar la información de dos personas, se debe dar el nombre y la edad de cada uno de ellos")

while i <= 2:
    nom = input("Indica el nombre de la persona:")
    edad = int(input("Indica la edad de la persona:"))
    dir[nom] = edad
    i += 1

Edades = list(dir.values())
Nombres = list(dir.keys())


if Edades[0] > Edades[1]:
    print(f"{Nombres[0]} es mayor que {Nombres[1]}")
elif Edades[1] > Edades[0]:
    print(f"{Nombres[1]} es mayor que {Nombres[0]}")
else:
    print(f"Tanto {Nombres[0]} como {Nombres[1]} tienen la misma edad")

