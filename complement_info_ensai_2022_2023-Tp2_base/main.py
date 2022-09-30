if __name__ == "__main__" :
    import requests
    from business_object.attack.attack_factory import AttackFactory

#response = requests.get("http://web-services.domensai.ecole/attack/4")
#print(response.json())

    def get_attack(entier) :
        url = "http://web-services.domensai.ecole/attack/"
        response = requests.get(url + str(entier)).json()
        print(response)
        type_attack = response["attack_type"]
        power = response["power"]
        name = response["name"]
        description = response["description"]
        return AttackFactory.instantiate_attack(type = type_attack,power = power, name = name, description =description )

    a= get_attack(3)
    print("end")