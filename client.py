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

  def fetch_weather(self):
    """
    Effectue une requète sur l'API OpenWeatherMaps pour récuperer la météo de la journée.
    Retourne un objet WeatherData
    """
    #FIXME
  
  def fetch_forecast(self):
    """
    Effectue une requète sur l'API OpenWeatherMaps pour récuperer les prévisions météo pour les 5 prochains jour.
    Retourn un objet ForecastData
    """
    #FIXME