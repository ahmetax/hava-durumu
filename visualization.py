import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np

def plot_temperature_forecast(forecast_data, city):
    """Tahmin verilerinden sıcaklık grafiği oluşturur"""
    times = []
    temps = []
    
    for item in forecast_data['list']:
        # Unix timestamp'i tarih formatına dönüştür
        time = datetime.fromtimestamp(item['dt'])
        times.append(time)
        temps.append(item['main']['temp'])
    
    plt.figure(figsize=(12, 6))
    plt.plot(times, temps, marker='o', linestyle='-', color='#FF5733')
    plt.title(f"{city.capitalize()} için 5 Günlük Sıcaklık Tahmini")
    plt.xlabel('Tarih ve Saat')
    plt.ylabel('Sıcaklık (°C)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Grafiği kaydet ve görüntüle
    plt.savefig('static/temperature_forecast.png')
    plt.close()

def plot_weather_conditions(forecast_data, city):
    """Hava koşullarının dağılımını gösteren pasta grafiği oluşturur"""
    conditions = {}
    
    for item in forecast_data['list']:
        condition = item['weather'][0]['main']
        if condition in conditions:
            conditions[condition] += 1
        else:
            conditions[condition] = 1
    
    labels = conditions.keys()
    sizes = conditions.values()
    
    plt.figure(figsize=(10, 8))
    plt.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, shadow=True)
    plt.title(f"{city.capitalize()} için 5 Günlük Hava Koşulları Dağılımı")
    plt.axis('equal')
    
    # Grafiği kaydet ve görüntüle
    plt.savefig('static/weather_conditions.png')
    plt.close()
