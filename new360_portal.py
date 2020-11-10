import requests
from get_token import response_data
# from get_token import token

url = 'https://new360nddprint.com/api/users/profile'

headers = {
    'Authorization': 'bearer ' + response_data['access_token']
}

user_data = {
    "enterprise": "NomeEmpresa",
    "grant_type": "password",
    "password": "1234567890",
    "username": "administrator"
}

response = requests.get(url=url, json=user_data, headers=headers)

if 200 <= response.status_code <= 299:
    print('p---i Status Code: ', response.status_code)
    print('p---i Reason: ', response.reason)
    print('p---i JSON: ', response.json())
else:
    print('p---e Status Code: ', response.status_code)
    print('p---e Reason: ', response.reason)
    print('p---e Reason: ', response.reason)
    print('p---e Text: ', response.text)
import requests
from get_token import response_data
# from get_token import token

url = 'https://new360nddprint.com/api/users/profile'

headers = {
    'Authorization': 'bearer ' + response_data['access_token']
}

user_data = {
    "enterprise": "NomeEmpresa",
    "grant_type": "password",
    "password": "1234567890",
    "username": "administrator"
}

response = requests.get(url=url, json=user_data, headers=headers)

if 200 <= response.status_code <= 299:
    print('p---i Status Code: ', response.status_code)
    print('p---i Reason: ', response.reason)
    print('p---i JSON: ', response.json())
else:
    print('p---e Status Code: ', response.status_code)
    print('p---e Reason: ', response.reason)
    print('p---e Reason: ', response.reason)
    print('p---e Text: ', response.text)
