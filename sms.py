import os
import requests
from dotenv import load_dotenv

load_dotenv()

password = os.getenv('password')
email = os.getenv('email')
phone = os.getenv('phone')


def sms_sender(message):
    url = 'http://api.sms-prosto.ru/?method=push_msg'
    payload = {
        'email': f'{email}',
        'password': f'{password}',
        'text': message,
        'phone': f'{phone}',
        'sender_name': 'Igrushki_1'
    }
    response = requests.post(url, data=payload)
    print(response.text)
    return response
