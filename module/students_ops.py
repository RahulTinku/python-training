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
