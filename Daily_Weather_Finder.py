# Create a program which finds the daily weather for a specified location 
# I will be using the site Weatherstack
# API key stored as env variable for safety

import requests
from dotenv import load_dotenv # loads env variables from .env file 
load_dotenv()
import os # to access environment variable in my script

def get_weather(api_key, city): 
    '''
    This function fetches weather for a given city using Weatherstack API.
    '''
    url = f"http://api.weatherstack.com/current?access_key={api_key}&query={city}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        print('Error fetching weather data')
        return None
    
def display_weather(weather_data):
    '''
    This function displays weather information. 
    '''

    if weather_data and 'current' in weather_data:
        current = weather_data['current']
        print(f"Weather for {weather_data['location']['name']}, {weather_data['location']['country']}:")
        print(f"- Temperature: {current['temperature']}°C")
        print(f"- Humidity: {current['humidity']}%")
        print(f"- Description: {current['weather_descriptions'][0]}")
    else:
        print('Error fetching data:', response.json())
        return None
# Main program
api_key = os.environ.get('WEATHERSTACK_API_KEY')  # Retrieve API key from environment variable
if not api_key:
    print("API key not found. Please set the WEATHERSTACK_API_KEY environment variable.")
    exit(1)

city = input('Enter a city: ')
weather_data = get_weather(api_key, city)
display_weather(weather_data)