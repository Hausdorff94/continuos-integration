from basic_operations import mysum, sub, mul, div


def test_mysum():
    assert mysum(2, 3) == 5


def test_sub():
    assert sub(2, 3) == -1


def test_mul():
    assert mul(2, 3) == 6


def test_div():
    a=2
    b=3
    if b == 0:
        assert div(a, 0) == "Error: Division by zero"
    else:
        assert div(a, 3) == a / b
