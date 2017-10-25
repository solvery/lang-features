from requests import put, get
put('http://192.168.0.9:5000/todo1', data={'data': 'Remember the milk'}).json
r = get('http://192.168.0.9:5000/todo1').json()
print r
put('http://192.168.0.9:5000/todo2', data={'data': 'Change my breakpads'}).json
r = get('http://192.168.0.9:5000/todo2').json()
print r
