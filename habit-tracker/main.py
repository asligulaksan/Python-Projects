import requests
import datetime


pixela_end = "https://pixe.la/v1/users"
USERNAME = YOUR USERNAME
TOKEN = YOUR TOKEN

user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}
#response = requests.post(url=pixela_end,json=user_params)
#print(response.text)

graph_end= f"{pixela_end}/{USERNAME}/graphs"

GRAPH_ID ="howmanypages1"
graph_params = {
    "id": GRAPH_ID,
    "name":"Reading Page",
    "unit": "Pages",
    "type": "int",
    "color": "momiji"
}
headers ={
    "X-USER-TOKEN": TOKEN}

#response_graph = requests.post(url=graph_end,json=graph_params,headers=headers)
#print(response_graph.text)

pixel_end= f"{graph_end}/{GRAPH_ID}"
today = datetime.datetime.now()

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity":input("how many pages did you read?"),
}
#response_pixel = requests.post(url=pixel_end,json=pixel_params,headers=headers)
#print(response_pixel.text)

update_end= f"{graph_end}/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
update_data = {
    "quantity":"40"
}
#uptade_response = requests.put(url=update_end,json=update_data, headers=headers)
#print(uptade_response.text)

delete_end= f"{graph_end}/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
#delete_rep = requests.delete(url=delete_end,headers=headers)
#print(delete_rep.text)