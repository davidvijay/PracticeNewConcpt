def foo(a,b,*args, **kwargs):
    print(a)
    print(b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(f"key : {key}, value : {kwargs[key]}")
        
foo(1,2,3,4,5,6,seven=7, eigh=8)


my_list = [1,2,3]


def foo(a,b,c):
    print(a,b,c) 
           
foo(my_list)


my_dict = {"a":1, "b":2, "c":3}

def foo (a,b,c):
    print(a,b,c)
    
foo(my_dict)