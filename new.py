import pprint

import requests


def test():
    payload = {
        'username': 'admin',
        'password': 'Stranger2020_',
    }
    response = requests.post('http://127.0.0.1:8000/api/v1/api-token-auth/', data=payload)
    result = response.json()
    print(result)
    return result


def test2():
    headers = {
        'Authorization': 'Token 80c65edde52d43a8ab260c261a7e41917860f814'
        # 'Authorization': 'Token d0b6e0e65976a1090dac7ca71882d3698aa8adfe'
        # 'Authorization': 'Token 44b77bb6694dc9e24638e60fe167f2fe753dd304'

    }
    payload = {
        "text": "re-re тест",
        "category": "2",
        "slug": "sup-harcho1",
        "title": "Суп-харчо1"
    }
    response = requests.patch('http://127.0.0.1:8000/api/v1/posts/93/comments/64/', headers=headers, data=payload)

    # for i in range(len(response)):
    #     print(response[i])
    # return response
    pprint.pprint(response.text)

test2()