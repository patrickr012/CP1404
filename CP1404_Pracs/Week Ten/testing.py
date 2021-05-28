"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
Patrick Robinson
12251568
"""

import doctest
from car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    test_car = Car()
    assert test_car.odometer == 0, "Car does not set odometer correctly"

    assert test_car.fuel == 0, "Default fuel is incorrect"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "fuel is incorrect"


run_tests()

doctest.testmod()


def format_phrase(phrase):
    """
    >>> format_phrase('hello')
    'Hello.'
    >>> format_phrase("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_phrase('Hello world.') #Running the tests for each criteria
    'Hello world.'
    """
    finished_phrase = phrase.capitalize()

    if finished_phrase[-1] != ".":
        finished_phrase += "."
    return finished_phrase
