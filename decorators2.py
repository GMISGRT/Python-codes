def sum(func):
    def op(x,y):
        print("====Sum Operations====")
        print(x+y)
        func(x,y)
    return op

@sum
def find_sum(x,y):
    pass

find_sum(2,3)

#=====================================================
def sub(func):
    def op(x,y):
        print("===Substraction===")
        print(x-y)
        func(x,y)
    return op
@sub
def find_sub(x,y):
    print("calling sub.")
    pass

find_sub(2, 1)

#======================================================
def decorator_function(func):
    def wrapper(arg):
        upper = arg.upper()
        return func(upper)
    return wrapper

@decorator_function
def decorated_function(name):
  print("your can call me", name)

decorated_function("tammy")

#=======================================================

def upper_name(func):
    def wrapper(*args):
        fname = args[0].upper()
        lname = args[1].upper()
        return func(fname,lname)
    return wrapper

@upper_name
def user_name(fname,lname):
    print("User name:",fname," ",lname)
    
user_name("qwerty", "keypad")

#=========================================================

def extend_upper(func):
    def wrapper(l):
        l2=[]
        for x in l:
            l2.append(chr(x))#ord() convert character to asscii & chr() convert ascii(numeric) to character
        return func(l2)
    return wrapper

@extend_upper
def print_list(l):
    for x in l:
        print(x)
l = [97,
     98,
     99,
     100,
     101,
     102,
     103]
print_list(l)


def extend_upper(func):
    def wrapper(l):
        l2 = []
        l3 = []
        for x in l:
            l2.append(ord(x)-32)
            for x2 in l2:
                l3.append(chr(x2))
        return func(l3)
    return wrapper


@extend_upper
def print_list(l):
    for x in l:
        print(x)

l = ['a','b','c','d','e']
print_list(l)

#https://realpython.com/inner-functions-what-are-they-good-for/
#https://www.geeksforgeeks.org/python-inner-functions/
