def cal(func):
    def inner_op(x):
        print("This is inner.",x)
        func(x)
        print("This is work.")
    return inner_op


#@cal
def arithmetic(x):
    print("arithmetic")
    
arithmetic = cal(arithmetic)

arithmetic("Hello")