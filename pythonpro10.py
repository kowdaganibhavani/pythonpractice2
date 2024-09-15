import requests


def get_weather(city, api_key):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        main = data['main']
        temperature = main['temp']
        humidity = main['humidity']
        description = data['weather'][0]['description']

        print(f"Weather  {city}:")
        print(f"Temperature: {temperature}°C")
        print(f"Humidity: {humidity}%")
        print(f"Description: {description}")
    else:
        print(f"City {city} not found!")


if __name__ == "__main__":
    city_name = input("Enter city name: ")
    api_key = 'your_openweathermap_api_key' 
    get_weather(city_name, api_key)
