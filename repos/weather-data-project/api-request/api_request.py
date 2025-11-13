import requests

api_url = "http://api.weatherstack.com/current?access_key=c1daaa12bdc16b18874f986cd03dffb6&query=New York"

def fetch_data():
    response = requests.get(api_url)
    print(response.json())

fetch_data()