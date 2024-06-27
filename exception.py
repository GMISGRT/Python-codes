try:
    x=int(input("Enter the value of x:"))
    y=int(input("Enter the value of y:"))
    print(y/x)
except:
    print("Division by zero.")


try:
    x=int(input("Enter the value:"))
    print(x)
except:
    print("An Exception occured, 'NameError'")
finally:
     print("Always Exception.")
