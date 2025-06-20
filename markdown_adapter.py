"""
Software API adapter for markdown.py
This module provides a function based API to markdown.py
since markdown.py only provides a CLI.
"""

from subprocess import Popen, PIPE, STDOUT
from tempfile import NamedTemporaryFile


def run_markdown(input_text):
    """
    The default method when we don't care which method to use.
    """
    return run_markdown_pipe(input_text)


def run_markdown_pipe(input_text):
    """
    Simulate: echo 'some input' | python markdown.py
    """
    pipe = Popen(["python", "markdown.py"], stdout=PIPE, stdin=PIPE, stderr=STDOUT)
    output = pipe.communicate(input=input_text.encode("utf-8"))[0]
    output_text = output.rstrip().decode("utf-8")
    return output_text.rstrip()


def run_markdown_file(input_text):
    """
    Simulate: python markdown.py fileName
    """
    temp_file = NamedTemporaryFile(delete=False)
    temp_file.write(input_text.encode("utf-8"))
    temp_file.close()
    pipe = Popen(
        ["python", "markdown.py", temp_file.name],
        stdout=PIPE,
        stdin=None,
        stderr=STDOUT,
    )
    output = pipe.communicate()[0]
    output_text = output.rstrip().decode("utf-8")
    return output_text.rstrip()


if __name__ == "__main__":
    input_text = "This is a **test** with *emphasis* and __strong__ text."
    print(run_markdown(input_text))
    print(run_markdown_file(input_text))
    print(run_markdown_pipe(input_text))
