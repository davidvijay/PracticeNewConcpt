import sys

def list_valu(x):
    my_list=[]
    for i in range(x):
        my_list.append(x)
     
    return my_list


def gen_value(x):
    for i in range(x):
        print("Inside Generator")
        yield i
        print("after yielded")


#print(sys.getsizeof(list_valu(100000)))
a=gen_value(10)
print("after generator")
print(next(a))
print(next(a))
print(next(a))
# for i in a:
#     print("Inside loop")
#     print(i)
        
