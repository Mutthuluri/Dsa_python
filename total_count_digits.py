def total_count_digits(n):
    count = 0
    while n!=0:
        if n%2 == 1:

            count += 1
        n = n//2

    return count

print(total_count_digits(15))
