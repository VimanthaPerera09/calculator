class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        #modifying for intentional conflicts in branch z
        result = x + y
        return result

    def subtract(self, x, y):
        #Modifying for intentional conflicts in branch z
        result = x - y
        return result

    def multiply(self, x, y):
        # Inside calculator.py (feature-x branch)
        # Modifying lines to create conflicts
        result = x * y
        return result


    def divide(self, x, y):
        #Modifying in branch y for intentinal conflicts
        if y == 0:
            raise ValueError("Cannot Divide by zero")
        else:
            result  = x/y
            return result

def main():
    calc = Calculator()

    while True:
        # Prompt user for operation
        print("\nAvailable operations:")
        print("1. Add (+)")
        print("2. Subtract (-)")
        print("3. Multiply (*)")
        print("4. Divide (/)")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        # Performing chosen operation or exit
        if choice == "5":
            print("Exiting...")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please enter a valid option (1-5).")
            continue

        # Prompt user for numbers
        try:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        # Performing the selected operation
        if choice == "1":
            result = calc.add(num1, num2)
            operation = "Addition"
        elif choice == "2":
            result = calc.subtract(num1, num2)
            operation = "Subtraction"
        elif choice == "3":
            result = calc.multiply(num1, num2)
            operation = "Multiplication"
        elif choice == "4":
            try:
                result = calc.divide(num1, num2)
                operation = "Division"
            except ValueError as e:
                print(f"Error: {e}")
                continue

        # Displaying the result
        print(f"Result of {operation}: {result}")

    print("Goodbye!")

if __name__ == "__main__":
    main()