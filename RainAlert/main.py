import requests
import smtplib

api_key = YOUR API KEY
Endpoint = "https://api.openweathermap.org/data/2.5/onecall"

my_email = YOUR EMAIL
password = YOUR EMAIL PASSWORD

parameters = {
    "lat":46.064941,
    "lon":13.230720,
    "appid": api_key,
    "exclude":"current,minutely,daily"
}
# getting weather data
response = requests.get(url=Endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()

# extracting next 12 hours weather data
next_12_hours= weather_data["hourly"][0:12]

will_rain = False

# returns True if there weather id is less than 700 (means it is going to rain)
for hour in range(0,12):
    if next_12_hours[hour]["weather"][0]["id"] < 700:
        will_rain = True

# if True, sends email for rain alert
if will_rain:
    print("Bring an umbrella")
    # smtp is set for gmail accounts
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()  # securing connection
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs=EMAIL TO SEND,
                            msg=f"Subject:Weather Alert!\n\n Bring an umbrella!")
