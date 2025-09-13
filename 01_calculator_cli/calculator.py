import math
import os

history_file = "history.txt"

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x / y

def power(x, y):
    return x ** y

def sqrt(x):
    if x < 0:
        return "Error: Negative number cannot have square root!"
    return math.sqrt(x)

def modulus(x, y):
    return x % y

def floor_divide(x, y):
    if y == 0:
        return "Error: Division by zero!"
    return x // y

def save_history(entry):
    with open(history_file, "a") as f:
        f.write(entry + "\n")

def show_history():
    if os.path.exists(history_file):
        print("\n=== Calculation History ===")
        with open(history_file, "r") as f:
            print(f.read())
    else:
        print("\nNo history available.")

def calculator():
    print("=== Advanced Calculator CLI ===")
    print("Operations: +, -, *, /, %, //, **, sqrt")
    print("Type 'history' to see past calculations, 'clear' to clear history, 'exit' to quit.\n")

    while True:
        expr = input("Enter calculation: ").strip()

        if expr.lower() == "exit":
            print("Exiting calculator. Goodbye!")
            break
        elif expr.lower() == "history":
            show_history()
            continue
        elif expr.lower() == "clear":
            open(history_file, "w").close()
            print("History cleared.")
            continue

        try:
            # Special handling for sqrt
            if expr.startswith("sqrt"):
                num = float(expr[4:].strip())
                result = sqrt(num)
            else:
                # Evaluate the expression safely
                allowed_names = {"__builtins__": None, "math": math}
                result = eval(expr, allowed_names)
        except Exception as e:
            print(f"Invalid input: {e}")
            continue

        print(f"Result: {result}")
        save_history(f"{expr} = {result}")

if __name__ == "__main__":
    calculator()
