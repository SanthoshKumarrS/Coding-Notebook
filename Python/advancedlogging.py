import logging

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(levelname)s:%(name)s:%(message)s')


def add(x, y):
    return x + y

def subtract(x, y):
    return x -y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        result =  x / y
    except ZeroDivisionError:
        logging.exception('Zero division error')
    else:
        return result

logging.debug(add(2,5))
logging.debug(subtract(10, 3))
logging.debug(multiply(4, 6))
logging.debug(divide(4,0))