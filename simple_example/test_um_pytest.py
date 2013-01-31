'''
Test unnecessary_math with pytest

To run tests : py.test             test_um_pytest.py
          or : python -m pytest    test_um_pytest.py
Verobse (-v) : py.test -v          test_um_pytest.py
          or : python -m pytest -v test_um_pytest.py
'''

from unnecessary_math import multiply

def test_numbers_3_4():
    assert multiply(3,4) == 12 

def test_strings_a_3():
    assert multiply('a',3) == 'aaa' 


