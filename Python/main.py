import requests

token = '8734f8ac8aad06fbc6abf53cd345da39' # Твой токен
url = 'https://pokemonbattle.me:9104'   # Базовый урл

responce_add_pokemon = requests.post (f'{url}/pokemons', headers={'trainer_token' : token}, json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(responce_add_pokemon.text)


change = requests.put (f'{url}/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": "9143",
    "name": "vaszw",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print(change.text)

add_pokeboll = requests.post (f'{url}/trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": "9143"
})
print(add_pokeboll.text)