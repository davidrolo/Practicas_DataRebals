ltiempo = []
o = 1
total = 0
tiempo = 0

print("Para terminar de capturar tiempos teclear cero (0)")
while o != "0":
    #ncompra = int(input("Teclee el valor de la compra: "))
    ntiempo = input("Teclee el tiempo de permanencia: ")
    if ntiempo != "0" and ntiempo != "":
        ltiempo.append(int(ntiempo))
    elif ntiempo < "0" or ntiempo == "":
        continue
    else:
        o = "0"

#print(f"Los valores de las compras realizadas son: {lcompra}")


for i in ltiempo:
    tiempo = sum(ltiempo)


# En esta parte se está cpnsiderando lo siguiente:
# Se cobra la primer hora a 25
# Se cobran las siguientes horas a 15, siendo no mas de 7 horas a este costo
# Se cobran los 200 extras cuando supera las 8 horas

print("\nPrimer postulado de cobro")
if tiempo <= 60:
    total = 25
elif tiempo > 60 and tiempo <= 480:
    tiempo2 = tiempo - 60
    total += (15 * (tiempo2 // 60)) + 25
elif tiempo > 540:
    tiempo2 = 420
    print(tiempo2 // 60)
    total += (15 * (tiempo2 // 60)) + 25 + 200


print(f"\nEl tiempo qie estuvo en el estacionamiento es de {tiempo // 60} horas")
print(f"Por lo que el costo a pagar es de: ${total}")


# En esta parte se está cpnsiderando lo siguiente:
# Se cobra la primer hora a 25
# Se cobran las siguientes horas a 15 y se agregan los 200 si supera las 8 horas
total = 0

if tiempo <= 60:
    total = 25
elif tiempo > 60 and tiempo <= 540:
    tiempo2 = tiempo - 60
    total += (15 * ((tiempo - 60) // 60)) + 25
elif tiempo > 540:
    tiempo2 = tiempo - 60
    total += (15 * (tiempo2 // 60)) + 25 + 200

print("\nSegundo postulado de cobro")
print(f"\nEl tiempo qie estuvo en el estacionamiento es de {tiempo // 60} horas")
print(f"Por lo que el costo a pagar es de: ${total}")
