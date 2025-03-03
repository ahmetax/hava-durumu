import requests
from apikeys import API_KEY

def get_current_weather(city):
    """Belirli bir şehir için güncel hava durumu verilerini çeker"""
    base_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"  # Celsius olarak sıcaklık
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Hata: {response.status_code} - {response.text}")
        return None

def get_forecast(city, days=5):
    """Belirli bir şehir için 5 günlük hava durumu tahminini çeker"""
    base_url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric",
        "cnt": days * 8  # Her gün için 8 veri noktası (3 saatte bir)
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Hata: {response.status_code} - {response.text}")
        return None
