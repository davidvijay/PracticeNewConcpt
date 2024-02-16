tuple is immutable

mytuple = ("Max,)

built-in function
mytuple = tuple("max", 28)

accessing
item = mytuple[0]

changing
mytuple[0] = "vijay" error 


inside a tuple checking
if "max" in mytuple
print("yes")
else:
print("no")

built-in
my_tuple= ('a', 'p', 'p', 'l', 'e')
print(mytuple.count('p')) return p occured times
print(mytuple.index('p'))-- first index occurence


tuple to list

mylist = list(my_tuple)
print(my_list)

list to tuple
mytuple_2 = tuple(my_list)
print(mytuple_2)

slicing

a= (1,2,3,4,5)
b=a[2:5]

index 2 to 4 it will come

step case
b=[::1]
it will print all the element default value is 1

b=[::2]
output will be 1, 3, 5



unpacking

my_tuple = "max", "28"
name, age = my_tuple

print(name)
print(age)

needs to same element inside the tuple

my_tuple = (0,1,2,3,4)
i1 *i2, i3 = my_tuple

print(i1)---0
print(i2)---[1,2,3]
print(i3)---4



tuple is more efficient when comparing with list because its immutaable

import sys

my_list = [1,2]
my_tuple = (1,2)

print(getsizeofmy(my_list)) --list byte value is larger
print(getsizeofmymy_tuple )








