import pandas as pd
import numpy as np

datos= pd.read_csv("C:\\Users\\david.rodriguez\\Practicas_DataRebels\\athlete_events.csv")

"SOLUCIÓN AL PRIMER PUNTO DE LA ACTIVIDAD"
medallas = ["Gold","Silver","Bronze"]
datos1a = datos[datos["Medal"].isin(medallas)]
datos1b = datos1a[datos1a["Age"] == datos1a["Age"].max()]
datos1c = datos1b[["Name","Age","Medal"]]
print(f"Estos son los competidores mas veteranos en conseguir una medalla\n{datos1c}")


"SOLUCIÓN AL SEGUNDO PUNTO DE LA ACTIVIDAD"
medallas = ["Gold"]
datos1a = datos[datos["Medal"].isin(medallas)]
datos1b = datos1a[datos1a["Age"] == datos1a["Age"].min()]
datos1c = datos1b[["Name","Age","Medal"]].sort_values(by=["Name"])
print(f"\n\n\nEstos son los competidores mas veteranos en conseguir una medalla\n{datos1c}")

#datos2=datos2["Age"].max()
#datos2=datos[datos["Sport"]=="Football"]


"SOLUCIÓN AL TERCER PUNTO DE LA ACTIVIDAD"
d1 = datos[datos["Medal"].notna()]
dq = datos.value_counts("Name")
veces = dq.values
nombres = dq.keys()
di1 = dict(zip(nombres,veces))
for i,j in di1.items():
    if j == dq.values.max():
        salida = d1[d1["Name"] == i]
        salida.to_csv("C:\\Users\\david.rodriguez\\Practicas_DataRebels\\El_Mas_Ganador.csv")
        print(f"\n\n\nEl registro que se buscaba ya fue almacenado en el archivo \n'El_Mas_Ganador.csv' que se encuentra en la siguiente ruta \n'C:\\Users\\david.rodriguez\\Practicas_DataRebels'")
