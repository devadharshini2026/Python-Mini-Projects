def currency_converter():

    rates = {
        "USD": 1.0,
        "INR": 82.50,
        "EUR": 0.93,
        "GBP": 0.81,
        "JPY": 148.0
    }

    print("=== Currency Converter ===")
    print("Supported currencies:", ", ".join(rates.keys()))

    while True:
        from_currency = input("Convert from (currency code, or 'exit' to quit): ").upper()
        if from_currency.lower() == "exit":
            break
        to_currency = input("Convert to (currency code): ").upper()
        try:
            amount = float(input(f"Amount in {from_currency}: "))
        except ValueError:
            print("Please enter a valid number.\n")
            continue

        if from_currency not in rates or to_currency not in rates:
            print("Unsupported currency. Try again.\n")
            continue

        converted = amount / rates[from_currency] * rates[to_currency]
        print(f"{amount} {from_currency} = {converted:.2f} {to_currency}\n")

    input("Press Enter to exit...")

if __name__ == "__main__":
    currency_converter()
