#1
from random import randint
omkar = [randint(0, 10) for i in range(11)]
print("Elements in omkar are: ", omkar)
print("Total of all items in omkar are:", sum(omkar))
my_list = [x for x in omkar if x > 5]
print("Elements greater than 5 in omkar: ", my_list)
print("Maximum Value in omkar: ",max(omkar))

#2 
from random import randint
array = [randint(0, 30) for i in range(11)]
print("sorted order of array is: ", sorted(array))

#3
a = [1,2,3,4,5]
b = [4,9,2,4]

print(list(set(a) ^ set(b)))

#4
a = [6,7,2,3]
b = [1,3,2,4]

def common(a,b): 
    c = [value for value in a if value in b] 
    return c

d=common(a,b)
print(d)
