class Calculator:
    def __init__(self):
        pass

    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        #Modifying in branch y for intentinal conflicts
        if y == 0:
            raise ValueError("Cannot Divide by zero")
        else:
            result  = x/y
            return result

if __name__ == "__main__":
    calc = Calculator()

    print("Addition:", calc.add(10, 5))         
    print("Subtraction:", calc.subtract(10, 5))  
    print("Multiplication:", calc.multiply(10, 5))  
    print("Division:", calc.divide(10, 5))       
    print("Division:", calc.divide(10, 0))      
