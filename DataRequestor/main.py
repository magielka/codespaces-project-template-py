from time import sleep
#from snap7.server import mainloop
import requests

res = requests.get("https://api.openaq.org/v2/locations/2178")

#https://docs.openaq.org/docs/getting-started

while (True):
    print('Test')
    sleep(2)



