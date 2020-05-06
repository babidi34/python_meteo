import client, display
from Models import weatherModels, coords

"""test_meteo = client.WeatherForecastClient()
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

display = display.WeatherForecast()
#display.print_today_weather()

display.print_forecast()
print(display.day)"""

"""recup_json = client.WeatherForecastClient()
recup_json = recup_json.fetch_forecast()
meteo = weatherModels.ForecastData()
meteo.parse(meteo,recup_json,5)
print("{day} :\n  Température minimal : {temp_min}\n\
      Température maximale : {temp_max}\n  Température moyenne de la journée : {temp_moy}\n  Température ressenti : {temp_ressenti}\n\
      Vitesse du vent : {vent}\n  Humidité : {humi}  ".format( \
      day=meteo.date, temp_min=meteo.temp_min, temp_max=meteo.temp_max, temp_moy=meteo.temp_moyenne,
      temp_ressenti=meteo.temp_ressenti, \
      vent=meteo.vitesse_vent, humi=meteo.taux_humi))



#print(recup_json['list'][10]['main']['temp_min'])"""

display = display.WeatherForecast()

display.print_forecast()
display.print_today_weather()