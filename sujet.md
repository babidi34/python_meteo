# Projet S2 : Station Météo - Palier 1


## Introduction

Ce projet, découpé en plusieurs paliers, vise à vous familiariser avec plusieurs concepts avancés de Python tels que :

* L'utilisation d'API
* Les workflows de traitement et d'affichage de données 
* La création d'interfaces consoles
* La création d'interfaces graphiques

Au cours de ce palier, l'objectif sera de récupérer et d'afficher correctement un certain nombre de données.
Ce 1er palier est découpé en un certain nombre d'étapes qui peuvent être implémentées de manière successive ou non, libre à vous de découper le travail comme vous l'entendez

## Critères de notation
* Ce projet sera uniquement noté en mini-soutenance au cours prochain
* Votre 

## Apercu du palier

Au cours de ce palier, vous allez implémenter un service de station météo basique dans une interface console. 

## Guidelines :

* Toutes les erreurs doivent être gérées convenablement (Pas d'interruption du script sauf si nécessaire)
* Vous pouvez rajouter :
  * Des fonctions dans les différents fichiers
* Imports autorisés :
  * datetime
  * argparse
  * requests
  * unittest et toute autre bibliothèque liée aux tests
* Toute autre bibliothèque entrainera l'application d'un malus sur la note de groupe

## Décomposition des fichiers

* `main.py` contiendra la gestion des interactions avec l'utilisateur (CLI)
* `client.py` implémentera les notions de client et les interactions avec l'API (Gestion des paramètres, Requêtes API, Traitement des résultats)
* `display.py` implémentera les fonctions liés au formatage des données et de leur affichage 
* Le dossier Models contient 2 fichiers liés aux types de données que vous allez manipuler : 
  * `coords.py` implémente la notion de Coordonées (Latitude, Longitude) et les manipulations nécessaires
  * `weatherModels.py` implémentera les modèles des données météo 

## Liste des fonctionnalités
* Localiser votre position grâce à votre adresse IP
* Afficher la météo actuelle à votre position actuelle
* Afficher les températures min/max pour la journée à votre position actuelle
* Afficher les prévisions météo pour les 5 prochains jours à votre position actuelle
* Agréger ces fonctions dans une interface type CLI

## Etape 1 : Récupération des coordonnées via l'IP

L'API de prévisions météorologiques que nous allons utiliser aujourd'hui utilisera vos coordonnées (Latitude, Longitude) afin de définir votre localisation. Pour cela, nous allons avoir besoin de récupérer ces coordonnées basées sur votre IP actuelle (pour le moment). Vous utilisez l'API https://docs.ipdata.co/ pour cela.

* Compléter le fichier `coordinates.py` du dossier Models avec les appels et traitements nécessaires :

* Deux attributs nécessaires : Latitude et Longitude
* Les méthodes `get_latitude()`, `get_longitude()` et `get_coords()` permettront de récupérer les valeurs de ces différents attributs pour utilisation ultérieure
* La méthode statique `fromIP()` agrège les traitements et permet de créer et renvoyer un objet Coordinates rempli avec vos coordonnées actuelles.

## Etape 2 : Création d'un client météo

Avant de récupérer nos données météo, nous aurons besoin  de créer un client, disposant d'un paramétrage spécifique afin de formater les informations correctement. La classe `WeatherForecastClient` du fichier `client.py` sera utilisée à cet effet :
  * Le constructeur prendra en paramètres les différents éléments de configuration nécessaires à votre client : Les coordonnées de la recherche météo, le système d'unité utilisée ainsi que la langue préférée (Vous trouverez le détail de formatage des requêtes sur la documentation de l'API : https://openweathermap.org/current#other )

  * Les méthodes `fetch_weather` et `fetch_forecast` seront responsables d'effectuer les appels API nécessaires (Respectivement la météo de la journée et les prévisions)

### Etape 2.5 : Création du modèle de données

Avant de pouvoir afficher nos informations météo de manière convenable, nous allons devoir faire le tri dans les infos que nous renvoie l'API :

* Nous utiliserons deux points d'entrée dans l'API pour récupérer les données météo actuelles (https://openweathermap.org/current#geo) ainsi que les prévisions pour les 5 prochains jours (https://openweathermap.org/forecast5#geo5)
* Chacun de ces points d'entrée renvoie des informations selon une structure différente, nous aurons donc besoin de récupérer les informations qui nous intéressent dans des objets dédiés `WeatherData` et `ForecastData` que vous devrez compléter dans le fichier `weatherModels.py` du dossier Models
* Les attributs à définir sont les suivants :
  * `WeatherData` :
    * Température actuelle
    * Température minimum actuelle dans la ville
    * Température maximum actuelle dans la ville
    * Température ressentie
    * Vitesse du vent
    * Heure de lever du soleil
    * Heure de coucher du soleil
    * Taux d'humidité
  * `ForecastData`:
    * Température minimum de la journée
    * Température maximum de la journée
    * Température moyenne chaque jour
    * Température ressentie moyenne chaque jour
    * Vitesse du vent moyenne chaque jour
    * Taux d'humidité moyen chaque jour
* L'objectif ici est de simplifier notre travail futur en pouvant directement accéder aux attributs de ces deux objets pour afficher les informations pertinentes. Il est donc nécessaire de relier les attributs de nos objets au JSON de réponse que nous obtiendrons sur nos 2 requêtes
* Ces 2 classes contiendront un constructeur permettant d'initialiser les attributs ainsi qu'une méthode `parse()`, prenant en paramètre un objet JSON qui viendra assigner les bonnes valeurs à nos attributs 
* Exemple:
```python
class WeatherData:

def __init__(self):
  self.temperature = 0

def parse(json):
   self.temperature = json['main']['temp']
openweather 
```

### Etape 2.9 : Utilisation de nos modèles de données

Maintenant que nos modèles de données sont prêts à être utilisés, nous allons pouvoir effectuer notre requête auprès de l'API. Ces appels seront effectués  dans les méthodes `fetch_weather()` et `fetch_forecast()` et renverront respectivement un objet de type `WeatherData` et `ForecastData` pour pouvoir les afficher ultérieurement.


## Etape 3 : Affichage des données et formatage

A cette étape, nous disposons de 2 objets fonctionnels contenant les informations météo dont nous avons besoin. L'objectif de cette étape est de formater ces informations de manière pertinente et lisible par l'utilisateur. 
Les deux méthodes `print_today_weather()` et `print_forecast_weather()` seront en charge de formater ces informations et de les afficher à l'utilisateur (L'utilisation de la fonction `str.format()` peut être intéressant à cette étape => Doc Python)


## Etape 4 : Création de l'interface Console

Afin de pouvoir accéder à l'ensemble des fonctionnalités de votre script, vous réaliserez une interface de type CLI comme détaillé dans le cours
* Le script doit être pouvoir appelé avec les arguments suivants :
* L'argument `period` (`p`) permet d'indiquer si nous voulons récupérer la météo du jour ou les prévisions à 5 jours. Il pourra prendre les valeurs 'today' et 'forecast'. Si absent, le script renverra par défaut la météo du jour
* L'argument `coordinates` (`-c`) permet d'indiquer les coordonnées du lieu dont nous souhaitons avoir la météo sous la forme `latitude,longitude`. Si absent, le script utilisera la localisation de votre adresse IP comme indiqué dans l'étape 1
* L'argument `help` (-h) permet d'afficher le fonctionnement du script et les arguments attendus (pris en charge de base par argparse)
* Chaque commande doit disposer d'un message d'aide indiquant à l'utilisateur la fonctionnalité de l'argument
* Si un utilisateur passe un mauvais argument au script, cela génerera une erreur et terminera l'exécution
* Exemples d'appels :

``` 
./meteo.py -h 
./meteo.py
./meteo.py -p today 
./meteo.py -c 43.42353,76.4545634
./meteo.py -p forecast -c 54.56452,23.546546
```

## Etape Transverse : Tests des fonctionnalités du script

Le fichier `tests.py` est à votre disposition pour rédiger l'ensemble de vos tests afin de vérifier le bon fonctionnement de votre script. 
2 types de tests seront attendus lors du suivi :
* Des tests unitaires : Tester vos fonctionnalités en appelant unitairement vos différentes fonctions à l'aide d'assertions (Doc python => bibliothèque `unittest` à creuser)
* Des tests de bout en bout : Tester votre script au global à l'aide de divers appels (Corrects et incorrects) : Voir exemple de l'étape 4
* Une option de votre CLI sera en mesure de lancer un panel de tests représentatif afin d'assurer la non-régression de votre Code

* La méthode d'implémentation de vos tests est libre, tout import est autorisé UNIQUEMENT dans le fichier `tests.py`

## Etape 5 : BONUS
Les bonus ne seront pris en compte que si l'ensemble du sujet est réalisé. Tout bonus implémenté sera valorisé sur la note finale

Quelques idées :
* Représenter l'icone de la météo par l'emoji correspondant
* Ajouter un paramètre de CLI  et les traitements associés permettant de passer le nom d'une ville a la place de ses coordonnées (une plus ample lecture de la documentation d'OpenWeatherMap peut vous aider)
* Ajouter un paramètre de CLI et les traitements associés permettant de représenter les prévisions sous forme de tableaux
* Gestion d'erreur modulaire




