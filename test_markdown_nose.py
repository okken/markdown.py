'''
Test markdown.py with nose 

To run tests: nosetests     test_markdown_nose.py
Verbose (-v): nosetests -v  test_markdown_nose.py
'''

from markdown_adapter import run_markdown

def test_non_marked_lines():
    print ('in test_non_marked_lines')
    assert run_markdown('this line has no special handling') \
            == '<p>this line has no special handling</p>'

def test_em():
    print ('in test_em')
    assert run_markdown('*this should be wrapped in em tags*') \
            == '<p><em>this should be wrapped in em tags</em></p>'

def test_strong():
    print ('in test_strong')
    assert run_markdown('**this should be wrapped in strong tags**') \
            == '<p><strong>this should be wrapped in strong tags</strong></p>'

