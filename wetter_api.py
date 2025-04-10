import requests
# Hinweis: Bitte deinen eigenen API-Key hier einfügen.
# Du bekommst ihn kostenlos auf https://openweathermap.org/api
apikey = "füge dein Key hier rein"

def wetter():
    city_name = input("Wie heißt die Stadt? ").capitalize()

    #Ich brauche erstmal die lat und lon daten damit ich sie von der wetter seite abfragen kann
    geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city_name}&limit=1&appid={apikey}"
    geo_res = requests.get(geo_url)
    geo_data = geo_res.json()
    if not geo_data:
        return f"Ich habe keine Stadt mit diesem namen gefunden. "
    else:
        lat = geo_data[0]["lat"]
        lon = geo_data[0]["lon"]
        #Jetzt muss ich die daten in die wetterurl eingeben um die wetter daten zu einem bestimmten ort zu kriegen
        weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&units=metric&appid={apikey}"
        weather_res = requests.get(weather_url)
        weather_data = weather_res.json()
        # Und jetzt muss ich nur noch ausgeben was im request ist also die temp weil die will ich ja
        return f"Die Temperatur in {city_name} Beträgt {weather_data['current']['temp']} C°"


if __name__ == "__main__":
    print(wetter())
