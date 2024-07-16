def only_odd(n):
    res = 0
    for i in n:
        res = res^i

    return res

n = [10,20,20,10,30,30,30]
print(only_odd(n))