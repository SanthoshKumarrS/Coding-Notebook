import source.shapes as shapes
from testing.tests.conftest import fix_rectangle


class TestCircle:

    def setup_method(self, method):
        print(f"Setting up {method}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down {method}")

    def test_area(self):
        print("Testing area")
        assert self.circle.area() == 3.14 * self.circle.radius ** 2

    def test_perimeter(self):
        print("Testing perimeter")
        assert self.circle.perimeter() == 2 * 3.14 * self.circle.radius


    def test_area(fix_rectangle):
        assert fix_rectangle.area() == 5 * 10
