import sys
from itertools import islice
def p():
    
    cases = int(sys.stdin.readline())
    string = [i[:len(i) -1] for i in islice(sys.stdin, cases)]
    for i in string:
        ops, ans = [], []
        for c in i:
            if c in ['+', '-', '*', '/', '^']:
                ops.append(c)
            elif c == ')':
                ans.append(ops.pop())
            elif c == '(':
                pass
            else:
                ans.append(c)
        
        print ''.join(ans)
                
p()
        
