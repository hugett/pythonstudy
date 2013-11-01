#An example of reading and writing Unicode strings: Writes
#a Unicode stirng to a file in utf-8 and reads it back in.

CODEC='utf-8'
FILE='unicode.txt'

hello_out = u"Hello world\n"
bytes_out = hello_out.encode(CODEC)
#print bytes_out
f = open(FILE, "w")
f.write(bytes_out)
f.close()

f = open(FILE, "r")
bytes_in = f.read()
f.close()
hello_in = bytes_in.decode(CODEC)
print hello_in
