def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero is not allowed."
    return x / y

def get_operation():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    return input("Enter choice(1/2/3/4/5): ")

def main():
    while True:
        choice = get_operation()
        
        if choice == '5':
            print("Exiting the calculator. Goodbye!")
            break
        
        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                continue
            
            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            elif choice == '4':
                result = divide(num1, num2)
                if isinstance(result, str):  # Check if the result is an error message
                    print(result)
                else:
                    print(f"{num1} / {num2} = {result}")
        else:
            print("Invalid choice. Please select a valid operation.")

if __name__ == "__main__":
    main()