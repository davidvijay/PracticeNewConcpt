# """
# argument vs parmater
# argument: time of calling a function 
# parameter: inside a funtion definition used or accessed
# """

# def name(name):
#     print(name)
    
# name("vijay")

# "postional and keyword argument"

# def foo(**a):
#     print(a)
    
# foo(a=1)

def foo(a,b,c):
    print(a,b,c)

my_list=[1,2,3]
foo(*my_list)


def foo(*args):
    print(args)
    # for i in args:
    #     print(i)
        
foo(1,2,3,4,5,6,7)


my_dict ={'a':1, 'b':2}
def foo(**kwargs):
    for key, value in kwargs.items():
        print(key, value)
        
foo(**my_dict)


number =0

def foo():
   global number 
   number = 3
   print(number)
    
    
foo()
print(number)


def foo():
    global var
    var=200
    
    
var=10
foo()
print(var)


def foo(my_list):
    my_list.append(4)
    
    
my_list=[1,2,3]
foo(my_list)
print(my_list)


def foo(my_list):
    my_list= my_list+ my_list[1000,2000]
    
foo(my_list)
print(my_list)