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
        'Authorization': 'Token 44b77bb6694dc9e24638e60fe167f2fe753dd304'
    }
    payload = {
        "text": "Проверка 2"
    }
    response = requests.post('http://127.0.0.1:8000/api/v1/posts/', headers=headers, params=payload)
    print(response.text)
    return response


test2()