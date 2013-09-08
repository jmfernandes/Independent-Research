import urllib
import ast
import json

class Number(object):
    def __init__(self):
        self.aquire = urllib.urlopen("http://www.prices.datanab.net/us/gasoline_json")
        self.unpacked = self.aquire.read()
#       self.data = ast.literal_eval(self.unpacked)
        self.data = json.loads(self.unpacked)

number = Number()
print number.data
print type(number.data)

dict = {
    "value": 3.492,
    "units": "dollars/gallon",
    "name": "Average Price of Gasoline in United States",
    "citation": "http://www.eia.gov/petroleum/gasdiesel/"
    }
data =json.dumps(dict)
print data
print type(dict)
#print type(numbers())
#hey = {"whoo":4}
#yo = json.dumps(hey)
#print type(yo)



exit()
import requests
import json
# api_user and api_pw not printed here for security reasons
r = requests.get('http://constants.herokuapp.com/physics/planck_constant', auth=('user', 'pass'))
r.status_code, "code"
r.headers['content-type'], "headers"
r.encoding, "encoding"
hey = r.text, "text"
json.dumps(hey)
print hey, "text"
print r.json, "json"
#print r.json["value"]
exit()

status = r.status_code # Produces 200 every time
rawdata = r.read()
print rawdata


exit()
import json
import urllib
aquire = urllib.urlopen("http://constants.herokuapp.com/physics/planck_constant")
unpacked = aquire.read()
print unpacked
data = json.loads(unpacked)
print data
#print data['citation']
print data['name']
#print data['value']
#print data['units']

#print data



exit()
import urllib
import os

f = urllib.urlopen("http://plancksconstant.herokuapp.com")
s = f.read()
f.close()
t = float(s)
#print t

dict = {'value': 5, 'units': 'meters', 'citation': 'wikipedia'};

print dict['value']
print dict['units']
print dict['citation']

import json
data = json.dumps(dict)

print data

enddata = json.loads(data)
print enddata['value'], "the end"