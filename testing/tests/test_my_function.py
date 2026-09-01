import pytest,source.my_function as my_function


def test_add():

    result = my_function.add(2, 3)
    assert result == 5


def test_divide():
    
    result = my_function.divide(10, 2)
    assert result == 5


def test_divide_by_zero():

    with pytest.raises(ZeroDivisionError):
        my_function.divide(10, 0)


def test_add_strings():
    result = my_function.add("hello ", "world")
    assert result == "hello world"