import pytest,source.shapes as shapes


def test_area(fix_rectangle):
    assert fix_rectangle.area() == 5 * 10

def test_perimeter(fix_rectangle):
    assert fix_rectangle.perimeter() == 2 * (5 + 10)