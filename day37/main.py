import requests
import os
from dotenv import load_dotenv
from datetime import datetime as dt

load_dotenv()
USERNAME = os.environ.get("PIXELA_USERNAME")
PIXELA_USR_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"
TODAY = dt.now().strftime("%Y%m%d")

# Create a user
create_user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}
# user = requests.post(url=PIXELA_USR_ENDPOINT, json=create_user_params)

# Create a graph
create_graph_params = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}
# graph = requests.post(url=f"{PIXELA_USR_ENDPOINT}/{USERNAME}/graphs",
#                       json=create_graph_params,
#                       headers=headers)

# Create a pixel on graph
create_pixel_params = {
    "date": TODAY,
    "quantity": "10.0"
}
# pixel = requests.post(url=f"{PIXELA_USR_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}",
#                       json=create_pixel_params,
#                       headers=headers)

# Update a pixel on graph
update_pixel_params = {
    "quantity": "20.0"
}
# pixel = requests.put(url=f"{PIXELA_USR_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}",
#                      json=update_pixel_params,
#                      headers=headers)

# Delete a pixel on graph
# pixel = requests.delete(url=f"{PIXELA_USR_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}",
#                         headers=headers)
