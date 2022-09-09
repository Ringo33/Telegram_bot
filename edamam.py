import os
from googletrans import Translator
import requests
from dotenv import load_dotenv

load_dotenv()

translator = Translator()

KEY = os.getenv('EDAMAM_KEY')
ID = os.getenv('EDAMAM_ID')

def recipe(data):
    query = translator.translate(data, src='ru', dest='en').text
    url = 'https://api.edamam.com/api/recipes/v2'
    payload = {
        'type': 'public',
        'q': query,
        'health': 'alcohol-free',
        'app_id': ID,
        'app_key': KEY
    }
    response = requests.get(url, params=payload).json()['hits'][0]['recipe']
    image = response['images']['REGULAR']['url']
    url_recipe = response['url']
    label = response['label']
    label_ru = translator.translate(label, src='en', dest='ru').text
    ingredient = ', \n- '.join(response['ingredientLines'])
    ingredient_ru = translator.translate(ingredient, src='en', dest='ru').text
    text = f'{label_ru} \n \n' \
           f'Ингредиенты: \n' \
           f'- {ingredient_ru} \n \n' \
           f'{url_recipe}'
    data = {
        'image': image,
        'text': text
    }
    return data
