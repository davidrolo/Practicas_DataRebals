import numpy as np

# Métodos para obtener el primer paso del ejercicio

m1 = np.array([[0,1,2],[3,4,5],[6, 7,8]])
print(f"Esta matriz se obtuvo creando el array directamento con los datos solicitados, el resulta es :L \n {m1}")

n1 = np.arange(3)
n2 = np.arange(3,6)
n3 = np.arange(6,9)

m2 = np.array([n1,n2,n3])
print(f"""Esta es otra forma de crear la matriz, se realizó la asignación de los valores a 3 variables, 
        a las cuales los valores se crearon con la función de 'arange', 
        posteriormente se creo el arreglo con los valores de estas variables y el resultado es: \n {m2}""")


m3 = np.reshape(np.array(range(9)),(3,3))
print(f"""Esta última se creo una sola sentenciá utilizando el método 'rechape' utilzando el comando 'range' 
        para obtener los valores del arreglo el reaultado es: \n{m3}""")


#Segundo paso del ejercicio

mi1 = np.identity(6)
print(mi1)