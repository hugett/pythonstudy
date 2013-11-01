f = open(r'e:\python\abc.txt', 'r')
for line in f:
    line = line.strip()
    if len(line)==0 or line[0] != '#':
        print line
f.close()
