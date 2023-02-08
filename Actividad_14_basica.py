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


num1 = input("Ingrese el primer valor para realizar las operaciones: ")
num2 = input("Ingrese el segundo valor para realizar las operaciones: ")

calculadora = calculadora(num1, num2)
calculadora.sumar()
calculadora.resta()
calculadora.multiplica()
calculadora.dividir()


