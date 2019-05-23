import requests
import json

API_KEY = '010a04660436d98ab0fdbc8021536d25'
#url = f'http://data.fixer.io/api/latest?access_key={API_KEY}&base=EUR&symbols=USD,AUD,CAD,PLN,MXN&format=1'

url = f'http://data.fixer.io/api/latest? \
    access_key={API_KEY}& \
    base=EUR& \
    symbols=USD& \
    format=1' 

'''
# We could use this with other subscription
url = f'http://data.fixer.io/api/convert? \
    access_key={API_KEY}& \
    from=GBP& \
    to=JPY& \
    amount = 25' 
'''

response = requests.get(url)
data = response.text
parsed = json.loads(data)
print(parsed)
