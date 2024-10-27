import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '06b763c7a40aad2e654421cbb4ef066d'
HEADER = {'content-type' : 'application/json', 'trainer_token': TOKEN}
TRAINER_ID = '7523'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params = {'trainer_id': TRAINER_ID})
    assert response.status_code == 200 