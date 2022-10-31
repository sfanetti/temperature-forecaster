import pprint
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
    return lambda x,pos: datetime.fromisoformat(get_dates(x)).strftime("%b %d %H:%M")



def main():
    print("Weather forecaster")
    city= str(input("What city do you want weather for? "))
    API_KEY = config["API_KEY"]
    API_URL = f"https://api.openweathermap.org/data/2.5/forecast?appid={API_KEY}&q={city}"
    r = requests.get(API_URL)
    response = r.json()
    pp = pprint.PrettyPrinter(indent=4)
    forecast_list = response["list"]

    today = datetime.now().strftime("%b-%d-%Y")

    dates = []
    wind_speeds = []
    temps = []
    days = set()
    for forecast in forecast_list:
        dt = forecast['dt_txt']
        days.add(datetime.fromisoformat(forecast['dt_txt']).strftime("%b/%d/%Y"))
        wind_speed = to_mph(forecast['wind']["speed"])
        temp = to_fahrenheit(forecast["main"]["feels_like"])
        temps.append(temp)
        pp.pprint(forecast["main"])
        dates.append(dt)
        wind_speeds.append(wind_speed)

    plt.title(f"The 5 day forecast for {city}")
    plt.plot(dates, temps, label="Temperature")
    plt.xlabel("Dates")
    plt.ylabel("Temperature in Fahrenheit")

    ax = plt.gca()
    ax.xaxis.set_major_formatter(formatter(dates))

    plt.tick_params(axis="x", labelrotation=90 )
    plt.show()

if __name__ == '__main__':
    main()