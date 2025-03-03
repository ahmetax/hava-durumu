from flask import Flask, render_template, request, redirect, url_for
import os
from weather_api import get_current_weather, get_forecast
from visualization import plot_temperature_forecast, plot_weather_conditions

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hava_durumu_uygulamasi'

# Static klasörünü oluştur
os.makedirs('static', exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    weather_data = None
    forecast_data = None
    error = None
    city = None
    
    if request.method == 'POST':
        city = request.form.get('city')
        
        if not city:
            error = "Lütfen bir şehir adı girin."
        else:
            # Güncel hava durumunu al
            weather_data = get_current_weather(city)
            
            if weather_data:
                # 5 günlük tahmini al
                forecast_data = get_forecast(city)
                
                if forecast_data:
                    # Grafikleri oluştur
                    plot_temperature_forecast(forecast_data, city)
                    plot_weather_conditions(forecast_data, city)
                else:
                    error = f"{city} için tahmin verileri alınamadı."
            else:
                error = f"{city} için hava durumu verileri alınamadı."
    
    return render_template('index.html', 
                           weather_data=weather_data, 
                           forecast_data=forecast_data,
                           error=error,
                           city=city)

if __name__ == '__main__':
    app.run(debug=True)
