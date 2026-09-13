# greatest of three numbers
def greatest_of_three():
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    c = int(input("Enter number 3: "))
    
    if a >= b and a >= c:
        print(f"{a} is the greatest number.")
    elif b >= a and b >= c:
        print(f"{b} is the greatest number.")
    else:
        print(f"{c} is the greatest number.")

greatest_of_three()