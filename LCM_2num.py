def gcd(a,b):
    if b==0:
        return a

    return gcd(b,a%b)

def lcm(a,b):
    return a*b//gcd(a,b)


value1 = int(input("Enter the 1st number"))
value2 = int(input("Enter the 2nd number"))

print(lcm(value1,value2))

