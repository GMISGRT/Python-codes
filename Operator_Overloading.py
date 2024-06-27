class Point:
    x=0
    y=0
    z=0
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z

    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)

    def __add__(self,other):
        x=self.x+other.x
        z=self.y+other.y
        y=self.z+other.z
        return Point(x,z,y)

P1=Point(2,3,4)
P2=Point(-1,2,5)
P3=Point(3,2,6)
print(P1+P2+P3)

class Point1:
    x=0
    y=0
    z=0
    def __init__(self,x=0,y=0,z=0):
        self.x=x
        self.y=y
        self.z=z
    
    def __str__(self):
        return "({0},{1},{2})".format(self.x,self.y,self.z)
    
    def __truediv__(self,other):
        x=self.x / other.x
        y=self.y / other.y
        z=self.z / other.z
        return Point1(x,y,z)

P1=Point1(40,20,44)
P2=Point1(10,5,6)
P3=Point1(2,4,6)
print(P1/P2/P3)