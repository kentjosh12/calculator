
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def get_operation():
    while True:
        operation = input("Enter an operation (+, -, *, /): ").strip()
        if operation in ['+', '-', '*', '/']:
            return operation
        else:
            print("Invalid operation. Please enter one of +, -, *, or /.")

def perform_calculation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."

def main():
    while True:
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        operation = get_operation()

        result = perform_calculation(num1, num2, operation)
        print(f"THE ANSWER OF {num1} {operation} {num2} = {result}")

        again = input("Do you want to perform another calculation? (Y/N): ").strip().lower()
        if again == 'n':
            print("PASI NA PASIPA PAKA?")  # Your custom message when exiting
            break
        elif again != 'y':
            print("Invalid input. Exiting the calculator.")
            break

if __name__ == "__main__":
    main()
