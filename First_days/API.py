import re
from urllib import response
from matplotlib.pyplot import get
import requests
import json

# response = requests.get('http://api.open-notify.org/iss-now.json')

# # raise status incase you fuck something up
# response.raise_for_status()
# print(response)

# print(response.json())

# data = response.json()
# longitude = data['iss_position']['longitude']
# print(longitude)

# parameters = {
#     'lat': -35.675148,
#     'lng': -71.542969,
#     'formatted': 0
# }
# response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
# response.raise_for_status()

# sunrise = response.json()['results']['sunrise']
# sunset = response.json()['results']['sunset']
# print(sunrise.split('T')[1], sunset.split('T')[1])

payloads = {'name': 'Joseph', 'ID': '123'}
r = requests.get('http://httpbin.org/get', params=payloads)
r.raise_for_status()
print(r.json())

#post request
r_post = requests.post('http://httpbin.org/post', params=payloads)
