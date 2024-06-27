class Employee:
    e_id=0
    e_name=""
    def __init__(self,e_id,e_name) :
        self.e_id=e_id
        self.e_name=e_name

    def display(self):
        print("Employee ID: ",self.e_id,"Employee name: ",self.e_name)

    def __del__(self):
        class_name = self.__class__.__name__
        print(class_name,"destroyed.")


E1=Employee(23425984,"QWERTY")
E2=Employee(32676687,"ASDFGH")
E3=Employee(12345678,"ZXCVBN")
E1.display()
E2.display()
E3.display()
print(id(E1),id(E2),id(E3))
