import requests
import pytest

def test_status_code():
    token = '8734f8ac8aad06fbc6abf53cd345da39' 
    response = requests.post('https://pokemonbattle.me:9104/pokemons', headers={'trainer_token' : token}, json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
    assert response.status_code == 201


def test_status_code():
    response = requests.get ('https://pokemonbattle.me:9104/trainers', params={'trainer_id' : 3619})
    response_body = response.text 
    assert response_body.json()['name'] == 'Ash28'