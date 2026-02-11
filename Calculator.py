# Write a simple calculator program
#when the program runs it prompts the user to enter first number , operator and second number.
#Based on the operator entered, it should provide the correct output
#(+ - * /)

def calculator():
    print("---Simple Python Calculator--")

    try:

        num1 = float(input("Enter first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # Perform calculation based on operator
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                return "Error"
            result = num1 / num2
        else:
            return("Invalid operator! Please use +, -, /, or *.")
        return f"Result: {num1} {operator} {num2} = {result}"

    except ValueError:
        return "Invalid input"

print(calculator())