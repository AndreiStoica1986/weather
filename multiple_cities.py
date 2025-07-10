import csv
import requests
import time

API_KEY = "e672fde063c3b90a8cadc3af2c8123c2"  # Replace with your actual key
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

INPUT_FILE = "C:/PythonApps/Weather/in/cities.csv"
OUTPUT_FILE = "C:/PythonApps/Weather/out/weather_output.csv"

def fetch_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()
        if response.status_code == 200:
            weather = data["weather"][0]["description"].title()
            temp = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            return [city, weather, temp, humidity, wind_speed]
        else:
            print(f"Error for {city}: {data.get('message')}")
            return [city, "N/A", "N/A", "N/A", "N/A"]
    except Exception as e:
        print(f"Exception for {city}: {e}")
        return [city, "N/A", "N/A", "N/A", "N/A"]

def main():
    with open(INPUT_FILE, newline='', encoding='utf-8') as infile, \
         open(OUTPUT_FILE, mode='w', newline='', encoding='utf-8') as outfile:

        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        writer.writerow(["city", "weather", "temperature", "humidity", "wind speed"])

        for row in reader:
            if not row: continue  # Skip empty lines
            city = row[0].strip()
            if city:
                result = fetch_weather(city)
                writer.writerow(result)
                time.sleep(1)  # To respect API rate limits

    print(f"Done. Output saved to: {OUTPUT_FILE}")

if __name__ == "__main__":
    main()
