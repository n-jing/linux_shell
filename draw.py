#! /usr/bin/python3


# plot data read from file. the data in the file must be in the form of
# any "tag numeric", "tag numeric numeric" or "numeric".


import numpy as np
import sys
import matplotlib.pyplot as plt


def FileColumn(path):
    fp = open(path, 'r')
    line = fp.readline()
    fp.close()
    line = line.split()
    return len(line)

col_num = FileColumn(sys.argv[1])
if (col_num == 2):
    p = np.loadtxt(sys.argv[1], usecols=(1))
elif (col_num == 3):
    p = np.loadtxt(sys.argv[1], usecols=(1, 2))
else:
    p = np.loadtxt(sys.argv[1], usecols=(0))
    
if (col_num == 3):
    x = p[:, 0]
    y = p[:, 1]
else:
    if (len(sys.argv) == 2):
        x = np.linspace(0, 1, len(p))
        y = p
    else:
        x = p
        c_num = FileColumn(sys.argv[2])
        if c_num == 1:
            y = np.loadtxt(sys.argv[2], usecols=(0))
        else:
            y = np.loadtxt(sys.argv[2], usecols=(1))



plt.plot(x, y)
plt.show()


# import re
# numeric_const_pattern = '[-+]? (?: (?: \d* \. \d+ ) | (?: \d+ \.? ) )(?: [Ee] [+-]? \d+ ) ?'
# numeric_find = re.compile(numeric_const_pattern, re.VERBOSE)
# result = numeric_find.findall("Sound Level: -.7 db or 15.2 or 3.1e-2 db")
