l = ["asdf","apple","banana"]

l.remove("asdf")

print(l) 

l.pop(0)

print(l)

l = [1,2,3,4,5]

l.pop()

print(l)

del l[2]

print(l)

#del l

print(l)

l.clear()

print(l)

l = [1,2,3,4,5]

for x in range(0,len(l),1):
    print(l[x])#l[0], l[1], l[2], l[3]

#List Comprehension
for x in l:
    print(x)

s = [x for x in l]

print(s)

s = [x for x in l if x == 5]
print(s)

for x in l:
    if x==5:
        break
    print(x)


l = ["apple","mango","orange"]

for x in l:
    s = x.upper()
    print(s)

s = [x.upper() for x in l]

print(s)

s.sort(reverse=True)
print(s)

l2 = ['q','w']

l3 = l+l2

print(l3)

l4 = l3.copy()

print(l4)

l5 = list(l4)

print(l5)

