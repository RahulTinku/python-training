'''
# while loop

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
'''

'''
for i in << sequence of elements>>
'''

def odd_series(n):
    # sequence of elements ----> [1,n]
    # range [1, n+1]
    # range [1, n+1, 2] -----> step size 2, i.e. increment by 2
    series = ''
    for i in range(1, n+1, 2):
        series += str(i) + ' '

    return series

n = int(input('Enter n : '))
print(odd_series(n=n)) 
