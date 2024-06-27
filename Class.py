class Sum:
    a=0
    b=0
    def add(self):
        self.a=int(input("Enter the value of a: "))
        self.b=int(input("Enter the value of b: "))
    def show_result(self):
        print("Sum=",self.a+self.b)

S=Sum()
S.add()
S.show_result()
print(type(S))
print(Sum.a)
print(S.a)

class Student:
    Name=""
    Rollno=0
    def studentprp(self):
        self.Name=input("")
        self.Rollno=input("")
    def show_result1(self):
        print("Data")

S = Student()
S.studentprp()
S.show_result1()
print("Student Name:")

class Student:
    roll = 0
    def stud_input(self):
        self.roll=2
    def stud_display(self):
        print("Roll:",self.roll)

s=Student()
s.stud_input()
s.stud_display()
s.__setattr__("name","qwerty")
print("Student Name:",getattr(s,"name"))
print(hasattr(s,"name"))

print(hasattr(s,"name"))
#delattr(s,"name")

