def max2(a, b):
    if a > b:
        return a
    return b

def min2(a, b):
    if a < b:
        return a
    return b

def my_max(seq):
    mx = seq[0]
    for i in seq:
        mx = max2(i, mx)
    return mx

def my_min(seq):
    mi = seq[0]
    for i in seq:
        mi = min2(i, mi)
    return mi
