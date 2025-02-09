marks = [4,50,23,5,6,7,8,2,11]

# create new list consisting of even marks more than 2 from the marks list (Filter)
'''def filter_list(marks):
    new_list = []
    for i in marks:
        if i%2 == 0 and i > 2:
            new_list.append(i)
    return new_list

print(filter_list(marks)) 
'''

# for comprehension (pre requisite is that we should be needing a new list from existing list
'''
new_list = [mark for mark in marks if mark %2 == 0 and mark > 2]
print(new_list)
'''

# create a new list consisting of marks from the marks list but where every mark is deducted by 1 (Mapping)
'''
new_list = [mark -1 for mark in marks ]
print(new_list)
'''
'''
new_list = []
for mark in marks:
    new_list.append(mark-1)
print(new_list)
'''

# create a new list consisting of odd marks from the marks list squared up in the list (filter and mapping)
new_list3 = [mark ** 2 for mark in marks if mark % 2]
print(new_list3)

