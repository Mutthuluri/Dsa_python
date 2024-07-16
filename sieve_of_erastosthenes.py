def sieve_of_erastosthenes(n):
    Prime = [True for i in range(n+1)]

    p = 2

    while p*p <=n:
        if Prime[p] == True:
            for i in range (p*p,n+1,p):
                Prime[i]=False

        p += 1

    for i in range(2,n+1):
        if Prime[i]==True:
            print(i)

sieve_of_erastosthenes(20)
