import requests

url = 'https://new360nddprint.com/api/users/profile'




user_data = {
    "enterprise": "NomeEmpresa",
    "grant_type": "password",
    "password": "1234567890",
    "username": "administrator"
}

response = requests.post(url=url, data=user_data)

if 200 <= response.status_code <= 299:
    print('t---i Status Code: ', response.status_code)
    print('t---i Reason: ', response.reason)
    response_data = response.json()

    # with open('token.txt', 'w') as file:
    #     file.write('Bearer ' + str(response_data))
    #     response_bearer = ('Bearer ' + str(response_data))

else:
    print('t---e Status Code: ', response.status_code)
    print('t---e Reason: ', response.reason)
    print('t---e Text: ', response.text)