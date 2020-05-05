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

  def print_today_weather(self):
    print("Température actuelle : {temp} \nTempérature minimal : {temp_min}\n\
Température maximale : {temp_max}\nTempérature ressenti : {temp_ressenti}\n\
Vitesse du vent : {vent}\nHeure de l'aube : {aube}\nHeure du crépuscule : {crepuscule}\nHumidité : {humi}  ".format(temp=self.temp, temp_min=self.temp_min, temp_max=self.temp_max, temp_ressenti=self.temp_ressenti, vent=self.vitesse_vent, aube=self.heure_lever,crepuscule=self.heure_coucher,humi=self.taux_humi))

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
    self.date = ""
  @staticmethod
  def parse(self,json):
    """
    Parse un dictionaire JSON pour remplir les attributs de ForecastData
    """
    #FIXME
    self.day = 0
    self.day_plus_1 = 8
    self.day_plus_2 = 16
    self.day_plus_3 = 24
    self.day_plus_4 = 32
    self.day_plus_5 = 40
    self.temp_min = json['list'][self.day]['main']['temp_min']
    self.temp_max = json['list'][self.day]['main']['temp_max']
    somme_max_min = self.temp_min_day + self.temp_max_day
    self.temp_moyenne = somme_max_min / 2 # pour obtenir la moyenne des températures max et mini sur une journée
    self.temp_ressenti = json['list'][self.day]['main']['pressure']
    self.vitesse_vent  =json['list'][self.day]['wind']['speed']
    self.taux_humi = json['list'][self.day]['main']['humidity']
    self.date = json['list'][self.day]['dt_txt'][0:10]
    return self


  def print_forecast_weather(self, day):
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
      self.day = 40
    print("{day} :\n  Température minimal : {temp_min}\n\
  Température maximale : {temp_max}\n  Température moyenne de la journée : {temp_moy}\n  Température ressenti : {temp_ressenti}\n\
  Vitesse du vent : {vent}\n  Humidité : {humi}  ".format(\
      day=self.date,temp_min=self.temp_min, temp_max=self.temp_max, temp_moy=self.temp_moyenne,temp_ressenti=self.temp_ressenti,\
      vent=self.vitesse_vent, humi=self.taux_humi))


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