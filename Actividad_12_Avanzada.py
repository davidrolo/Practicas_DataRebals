import pandas as pd
import numpy as np

datos= pd.read_csv("C:\\Users\\david.rodriguez\\Practicas_DataRebels\\athlete_events.csv")


"SOLUCIÓN AL PRIMER PUNTO DE LA ACTIVIDAD"
medallas = ["Gold","Silver","Bronze"]
Nocs = ["MEX","COL","ARG"]
datos1a = datos[datos["Medal"].isin(medallas)]
datos1b = datos1a[datos1a["NOC"].isin(Nocs)]
datos1c = datos1b[datos1b["Age"] == datos1b["Age"].max()]
datos1d = datos1c[["Name","Age","Medal"]]
print(f"Estos son los competidores mas veteranos en conseguir una medalla\n{datos1d}")


"SOLUCIÓN AL SEGUNDO PUNTO DE LA ACTIVIDAD"
medallas = ["Gold"]
Nocs = ["USA","CAN"]
datos1a = datos[datos["Medal"].isin(medallas)]
datos1b = datos1a[datos1a["NOC"].isin(Nocs)]
datos1c = datos1b[datos1b["Age"] == datos1b["Age"].min()]
datos1d = datos1c[["Name","Age","Medal"]]
print(f"\n\n\nEstos son los competidores mas veteranos en conseguir una medalla\n{datos1d}")


"SOLUCIÓN AL TERCER PUNTO DE LA ACTIVIDAD"
medallas = ["Gold","Silver","Bronze"]
Nocs = ["USA","CHN","RUS"]
datos1a = datos[datos["Medal"].isin(medallas)]
datos1b = datos1a[datos1a["NOC"].isin(Nocs)]
dq = datos1b.value_counts("Name")
veces = dq.values
nombres = dq.keys()
di1 = dict(zip(nombres,veces))
for i,j in di1.items():
    if j == dq.values.max():
        salida = datos1b[datos1b["Name"] == i]
        salida.to_csv("C:\\Users\\david.rodriguez\\Practicas_DataRebels\\El_Mas_Ganador2.csv")
        print(f"\n\n\nEl registro que se buscaba ya fue almacenado en el archivo \n'El_Mas_Ganador2.csv' que se encuentra en la siguiente ruta \n'C:\\Users\\david.rodriguez\\Practicas_DataRebels'")
