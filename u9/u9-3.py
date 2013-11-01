import os
filename = raw_input('input the filename: ')
if os.path.isfile(filename):
    f = open(filename, 'r')
    print 'the file has', sum(1 for i in f), 'lines'
    f.close()
else:
    print 'it is not a file'
