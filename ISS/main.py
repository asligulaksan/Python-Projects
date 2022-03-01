import requests
MY_LAT = 40.773075
MY_LNG =30.394817
import time
from datetime import datetime

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted":0 #24 hour time (1-> 12 hour time)
}

response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise.split("T"))
print(sunset.split("T"))

time_now = datetime.now()

print(time_now)