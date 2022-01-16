import requests

r = requests.get('http://127.0.0.1:5001/employee/jun')
print(r.text)

r = requests.post('http://127.0.0.1:5001/employee', data={'name': 'jun'})
print(r.text)

r = requests.put('http://127.0.0.1:5001/employee',
                 data={'name': 'jun', 'new_name': 'hayashi'})
print(r.text)

r = requests.delete('http://127.0.0.1:5001/employee', data={'name': 'jun'})
print(r.text)
