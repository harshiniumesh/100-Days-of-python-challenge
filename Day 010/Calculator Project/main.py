# def add(n1, n2):
#     return n1 + n2
# my_favourite_calculation = add
# print(my_favourite_calculation(3, 5))
#
# def subtract(n1, n2):
#     return n1 - n2
# my_favourite_calculation = subtract
# print(my_favourite_calculation(3, 5))
#
# def multiply(n1, n2):
#     return n1 * n2
# my_favourite_calculation = multiply
# print(my_favourite_calculation(3, 5))
#
# def divide(n1, n2):
#     return n1 / n2
# my_favourite_calculation =divide
# print(my_favourite_calculation(3, 5))
#
# operations = {
#     "+": add,
#     "-": subtract,
#     "*": multiply,
#     "/": divide,
# }
#
# # print(operations["*"](4,8))
#
# def calculator():
#     should_accumulate = True
#     num1 = float(input("What is the first number?:"))
#
#     while should_accumulate:
#         for symbol in operations:
#             print(symbol)
#         operation_symbol = input("What is the operation?:")
#
#         num2 = float(input("What is the second number?:"))
#         answer = operations[operation_symbol](num1, num2)
#         print(f"{num1} {operation_symbol} {num2} = {answer}")
#
#         choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start again")
#         if choice == "y":
#             num1 = answer
#         else:
#             should_accumulate = False
#             print("\n" * 20)
#             calculator()
#
# calculator()
import art
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        print("Error: Division by zero is not allowed.")
        return None
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

def get_number(prompt):
    while True:
        user_input = input(prompt).strip()
        if user_input == "":
            print("You must enter a number, not just press Enter.")
            continue
        try:
            return float(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = get_number("What is the first number?: ")

    while should_accumulate:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("What is the operation?: ")

        num2 = get_number("What is the second number?: ")
        answer = operations[operation_symbol](num1, num2)

        # Handle division by zero returning None
        if answer is None:
            num1 = get_number("Enter a new number (since division failed): ")
            continue

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, 'n' to start again, or 'q' to quit: ")
        if choice == "y":
            num1 = answer
        elif choice == "n":
            print("\nStarting fresh...\n")
            num1 = get_number("What is the first number?: ")
        elif choice == "q":
            should_accumulate = False
            print("Goodbye!")

calculator()
