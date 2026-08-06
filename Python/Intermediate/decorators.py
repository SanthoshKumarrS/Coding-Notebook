#Decorators
import functools


def startenddecorator(func): 
    
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper


@startenddecorator
def add5(x):
    return x+5
    

#add = add5(10)
#print(add)

def repeat(num_times):
    def decorator_repeat(func):
        @functools.wraps(func)
        def wrapper(*args,**kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat



@repeat(num_times = 7)
def greet(name): 
    print(f'Hello {name}')


#greet('John')