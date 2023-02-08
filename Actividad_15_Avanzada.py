import pandas as pd
import numpy as np

dict_1={
    "Nombre":["Ringo","John","Paul","George","Yoko"],
    "Edad":[45,34,42,38,47],
    "Salario":[12000,14000,13000,11000,10000],
    "Genero":["M","M","M","M","F"]
}

data=pd.DataFrame(dict_1)

print(f"El valor de la media de los Salarios es: {data['Salario'].mean()}")
print(f'El valor de la mediana de los Salarios es: {data["Salario"].median()}')
print(f'El valor de la desviación standard de los Salarios es: {data["Salario"].std()}')
print(f'El valor de la moda de los Salarios es: {data["Salario"].mode()}')
print(f'El valor de la varianza de los Salarios es: {data["Salario"].var()}')
print(f'El valor máximo de los Salarios es: {data["Salario"].max()}')
print(f'El valor mínimo de los Salarios es: {data["Salario"].min()}')
print(f'La suma de los Salarios es: {data["Salario"].sum()}')
print(f'El producto de los Salarios es: {data["Salario"].prod()}')
