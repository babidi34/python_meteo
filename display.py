import client
from Models import weatherModels

class WeatherForecast:
  """
  La class WeatherForcast utilise un WeatherForecastClient pour afficher les informations météo
  """

  def __init__(self):
    """
    Créer une instance de WeatherForecast avec un client donné
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

    self.temp_min_day = 0
    self.temp_max_day = 0
    self.temp_moyenne = 0
    self.temp_ress_moy = 0
    self.vitesse_vent_moy = 0
    self.taux_humi_moy = 0
    self.day = 0
    self.date = ""

  def print_today_weather(self):
    """
    Print les informations météo de la journée
    """
    #FIXME
    recup_json = client.WeatherForecastClient()
    recup_json = recup_json.fetch_weather()
    meteo = weatherModels.WeatherData()
    meteo.parse(meteo,recup_json)
    self.temp = meteo.temp
    self.temp_min = meteo.temp_min
    self.temp_max = meteo.temp_max
    self.temp_ressenti = meteo.temp_ressenti
    self.vitesse_vent = meteo.vitesse_vent
    self.heure_lever = meteo.heure_lever
    self.heure_coucher = meteo.heure_coucher
    self.taux_humi = meteo.taux_humi

    print("Température actuelle : {temp} \nTempérature minimal : {temp_min}\n\
        Température maximale : {temp_max}\nTempérature ressenti : {temp_ressenti}\n\
        Vitesse du vent : {vent}\nHeure de l'aube : {aube}\nHeure du crépuscule : {crepuscule}\nHumidité : {humi}  ".format(
      temp=self.temp, temp_min=self.temp_min, temp_max=self.temp_max, temp_ressenti=self.temp_ressenti,
      vent=self.vitesse_vent, aube=self.heure_lever, crepuscule=self.heure_coucher, humi=self.taux_humi))

  def print_forecast(self):
    """
    Print les prévisions météo pour les 5 prochains jours
    """
    #FIXME
    recup_json = client.WeatherForecastClient()
    recup_json = recup_json.fetch_forecast()
    meteo = weatherModels.ForecastData()
    for i in range(0,5):

      meteo.parse(meteo,recup_json,i)

      self.temp_min_day = meteo.temp_min
      self.temp_max_day = meteo.temp_max
      somme_max_min = self.temp_min_day + self.temp_max_day
      self.temp_moyenne = somme_max_min
      self.temp_ress_moy = meteo.temp_ressenti
      self.vitesse_vent_moy = meteo.vitesse_vent
      self.taux_humi_moy = meteo.taux_humi
      self.day = meteo.day
      self.date = meteo.date


      print("{day} :\n  Température minimal : {temp_min}\n\
        Température maximale : {temp_max}\n  Température moyenne de la journée : {temp_moy}\n  Température ressenti : {temp_ressenti}\n\
        Vitesse du vent : {vent}\n  Humidité : {humi}  ".format( \
        day=self.date, temp_min=self.temp_min_day, temp_max=self.temp_max_day, temp_moy=self.temp_moyenne,
        temp_ressenti=self.temp_ressenti, \
        vent=self.vitesse_vent_moy, humi=self.taux_humi_moy))