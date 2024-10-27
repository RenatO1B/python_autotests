import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '06b763c7a40aad2e654421cbb4ef066d'
HEADER = {'content-type' : 'application/json', 'trainer_token': TOKEN}

body_confirmation = {
    "trainer_token": TOKEN
}

body_crate = {
   "name": "Бульбазавар",
    "photo_id": 445
 }

body_knockout = {
        "pokemon_id": "73926"
}

body_newname = {
    "pokemon_id": "80379",
    "name": "Бульбазавар 2",
    "photo_id": 444
}

body_pokeboll = {
    "pokemon_id": "73927"
}

'''response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_crate)
print(response_create.text)'''

'''response_create = requests.post(url = f'{URL}/pokemons/knockout', headers = HEADER, json = body_knockout)
print(response_create.text)'''

response_create = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_pokeboll)
print(response_create.text)

message = response_create.json()['message']
print(message)