def length_converter():
    print("\n=== Length Converter ===")
    meters = float(input("Enter length in meters: "))
    print(f"{meters} meters = {meters * 100} centimeters")
    print(f"{meters} meters = {meters * 39.3701} inches")
    print(f"{meters} meters = {meters * 3.28084} feet\n")

def temperature_converter():
    print("\n=== Temperature Converter ===")
    celsius = float(input("Enter temperature in Celsius: "))
    print(f"{celsius}°C = {(celsius * 9/5) + 32}°F")
    print(f"{celsius}°C = {celsius + 273.15}K\n")

def weight_converter():
    print("\n=== Weight Converter ===")
    kg = float(input("Enter weight in kilograms: "))
    print(f"{kg} kg = {kg * 1000} grams")
    print(f"{kg} kg = {kg * 2.20462} pounds\n")

def main():
    print("=== Unit Converter ===")
    while True:
        print("1. Length Converter")
        print("2. Temperature Converter")
        print("3. Weight Converter")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            length_converter()
        elif choice == "2":
            temperature_converter()
        elif choice == "3":
            weight_converter()
        elif choice == "4":
            break
        else:
            print("Invalid option. Please try again.\n")

    input("Press Enter to exit...")  # Keeps the console open

if __name__ == "__main__":
    main()
