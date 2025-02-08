'''
marks >= 70 => Grade A
marks >= 60 => Grade B
marks >= 40 => Grade C
marks < 40 => Grade F
Grade > 100 or  Grade < 0 => Grade Invalid
'''

def calculate_grade(marks):
    if (marks <0 or marks > 100):
        grade = 'Invalid grade'
    elif marks >= 70:
        grade = 'Grade A'
    elif marks >=60:
        grade = 'Grade B'
    elif marks >=40:
        grade ='Grade C'
    else:
        grade ='Grade F'
    return grade

marks = int(input('Enter marks : '))
print(calculate_grade(marks = marks))
