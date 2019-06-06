fname = input('Please enter the filename : ') #mbox-short.txt
fhandle = open(fname)

count = 0
total = 0

for line in fhandle:
    if not line.startswith('X-DSPAM-Confidence:'):
        continue
    count = count + 1
    npos = line.find(' ')
    num = float(line[npos + 1:])
    total = total + num

average = total/count
print('Average spam confidence:', average)
