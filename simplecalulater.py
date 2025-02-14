num1 = int(input("Enter value 1: "))
num2 = int(input("Enter value 2: "))
opr = input("Enter operator (+, -, *, /): ")

# Perform operation
if opr == "+":
    print(f"{num1} + {num2} = {num1 + num2}")
elif opr == "-":
    print(f"{num1} - {num2} = {num1 - num2}")
elif opr == "*":
    print(f"{num1} * {num2} = {num1 * num2}")
elif opr == "/":
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error: Division by zero!")
else:
    print("Invalid choice. Please choose a valid operator.")
