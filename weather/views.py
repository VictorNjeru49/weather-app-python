from django.shortcuts import render
import json
import urllib.request
# Create your views here.
def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        res = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city)
        data = res.read()
        json_data = json.loads(data)
        setdata={
            "country_code": str(json_data['sys']['country']),
            "description": str(json_data['weather'][0]['description']),
            "coordinate": str(json_data['coord']['lon']) + ' '
            + str(json_data['coord']['lat']),
            "temp": str(json_data['main']['temp']) + 'k',
            "pressure": str(json_data['main']['pressure']),
            "humidity": str(json_data['main']['humidity']),
        }
    else:
        city= ''
        setdata = {}
    return render(request, 'index.html', {'city': city, 'data': setdata})