//direct approach

import datetime as dt
import requests
from bardapi import Bard
import os
import time

BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read().strip()
CITY = input("Enter the city name: ")

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY

response = requests.get(url).json()

# Check if 'weather' key exists in the response
if 'weather' in response:
    weather_description = response['weather'][0]['description']
else:
    weather_description = 'N/A'

# Check if 'main' and 'wind' keys exist in the response
if 'main' in response and 'wind' in response:
    temperature = response['main']['temp']
    humidity = response['main']['humidity']
    wind_speed = response['wind']['speed']
else:
    temperature = humidity = wind_speed = 'N/A'

os.environ["_BARD_API_KEY"] = "XQi-zo35S2xCxJu5JBOqeBEnM41NlAO4xhmHjWN5V1CLIloJ5yKQNJhuZNhz7Y9pxf7sOA."

message = f"Weather forecast for {CITY}:\nDescription: {weather_description}\nTemperature: {temperature}°C\nHumidity: {humidity}%\nWind Speed: {wind_speed} m/s dont display the stats, just convert the temperature into celcius. show the city name and temperature and  create a narrative prompt with emojis and  with the temperature and with a bit of weather description and also what should i do and what should i carry with myself. keep the prompt simple,short and concise"

bard_response = Bard().get_answer(message)
answer_content = bard_response['content']


for char in answer_content:
    print(char, end='',flush=True)
    time.sleep(.03)

