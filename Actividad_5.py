# Parte 1 del ejercicio

print("Parte 1 del ejercicio")
otraesdad = 24
miedad = otraesdad / 2
if miedad.is_integer():
    miedad = int(miedad)

print(f"Yo tengo {miedad} años. \n Esto considerando la premisa que doblada da {otraesdad} años\n\n")


#Parte 2 del ejercicio
"""Lógica considerando la explicación de Federico en el chat del grupo del curso
6 = (X / 3) - 15
6 - 15 = X/3
(6 + 15) * 3 = X

X = (6 + 15) * 3"""

print("Parte 2 del ejercicio")
miedad2 = 6
hermana = (miedad2 + 15) * 3
print(f"Mi hermana tiene {hermana} años de edad\n\n")


#Parte 3 del ejercicio

print("Parte 3 del ejercicio")
x = miedad
y = hermana

print(f"La primer persona tiene {x} años de edad\n\n")
print(f"La primer persona tiene {y} años de edad\n\n")
print(f"por lo que se detemina que: \n")

if x>y:
    print(f"La persona mayor es la que tiene {x} años\n\n")
elif y>x:
    print(f"La persona mayor es la que tiene {y} años")
else:
    print(f"Ambas perosonas tienen la misma edad ya que tienen {x} años")
