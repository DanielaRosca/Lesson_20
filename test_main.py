from main import add

def test_add_positive_numbers():  # new *
    assert add(a=2, b=3) == 5

def test_add_negative_numbers():  # new *
    assert add(-1, -4) == -5

def test_add_mixed_numbers():  # new *
    assert add(a=-2, b=5) == 3
