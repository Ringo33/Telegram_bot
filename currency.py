import requests


def currency_rate():
    url = 'https://cdn.cur.su/api/cbr.json'
    usd = round(requests.get(url).json().get('rates').get('RUB'), 2)
    euro = round((1 / requests.get(url).json().get('rates').get('EUR')) * usd, 2)
    # data = {
    #     'USD': f'Курс USD = {usd} руб.',
    #     'EURO': f'Курс EURO = {euro} руб.'
    # }
    data = f'Курс USD = {usd} руб. \n' \
           f'Курс EURO = {euro} руб.'
    return data

def cryptocurrency_rate():
    url = 'https://api.coingecko.com/api/v3/simple/price'
    btc = requests.get(f'{url}?ids=bitcoin'
                       f'&vs_currencies=usd').json()['bitcoin']['usd']
    eth = requests.get(f'{url}?ids=ethereum'
                       f'&vs_currencies=usd').json()['ethereum']['usd']
    rvn = requests.get(f'{url}?ids=ravencoin'
                       f'&vs_currencies=usd').json()['ravencoin']['usd']
    etc = requests.get(f'{url}?ids=ethereum-classic'
                       f'&vs_currencies=usd').json()['ethereum-classic']['usd']
    doge = requests.get(f'{url}?ids=dogecoin'
                        f'&vs_currencies=usd').json()['dogecoin']['usd']

    data = f'Курс BTC = {btc} USD \n' \
           f'Курс ETH = {eth} USD \n' \
           f'Курс RVN = {rvn} USD \n' \
           f'Курс ETC = {etc} USD \n' \
           f'Курс DOGE = {doge} USD'
    return data

print(cryptocurrency_rate())

print(currency_rate())