import client, Models

test_meteo = client.WeatherForecastClient()
test_meteo = test_meteo.fetch_weather()

test_meteo5 = client.WeatherForecastClient()
test_meteo5 = test_meteo5.fetch_forecast()
print(test_meteo)
print(test_meteo5)