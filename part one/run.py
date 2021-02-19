#!/venv/bin/python
from flask import Flask
from pyowm import OWM
from flask import request

app = Flask(__name__)

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

    if (request.args.get('humidity')):
        weather_details['humidity'] = weather_at_place.weather.humidity

    if (request.args.get('detail')):
        weather_details['detail'] = weather_at_place.weather.detailed_status

    return weather_details

# Keep this at the bottom of app.py
app.run(debug=True)
