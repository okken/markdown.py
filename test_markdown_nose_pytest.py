'''
Test markdown.py with nose or pytest

To run tests: nostests         test_markdown_nose_pytest.py
          or: py.test          test_markdown_nose_pytest.py
          or: python -m pytest test_markdown_nose_pytest.py

Verbose (-v): nostests -v         test_markdown_nose_pytest.py
          or: py.test -v          test_markdown_nose_pytest.py
          or: python -m pytest -v test_markdown_nose_pytest.py
'''

from markdown_adapter import run_markdown

def setup_module(function):
    'I could do some setup here if I wanted to'
    pass

def test_non_marked_lines():
    assert ( run_markdown('this line has no special handling') == 
            '<p>this line has no special handling</p>')

def test_em():
    assert ( run_markdown('*this should be wrapped in em tags*') ==
            '<p><em>this should be wrapped in em tags</em></p>')

def test_strong():
    assert ( run_markdown('**this should be wrapped in strong tags**') ==
            '<p><strong>this should be wrapped in strong tags</strong></p>')

