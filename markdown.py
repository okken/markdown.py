"""
 Markdown.py
 0 just print whatever is passed in to stdin
 0 if filename passed in as a command line parameter, 
   then print file instead of stdin
 1 wrap input in paragraph tags
"""

import fileinput

for line in fileinput.input():
     print '<p>' + line + '</p>',

