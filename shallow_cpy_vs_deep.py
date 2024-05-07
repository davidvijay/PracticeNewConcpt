# Actual copy

a= 6
b = a
b= 7
print(b)
print(a)

# Shallow copy
import copy
my_list = [[1,2,3,4,5] , [6,7,8,9]]
copy_lst = copy.deepcopy(my_list[:])
copy_lst[0][0]= -10
print(copy_lst)
print(my_list)

class person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
class employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
p1 = person("David", 21)
p2 = person("Vijay", 19)

emp = employee(p1, p2)
emp_clone = copy.deepcopy(emp)
emp_clone.name.name = "Ajith"
print(emp_clone .name.name)
print(emp.name.name)






