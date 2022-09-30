import requests
from business_object.attack import AttackFactory

response = requests.get("http://web-services.domensai.ecole/attack/4")
print(response.json())

def get_attack(entier) :
    url = "http://web-services.domensai.ecole/attack"
    response = requests.get(url + str(entier)).json()
    type_attack = response["attack_type"]
    power = response["power"]
    name = response["name"]
    description = response["description"]
    return AttackFactory(type_attack, power, name, description )
    
    
    
    