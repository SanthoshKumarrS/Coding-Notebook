import pytest,my_function as my_function


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


@pytest.mark.slow
def test_very_slow():
    pytest.skip("Skipping this test for now")


@pytest.mark.skip(reason = "Skipping this test for now")
def test_skip():
    assert 1 == 1


