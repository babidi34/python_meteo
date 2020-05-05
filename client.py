import requests
from requests import get
from Models import coords

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
    self.systeme_unite="metric"
    self.langue="fr"
    mes_coord = coords.Coordinates()
    mes_coord.fromIP(mes_coord)
    self.lat = mes_coord.lat
    self.lon = mes_coord.lon

  def fetch_weather(self):
    """
    Effectue une requète sur l'API OpenWeatherMaps pour récuperer la météo de la journée.
    Retourne un objet WeatherData
    """
    #FIXME
    meteo_requete = get('http://api.openweathermap.org/data/2.5/weather?lat='+self.lat+'&lon='+self.lon+'&lang='+self.langue+'&units='+self.systeme_unite+'&appid='+WeatherForecastClient.api_key)
    meteo = meteo_requete.json()
    return meteo
  
  def fetch_forecast(self):
    """
    Effectue une requète sur l'API OpenWeatherMaps pour récuperer les prévisions météo pour les 5 prochains jour.
    Retourn un objet ForecastData
    """
    #FIXME
    meteo_r5 = get('http://api.openweathermap.org/data/2.5/forecast?lat='+self.lat+'&lon='+self.lon+'&lang='+self.langue+'&units='+self.systeme_unite+'&appid='+WeatherForecastClient.api_key)
    meteo5 = meteo_r5.json()
    return meteo5



