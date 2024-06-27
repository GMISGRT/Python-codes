class Human:
    "This class belongs to method learning."
    def SayHello(self, name=None):
        if name is not None:
            print("Hello "+ name)
        else:
            print("Bye")

obj=Human()
obj.SayHello()
obj.SayHello("QWERTY")
