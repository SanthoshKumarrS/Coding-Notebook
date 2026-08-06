import logging

# logging.basicConfig(level=logging.INFO)
logging.basicConfig(filename='example.log', level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def add(x, y):
    return x + y

def subtract(x, y):
    return x -y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

logging.info(add(2,5))
logging.info(subtract(10, 3))
logging.info(multiply(4, 6))
logging.info(divide(4,2))