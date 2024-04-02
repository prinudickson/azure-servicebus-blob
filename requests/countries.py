import requests
from icecream import ic

base_url = 'https://api.countrylayer.com/v2/'

r = requests.get(base_url + 'all')

ic(r.text)