# Implement a python code for arithmetic calculator for operation *, / , + , -

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = input("Enter choice(+,-,*,/):")
if choice == '+':
	print(num1 + num2);
elif choice == '-':
	print(num1 - num2);
elif choice == '*':
	print(num1 * num2);
elif choice == '/':
	print(num1 / num2);
else:
	print("invalid input")

