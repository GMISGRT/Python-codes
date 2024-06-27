def sum():
    print(f"sum of 2 & 3,\n{2+3}")

sum()

def sub():
    print(f"sub of 2 & 3,\n{2-3}")

sub()

def mul():
    print(f"multiplication of 2 & 3,\n{2*3}")

mul()

def div():
    print(f"division of 2 & 3,\n{2/3}")

div()

def sum(a,b):
    print(f"Sum of a & b,\n{a+b}")

a=int(input("Enter the value a:"))
b=int(input("ENter the value b:"))
sum(a,b)

if __name__=="__main__":
    sum(a,b)

def sum(a,b=89):
    print(f"Sum of a & b,\n{a+b}")
a=int(input("Enter the value a:"))
sum(a,)

