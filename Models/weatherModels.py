import requests
class WeatherData:
  def __init__(self):
    """
    Créer une instance vide de WeatherData.
    """
    #FIXME
    self.temp = 0
    self.temp_min = 0
    self.temp_max = 0
    self.temp_ressenti = 0
    self.vitesse_vent = 0
    self.heure_lever = 0
    self.heure_coucher = 0
    self.taux_humi = 0

  @staticmethod
  def parse(json):
    """
    Parse un dictionaire JSON pour remplir les attributs de WeatherData
    """
    #FIXME
    WeatherData.temp = json['main']['temp']
    WeatherData.temp_min = json['main']['temp_min']
    WeatherData.temp_max = json['main']['temp_max']
    WeatherData.temp_ressenti = json['main']['pressure']
    WeatherData.vitesse_vent = json['wind']['speed']
    WeatherData.heure_lever = json['sys']['sunrise']
    WeatherData.heure_coucher = json['sys']['sunset']
    WeatherData.taux_humi = json['main']['humidity']

class ForecastData:
  def __init__(self):
    """
    Créer une instance vide de ForecastData
    """
    #FIXME
    self.temp_min_day = 0
    self.temp_max_day = 0
    self.temp_moyenne = 0
    self.temp_ress_moy = 0
    self.vitesse_vent_moy = 0
    self.taux_humi_moy = 0
    self.day = 0
    self.day_plus_1 = 8
    self.day_plus_2 = 16
    self.day_plus_3 = 24
    self.day_plus_4 = 32
    self.day_plus_5 = 40
  @staticmethod
  def parse(json):
    """
    Parse un dictionaire JSON pour remplir les attributs de ForecastData
    """
    #FIXME
    ForecastData.day = 0
    ForecastData.day_plus_1 = 8
    ForecastData.day_plus_2 = 16
    ForecastData.day_plus_3 = 24
    ForecastData.day_plus_4 = 32
    ForecastData.day_plus_5 = 40
    ForecastData.temp_min_day = json['list'][ForecastData.day]['main']['temp_min']
    ForecastData.temp_max_day = json['list'][ForecastData.day]['main']['temp_max']
    somme_max_min = ForecastData.temp_min_day + ForecastData.temp_max_day
    ForecastData.temp_moyenne = somme_max_min / 2 # pour obtenir la moyenne des températures max et mini sur une journée
    ForecastData.temp_ress_moy = json['list'][ForecastData.day]['main']['pressure']
    ForecastData.vitesse_vent_moy  =json['list'][ForecastData.day]['wind']['speed']
    ForecastData.taux_humi_moy = json['list'][ForecastData.day]['main']['humidity']

""" Pour tester WeatherData.parse(json)
n = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Nanterre&units=metric&lang=fr&appid=f3143d70cd7df528a06b96cd3ef2a841')
n = n.json()
WeatherData.parse(n)
print(WeatherData.temp_max)
"""
""" Pour tester ForecastData.parse(json)
n = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Nanterre&units=metric&lang=fr&appid=f3143d70cd7df528a06b96cd3ef2a841')
n = n.json()
ForecastData.parse(n)
print(ForecastData.temp_min_day)"""