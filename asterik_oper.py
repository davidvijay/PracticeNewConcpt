power = 2 **4
print(power)

my_list = [1,2,3,4,5,6]

first, *middle, second_last, last = my_list
print(first)
print(middle)
print(second_last)
print(last)

my_tuple = (1,2,3)
first, second, third = my_tuple
print(first)
print(second)
print(third)

my_list = [1,2,3,4]
my_tuple = (5,6,7)

newlist = [*my_list, *my_tuple]
print(newlist)


dict_1 = {'a':1, 'b':2}
dict_2 = {'c':3, 'd':4} 

new_dict = {**dict_1, **dict_2}
print(new_dict)