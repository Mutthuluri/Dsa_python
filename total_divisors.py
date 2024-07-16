def printDivisors(n):
    for i in range(1, n + 1):
        if n % i == 0:

            print(i)


printDivisors(100)