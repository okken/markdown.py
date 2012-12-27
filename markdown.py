"""
 Markdown.py
 First attempt
 - just print whatever is passed in to stdin
 - if filename passed in as a command line parameter, 
   then print file instead of stdin
"""

import fileinput

for line in fileinput.input():
    print line,  

