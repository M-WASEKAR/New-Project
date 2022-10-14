class calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def addition(self):
        return self.num1 + self.num2

    def substraction(self):
        return self.num1 - self.num2

    def multiplication(self):
        return self.num1 * self.num2

    def division(self):
        return self.num1 / self.num2


num1 = int(input("Enter the first number"))
num2 = int(input("Enter the last number"))
casio = calculator(num1, num2)

print("the additin of ", casio.addition())
print("the substraction is :", casio.substraction())
print("the multification is :", casio.multiplication())
print("the  devision is :", casio.division())
