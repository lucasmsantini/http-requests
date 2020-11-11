import requests
from post_token import post_token
from altera_politica import altera_politica


def put_token(enterprise="N5_TES66", grant_type="password", password="*****", username="admin"):
    print('Token de acesso: ', post_token())

    headers = {'Authorization': 'bearer ' + post_token()}

    access_data = {
        "enterprise": enterprise,
        "grant_type": grant_type,
        "password": password,
        "username": username
    }
    response = requests.get(url='https://360.nddprint.com/api/users/profile', json=access_data, headers=headers)
    print(altera_politica())
    print('Status Code final: ', response.status_code)


put_token()
