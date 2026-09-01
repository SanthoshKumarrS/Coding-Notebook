import pytest,source.shapes as shapes

#parameterize is a decorator that allows you to run a test function
# multiple times with different input values. 
# It takes two arguments: 
# the first is a string that specifies the names of the parameters
# the second is a list of tuples that contain the values for each parameter.

@pytest.mark.parametrize("side_length,expected_area", 
[
    (2, 4),
    (3, 9),
    (4, 16),
])
def test_multiple_square_areas(side_length,expected_area):
    assert shapes.Square(side_length).area() == expected_area


