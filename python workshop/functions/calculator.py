def userInput():
    first_input = int(input("Enter the first number: "))
    second_input = int(input("Enter the second number: "))
    return first_input, second_input

def add(a=0, b=0):
    return a + b

def sub(a=0, b=0):
    return a - b

def mult(a=0, b=0):
    return a * b

print("Welcome to Calculator")

while True:
    print("\nSelect the option:\n 1: Add \n 2: Sub \n 3: Mul \n 4: Stop")
    choose = int(input("Enter choice: "))

    if choose == 1:
        x, y = userInput()
        print(f"Addition of two numbers: {add(x, y)}")

    elif choose == 2:
        x, y = userInput()
        print(f"Subtraction of two numbers: {sub(x, y)}")

    elif choose == 3:
        x, y = userInput()
        print(f"Multiplication of two numbers: {mult(x, y)}")

    elif choose == 4:
        print("Calculator stopped.")
        break

    else:
        print("Invalid option. Please try again.")
