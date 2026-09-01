import pytest,source.shapes as shapes


#Storing the fixture in a separate file conftest.py 
#so that it can be used across multiple test files
# More like a global fixture

@pytest.fixture 
def fix_rectangle():
    return shapes.Rectangle(5, 10)