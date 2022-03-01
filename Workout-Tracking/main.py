import requests
import datetime

APP_KEY = YOUR API KEY
APP_ID = YOUR API ID

headers = {
    "x-app-id":APP_ID,
    "x-app-key":APP_KEY
}
get_data = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise = input("Tell me what you did?: ")
exercise = exercise.lower()
GENDER="Female"
WEIGHT = 50
HEIGHT = 150
AGE = 24

params={
 "query":exercise,
 "gender":GENDER,
 "weight_kg":WEIGHT,
 "height_cm":HEIGHT,
 "age": AGE
}

response = requests.post(url=get_data, json=params, headers=headers)
result = response.json()

today = datetime.datetime.now()

workout_url ="https://api.sheety.co/"API"/workoutRecords/workouts"

for exercise in result["exercises"]:
    data = {
        "workout":{
             "date": today.strftime("%d/%m/%Y"),
             "time": today.time().strftime("%H:%M:%S"),
             "exercise": exercise["name"].title(),
             "duration": exercise["duration_min"],
             "calories": exercise["nf_calories"]
        }
    }
    basic_headers = {"Authorization": "Basic AUTH_KEY"}
    data_add = requests.post(workout_url,json=data,auth=(USERNAME,PASSWORD),headers=basic_headers)
    print(data_add.text)
