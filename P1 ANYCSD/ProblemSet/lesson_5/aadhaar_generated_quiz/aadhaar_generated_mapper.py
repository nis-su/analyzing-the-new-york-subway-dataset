import sys
import string

def mapper():
    for line in sys.stdin:
        data = line.strip().split(",")
        if len(data) !=12 or data[0] == 'Registrar':
            continue
        print "{0}\t{1}".format(data[3], data[8])
        
mapper()