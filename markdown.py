"""
Markdown.py
1. just print whatever is passed in to stdin
2. if filename passed in as a command line parameter,
   then print file instead of stdin
3. wrap input in paragraph tags
4. convert single asterisk or underscore pairs to em tags
5. convert double asterisk or underscore pairs to strong tags

"""

import fileinput
import re


def convertStrong(line):
    line = re.sub(r"\*\*(.*)\*\*", r"<strong>\1</strong>", line)
    line = re.sub(r"__(.*)__", r"<strong>\1</strong>", line)
    return line


def convertEm(line):
    line = re.sub(r"\*(.*)\*", r"<em>\1</em>", line)
    line = re.sub(r"_(.*)_", r"<em>\1</em>", line)
    return line


for line in fileinput.input(encoding="utf-8"):
    line = line.rstrip()
    line = convertStrong(line)
    line = convertEm(line)
    print(f"<p>{line}</p>")
