import calc


def test_positive():
    assert calc.square(2) == 4
    assert calc.square(3) == 9


def test_negative():
    assert calc.square(-2) == 4
    assert calc.square(-3) == 9


def test_zero():
    assert calc.square(0) == 0
