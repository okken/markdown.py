"""
An example script showing how to use the api adapter
"""

from markdown_adapter import run_markdown, run_markdown_pipe, run_markdown_file

SAMPLE_INPUT = [
        'apple',
        '**bold**',
        '*emphasis*',
        '# H1 header',
        '## H2 header',
        '''
        this
        has
        multiple lines''']

for s in SAMPLE_INPUT:
    out      = run_markdown(s)
    out_pipe = run_markdown_pipe(s)
    out_file = run_markdown_file(s)
    print('-' * 40)
    print('-- this --')
    print(s)
    if s.rstrip() == out.rstrip():
        print('-- returns (same as input) --')
    else:
        print('-- returns --')
    print(out,)

    if out != out_pipe:
        print('-- run_markdown_pipe() returns something different --')
        print(out_pipe,)

    if out != out_file:
        print('-- run_markdown_file() returns something different --')
        print(out_file,)