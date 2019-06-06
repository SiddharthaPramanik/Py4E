# The program will use urllib to read the HTML from the data files below,
# extract the href= vaues from the anchor tags, scan for a tag that is in
# a particular position relative to the first name in the list, follow that
# link and repeat the process a number of times and report the last name
# you find.

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ') # http://py4e-data.dr-chuck.net/known_by_Harper.html
count = int(input('Enter count: '))
position = int(input('Enter position: ')) - 1
lastname = str()

for i in range(count):
    print(f'Retrieving: {url}')
    webpage = urlopen(url, context = ctx).read()
    soup = BeautifulSoup(webpage, 'html.parser')
    anchortags = soup('a')

    url, lastname = [(tag.get('href', None), tag.contents[0]) for tag in anchortags][position]

print(f'Last name is: {lastname}')
