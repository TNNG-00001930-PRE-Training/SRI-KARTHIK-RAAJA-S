'''The calculator should be a command-line application.
2. It should support basic arithmetic operations: addition, subtraction, multiplication, and division.
3. The user should be able to input two numbers and the desired operation.
4. The program should perform the requested operation on the two numbers and display the result.
5. Proper input validation should be implemented to handle non-numeric inputs or divide-by-zero cases.
6. The program should provide a menu or prompt to allow the user to perform multiple calculations or exit the program.'''


def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def calculator():
    while True:
        print("\nChoose operation:")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")

        choice = input("Enter choice (1/2/3/4/5): ")

        if choice not in ['1', '2', '3', '4', '5']:
            print("Invalid choice. Please enter a valid option.")
            continue

        if choice == '5':
            print("Goodbye!")
            break

        try:
            num1 = float(input("Enter 1st number: "))
            num2 = float(input("Enter 2nd number: "))
        except ValueError:
            print("Invalid input! provide numeric values.")
            continue

        if choice == '1':
            print("Result:", add(num1, num2))
        elif choice == '2':
            print("Result:", subtract(num1, num2))
        elif choice == '3':
            print("Result:", multiply(num1, num2))
        elif choice == '4':
            try:
                print("Result:", divide(num1, num2))
            except ValueError as e:
                print(e)

if __name__ == "__main__":
    calculator()
