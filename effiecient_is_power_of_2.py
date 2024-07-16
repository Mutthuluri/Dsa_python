def eff_powof2(n):
    if n == 0:
        return False
    return (n&(n-1)==0)

n = int(input("Enter a number: "))
print(eff_powof2(n))