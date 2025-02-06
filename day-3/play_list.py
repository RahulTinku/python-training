el = []
print(type(el))

cars =['bmw','audi','toyota'] # homogenous data
s1 = ['Rahul', 10, 'male', 90] # heterogenous data ---> list is not ideal data structure for this

# lopping

for car in cars:
    print(car.capitalize())


#indexing
print(cars[0])
print('last element ',cars[-1])

cars[-1] = 'kia'

print('latest ',cars)

#slicing
marks = [4,50,23, 5,6,7,8,2,11]
## marks of first 4 students
print(marks[0:4])

# marks of last 3 students
print(marks[-3:])


# bifs
print(len(marks))
print(max(marks))
print(min(marks))
print(sum(marks)/ len(marks))

# OOPS
# ['bmw', 'audi', 'kia']
cars.append('hyundai i10')

# add 1 in last
# ['bmw', 'audi', 'kia', 'hyundai i10']

#add multiple in last
cars.extend(['mercedes', 'jaguar'])
# ['bmw', 'audi', 'kia', 'hyundai i10', 'mercedes', 'jaguar']

# add multiple at any index
cars.insert(1, 'jeep')

# remove element
print(cars.pop())

# remove element from index
cars.pop(2)

# remove element from list by element name
cars.remove('jeep')
print(cars)

# does not perform opertaion on original list
copy_marks = marks.copy()
copy_marks.reverse()

# membership
print('audi' in cars) # false
print('kia' in cars) # true

# other oops
print(marks.count(4))
print(marks.count(0))

# sorting
copy_marks = marks.copy()
copy_marks.sort()
print(copy_marks)

# sort in reverse order
another_copy = marks.copy()
another_copy.sort(reverse=True)
print(another_copy)





