'''
it should display a menu to the user
press 1 - even series
press 2 - odd serires
press 3 - calculating series
press 4 -  Exit
Please enter your option
'''

# import the module
import series as ser

# import directly the function from the module
from students_ops import calculate_grade

while True:
    print('1: Even Series')
    print('2: Odd Series')
    print('3: Calculating grade ')
    print('4: Exit')
    option = int(input("please enter your option - "))

    if option == 1:
        n = int(input('Enter n : '))
        print(ser.even_series(n=n))
    elif option == 2:
        n = int(input('Enter n : '))
        print(ser.odd_series(n=n))
    elif option == 3:
        n = int(input('Enter your marks : '))
        print(calculate_grade(marks = n))
    else:
        break