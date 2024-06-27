class Student:
    Name=""
    Rollno=0
    def studentprf(self):
        self.Name=input("Enter name:")
        self.Rollno=int(input("Enter roll no.:"))
    def show_result1(self):
        print("Data")

S = Student()
S.studentprf()
S.show_result1()

class Employee:
    Name=""
    Employeecode=0
    Salary=0
    Gender=""
    Address=""
    def employeeprf(self):
        self.Name=input("Enter name:")
        self.Employeecode=int(input("Enter code:"))
        self.Salary=input("Enter the salary:")
        self.Gender=input("Enter the Gender(M/F):")
        self.Address=input("Enter the Address:")
    def show_result2(self):
        print("Employee Data")

S = Employee()
S.employeeprf()
S.show_result2()

