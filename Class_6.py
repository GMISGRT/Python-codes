class A:
    x=0

    def Myparent(self):
        print("This is a Parent class.")

class B:
    y=0

    def Myparent(self):
        print("This is a Child class.")   #Overrides parent class.

B=B()
B.Myparent()    #Parent class is overridden.