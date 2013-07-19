'''Created this file for placing all the signatures of functions in
functions.py into another file
_functions_signatures.py'''

import os
cur = os.getcwd()

read_file = cur + '\\functions.py'
write_file = cur + '\\__functions_signatures.py'

r = open(read_file)
w = open(write_file, 'w+')
try:
    temp = False
    num = 0
    for line in r:
        if line[0] == '#':
            num += 1
            num_str = "%04d" %num
            #Write the Function Number line without the ending newline
            w.write(line[2:len(line)-1] + num_str )
            temp = True
        elif temp == True:
            #Write the signature
            w.write(" " + line[4:])
            temp = False
finally:
    r.close()
    w.close()
