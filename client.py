import requests
from requests import get

class WeatherForecastClient:
  """
  La class WeatherForecastClient permet de préparer vos requêtes vers OpenWeatherMaps, avec des réglages données
  """

  api_url = 'https://api.openweathermap.org/data/2.5'
  api_key = 'f3143d70cd7df528a06b96cd3ef2a841'


  def __init__(self):
    """
    Créer une instance de WeatherForecastClient,
    avec des paramètres tel que le système d'unité et la langue
    """
    #FIXME
    self.systeme_unite="Celsius"
    self.langue="français"
    self.ville = input("Saisissez votre ville : ")


  def fetch_weather(self):
    """
    Effectue une requète sur l'API OpenWeatherMaps pour récuperer la météo de la journée.
    Retourne un objet WeatherData
    """
    #FIXME
    meteo_requete = get('http://api.openweathermap.org/data/2.5/weather?q='+self.ville+'&appid='+WeatherForecastClient.api_key)
    meteo = meteo_requete.json()['weather']
# pour mes tests    print(meteo)
    return meteo
  
  def fetch_forecast(self):
    """
    Effectue une requète sur l'API OpenWeatherMaps pour récuperer les prévisions météo pour les 5 prochains jour.
    Retourn un objet ForecastData
    """
    #FIXME
    meteo_r5 = get('http://api.openweathermap.org/data/2.5/forecast?q='+self.ville+'&appid='+WeatherForecastClient.api_key)
    meteo5 = meteo_r5.json()['list']
# pour mes tests    print(meteo5)
    return meteo5
"""  Pour mes tests
test_meteo = WeatherForecastClient()
test_meteo.fetch_weather()

test_meteo5 = WeatherForecastClient()
test_meteo5.fetch_forecast()"""