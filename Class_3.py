class A:     #base,parent,super class
    x=0

class B:     #derived,sub,child , classB extends classA
    y=0
    def input(self):
        self.x=int(input("Enter the value of x: "))
        self.y=int(input("Enter the value of y: "))

    def display(self):
        print("x= ",self.x,"y= ",self.y)

B=B()
B.input()
B.display()