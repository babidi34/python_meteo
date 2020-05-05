import client
from Models import weatherModels

test_meteo = client.WeatherForecastClient()
test_meteo = test_meteo.fetch_weather()

test_meteo5 = client.WeatherForecastClient()
test_meteo5 = test_meteo5.fetch_forecast()
print(test_meteo)
print(test_meteo5)

#meteo_day = weatherModels.WeatherData.parse(test_meteo)
meteo_day = weatherModels.WeatherData()
meteo_day.parse(meteo_day,test_meteo)
print(meteo_day.temp)
meteo_day.print_today_weather()
