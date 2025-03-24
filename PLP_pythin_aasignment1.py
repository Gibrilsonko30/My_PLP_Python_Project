def main():
    try:
        # Get input from the user
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Enter the operation (+, -, *, /): ")

        # Perform calculation based on the operator
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            print("Invalid operator. Please use one of +, -, *, or /.")
            return

        # Display the result
        print(f"{num1} {operator} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values for numbers.")

if __name__ == "__main__":
    main()
