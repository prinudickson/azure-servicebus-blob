import requests
from icecream import ic

# ##GET
# #1
# response = requests.get('https://eovoqeb8t1z4rqw.m.pipedream.net')

# #2
# response = requests.get('https://reqres.in/api/users/2')

# text_data = response.text
# json_data = response.json()

# ic(text_data)
# ic(json_data)

# #3 - params in the url
# response = requests.get('https://eovoqeb8t1z4rqw.m.pipedream.net?key1=val1&key2=val2')

# #4 - params arguement
# payload = {'key1': 'val1', 'key2': 'val2'}
# response = requests.get('https://eovoqeb8t1z4rqw.m.pipedream.net', params=payload)

# #5 - headers arguement
# headers = {'token-x': 'Bearer 76768768687686uhgjhg7576575765765765765765123123'}
# response = requests.get('https://eovoqeb8t1z4rqw.m.pipedream.net', headers=headers)

# ##POST
# #6 
# response = requests.post('https://eovoqeb8t1z4rqw.m.pipedream.net')

# ##DELETE
# #7
# response = requests.delete('https://eovoqeb8t1z4rqw.m.pipedream.net')

# ##PUT
# #8 
# response = requests.put('https://eovoqeb8t1z4rqw.m.pipedream.net')

# ##PATCH
# #9
# response = requests.patch('https://eovoqeb8t1z4rqw.m.pipedream.net')

# ##POST
# #10 - POST JSON
# data = {
#     "name": "mmm2223",
#     "job": "lallaalal"
# }
# response = requests.post('https://reqres.in/api/users', json=data)

# ic(response)
# ic(response.json())

# #11 - POST FORMDATA
# data = {
#     "name": "mmm2223",
#     "job": "lallaalal"
# }
# response = requests.post('https://httpbin.org/post', data=data)

# ic(response)
# ic(response.json())

# #12 - POST IMAGE
# #files = {'file' : open('cat.jpeg', 'rb')}
# files = {'file' : ('cat.jpeg',open('cat.jpeg', 'rb'),'image/jpeg')}
# response = requests.post('https://eovoqeb8t1z4rqw.m.pipedream.net', files=files)

# #13 - SAVE IMAGE

# response = requests.get('https://httpbin.org/image/jpeg')
# ic(response.headers)

# with open('image.jpg', 'wb') as fd:
#     for chunk in response.iter_content(chunk_size=500):
#         fd.write(chunk)

# #14 - Exceptions

# response = requests.get('https://httpbin.org/status/200')

# try:
#     response.raise_for_status()
# except requests.exceptions.HTTPError:
#     ic("EROOR ERRROORR ERRROOORRR")

# ic(response)

#15 - Auth Basic

from requests.auth import HTTPBasicAuth

response = requests.get('https://httpbin.org/basic-auth/user/passwd', auth=HTTPBasicAuth('user', 'passwd'))
ic(response)