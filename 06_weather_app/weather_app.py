import requests

API_KEY = "your_api_key_here"  # Replace with your OpenWeatherMap API key
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch weather data for a given city."""
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        weather = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].title()
        }
        return weather
    except requests.exceptions.HTTPError:
        print("❌ City not found. Please try again.")
    except Exception as e:
        print("⚠️ Error:", e)


def menu():
    """Menu loop for weather app."""
    while True:
        print("\n=== Weather App ===")
        city = input("Enter city name (or type 'exit' to quit): ").strip()
        if city.lower() == "exit":
            print("Goodbye!")
            break

        weather = get_weather(city)
        if weather:
            print(f"\n🌍 Weather in {weather['city']}:")
            print(f"🌡️ Temperature: {weather['temperature']}°C")
            print(f"💧 Humidity: {weather['humidity']}%")
            print(f"☁️ Condition: {weather['description']}")


if __name__ == "__main__":
    menu()
