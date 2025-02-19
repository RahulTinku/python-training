def perimeter(length=10, breath = 5):
    return 2 * (length + breath)

def area(length, breath):
    return length * breath

len = int(input('Enter Length : '))
b = int(input('Enter Breadth : '))
 # named parameter 
 # I can call like perimeter(breath = b, length = len) as well
p = perimeter(length = len, breath = b)

# unnamed parameter
a = area(len, b)

print('The perimeter is : ', str(p))
print(' The area of rectangle is : ', str(a))

print('This is with set breadth 5 : ', perimeter(10))

# perimeter with default length value and breadth passed by the user 
print('This is perimeter, breadth added by user : ', perimeter(breath=7)) 
