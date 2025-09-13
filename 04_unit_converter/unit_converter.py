import os
history_file = "history.txt"

def save_history(entry):
    with open(history_file, "a") as f:
        f.write(entry + "\n")

def show_history():
    if os.path.exists(history_file):
        print("\n=== Conversion History ===")
        with open(history_file, "r") as f:
            print(f.read())
    else:
        print("\nNo history available.")

def length_converter():
    print("\nLength Converter (meters ↔ kilometers ↔ miles)")
    value = float(input("Enter value: "))
    unit = input("Enter unit (m/km/miles): ").lower()
    
    if unit == "m":
        km = value / 1000
        miles = value / 1609.34
    elif unit == "km":
        m = value * 1000
        miles = value / 1.60934
    elif unit == "miles":
        m = value * 1609.34
        km = value * 1.60934
    else:
        print("Invalid unit!")
        return
    
    if unit == "m":
        print(f"{value} m = {km:.2f} km = {miles:.2f} miles")
        save_history(f"{value} m = {km:.2f} km = {miles:.2f} miles")
    elif unit == "km":
        print(f"{value} km = {m:.2f} m = {miles:.2f} miles")
        save_history(f"{value} km = {m:.2f} m = {miles:.2f} miles")
    elif unit == "miles":
        print(f"{value} miles = {m:.2f} m = {km:.2f} km")
        save_history(f"{value} miles = {m:.2f} m = {km:.2f} km")

def weight_converter():
    print("\nWeight Converter (kg ↔ g ↔ pounds)")
    value = float(input("Enter value: "))
    unit = input("Enter unit (kg/g/lb): ").lower()
    
    if unit == "kg":
        g = value * 1000
        lb = value * 2.20462
    elif unit == "g":
        kg = value / 1000
        lb = value / 453.592
    elif unit == "lb":
        kg = value / 2.20462
        g = kg * 1000
    else:
        print("Invalid unit!")
        return
    
    if unit == "kg":
        print(f"{value} kg = {g:.2f} g = {lb:.2f} lb")
        save_history(f"{value} kg = {g:.2f} g = {lb:.2f} lb")
    elif unit == "g":
        print(f"{value} g = {kg:.2f} kg = {lb:.2f} lb")
        save_history(f"{value} g = {kg:.2f} kg = {lb:.2f} lb")
    elif unit == "lb":
        print(f"{value} lb = {kg:.2f} kg = {g:.2f} g")
        save_history(f"{value} lb = {kg:.2f} kg = {g:.2f} g")

def unit_converter():
    print("=== Unit Converter ===")
    print("Options:")
    print("1. Length")
    print("2. Weight")
    print("Type 'history' to view past conversions or 'exit' to quit.\n")
    
    while True:
        choice = input("Select option (1/2): ").strip().lower()
        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
