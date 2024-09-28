gitprint("Welcome to our calculator app!")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

choice = input("Choose either: add, subtract, multiply, or divide: ")

if choice == "add":
    print(f"{num1} + {num2} = {num1 + num2}")

elif choice == "subtract":
    print(f"{num1} - {num2} = {num1 - num2}")

elif choice == "multiply":
    print(f"{num1} * {num2} = {num1 * num2}")

elif choice == "divide":
    print(f"{num1} / {num2} = {num1 / num2}")

else:
    print("Wrong input")
