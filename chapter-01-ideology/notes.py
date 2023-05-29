##### Chapter 1 Notes ######
# pg. 13 Test Code - Unit Testing

EPS = 0.00001
# a small number to use when comparing floating-point values


def add(x, y):
    print(x+y)
    return x + y


def test_add():
    assert (add(2, 3) == 5)
    assert (add(-2, 3) == 1)
    assert (add(-1, -1) == 2)
    assert (abs(add(2.4, 0.1) - 2.5) < EPS)


test_add()
