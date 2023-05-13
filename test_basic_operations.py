from basic_operations import mysum, sub, mul, div

def test_mysum():
    assert mysum(2,3) == 5

def test_sub():
    assert sub(2,3) == -1

def test_mul():
    assert mul(2,3) == 6

def test_div():
    assert div(2,3) == 2/3