import json
from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurrencies/quote?format=json") as response:
    source = response.read()

data = json.loads(source)
# print(data)
# data_dent = json.dumps(data, indent=2)
# print(data_dent)
result = {}
for resource in data['list']['resources']:
    name = resource['resource']['fields']['name']
    price = resource['resource']['fields']['price']
    result[name] = price
    # print(resource)
print(result)
