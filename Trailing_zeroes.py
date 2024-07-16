def Trailing_zeroes(n):
    count = 0
    i = 5
    while n//i >=1:
        count = count + n//i
        i = i*5

    return count

input1 = int(input("Enter a number: "))
print(Trailing_zeroes(input1))
