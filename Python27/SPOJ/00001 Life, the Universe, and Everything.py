import sys

def p():
    for line in sys.stdin:
        if int(line) - 42:
            print line
        else:
            break
        
p()
