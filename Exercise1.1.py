import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
import json

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


counts = list()

while True:
    #address = http://py4e-data.dr-chuck.net/comments_766658.json
    address = input('Enter location: ')
    if len(address) < 1 : break
    
    print('Retrieving', address)
    connection=urllib.request.urlopen(address, context=ctx)
    
    data = connection.read()
    print('Retrieved', len(data), 'characters')
    print("==============================")
    print(data.decode())
    print("==============================")
    try: js = json.loads(data)
    except: js = None
    comments = js['comments']
    for comment in comments:
        counts.append(comment['count'])
    print ('Count', len(comments))
    print ('Sum', sum(counts))
