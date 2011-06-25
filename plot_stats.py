"""
Code to plot stats
"""

# twitter id  - followers  - followees

import os
import sys
import pylab as P
import numpy as np


if __name__ == '__main__':

    filename = sys.argv[1]
    assert os.path.isfile(filename)

    # read data
    data = []
    f = open(filename)
    for line in f.xreadlines():
        if line == '' or line.strip() == '':
            continue
        print line.strip().split('\t')
        data.append(map(lambda x: int(x), line.strip().split('\t')))
    f.close()

    # order by followers
    order = np.argsort(np.array(map(lambda x: x[1], data)))[-1::-1]
    data = np.array(data)[order]

    P.figure()
    P.plot([d[1] for d in data], label='followers')
    P.title('Artist followers')
    P.legend(loc='upper right')
    P.show(False)

    P.figure()
    P.plot([d[2] for d in data], 'r', label='followees')
    P.title('Artist followees')
    P.legend(loc='upper right')
    P.show(True)
