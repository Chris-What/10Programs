#Program 1

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print(f"The bigger number is {num1}.")
elif num1 < num2:
    print(f"The bigger number is {num2}.")
else:
    print("There is no bigger number, both numbers are equal.")