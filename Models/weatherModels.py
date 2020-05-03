
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
    self.temp = json['main']['temp']
    self.temp_min = 0
    self.temp_max = 0
    self.temp_ressenti = 0
    self.vitesse_vent = 0
    self.heure_lever = 0
    self.heure_coucher = 0
    self.taux_humi = 0

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

  @staticmethod
  def parse(json):
    """
    Parse un dictionaire JSON pour remplir les attributs de ForecastData
    """
    #FIXME