def get_number(prompt):
    """Ask for a valid number"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")
def calculate(num1, num2, operation):
    """Perform the selected arithmetic operation"""
    if operation == '1':
        return num1 + num2
    elif operation == '2':
        return num1 - num2
    elif operation == '3':
        return num1 * num2
    elif operation == '4':
        if num2 == 0:
            return None
        return num1 / num2
def main():
    """Run the Simple Calculator."""
    while True:
        print("\n ======= SIMPLE CALCULATOR =======")
        print("1. Addition\n2. Subtraction\n3. Multiplicationn\n4. Division\n5. Exit")
        choice = input("Choose an operation (1-5): ")
        if choice == '5':
            print("Calculator closed. Goodbye!")
            break
        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice! Choose an option from 1 to 5.")
            continue
        num1 = get_number("Enter the first number: ")
        num2 = get_number("Enter the second number: ")
        if choice == '4' and num2 == 0:
            print("Error: Division by zero is not allowed.")
            continue
        result = calculate(num1, num2, choice)
        if result is not None:
            print(f"Result: {result}")
if __name__ == "__main__":
    main()