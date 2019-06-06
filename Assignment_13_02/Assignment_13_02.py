# The program will prompt for a URL, read the JSON data from that URL
# using urllib and then parse and extract the comment counts from the
# JSON data, compute the sum of the numbers in the file

from urllib.request import urlopen
import ssl
import json

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location : ') # http://py4e-data.dr-chuck.net/comments_206094.json
print(f'Retrieving {url}')
data = urlopen(url, context = ctx).read().decode()
print(f'Retrieved {len(data)} characters')

try:
    js = json.loads(data)
except:
    js = None

if not js:
    print('Failed to Retrieve Data!!')
else:
    comments = js["comments"]
    print(f'Count : {len(comments)}')
    print(f'{sum([comment["count"] for comment in comments])}')
