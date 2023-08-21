import requests

response = requests.get("https://api.example.com/data")
data = response.json()


#This code sends a GET request to an API, receives a response, and parses it as JSON data using the requests library.