import requests


def post_token(enterprise='n5_tes66', grant_type='password', username='admin  ', password='*****'):
    user_data = {
        "enterprise": enterprise,
        "grant_type": grant_type,
        "password": password,
        "username": username
    }

    response = requests.post(url='https://360.nddprint.com/token', data=user_data)
    return response.json()['access_token']
