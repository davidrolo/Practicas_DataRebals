import math as mt

def cuadratica(a=0, b=0, c=0):
    v1 = b * (-1)
    v2 = b**2 - (4*a*c)
    #v3 = mt.sqrt(v2)
    v4 = 2 * a
    if v2 < 0:
        x1 = "("+str(v1/v4)+"+ bi)"
        x2 = "("+str(v1/v4)+"- bi)"
    else:
        v3 = mt.sqrt(v2)
        v4 = 2 * a
        x1 = (v1 + v3) / v4
        x2 = (v1 - v3) / v4
    return x1,x2

valores = []
args = ("a","b","c")

for i in range(3):
    #valores.append(int(input("Dame el valor de la ecuación cuadratica:  ")))
    itro = input("Dame el valor de la ecuación cuadratica:  ")
    if itro == "":
        valores.append("0")
    else:
        valores.append(itro)

param = dict(zip(args,valores))

x = cuadratica(int(param["a"]),int(param["b"]),int(param["c"]))


print(x)



