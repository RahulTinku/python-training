from lib.college.student import Student

print(Student.count)
s1 = Student(name = 'John', gender = 'male', roll=10, marks=90)
# add attributes to the objects
s2 = Student('Jane', 'female', 20, 45)
s2.mood = 'angry'

s3 = Student()

s4 = Student.new_instance(name="James", gender='male', roll=30, marks= 86)

print(s1.get_details())
print(s2.mood)
print(s3)

print(Student.count)
print(s4.get_details())