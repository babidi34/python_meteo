class WeatherData:
  def __init__(self):
    """
    Créer une instance vide de WeatherData.
    """
    #FIXME


  @staticmethod
  def parse(self,json):
    """
    Parse un dictionaire JSON pour remplir les attributs de WeatherData
    """
    #FIXME
    self.temp = json['main']['temp']
    self.temp_min = json['main']['temp_min']
    self.temp_max = json['main']['temp_max']
    self.temp_ressenti = json['main']['pressure']
    self.vitesse_vent = json['wind']['speed']
    self.heure_lever = json['sys']['sunrise']
    self.heure_coucher = json['sys']['sunset']
    self.taux_humi = json['main']['humidity']
    return WeatherData


class ForecastData:
  def __init__(self):
    """
    Créer une instance vide de ForecastData
    """
    #FIXME

  @staticmethod
  def parse(self,json, day):
    """
    Parse un dictionaire JSON pour remplir les attributs de ForecastData
    """
    #FIXME
    if day == 0:
      self.day = 0
    elif day == 1:
      self.day = 8
    elif day == 2:
      self.day = 16
    elif day == 3:
      self.day = 24
    elif day == 4:
      self.day = 32
    elif day == 5:
      self.day = 39

    self.temp_min = json['list'][self.day]['main']['temp_min']
    self.temp_max = json['list'][self.day]['main']['temp_max']
    somme_max_min = self.temp_min + self.temp_max
    self.temp_moyenne = somme_max_min / 2 # pour obtenir la moyenne des températures max et mini sur une journée
    self.temp_ressenti = json['list'][self.day]['main']['pressure']
    self.vitesse_vent  =json['list'][self.day]['wind']['speed']
    self.taux_humi = json['list'][self.day]['main']['humidity']
    self.date = json['list'][self.day]['dt_txt'][0:10]
    return self




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