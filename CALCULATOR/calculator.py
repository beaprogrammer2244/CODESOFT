def add(a, b):
    return a + b

def subtract(a, b):
    return a - b, b - a

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    result1 = a / b
    result2 = b / a if a != 0 else "Cannot divide by zero"
    return result1, result2

def calculator():
    print("\n\tWelcome here")

    while True:
        try:
            a = float(input("\nEnter your 1st number = "))
            b = float(input("\nEnter your 2nd number = "))
        except ValueError:
            print("\tERROR :- Invalid input. Please enter valid numbers.")
            continue

        print("\nPress :-\n",
              "\t1 -> for Addition\n",
              "\t2 -> for Subtraction\n",
              "\t3 -> for Multiplication\n",
              "\t4 -> for Division")

        choice = input("Enter your choice = ")

        if choice.isdigit():
            choice = int(choice)

            if choice == 1:
                result = add(a, b)
                print(f"\tResult for ({a} + {b}) = {result}\n")
            elif choice == 2:
                result1, result2 = subtract(a, b)
                print(f"\tResult for ({a} - {b}) = {result1}")
                print(f"\tResult for ({b} - {a}) = {result2}\n")
            elif choice == 3:
                result = multiply(a, b)
                print(f"\tResult for ({a} x {b}) = {result}\n")
            elif choice == 4:
                result1, result2 = divide(a, b)
                print(f"\tResult for ({a} / {b}) = {result1}")
                print(f"\tResult for ({b} / {a}) = {result2}\n")
            else:
                print("\tERROR :- No such operation code found. Try Again\n")
                continue
        else:
            print("\tERROR :- Invalid input. Please enter a valid operation code.\n")
            continue

        quit_choice = input("Want to continue? (Y/n) = ")
        if quit_choice.lower() != 'y':
            break

if __name__ == "__main__":
    calculator()
