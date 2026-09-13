# function with arguments

def add(a, b):
    return a + b
result = add(5, 10) 
print(result)

# factorial function
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)
  
n = int(input("Enter a number: "))
result = factorial(n)
print(f"The factorial of {n} is: {result}")  