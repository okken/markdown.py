'''
Test unnecessary_math with nose or pytest

To run tests: nostests         test_um_nose_pytest.py
          or: py.test          test_um_nose_pytest.py
          or: python -m pytest test_um_nose_pytest.py

Verbose (-v): nostests -v         test_um_nose_pytest.py
          or: py.test -v          test_um_nose_pytest.py
          or: python -m pytest -v test_um_nose_pytest.py
'''

from unnecessary_math import multiply

def setup_module(function):
    'I could do some setup here if I wanted to'
    pass

def test_numbers_3_4():
    assert ( multiply(3,4) == 12 )

def test_strings_a_3():
    assert ( multiply('a',3) == 'aaa')

