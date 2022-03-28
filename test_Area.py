import Area
import pytest

@pytest.mark.skip(reason = "currently no need to execute this")
def test_area():
    a = 20
    b = 5
    r = Area.area(a, b)
    assert a*b == r

@pytest.mark.myproject
def test_perimeter():
    a = 10
    b = 5
    r = Area.perimeter(a, b)
    assert 2*(a+b) == r

@pytest.mark.myproject
def test_square():
    b = 5
    r = Area.square(b)
    assert b*b == r