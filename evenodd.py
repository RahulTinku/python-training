def even_or_odd(n):
    if n%2:
        ans = 'odd'
    else:
        ans = 'even'
    return ans

n = int(input('Enter the number - '))
print(even_or_odd(n = n))