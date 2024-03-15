#filter is used to filter the values from the iterables or collections

test_list = [1,2,46,7,8]
new_list = []
for i in test_list:
    if(i%2==0):
        new_list.append(i)
print(new_list)

evens = filter(lambda x: x%2==0,test_list)

#map is used to perform the logic operations in the collections

doubles = map(lambda x: x*2,test_list)


# reduce function is imported from functools it is used to apply the logic and the result as a single value

from functools import reduce

sum = reduce(lambda  x, y=0: x+y,test_list)