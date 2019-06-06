# The program will prompt for a URL, read the XML data from that URL
# using urllib and then parse and extract the comment counts from the
# XML data, compute the sum of the numbers in the file.

from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location : ') # http://py4e-data.dr-chuck.net/comments_206093.xml
print(f'Retrieving : {url}')
webpage = urlopen(url, context = ctx).read()
print(f'Retrieved {len(webpage)} characters')
tree = ET.fromstring(webpage)
counts = tree.findall('.//count')

print(f'Count : {len(counts)}')
print(f'sum : {sum([int(count.text) for count in counts])}')
