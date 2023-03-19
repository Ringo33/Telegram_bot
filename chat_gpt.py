import os
from pprint import pprint
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests

# token = os.getenv('CHAT_GPT_KEY')
openai.api_key = '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'

def chat_gpt(data):
    output = openai.ChatCompletion.create(
        model = 'gpt-3.5-turbo',
        messages = [
            {
                "role": "user",
                "content": f"{data}"
            }
        ]
    )
    data = {
        'text': output.choices[0]['message']['content']
    }

    return data

# pprint(chat_gpt())