# The program will use urllib to read the HTML from the data files below,
# and parse the data, extracting numbers and compute the sum of the numbers'
# in the file.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') # http://py4e-data.dr-chuck.net/comments_206091.html
webpage = urlopen(url, context = ctx).read()
soup = BeautifulSoup(webpage, 'html.parser')

spantags = soup('span')

print(sum([int(tag.contents[0]) for tag in spantags]))
