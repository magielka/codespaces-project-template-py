from time import sleep
#from snap7.server import mainloop
import requests

res = requests.get("https://api.openaq.org/v2/locations/2178", headers={"X-API-Key": "e67ea0ea28016a462c9b5dc7a351b9f0f24c318c140f3c8d0c6800b31b038bbe"})
import requests

url = "https://api.openaq.org/v2/locations?limit=100&page=1&offset=0&sort=desc&radius=1000&country=PL&city=Wroc%C5%82aw&order_by=lastUpdated&dump_raw=false"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)

url = "https://api.openaq.org/v2/sources?limit=100&page=1&offset=0&sort=asc&order_by=sourceName"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)


#https://docs.openaq.org/docs/getting-started

while (True):
    print('Test')
    sleep(2)



