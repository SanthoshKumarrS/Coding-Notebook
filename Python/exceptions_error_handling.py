class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    pass
        
def test_value(x):
    if x > 100:
        raise ValueTooHighError('value is too high')
    if x < 5:
        raise ValueTooLowError('Value is too low')
    
try:
    test_value(200)
except ValueTooLowError as e:
    print(e)
except ValueTooHighError as e:
    print(e)
