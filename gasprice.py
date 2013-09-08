import urllib
import ast
aquire = urllib.urlopen("http://www.prices.datanab.net/us/gasoline_json")
unpacked = aquire.read()
data = ast.literal_eval(unpacked)
#print data
#print data['citation']
#print data['name']
print data['value']
miles = 15
price = data['value']*miles
print price