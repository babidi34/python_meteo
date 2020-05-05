import requests
from requests import get

class Coordinates:

  def __init__(self, lat=0, lon=0):
    """
    Créer une instance de Coordinates pour les latitude & longitude données
    """
    #FIXME
    self.lat = lat
    self.lon = lon
    self.coords = str(self.lat)+","+str(lon)
# pour test    print(self.lat,self.lon)
# pour test    print(self.coords)

  def get_latitude(self):
    """
    Getter pour la latitude
    """
    #FIXME
    return self.lat

  def get_longitude(self):
    """
    Getter pour la longitude
    """
    #FIXME
    return self.lon

  def get_coords(self):
    """
    Getter pour les coordonnées
    """
    ##FIXME
    return self.coords


  @staticmethod
  def fromIP(self):
    """
    Créer une instance de Coordinates en effectuant une requêtes vers l'API IPData pour récuperer
    les latitude et longitude via l'IP 
    """
    api_url = 'https://api.ipdata.co/'
    api_key = 'ce6ce07a42a7e7416d4eb42a44c11ca7b7af2781b4b2e53416a6c634'
    ##FIXME

    self.lat = get('https://api.ipdata.co/latitude?api-key='+api_key).text
    self.lon = get('https://api.ipdata.co/longitude?api-key='+api_key).text
    iplocal = get('https://api.ipdata.co/ip?api-key='+api_key).text
    #coord_iplocal = Coordinates(lat_iplocal,lon_iplocal)

# pour tester :  Coordinates.fromIP()