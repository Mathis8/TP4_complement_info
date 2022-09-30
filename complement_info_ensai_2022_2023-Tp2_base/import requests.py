import requests

response = requests.get("https://data.rennesmetropole.fr/api/records/1.0/search?dataset=menus-cantines")
print(response.json())