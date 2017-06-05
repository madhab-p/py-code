'''
Created on Apr 18, 2017

@author: pneela
'''
import requests

r = requests.get('https://www.interflora.co.uk')
print(r.status_code)

print(type(r.raw))

print("\n".join(dir(r)))