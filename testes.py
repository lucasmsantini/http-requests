import requests

payload = {'page': 2, 'cont': 25}
payload2 = {'username': 'corey', 'password': 'testing'}
r = requests.post('https://httpbin.org/post', data=payload2)
s = requests.get('https://httpbin.org/get', params=payload)
t = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('corey', 'testing'))
u = requests.get('https://httpbin.org/basic-auth/corey/testing', auth=('coreyereererer', 'testing'))
v = requests.post
print(s.url)
print('-------------------------------------------------------------')
print(r.text)
print('-------------------------------------------------------------')
r_dict = r.json()
print(r_dict['form'])
print('origin-------------------------------------------------------------')
print(r_dict['origin'])
print('-------------------------------------------------------------')
print(t.text)
print('-------------------------------------------------------------')
print(u.text)
print('-------------------------------------------------------------')
print(u.status_code)
print(u.content)