# write  a progrsm to create four basic classes having individual methods addition(),substraction(),multiplication(),division(),respectively.Create a derived class for all above (multiple inheritance)having member data:data1,data2.create an object and then performance operations on th data1 and d# Base class 1
class Addition:
    def addition(self, a, b):
        return a + b



class Subtraction:
    def subtraction(self, a, b):
        return a - b



class Multiplication:
    def multiplication(self, a, b):
        return a * b



class Division:
    def division(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Division by zero not possible"


class Calculator(Addition, Subtraction, Multiplication, Division):
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2

    def display(self):
        print("Data1:", self.data1)
        print("Data2:", self.data2)
        print("Addition:", self.addition(self.data1, self.data2))
        print("Subtraction:", self.subtraction(self.data1, self.data2))
        print("Multiplication:", self.multiplication(self.data1, self.data2))
        print("Division:", self.division(self.data1, self.data2))

data1 = float(input("Enter first number: "))
data2 = float(input("Enter second number: "))


obj = Calculator(data1, data2)
obj.display()