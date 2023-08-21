import requests
from requests.auth import HTTPBasicAuth

###### API BACKENDS for test
# https://httpbin.org
# https://designer.mocky.io/
# https://www.mockable.io/
# https://jsonplaceholder.typicode.com/
# https://beeceptor.com/
# https://mockapi.io/
# https://quickmocker.com/


###### Simple get and how to read response
print('\n\n 1) Simple get and how to read response')
response = requests.get("http://api.open-notify.org/astros.json")
print(response)
print('\n\n 1.1) Response Status Code')
print(response.status_code)
# print(response.content)
# print(response.text)
print('\n\n 1.2) Response body')
print(response.json())
print('\n\n 1.3) Response Headers')
print(response.headers)

##
# print('\n\n 1.4) Different call methods')
# response = requests.get('http://api.open-notify.org/astros.json', max_redirects=2)          # Limit redirects
# response = requests.get('http://api.open-notify.org/astros.json', allow_redirects=False)    # Block redirects
# response = requests.get('http://api.open-notify.org/astros.json', timeout=0.01)             # Set timeout (raises exceptions.Timeout)
# response = requests.get('http://httpbin.org/headers',                                       # Passing custom headers
#               headers={'Authorization' : 'Bearer {access_token}'}
#            )


###### Using a query string
print('\n\n 2) Using a query string')
query = {'lat':'45', 'lon':'180'}
response = requests.get('http://api.open-notify.org/iss-pass.json', params=query)
print(response.json())


###### Other HTTP Verbs
print('\n\n 3) Other Verbs')
print('\n\n 3.1) Post')
response = requests.post('https://httpbin.org/anything', data = {'key':'value'})
print(response.status_code)
print(response.json())
print('\n\n 3.2) Put')
response = requests.put('https://httpbin.org/anything', data = {'key':'value'})
print(response.status_code)
print(response.json())
print('\n\n 3.3) Delete')
response = requests.delete('https://httpbin.org/anything', data = {'key':'value'})
print(response.status_code)
print(response.json())


###### Error Handling
print('\n\n 4) Error Handling')
print('\n\n 4.1) Via Response Code')
response = requests.get("http://api.open-notify.org/astros-wrong.json")
if (response.status_code == 200):
    print("The request was a success!")
    # Code here will only run if the request is successful
elif (response.status_code == 404):
    print("Result not found!")
    # Code here will react to failed requests
print('\n\n 4.2) Via Try-Except')
try:
    response = requests.get('http://api.open-notify.org/astros-wrong.json')
    response.raise_for_status()
    # Additional code will only run if the request is successful
except requests.exceptions.HTTPError as error:
    print(error)
    # This code will run if there is a 404 error.
print('\n\n 4.3) All Problems')
try:
    response = requests.get('http://api.open-notify.org/astros.json', timeout=5)
    response.raise_for_status()
    # Code here will only run if the request is successful
except requests.exceptions.HTTPError as errh:
    print(errh)
except requests.exceptions.ConnectionError as errc:
    print(errc)
except requests.exceptions.Timeout as errt:
    print(errt)
except requests.exceptions.RequestException as err:
    print(err)


###### Authentication
print('\n\n 5) Authentication')
print('\n\n 5.1) Basic Auth')
# response = requests.get('https://api.github.com/user', auth=HTTPBasicAuth('username', 'password'))
# print(response)
# print(response.text)
# print(response.status_code)
# print(response.json())

payload={'password' : 'zero', 'email' : 'admin@fauna.life'}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    # Pass Authentication Token
    # 'Cookie': 'fl-auth-token=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2VtYWlsIjoiYWRtaW5AZmF1bmEubGlmZSIsInVzZXJfZmx1aWQiOiIweDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAwMDAiLCJpYXQiOjE2NDMwMjQ4NjYsImV4cCI6MTY0MzAzMjA2Nn0.OWOz50H8nn-Qw3D5KgtmG7-lBgp3CD__yBj0IlwMZSY'
}

# response = requests.request("POST", url, headers=headers, data=payload)
# response = requests.post('http://localhost:8088/user/login', headers=headers, data = payload)
response = requests.post('http://localhost:8088/user/login', data = payload)
print(response.text)
print(response.headers)