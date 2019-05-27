'''
Following Script when run will interactively display text files or parts of a string
utility can be used to view documentation or text 

@author: M.Brohi
'''
from pip._vendor.pyparsing import line #if python v3
import sys

def more(text, numlines=15):
    lines = text.split('/n')
    while lines:
        chunk = lines[:numlines]
        lines = lines[numlines:]
        for line in chunk : print line "More?y"
        
        if lines and input('More?') not in ['y' , 'Y']: break
        
if __name__ == '__main__':
    
    more(open(sys.argv[1]).read(),10)