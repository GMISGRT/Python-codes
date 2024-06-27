mytuple=("apple","mango","orange")
myitr=iter(mytuple)
print(next(myitr))
print(next(myitr))
print(next(myitr))

mydict = {"roll":12345,"name":"qwerty","address":"add"}




class Myiterator:
    def __iter__(self):
        self.a=0
        return self

    def __next__(self):

        #if self.a<50:
            self.a+=10000000
            return self.a
        #else:
            #raise StopIteration

myitr = Myiterator()
itr = iter(myitr)

for x in itr:
    print(x)