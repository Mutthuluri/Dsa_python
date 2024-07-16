def is_power_of_2(n):
        while n != 1:
            if n %2 != 0:
                return False
            n = n//2
        return True

n = int(input("Enter a number: "))
print(is_power_of_2(n))

