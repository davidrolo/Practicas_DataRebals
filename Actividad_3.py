import numpy as np

l1 = []
i = 3
while i <= 45:
    l1.append(i)
    i += 1

arr1 = np.array(l1)
print(f"El resultado del primer punto es {arr1}")


l2 = []
i = 0
while i <= 4:
    l2.append(i)
    i += 1

l3 = list(l2+l2)
arr2 = np.array(l3)
print(f"Arreglo sin ordenar {arr2}")

print(f"Arreglo ardenado:  {np.sort(arr2)}")

