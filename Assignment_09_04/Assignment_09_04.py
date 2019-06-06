fname = 'mbox-short.txt' #input('Please enter the filename : ') #'mbox-short.txt'
fhandle = open(fname)

senderdict = dict()

for line in fhandle:
    if not line.startswith('From '):
        continue
    sender = line.split()
    senderdict[sender[1]] = senderdict.get(sender[1], 0) +1

topsender = None
topcount = 0
for sender, count in senderdict.items():
    if topsender == None or count > topcount:
        topsender = sender
        topcount = count

print(topsender, topcount)