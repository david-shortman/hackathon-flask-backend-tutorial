from flask import Flask
app = Flask(__name__)

from pyowm import OWM
from flask import request

@app.route('/')
def hello():
    return 'Hello there'

owm = OWM('YOUR_API_KEY_HERE')

@app.route('/weather/<country>/<city>')
def weather(country, city):
    weather_manager = owm.weather_manager()
    weather_at_place = weather_manager.weather_at_place(f'{country},{city}')
    temperature = weather_at_place.weather.temperature('celsius')
    
    weather_details = {
        'temp_celsius': temperature['temp'],
        'temp_kelvin': temperature['temp'] + 273
    }
    if (request.args.get('show_humidity')):
        weather_details['humidity'] = weather_at_place.weather.humidity
    if (request.args.get('show_precipitation')):
        weather_details['precipitation_last_hour'] = weather_at_place.weather.rain['1h']
    return weather_details

# Keep this at the bottom of app.py
app.run(debug=True)