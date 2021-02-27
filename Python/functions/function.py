def outer():
    print("outer")
    def inner():
        print("inner")
    return inner
z=outer()
z()


'''
    #return : IT is used to return the value from the function
    def hello():
            print("Hello")
            return hello
    print(hello)
    x=hello()
    print(x)
'''

'''
    def one():
        print("in one")
    def two(func):
        print("in two")
        print("func in two is",func)
        func()
        print("end two")
    print(one)
    two(one)
'''


'''
#nested function returning address
def outer():
    print("in outer")
    def inner():
        print("in inner")
    return inner
z=outer()
print(z)
z()
'''

'''
Decorators:
    
'''