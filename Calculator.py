def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

def subtract(a, b):
    return a - b

def division(a, b):
    return a / b

print("Select Option")
print("1. Addition")
print ("2. Subtraction")
print ("3. Multiplication")
print ("4. Division")

choice = int(input("Enter Your choice 1/2/3/4"))

num1 = float(input("Enter first number:"))
num2 = float(input("Enter second number:"))
if choice == 1:
    print("The answer is {2}".format(num1, num2, add(num1, num2)))
elif choice == 2:
    print("The answer is {2}".format(num1, num2, subtract(num1, num2)))
elif choice == 3:
    print("The answer is {2}:".format(num1, num2, multiply(num1, num2)))
elif choice == 4:
    print("The answer is {2}".format(num1, num2, division(num1, num2)))
else:
    print("Invalid Choice")