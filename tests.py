import client
from Models import weatherModels, coords

test_meteo = client.WeatherForecastClient()
print(test_meteo.lat)
print(test_meteo.lon)
test_meteo = test_meteo.fetch_weather()

test_meteo5 = client.WeatherForecastClient()
test_meteo5 = test_meteo5.fetch_forecast()
print(test_meteo)
print(test_meteo5)

#meteo_day = weatherModels.WeatherData.parse(test_meteo)
meteo_day = weatherModels.WeatherData()
meteo_day.parse(meteo_day,test_meteo)
meteo_day.print_today_weather()

meteo_day5 = weatherModels.ForecastData()
meteo_day5.parse(meteo_day5,test_meteo5)
meteo_day5.print_forecast_weather(1)

mes_coord = coords.Coordinates()
mes_coord.fromIP(mes_coord)
print(mes_coord.lat)
print(mes_coord.lon)
