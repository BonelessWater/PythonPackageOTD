'''
Day 1, June 4th 2025: 

Welcome to pprint.py, straight from the Python standard library!

They say not to judge a book by its cover, but if you did, judge 
it with pprint. From ugly mumbo jumbo to beautiful text straight 
to your terminal. Debugging has never been made easier.
'''

import pprint

test = [[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

print("Hard-to-read, default print")
print(test)

# Create a PrettyPrinter
pp = pprint.PrettyPrinter()

# This will print to stdout with proper indentation/line‐breaking
print("\nPretty printed output")
pp.pprint(test)

# This will return a string with proper indentation/line‐breaking
pretty_string = pp.pformat(test)
print("\nPretty printed string")
print(pretty_string)

# This will write to a file with proper indentation/line‐breaking
with open('pretty_output.txt', 'w') as f:
    pp = pprint.PrettyPrinter(stream=f)
    pp.pprint(test)

