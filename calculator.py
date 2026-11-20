# Simple Calculator Project
# Developed for CodeOrbit Tech Internship

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
    if num2 == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return num1 / num2

# Main calculator function
def calculator():
    print("=" * 40)
    print("    CodeOrbit Tech - Simple Calculator")
    print("=" * 40)

    # Loop to allow multiple calculations
    while True:
        # Display the menu of operations
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        # Get operation choice from the user
        choice = input("Enter your choice (1-5 or +, -, *, /): ").strip()

        # Check if the user wants to exit
        if choice in ('5', 'exit', 'Exit'):
            print("\nThank you for using the calculator. Goodbye!")
            break

        # Validate that the choice is one of the supported operations
        if choice not in ('1', '2', '3', '4', '+', '-', '*', '/'):
            print("Invalid choice! Please select a valid option from the menu.")
            continue

        # Get two numbers from the user with error handling using try/except
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numeric values.")
            continue

        # Perform the calculation based on the user's choice
        if choice in ('1', '+'):
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")

        elif choice in ('2', '-'):
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")

        elif choice in ('3', '*'):
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")

        elif choice in ('4', '/'):
            # Handle division by zero using try/except
            try:
                result = divide(num1, num2)
                print(f"Result: {num1} / {num2} = {result}")
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")

        # Ask the user if they want to perform another calculation
        repeat = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if repeat not in ('yes', 'y'):
            print("\nThank you for using the calculator. Goodbye!")
            break

# Entry point of the program
if __name__ == "__main__":
    calculator()
