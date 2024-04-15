class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        # Inside calculator.py (feature-x branch)
        # Modifying lines to create conflicts
        result = x * y
        return result


    def divide(self, x, y):
        return x / y

if __name__ == "__main__":
    calc = Calculator()

    print("Addition:", calc.add(10, 5))         
    print("Subtraction:", calc.subtract(10, 5))  
    print("Multiplication:", calc.multiply(10, 5))  
    print("Division:", calc.divide(10, 5))       
    print("Division:", calc.divide(10, 0))      
