import requests
api_key='2b5989d9c8a35b5af6645a39fd063a32'
url='http://api.openweathermap.org/data/2.5/weather?q={}&appid={}'
import datetime
def getweather(city):
    result = requests.get(url.format(city, api_key))
      
    if result:
        json = result.json()
        city = json['name']
        country = json['sys']
        temp_kelvin = json['main']['temp']
        temp_celsius = temp_kelvin-273.15
        temp_min=json['main']['temp_min']-273.15
        temp_max=json['main']['temp_max']-273.15
        weather1 = json['weather'][0]['main']
        final = [city, country, temp_kelvin, 
                 temp_celsius, weather1,temp_min,temp_max]
        return final
    else:
        print("NO Content Found")
        pass
    pass
def response(city):
    weather = getweather(city)
      
    if weather:
        location_l= weather[1]
        cityy=str(weather[0])
        temperature_l= weather[3]
        temperature_l=round(temperature_l,2)
        weather_l= weather[4]
        #print(cityy,location_l['country'],temperature_l,weather_l,sep='\n')
        ans="\n".join([cityy,location_l['country'],str(temperature_l),weather_l])
        print(ans)
        return ans
    else:
        print('Error', "Cannot find {}".format(city))
#ans=response('delhi')
import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = False

# Create some test data for our catalog in the form of a list of dictionaries.
books = [
    {'id': 0,
     'title': 'A Fire Upon the Deep',
     'author': 'Vernor Vinge',
     'first_sentence': 'The coldsleep itself was dreamless.',
     'year_published': '1992'},
    {'id': 1,
     'title': 'The Ones Who Walk Away From Omelas',
     'author': 'Ursula K. Le Guin',
     'first_sentence': 'With a clamor of bells that set the swallows soaring, the Festival of Summer came to the city Omelas, bright-towered by the sea.',
     'published': '1973'},
    {'id': 2,
     'title': 'Dhalgren',
     'author': 'Samuel R. Delany',
     'first_sentence': 'to wound the autumnal city.',
     'published': '1975'}
]


@app.route('/', methods=['GET'])
def home():
    return '''<h1>RESTAURANT CHATBOT</h1>
<p>Order Food Here.</p>'''


@app.route('/api/v1/resources/books/all', methods=['GET'])
def api_all():
    return jsonify(books)


@app.route('/api/v1/resources/books', methods=['GET'])
def api_id():
    # Check if an ID was provided as part of the URL.
    # If ID is provided, assign it to a variable.
    # If no ID is provided, display an error in the browser.
    if 'id' in request.args:
        idd = request.args['id']
    else:
        return "Error: No id field provided. Please specify an id."
    print("sssssssss",idd)
    # Create an empty list for our results
    """
    results = []

    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for book in books:
        if book['id'] == id:
            results.append(book)
    """
    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    #print(response(idd))
    idd=str(idd)
    idd=idd.replace("%", " ")
    return str(response(idd))

import os
port = int(os.environ.get('PORT', 5000))
app.run(host='0.0.0.0', port=port)
