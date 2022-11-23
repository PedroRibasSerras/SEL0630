from requests import get
import json
from pprint import pprint



URL = 'http://apex.oracle.com/pls/apex/raspberrypi/weatherstation/getlatestmeasurements/966583'

weather = get(URL).json()['items']
pprint(weather)

string = ''

info = weather[0]['updated_by']
string += str(info) + '\n'
pprint(info)

info = weather[0]['updated_on']
string += str(info) + '\n'
pprint(info)

info = weather[0]['ambient_temp']
string += str(info) + '\n'
pprint(info)

info = weather[0]['humidity']
string += str(info) + '\n'
pprint(info)


print(string)