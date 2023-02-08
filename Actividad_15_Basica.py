import pandas as pd
import numpy as np

dict_1={
    "Nombre":["Ringo","John","Paul","George","Yoko"],
    "Edad":[45,34,42,38,47],
    "Salario":[12000,14000,13000,11000,10000],
    "Genero":["M","M","M","M","F"]
}

data=pd.DataFrame(dict_1)

maxim = data["Salario"].max()
minim = data["Salario"].min()

rango = {"Maximo":maxim,"Minimo":minim}

print(f"El rango salaria es: {rango}")