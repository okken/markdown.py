# Markdown.py
# First attempt
# - just print whatever is passed in to stdin
# - if filename passed in, print file instead of stdin

import fileinput
for line in fileinput.input():
    print line,  # print the line, the comma says don't add a newline
