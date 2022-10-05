# import requests
# import time
#
# DOMAIN = 'http://127.0.0.1:8000'
#
#
# def timeout():
#     time.sleep(2)
#
#
# def get_url(url):
#     return f'{DOMAIN}{url}'
#
#
# timeout()
#
# # когда не авторизован (401)
# response = requests.get(get_url('/api/projects/'))
# assert response.status_code == 401
#
# #обычная авторизация базовая
# response = requests.get(get_url('/api/projects/'), auth=('Nikola', '1'))
# assert response.status_code == 200
#
# timeout()
#
# #авторизация через токен
# TOKEN = '070dcb59ba32fe44af7b51dc1ebe33400f5bedc2'
# # response = requests.get(get_url('/api/projects/'), headers={'Authorization': f'Token {TOKEN}'})
# headers = {'Authorization': f'Token {TOKEN}'}
# response = requests.get(get_url('/api/projects/'), headers=headers)
# assert response.status_code == 200
#
# timeout()
#
# # авторизация jwt и получаем токен
# response = requests.post(get_url('/api/token/'), data={'username': 'Nikola', 'password': '1'})
# result = response.json()
# # это токен
# access = result['access']
# print('Первый токен',access,end=f'\n{150*"*"}\n')
# # для рефреша
# refresh = result['refresh']
# print('refresh',refresh,end=f'\n{150*"*"}\n')
# timeout()
# # Авторизуемся с ним
# headers = {'Authorization': f'Bearer {access}'}
# response = requests.get(get_url('/api/projects/'), headers=headers)
# assert response.status_code == 200
#
# timeout()
# # Рефрешим токен ( ДЛЯ ОБНОВЛЕНИЯ)
# response = requests.post(get_url('/api/token/refresh/'), data={'refresh': refresh})
# result = response.json()
# # это наш токен
# access = result['access']
# print('Обновленный токен',access,end=f'\n{150*"*"}\n')
# print('refresh',refresh,end=f'\n{150*"*"}\n')
# timeout()
# # Авторизуемся с ним
# headers = {'Authorization': f'Bearer {access}'}
# response = requests.get(get_url('/api/projects/'), headers=headers)
# assert response.status_code == 200