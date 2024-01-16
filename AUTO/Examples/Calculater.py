def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def calculator():
    while True:
        print("Options:")
        print("Enter '1' for addition")
        print("Enter '2' for subtraction")
        print("Enter '3' for multiplication")
        print("Enter '4' for division")
        print("Enter '0' to exit")

        choice = input("Enter your choice: ")

        if choice == '0':
            print("Calculator closed.")
            break
        elif choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                result = add(num1, num2)
            elif choice == '2':
                result = subtract(num1, num2)
            elif choice == '3':
                result = multiply(num1, num2)
            elif choice == '4':
                result = divide(num1, num2)
            print("Result: ", result)
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    calculator()