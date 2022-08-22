import os
import requests
from dotenv import load_dotenv
import pprint

load_dotenv()

token = os.getenv('Token')


def vk_status(data):
    payload = {
        'owner_id': str(data),
        'count': 1,
        'access_token': token,
        'v': '5.131'
    }
    response = requests.post('https://api.vk.com/method/wall.get', data=payload)
    text = response.json()['response']['items'][0]['text']
    image = response.json()['response']['items'][0]['attachments'][0]['photo']['sizes'][4]['url']
    data = {
        'text': text,
        'image': image
    }
    return data

# pprint.pprint(vk_status(-14785431))
