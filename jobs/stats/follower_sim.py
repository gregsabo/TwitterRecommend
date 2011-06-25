# import code from Divisi2, a sparse matrix machine-learning library
# from the Media Lab
# (http://csc.media.mit.edu/docs/divisi2)
import divisi2
import numpy as np
from csc_utils.ordered_set import OrderedSet

fakebands = OrderedSet([])

file = open('social-graph.small')
for line in file:
    band, fan = line.strip().split()
    fakebands.add(band)

NBANDS = len(fakebands)
NBITS = 12
MODULO = 1<<NBITS
print NBANDS

matrix = divisi2.DenseMatrix(
    np.zeros((NBANDS, MODULO)),
    row_labels = fakebands
)

file.seek(0)
counter = 0
for line in file:
    band, fan = line.strip().split()
    row = matrix.row_labels.index(band)
    col = hash(fan) % MODULO
    matrix[row,col] += 1
    counter += 1
    if counter % 1000 == 0:
        print counter
file.close()

U, S, V = matrix.normalize_rows(offset=0.01).svd(k=20)
similarity = U * S
divisi2.save(similarity, 'similarity.mat')
