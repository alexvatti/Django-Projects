from django.shortcuts import render

# Create your views here.
import requests
from django.shortcuts import render

def weather_view(request):
    weather_data = None
    city = request.POST.get('city')

    if request.method == 'POST' and city:
        api_key = ''  # Replace with your actual WeatherAPI key
        url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            weather_data = {
                'city': data['location']['name'],
                'region': data['location']['region'],
                'country': data['location']['country'],
                'temperature': data['current']['temp_c'],
                'condition': data['current']['condition']['text'],
                'icon': data['current']['condition']['icon']
            }
        else:
            weather_data = {'error': f"City '{city}' not found or invalid request."}

    return render(request, 'weather.html', {'weather': weather_data})
