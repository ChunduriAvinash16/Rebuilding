'''
Decorators:
   Decorators are the function which is used to enhance the functionality of another function
   Decorators are also reffered as one function provides additional code to another function 
   @ is used to decorate a function
   annotation - extra information to the function
Rules for an decorators
    1) Decorator function should always be nested function
    2) The Decorator function should accept the address of the function which needs to decorator
    3) The Decorator function must return the address of inner function
'''

def wrapper(func): 
    def inner(val): 
        print("Inner function")
        func(val)
        print("Exit inner")
    return inner
#decorator function

@wrapper
def needs_decorator(val):
    print("Inside Decorator")
    print(val)

needs_decorator(2) #1


''' the internal meaning for above statment is 
z=wrapper(needs_decorator)
z()
'''



