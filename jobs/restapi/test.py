#test the API

import requests

resp = requests.get('http://127.0.0.1:5000/user/Elvin')

print(resp.status_code)
print(resp.headers['content-type'])
print(resp.encoding)
print(resp.json)
print(resp.text)

if resp.status_code != 200:
    #this means something went wrong
    raise ApiError('GET {}'.format(resp.status_code))
#for item in resp.json:
#    print('{} {}'.format(item['name'],item['age'],item['occupation']))

#resp = requests.get('')

#if resp.status_code != 200:
#    #this means something went wrong
#    raise.ApiError()
#for item in resp.json:
#    print()

