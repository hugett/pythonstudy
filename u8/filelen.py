#计算文件中所有非空白字符的数目
f = file('../abc.txt', 'r')
print sum(len(word) for line in f for word in line.split())
