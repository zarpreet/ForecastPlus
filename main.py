from flask import Flask
from flask import render_template
from flask import request
# from bs4 import BeautifulSoup
import requests
# import weather
from weather import forecast
from weather import weather_image
from weather import clothing_option
from weather import weather_info
from weather import error_image

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
  data = {  

    }
  return render_template("index.html", data=data)

@app.route("/forecastPlus", methods=["GET", "POST"])
def handle_forecastPlus():
  if request.method == "GET":
    return "You're getting the ForecastPlus page."
  else:
    form = request.form
    city = form['city']
    try:
      result = forecast(city)
      weather = result[0]
      temp = result[1]   
      clothing_items = clothing_option(temp)
      weather_information = weather_info(weather)
      results = (f"{city} has {weather} and a temperature of {temp}°F")
      image = weather_image(weather)
      clothing = (f"{clothing_items} \n {weather_information}")
      return render_template("/results.html",results=results, image = image, clothing = clothing)
    except:
      results = (f'Your input of {city} was invalid. Try again.')
      image = error_image()
      return render_template("/results.html",results=results, image = image)

app.run(host='0.0.0.0', port=81, debug=True)