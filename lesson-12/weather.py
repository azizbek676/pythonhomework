import requests
api_key = 'your_api_key_here'
city = 'Tashkent'
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
response = requests.get(url)
data = response.json()
if response.status_code == 200:
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    weather_description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Pressure: {pressure} hPa")
    print(f"Weather: {weather_description}")
    print(f"Wind Speed: {wind_speed} m/s")
else:
    print("Error fetching data, please check the city name and API key.")
