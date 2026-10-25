import art

def add(n1, n2):
    return n1 + n2  # multiply 2 numbers

def subtract(n1, n2):
    return n1 - n2  # subtract 2 numbers

def multiply(n1, n2):
    return n1 * n2  # multiply 2 numbers

def divide(n1, n2):
    return n1 / n2  # divide 2 numbers

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    """
    Run the calculator and print the result.

    Returns:
        None
    """
    print(art.logo)
    game_over = False
    num1 = float(input("What's the first number?: "))

    while not game_over:
        for operation in operations:
            print(operation)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        total = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {total}")

        choice = input(f"Type 'y' to continue calculating with {num1}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = total  # num1 becomes the total of the previous calculation
        else:
            print("\n" * 20)
            calculator()
            game_over = True

calculator()


