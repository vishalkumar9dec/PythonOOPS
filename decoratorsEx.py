def my_decorator(func):
    def wrapper():
        print('before function is called')
        func()
        print('after function is called')
    return wrapper


@my_decorator
def say_whee():
    print('Whee !!! ')

'''
    say_whee is being passed to my_decorator function as argument. then at line 6 when wrapper func is returned it 
    first prints the statement and then executes the function and prints the statement. wrapper funcation can refer to the 
    func() as it has its reference.
'''

#say_whee=my_decorator(say_whee) --> another method to call implement the decorator in python

say_whee()
