def even_or_odd(n):
    # scope of n is within the function
    if n%2:
        # scope of ans variable is enclosing function block (even_or_odd)
        ans = 'odd'
    else:
        # scope of ans variable is enclosing function block (even_or_odd)
        ans = 'even'
    return ans

n = int(input('Enter the number - ')) # scope of n is only within this file
print(even_or_odd(n = n))
