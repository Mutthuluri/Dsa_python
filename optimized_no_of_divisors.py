import math
def optimized_no_of_divisors(n):
    for i in range(1,int(math.sqrt(n)+1)):
        if n%i == 0:
            if n/i == i:
                print(i)
            else:
                print(i,n/i)


optimized_no_of_divisors(100)