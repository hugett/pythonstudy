from time import clock

def timeit(func, *nkwargs, **kwargs):
    start_time = clock()
    retval = func(*nkwargs, **kwargs)
    end_time = clock()
    return (end_time - start_time, retval)

def fact1(N):
    'use reduce'
    return reduce(lambda x, y: x * y, range(1, N + 1))

def fact2(N):
    'use iter'
    ret = 1
    for i in xrange(1, N + 1):
        ret *= i
    return ret

def fact3(N):
    if N == 1:
        return 1
    return N * fact3(N - 1)

print timeit(fact1, 500)
print timeit(fact2, 500)
print timeit(fact3, 500)

