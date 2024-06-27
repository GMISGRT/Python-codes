class A:
    x = 0
    z = 0
    def __init__(self):
        self.x = 10
    def a(self):
        print("Parent class method.")

class B(A):
    y=0
    def __init__(self):
        super().__init__()  #constructer calling
        self.y = 30
        #super().z=90  #attribute calling
        super().a() #calling parent class method
    

    def display(self):
        print(self.x," ",self.y)

if __name__=="__main__":
    B=B()
    B.display()
