class Calculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        if self.num2 != 0:
            return self.num1 / self.num2
        else:
            return "Error: Division by zero"
    def square(self):
        return self.num1 ** 2, self.num2 ** 2
a = Calculator(10, 5)
print("Addition:", a.add())
print("Subtraction:", a.subtract())
print("Multiplication:", a.multiply())
print("Squares:", a.square())