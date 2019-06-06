fname = 'mbox-short.txt'#input('Enter File name : ')
fhandle = open(fname)

hdict = dict()

for line in fhandle:
    if not line.startswith('From '):
        continue
    epos = line.find(':')
    spos = epos - 2
    hour = line[spos:epos]
    hdict[hour] = hdict.get(hour,0) + 1

# hlist = sorted([(k,v) for k,v in hdict.items()])

hlist = sorted(hdict.items())

for k,v in hlist:
    print(k,v)

