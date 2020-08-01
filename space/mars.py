import requests
from random import choice

rover_url = 'https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos'

def get_mars_photo_url(sol, api_key='DEMO_KEY'):
    params = { 'sol': sol, 'api_key': api_key }
    response = requests.get(rover_url, params)
    response_dictionary = response.json()
    photos = response_dictionary['photos']

    return choice(photos)['img_src']
