#�����ļ������зǿհ��ַ�����Ŀ
f = file('../abc.txt', 'r')
print sum(len(word) for line in f for word in line.split())
