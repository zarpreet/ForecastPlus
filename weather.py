import requests

api_key = '04c28c4c4860521e10f6b86634377ed7'

def forecast(city):
    weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    weather = weather_data.json()['weather'][0]['main']
    temperature = weather_data.json()['main']['temp']
    temp = round(1.8 * (temperature - 273.15) + 32)

    return weather, temp

def weather_image(weather):
  if weather == "Clouds" or weather == "clouds":
    return "/static/images/cloud.jpg"
  elif weather == "Rain" or weather == "rain":
    return "/static/images/rain.jpg"
  elif weather == "Clear" or weather == "clear":
    return "/static/images/clear.jpg"
  elif weather == "Thunderstorm" or weather == "thunderstorm":
    return "/static/images/thunderstorm.jpg"
  elif weather == "Mist" or weather == "mist":
    return "/static/images/mist.jpg"


def clothing_option(temp):
  if temp >= 101:
    return "Heat wave! Experts recommend not to go outside! Use Sunscreen!"
  elif temp >= 90:
    return "Experts recommend to wear shorts and a tank top! Use Sunscreen!"
  elif temp > 72:
    return "Experts recommend shorts and a T-shirt. Use Sunscreen."
  elif temp < 72 and temp > 32:
    return "It may begin to get chilly in the later parts of the afternoon. A sweatshirt is recommended!"
  elif temp < 32:
    return "It is below freezing! Wear a heavy winter coat, hats, and gloves!"
  
def weather_info(weather):
  if weather == 'Rain' or weather == 'rain' or weather == 'Thunderstorm' or weather == 'thunderstorm':
    return 'Experts recommend wearing a raincoat or carrying an umbrella while outside.'
  elif weather == "clear" or weather == "Clear":
    return "Experts say it is a great day to go outside if it is not too hot!"
  elif weather == 'mist' or weather == 'Mist':
    return 'Experts warn that it might be difficult to see outside. Be careful!'
  elif weather == "clouds" or weather == "Clouds":
    return 'Experts say that it could be a good day to go outside if it is not too cloudy!'

def error_image():
  return "/static/images/error.jpg"