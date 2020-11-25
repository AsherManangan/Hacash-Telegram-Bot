import json
import requests

address_input = input("Enter your HAC address: ")

url = ("http://8.210.144.170:8083/query?action=balances&address_list="+address_input)
result = requests.get(url)
src = result.text
data = json.loads(src)

print("HAC: ")
print(data['list'][0]['hacash'])
print("BTC: ")
print (data['list'][0]['satoshi'])
print("HACD: ")
print(data['list'][0]['diamond'])

