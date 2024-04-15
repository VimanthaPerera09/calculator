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
        return x * y

    def divide(self, x, y):
        return x / y

if __name__ == "__main__":
    calc = Calculator()

    print("Addition:", calc.add(10, 5))         
    print("Subtraction:", calc.subtract(10, 5))  
    print("Multiplication:", calc.multiply(10, 5))  
    print("Division:", calc.divide(10, 5))       
    print("Division:", calc.divide(10, 0))      
