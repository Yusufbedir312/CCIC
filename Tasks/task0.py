num1 = int(input("Enter first integer num : \n"))
num2 = int(input("Enter second integer num : \n"))
Op = input("choose an operation + , - , * , /  \n")

if Op == "+":
    print(num1 + num2)
elif Op == "-":
    print(num1 - num2)
elif Op == "*":
    print(num1 * num2)
elif Op == "/":
    print(num1 / num2)
else:
    print("not a vaild number or operation")
