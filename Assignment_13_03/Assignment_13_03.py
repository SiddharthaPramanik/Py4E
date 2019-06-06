# The program will prompt for a location, contact a web service and
# retrieve JSON for the web service and parse that data, and retrieve
# the first place_id from the JSON. A place ID is a textual identifier
# that uniquely identifies a place as within Google Maps.

import urllib.request, urllib.parse
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# API info
serviceurl = 'http://py4e-data.dr-chuck.net/json?'
api_key = 42

# Generate the complete URL for API
param = dict()
param["address"] = input('Enter location : ') # Kazan Federal University
param["key"] = api_key
url = serviceurl + urllib.parse.urlencode(param)

# Get data from URL
print(f'Retrieving : {url}')
data = urllib.request.urlopen(url, context = ctx).read().decode()
print(f'Retrieved {len(data)} characters')

# Retrieve required data from JSON
try:
    js = json.loads(data)
except:
    js = None

if not js or 'status' not in js or js['status'] != 'OK':
    print('Unable to retrieve data')
else:
    # print(json.dumps(js, indent = 4))
    print(f'Place Id {js["results"][0]["place_id"]}')
