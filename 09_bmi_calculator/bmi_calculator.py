def calculate_bmi(weight, height):
    return weight / (height ** 2)

def main():
    print("=== BMI Calculator ===")

    try:
        weight = float(input("Enter weight in kilograms: "))
        height = float(input("Enter height in meters: "))
    except ValueError:
        print("Invalid input! Please enter numeric values.")
        return

    bmi = calculate_bmi(weight, height)
    print(f"\nYour BMI: {bmi:.2f}")

    if bmi < 18.5:
        print("Category: Underweight")
    elif 18.5 <= bmi < 24.9:
        print("Category: Normal weight")
    elif 25 <= bmi < 29.9:
        print("Category: Overweight")
    else:
        print("Category: Obesity")

if __name__ == "__main__":
    main()
