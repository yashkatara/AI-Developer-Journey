a = int(input("Enter your age: "))
if (a%2 == 0):
    print("Your age is even.")
if a >= 18:
 print("You are eligible to vote.")
elif a<0:
    print("Age cannot be negative.")
else:
    print("You are not eligible to vote.")  
    print("You will be eligible to vote in", 18-a, "years.")
    print("End of the program")
    