def power(x,y):
    if y == 0 :
        return 1
    temp = power(x,y//2)
    if y %2 == 0:
        return temp * temp
    else:
        return temp * temp * x


print(power(3,20))
