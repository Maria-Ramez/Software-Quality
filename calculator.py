password = "admin123"

def calculate(a, b, operation):
    result = 0

    if operation == "add":
        result = a + b

    if operation == "subtract":
        result = a - b

    if operation == "multiply":
        result = a * b

    if operation == "divide":
        result = a / b

    return result


def print_result(a, b, operation):
    result = calculate(a, b, operation)
    print("The result is: " + str(result))


def calculate_again(a, b, operation):
    result = 0

    if operation == "add":
        result = a + b

    if operation == "subtract":
        result = a - b

    if operation == "multiply":
        result = a * b

    if operation == "divide":
        result = a / b

    return result