def func(*args):
    print(args)


func('test','argument')


def kfunc(**kwargs):
    print(kwargs)

kfunc(first='Vishal', last='Vishal')