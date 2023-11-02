import requests, json, openai

city = input("Введите город: ")
url = 'https://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&lang=ru&appid=79d1ca96933b0328e1c7e3e7a26cb347'
weather_data = requests.get(url).json()
weather_data_structure = json.dumps(weather_data, indent=2)

temperature = round(weather_data['main']['temp'])
temperature_feels = round(weather_data['main']['feels_like'])
print('Сейчас в городе', city, str(temperature), '°C')
print("Ощущается как", temperature_feels, '°C')
