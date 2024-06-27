#a=6
#b=5
#print(a+b)
#a=int(input ("a"))
#b=int(input ("b"))
#c=a+b
#print(c)


#a=2
#print(type(a))
#a=3.4
#print(type(a))
#a=[1,2,3,'a']
#print(type(a))
#a=(1,2,3,'a')
#print(type(a))
#a={1,2,3,'a'}
#print(type(a))
#a={1:'q',2:'y'}
#print(type(a))
#a=(2+3j)
#print(type(a))


#r=int(input("Enter the value of radius:-"))
#print("Area of the Circle=",(3.14*r**2))
#print("Perimeter of Circle=",(2*3.14**r))


#a=17
#b=3
#print(a%b)

# SHORTHAND OPERATOR

#a=34
#b=87
#a=a+b
#print(a)
#a+=b
#print (a)

#a=6
#b=2
#a*=b
#b=a//b
#a//=b
#print(a,b)

#a=8
#b=4
#a+=b
#b=a-b
#a-=b
#print(a,b)# SHORTHAND OPERATOR


#a=(129+56)*8-9/8
#print(a)

# COMPARISION OPERATOR

#a=2
#b=4
#print(a==b)
#print(a!=b)
#print(a<b)
#print(a>b)

# LOGICAL OPERATOR

#a=2
#b=3
#c=1
#print((a>b)and(a>c))
#print((a>b)or(a>c))
#print(not(a>b)and(a>c))

# MEMBERSHIP OPERATOR 

#l=[1,2,3,4,5,True,"aa",4j]
#print(1 in l)
#print(True in l)
#print(6 in l)
#print("aa" in l)
#print(4j in l)

#BITWISE OPERATOR

#a=64
#=65
#print(a|b)
#A=5677
#B=654
#print(A|B)

#A=78      #78=1001110
#B=79      #79=1001111
#print("A bitwise and(&) B :",A&B)
#  1001110
#  1001111
# =========
#  1001110: 78
#print("A bitwise or(|)  B :",A|B)
#  1001110
#  1001111
# =========
#  1001111: 79
#print("A bitwise xor(^) B :",A^B)
#  1001110
#  1001111
# =========
#  0000001: 1
#print("A bitwise not(~)   :",~A)
#  n=78  ~ = -(78+1)
#print("B bitwsie not(~)   :",~B)
#  n=79  ~ = -(79+1)
#print("A right shift(>>) 3:",A>>3)
#print("B right shift(>>) 3:",B>>3)
#print("A left shift(<<) 3 :",A<<3)
#print("B left shift(<<) 3 :",B<<3)

# CONTROL STATEMENTS

#age=int(input("Your Age:"))
#if age>=18:
#  print("Elligible for voting")
#else:
#    print("Not elligible for voting")

#n=int(input("Enter your number:"))
#if n%2==0:
#    print("Even number")
#else:
#    print("Odd number")

#Month=int(input("Enter the number for the Month:\n"))
#if Month==1:
#    print("January")
#elif Month==2:
#    print("February")
#elif Month==3:
#    print("March")
#elif Month==4:
#    print("April")
#elif Month==5:
#    print("May")
#elif Month==6:
#    print("June")
#elif Month==7:
#    print("July")
#elif Month==8:
#    print("August")
#elif Month==9:
#    print("September")
#elif Month==10:
#    print("October")
#elif Month==11:
#    print("November")
#elif Month==12:
#    print("December")
#else:
#    print("Not available")

# NESTED IFELSE

#x=int(input("X="))
#y=int(input("Y="))
#z=int(input("Z="))
#if x>y:
    #if x>z:
        #print(x," is greatest")
    #else:
        #print(z,"is the greatest")

#else:
    #if y>z:
     #   print(y,"is the greatest")
    #else:
#        print(z,"is the greatest")


#x=int(input("Enter the of X:"))
#if x%5==0:
#    if x%11==0:
#        print(x,"is divisible by 5 & 11")
#    else:
#        print(x,"is divisible by 5 only")
#else:
#    if x%11==0:
#        print(x,"is divisible by 11 only")
#    else:
#        print(x,"is not divisivle by neither 5 nor 11")

# LOOPS 

#for i in range(1,101,1):
#    print(i,end="  ")

#for _ in range(0,201,4):
#    print(_,end=" ")

#print("\n")

#x=0
#for _ in range(0,201,4):
#    x+=_
#    print(_,end=" ")
#print("\n")
#print("Sum=",x)

#l=[1,2,3,4,5]
#for x in range (0,len(l),1):
#    print(l[x])

#for x in l:
#    print(x)

#s=[x for x in l]
#print(s)

#s.sort(reverse=True)
#print(s)

#l=["apple","orange","mango"]

#for x in l:
#     s=x.upper()
#    print(s)

#s=[x.upper() for x in l]
#print(s)

#s.sort()
#print(s)

#s.sort(reverse=True)
#print(s)

#l2=["q","w"]
#l3=l+l2
#print(l3)

#l4=l3.copy()
#print(l4)

#l5=list(l4+l3)
#print(l5)

#_=65
#while (_<=90):
#    print(_,end=" ")
#    _+=1


#t=(1,2,3,4)
#x=list(t)
#x.append("kamala")
#print(x)
#y=tuple(x)
#print(y)

#n=int(input("Enter the no."))
#i=2
#while n!=0:
#    if n%i==0:
#        break
#    i+=1
#if n==i:
#    print("Prime number:",n)
#else:
#    print("Not Prime:",n)

#print("\n")

#i=2
#n=1
#while (n<=10):
#    while n!=0:
#        if n%i==0:
#            break
#        i+=1
#    if n==i:
#        print(n)
#    else:
#        print()
#    n+=1

#n1=int(input("Enter the 1st range:"))
#n2=int(input("Enter the 2nd range:"))
#j=0
#t=0
#for k in range(n1,n2,1):
#    for j in range (2,k+1,1):
#        if(k%j==0):
#            break
#
#    if (k==j):
#        print("Prime no.:",k)
#        t+=1
#    else:
#        print("Not prime:",k)

#print("Total no.of primes",t)

#t=[1,2,4,4,6,6]
#print(t)

s={1,4,6,7}
s2={"apple","mango"}

s.add("hebrew")
print(s)

s3={1,"b"}
s4={2,1,"a"}

s4.update(s3)
print(s4)

s5=[2,5,6]

s3.update(s5)
print(s3)

s3.remove(5)
print(s3)

s3.discard("z")
print(s3)

s3.pop()
print(s3)

s6={4,"g",89}
s6.clear()


s7={1,0,9,8,7,"a","p"}
for x in s7:
    print(x)

print(len(s7))

s8={"c","d","f"}
s9=s8.union(s7)

s="Lorem Ipsum is simply dummy text of the printing and typesetting industry.\
   Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,\
   when an unknown printer took a galley of type and scrambled it to make a type \
   specimen book. It has survived not only five centuries, but also the leap into \
   electronic typesetting, remaining essentially unchanged. It was popularised in \
   the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, \
   and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

print(s)
print(len(s))

for x in s:
    print(x,end=" ")

if "popularised" in s:
    print("True")

b= "Hello World"
print(b[2:5])

a="Hello World"
print((a.upper))
print(a.upper())

c="Hello World"
print(a)
print(a.strip())

print (a.replace("H","B"))

print(s.split(" "))

x="Ram"
y=90
print(f"My name is {x},{y}")

print(c := int(input("Enter 1:"))+int(input("Enter 2:")))

