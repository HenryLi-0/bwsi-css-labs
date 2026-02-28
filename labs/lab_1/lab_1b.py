"""
lab_1b.py

This is a script that implements a simple calculator. It takes two numbers and an operation,
then performs the operation and returns the result. 

The script asks the user to input the numbers and the operation to be performed,
and prints the result to the terminal window.

"""
class Operation:
    ADD = "add"
    SUBTRACT = "subtract"
    MULTIPLY = "multiply"
    DIVIDE = "divide"

    OPERATIONS = [ADD, SUBTRACT, MULTIPLY, DIVIDE] 
    # because comparing raw strings for this is sketchy

def simple_calculator(operation: Operation, num1: float, num2: float) -> float:
    """
    Function that takes in two numbers and an operation (add, subtract, multiply, divide),
    then performs the operation on the two numbers and returns the result.

    Args:
        operation (str): The operation to perform ("add", "subtract", "multiply", "divide").
        num1 (float): The first number.
        num2 (float): The second number.

    Returns:
        float: The result of the operation.
    """
    
    if operation == Operation.ADD:
        return num1 + num2
    elif operation == Operation.SUBTRACT:
        return num1 - num2
    elif operation == Operation.MULTIPLY:
        return num1 * num2
    elif operation == Operation.DIVIDE:
        if num2 != 0:
            return num1 / num2
        else:
            raise ValueError("Cannot divide by zero.")
    else:
        raise ValueError("Invalid operation. Please choose from 'add', 'subtract', 'multiply', or 'divide'.")

def inputFloat(prompt:str) -> float:
    while True:
        try:
            return float(input(prompt))
        except:
            print("please input a number!")

def inputOperation(prompt:str) -> float:
    while True:
        temp = input(prompt).strip().lower()
        if temp in Operation.OPERATIONS:
            return temp
        else:
            print("please input an operation!")

def main():
    
    print(f"===== Simple Calculator =====")

    # Ask the user for sample input    
    num1 = inputFloat("Enter the first number: ")
    num2 = inputFloat("Enter the second number: ")
    operation = inputOperation("Enter the operation (add, subtract, multiply, divide): ")

    # Perform the calculation and display the result
    result = simple_calculator(operation, num1, num2)
    print(f"The result of {operation if operation!=Operation.DIVIDE else "divid"}ing {num1} and {num2} is: {result}")


if __name__ == "__main__":
    main()
