"""Actividad: Básica

Crear un programa que permita al usuario ingresar los montos de las compras de un cliente (se desconoce la cantidad de datos que se cargarán, que pueden cambiar en cada ejecución), cortando el ingreso de datos cuando el usuario ingresa el monto 0.
Si ingresa una cantidad negativa, no debe procesarse y se le debe solicitar que ingrese una nueva cantidad. Al finalizar, informar el total a pagar teniendo en cuenta que, si las ventas superan el total de $1000, se debe aplicar un 10% de descuento."""


lcompra = []
o = 1
total = "0"

print("Para terminar de capturar cantidades teclear cero (0)")
while o != "0":
    #ncompra = int(input("Teclee el valor de la compra: "))
    ncompra = input("Teclee el valor de la compra: ")
    if ncompra != "0" and ncompra != "":
        lcompra.append(int(ncompra))
    elif ncompra < "0" or ncompra == "":
        continue
    else:
        o = "0"

#print(f"Los valores de las compras realizadas son: {lcompra}")


for i in lcompra:
    total = sum(lcompra)

if total > 1000:
    print(f"\nSubtotal:  {total}\nTotal a pagar: {total * 0.9}")
else:
    print(f"\nSubtotal:  {total}\nTotal a pagar: {total}")