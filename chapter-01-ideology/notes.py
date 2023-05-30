######################### Chapter 1 Notes ##########################

"""
pg. 13 Test Code - Unit Testing 

Creating unit tests can be costly. Consider these three points each time you code:

1. How  many times is this code called by other code?
2. If this code WERE wrong, how detrimental to the results would it be?
3. How noticeable would an error be if it occurred?
"""

EPS = 0.00001
# a small number to use when comparing floating-point values


def add(x, y):
    print(x+y)
    return x + y


def test_add():
    assert (add(2, 3) == 5)
    assert (add(-2, 3) == 1)
    assert (add(-1, -1) == -2)
    assert (abs(add(2.4, 0.1) - 2.5) < EPS)
    print("All tests passed")


test_add()
