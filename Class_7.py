class A:
    x=0

class B(A):
    y=0

class C(B):
    z=0

    def input(self):
        self.x=int(input("Enter the value of x= "))
        self.y=int(input("Enter the value of y= "))
        self.z=int(input("Enter the value of z= "))

    def output(self):
        print("x=",self.x,"y=",self.y,"z=",self.z)

C=C()
C.input()
C.output()
