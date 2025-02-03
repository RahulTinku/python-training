def perimeter(length, breath):
    return 2 * (length + breath)

def area(length, breath):
    return length * breath

len = 10
b = 4

p = perimeter(len,b)
a = area(len, b)

print('The perimeter is : ', p)
print(' The area of rectangle is : ', a)