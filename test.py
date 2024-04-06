import requests
import base64

url = ''
path_photo = ''

print(requests.post(f'{url}/registration', json={'data': {'name': 't1e2st', 'password': 'test', 'contraindications': 'testing, tree ewfw ef wef we f we f'}}).json())

print(requests.post(f'{url}/get', json={'data': {'name': 'te2st', 'password': 'test'}}).json())

print(requests.post(f'{url}/edit', json={'data': {'name': 'te2st', 'password': 'test', 'contraindications': 'сахар'}}).json())

with open(path_photo, 'rb') as f:
    image_bytes = f.read()

image_base64 = base64.b64encode(image_bytes).decode('utf-8')

data = {'data': {'name': 'te2st', 'password': 'test', 'image': image_base64}}

response = requests.post(f'{url}/upload', json=data)

print(response.json())
