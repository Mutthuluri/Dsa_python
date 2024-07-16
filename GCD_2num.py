def GCD(a,b):
    while a!=b:

        if a > b:
            a = a-b
        else:
            b = b-a

    return a

value1 = int(input('Enter first number: '))
value2 = int(input('Enter second number: '))
print(GCD(value1,value2))