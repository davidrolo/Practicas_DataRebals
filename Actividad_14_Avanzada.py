import numpy as np

class calculadora:
    def __init__(self, num1, num2):
        self.num1 = float(num1)
        self.num2 = float(num2)

    def sumar(self):
        suma = self.num1 + self.num2
        print(f"El resultado de la suma de los valores dados es: {suma}")

    def resta(self):
        resta = self.num1 - self.num2
        print(f"El resultado de la resta de los valores dados es: {resta}")

    def multiplica(self):
        producto = self.num1 * self.num2
        print(f"El resultado de multiplicar los datos dados es: {producto}")

    def dividir(self):
        if self.num2 == 0:
            print("Debido a que el divisor tiene valor cero, esta operación no se puede realizar")
        else:
            division = self.num1 / self.num2
            print(f"El resultado de dividir {self.num1} entre {self.num2} es: {division}")

class calculadora_Avanzada(calculadora):
    def __init__(self, num1, num2, pot):
        #calculadora.__init__(self, num1, num2)
        self.num1 = float(num1)
        self.num2 = float(num2)
        self.pot = pot

    def raiz(self):
        rc = np.sqrt(self.num1)
        print(f"La raíz cuadrada de {self.num1} es: {rc}")
        rc2 = np.sqrt(self.num2)
        print(f"La raíz cuadrada de {self.num2} es: {rc2}")

    def potencia(self):
        p1 = self.num1**int(pot)
        print(f"El resultado de elevar {self.num1} a la {pot}a potencia es: {p1}")
        p2 = self.num2**int(pot)
        print(f"El resultado de elevar {self.num2} a la {pot}a potencia es: {p2}")

num1 = input("Ingrese el primer valor para realizar las operaciones: ")
num2 = input("Ingrese el segundo valor para realizar las operaciones: ")

calculadora = calculadora(num1, num2)
calculadora.sumar()
calculadora.resta()
calculadora.multiplica()
calculadora.dividir()
pot = input("A que potencia quieres elevar los valores dados: ")
calculadora_Avanzada = calculadora_Avanzada(num1,num2,pot)
calculadora_Avanzada.raiz()
calculadora_Avanzada.potencia()
