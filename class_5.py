class __JustCounter:   #prvt class
    __secretCount=0    #prvt 
    def count(self):
        self.__secretCount+=1
        print(self.__secretCount)

J=__JustCounter()
print(J)
J.count()
J.count()
J.count()
#print(J.__secretCount)