def optimized_gcd(a,b):
    if b == 0:
        return a

    return optimized_gcd(b,a%b)

value1 = int(input("Enter first number: "))
value2 = int(input("Enter second number: "))
print(optimized_gcd(value1,value2))
