'''
Test unnecessary_math with nose 

To run tests : nosetests    test_um_nose.py
Verobse (-v) : nosetests -v test_um_nose.py
'''

from unnecessary_math import multiply

def test_numbers_3_4():
    assert multiply(3,4) == 12 

def test_strings_a_3():
    assert multiply('a',3) == 'aaa' 


