def shout (text):
    return text.upper()

yell = shout
print(yell("hello"))


def X(text):
    return (text)

M=X
print(M("Welcome To Python"))

#  Passing the function as an argument.
def X1(text):
    return text.upper()

def X2(text):
    return text.upper()

def H(func):
    print(X1("This is X1"))
    print(X2("This is X2"))
    print("This is H")

    s=func("Hi I am created as function.")
    return s

print(H(X1))
print(H(X2))
    
def create_adder(x):
    def adder(y):
        return x+y
    return adder

add_15 = create_adder(15)

print(add_15(10))

import math
def area_circle(r):
    def area(y):
        return y*r*r
    return area

area_C = area_circle(2)
print(area_C(math.pi))