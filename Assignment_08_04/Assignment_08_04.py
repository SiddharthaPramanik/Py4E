fname = input('Enter the file name : ') #'romeo.txt'
fhandle = open(fname)

words = list()

for line in fhandle:
    pieces = line.split()
    for word in pieces:
        if word in words:
            continue
        words.append(word)

words.sort()
print(words)
