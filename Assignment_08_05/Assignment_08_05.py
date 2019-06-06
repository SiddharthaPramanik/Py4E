fname = 'mbox-short.txt' #input('Enter the file name : ') 
fhandle = open(fname)

count = 0

for line in fhandle:
    if not line.startswith('From '):
        continue
    llist = line.split()
    print(llist[1])
    count = count + 1

print("There were", count, "lines in the file with From as the first word")