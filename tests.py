class Coordinates:

  def __init__(self, lat, lon):
    """
    Créer une instance de Coordinates pour les latitude & longitude données
    """
    #FIXME
    self.lat = lat
    self.lon = lon
    print("la latitude: ", self.lat,", la longitude: ",self.lon)

coorman = Coordinates(75.0,14.3)
print(coorman.lat)
