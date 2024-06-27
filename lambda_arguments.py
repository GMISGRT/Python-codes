x = lambda x,y:x+y
print(x(2,3))
print(x(4,5))

a= lambda x,y:x*y
print(a(x=int(input("Enter x:")),y=int(input("Enter y:"))))

x=lambda x,y:print(f"{x} is greater i.e, x.") if(x>y) else print(f"{y} is greater i.e, y.")
x(int(input("Enter x:")),int(input("Enter y:")))

#a=lambda a,b,c : print(f"{a} is greatest i.e, a.") \
#    if (a>b and a>c) else (print(f"{b} is greatest i.e, b.") \
#    if (b>a and b>c) else (f"{c} is greatest i.e, c."))
#a(a=(int(input("Enter a:"))),b=int(input("Enter b:")),c=int(input("Enter c:")))

def sum():
    return lambda x,y:x+y
s=sum()
print(s(2,3))

li = [1,2,3,4,5,6,7,8,9,65,56,77,88,99,375,8768]
list=list(filter(lambda x:x%2!=0,li))                # For listing out odd numbers. 
print(list)

#max of 1 list in 1 file

#li1 = [2,4,6,8,85,757,36778,869]
#list1=list(map(lambda x:x**2,li1))
#print(list1)

li2 = []
list2=list()