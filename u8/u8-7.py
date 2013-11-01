def isperfect(num):
    if sum(x for x in range(1, num / 2 + 1) if num % x == 0) == num:
        return True
    else:
        return False

def func(num):
    return [x for x in range(1, num / 2 + 1) if num % x == 0]

for i in range(1, 1000):
    if isperfect(i):
        print i,func(i)
