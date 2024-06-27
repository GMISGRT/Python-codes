n=int(input("Enter no:"))
for i in range(2,(n+1) ,1):
    if n%i==0:
        break
if n==i:
    print("prime")
else:
    print("composite")
