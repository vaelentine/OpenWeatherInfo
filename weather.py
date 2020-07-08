import dotenv
import os
import requests


def get_weather(api_key):
    city_name = input('enter city name: ')
    weather_api_address = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"
    api_request = requests.get(weather_api_address)
    print(api_request.json())

def main():
    #init
    dotenv.load_dotenv()
    api_key = os.getenv('api_key')
    get_weather(api_key)

if __name__ == "__main__":
    main()
