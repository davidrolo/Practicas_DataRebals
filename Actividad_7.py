"""# Actividad: Básica
#
# Hagamos un programa que determine si eres mayor de edad o no utilizando las funciones if y else. Para esto, se debe crear una variable donde el usuario pueda ingresar su edad (utiliza un input para este paso) y el programa despliegue un mensaje que muestre si es mayor de edad (>= 18 años) o menor de edad."""


edad = int(input("Ingresa tu edad: "))

if edad >= 18:
    print("Eres mayor de edad")
else:
    print(f"Ere menor de edad, te faltan {18-edad} años para ser mayor de edad")