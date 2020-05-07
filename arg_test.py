import argparse, display, Models, client

display = display.WeatherForecast()

def today(display):
    display.print_today_weather()
def forecast(display):
    display.print_forecast()

parser = argparse.ArgumentParser()
#parser.add_argument("echo", help="affiche ce que vous entrez en argument")
parser.add_argument("-p", "--period", help="today for temperature of day or"
                                        " forecast for the temperature of five next days")
args = parser.parse_args()
#print(args.echo)
if args.period == "today":
    print("meteo du jour :")
    today(display)
elif args.period == "forecast":
    forecast(display)
elif args.period != "today" and args.period != "forecast":
    print("merci d'entrer 'today' pour la meteo du jour ou 'forecast'"
          "pour la meteo des 5 prochains jours")
print(args.period)

"""
display = display.WeatherForecast()
Température des 5 prochains jours :
display.print_forecast()
Température actuelle :
display.print_today_weather()


"""