import re

fname = 'regex_sum_206089.txt' #input('Enter the file name')
fhandle = open(fname)

print(sum([int(num) for num in re.findall('[0-9]+', fhandle.read())]))