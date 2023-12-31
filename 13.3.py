#Calling a JSON API
#In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py. 
#The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data, 
#and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.


import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Set the API endpoint for the assignment
serviceurl = 'http://py4e-data.dr-chuck.net/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1:
        break

    parms = dict()
    parms['address'] = address
    # Add the required 'key' parameter with the value '42'
    parms['key'] = '42'
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    # Extract and print the place
