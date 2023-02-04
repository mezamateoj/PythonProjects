import re
from urllib import response
from matplotlib.pyplot import get
import requests
import json

payloads = {'name': 'Joseph', 'ID': '123'}
r = requests.get('http://httpbin.org/get', params=payloads)
r.raise_for_status()
print(r.json())

#post request
r_post = requests.post('http://httpbin.org/post', params=payloads)
