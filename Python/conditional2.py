marks1 = int(input("Enter your marks: "))
marks2 = int(input("Enter your marks: "))
marks3 = int(input("Enter your marks: "))
total_percantage = (marks1 + marks2 + marks3) / 3
if total_percantage >= 90:
    print("Your grade is A")
elif total_percantage >= 80:
    print("Your grade is B")
elif total_percantage >= 70:
    print("Your grade is C")  