import requests


def test():
    payload = {
        'username': 'admin',
        'password': 'Stranger2020_',
    }
    response = requests.post('http://127.0.0.1:8000/api-token-auth/', data=payload)
    result = response.json()
    print(result)
    return result


def test2():
    headers = {
        'Authorization': 'Token 97d414bcf4f1fd0f2be7dd0707b858210798ed34'
    }
    payload = {
        'text': 'Проверка связи'
    }
    response = requests.get('http://127.0.0.1:8000/api/v1/posts/', headers=headers)
    print(response)
    return response


test2()