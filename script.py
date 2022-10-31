import pprint
import time
import requests
from matplotlib import pyplot as plt
from datetime import datetime
from dotenv import dotenv_values 

config = dotenv_values(".env")

def to_fahrenheit(K):
    return round((float(K) - 273.15)* 1.8000+ 32.00)

def to_celcius(K):
    return round(float(K) - 273.15)

def to_mph(kph):
    return float(kph) * 0.62137119

def formatter(dates):
    def get_dates(x):
        try:
            return dates[int(x)]
        except:
            return ""
    def fmt(x):
        dt = datetime.fromisoformat(get_dates(x))
        if dt.hour == 0 or x == 0 or x == len(dates) - 1:
            return dt.strftime("%b %d %#I %p")
        else:
            return dt.strftime("%#I %p")
    return lambda x,pos: fmt(x)

def get_city_weather(city):
    pp = pprint.PrettyPrinter(indent=4)

    API_KEY = config["API_KEY"]
    API_URL = f"https://api.openweathermap.org/data/2.5/forecast?appid={API_KEY}&q={city}"

    r = requests.get(API_URL)
    response = r.json()
    pp.pprint(response)

    forecast_list = response["list"]

    dates = []
    temps = []

    for forecast in forecast_list:
        dt = forecast['dt_txt']
        temp = to_fahrenheit(forecast["main"]["feels_like"])
        temps.append(temp)
        dates.append(dt)

    plt.title(f"The 5 day forecast for {city}")
    plt.plot(dates, temps)
    plt.xlabel("Dates")
    plt.ylabel("Temperature in Fahrenheit")

    ax = plt.gca()
    ax.xaxis.set_major_formatter(formatter(dates))

    plt.tick_params(axis="x", labelrotation=90 )
    plt.show()

def main():
    print("Weather forecaster")
    city = str(input("For what region do you want weather? "))
    if city.upper() == "NONE":
        exit()
    try:
        get_city_weather(city)
    except:
        print("Sorry we could not find that region")
        time.sleep(2)
        main()  

if __name__ == '__main__':
    main()