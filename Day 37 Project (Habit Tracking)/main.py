import requests
from datetime import datetime

USERNAME = "tracymcgravy"
TOKEN = "tracypixelatoken123"
GRAPH_ID = "graph1"


pixela_endpoint = "https://pixe.la/v1/users"

headers = {
    "X-USER-TOKEN": TOKEN
}

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"

}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# POSTING A PIXEL

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2024, month=1, day=7)

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "10",
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_data, headers=headers)
# print(response.text)

# UPDATING A PIXEL

update_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240103"

update_pixel = {
    "quantity": "12"
}

# response = requests.put(url=update_pixel_endpoint, json=update_pixel, headers=headers)
# print(response.text)

# DELETING A PIXEL

delete_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20240107"

response = requests.delete(url=delete_pixel_endpoint, headers=headers)
print(response.text)
