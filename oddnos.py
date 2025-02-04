def odd_series(n):
    i =1
    series =''
    while i <= n:
        if i%2:
            series += str(i) + ' '
        i += 1
    return series

n = int(input("Enter n : "))
print(odd_series(n=n))