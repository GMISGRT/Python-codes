class Sum:
    "This is a sum of two variables."
    a=0
    b=0
    count=0
    def __init__(self):  # to initialise a object
        print("Hello")
        Sum.count+=1

    def __str__(self):   #
        return "({0}  {1})".format(self.a,self.b)
    
    def sum(self,x,y):
        z=6
        self.a=x
        self.b=y
        z+=1
        print("z=",z)
        
    def show_result(self):
            print("Sum= ",self.a+self.b)

S1 = Sum()
S1.sum(2,3)
print(str(S1))
S1.show_result()
print("Count= ",Sum.count)

S2 = Sum()
S2.sum(3,4)
S2.show_result()
print("Count= ",Sum.count)

S3 = Sum()
S3.sum(4,5)
S3.show_result()
print("Count= ",Sum.count)

print(Sum.__doc__)

print(hasattr(S1,"a"))
print(setattr(S1,"c",6))
print(hasattr(S1,"c"))
print(getattr(S1,"c"))
print(delattr(S1,"c"))
print(hasattr(S1,"c"))

print(Sum.__dict__)
print(Sum.__name__)
print(Sum.__module__)
print(Sum.__bases__)