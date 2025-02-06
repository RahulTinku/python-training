class Student:
    # class attributes
    count = 0
    # define __init__
    # Constructor
    def __init__(self, name=None, gender=None, roll=None, marks=None):
        # self  - reference to the current object
        self.name = name
        self.gender = gender
        self.roll = roll
        self.marks = marks
        # access the class attributes using the class name
        Student.count += 1

    # Instance (Object) Method
    def get_details(self):
        #self -> s1, s2
        return 'Name: '+ self.name + '\nGender: ' + self.gender \
        + '\nRoll: ' + str(self.roll) + '\nMarks: ' + str(self.marks)
    
    # class Methods
    def new_instance(name=None, gender=None, roll=None, marks=None):
        return Student(name=name, gender=gender, roll=roll, marks=marks)
        
