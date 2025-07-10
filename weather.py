import tkinter as tk
from tkinter import messagebox
import requests

# Replace this with your actual API key
API_KEY = "e672fde063c3b90a8cadc3af2c8123c2"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather():
    city = city_entry.get()
    if not city:
        messagebox.showwarning("Input Error", "Please enter a city name.")
        return

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params)
        print("Request URL:", response.url)  # 👈 See the actual URL sent
        response.raise_for_status()
        data = response.json()
        print("Response JSON:", data)        # 👈 See the full response

        weather = data["weather"][0]["description"].title()
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = (
            f"Weather: {weather}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
        result_label.config(text=result)

    except requests.exceptions.HTTPError:
        messagebox.showerror("Error", "City not found or API error.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# GUI setup
root = tk.Tk()
root.title("Weather App")

tk.Label(root, text="Enter City:").pack(pady=5)

city_entry = tk.Entry(root, width=30)
city_entry.pack(pady=5)

tk.Button(root, text="Get Weather", command=get_weather).pack(pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
result_label.pack(pady=10)

root.mainloop()
