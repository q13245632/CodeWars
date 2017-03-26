# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-21


import math
class Sudoku(object):
    #your code here
    def __init__(self,arr):
        self.object = arr
    def is_valid(self):
        self.row = len(self.object)
        if not all(len(i) == self.row for i in self.object):
            return False
        all_set = set(xrange(1,self.row+1))
        if not all(set(i) == all_set for i in self.object):
            return False
        all_cols = [[x[i] for x in self.object if str(x[i]).isdigit()] for i in xrange(self.row)]
        if not all(set(i) == all_set for i in all_cols):
            return False
        self.n = int(math.sqrt(self.row))
        all_littles = [[self.object[i][k] for i in xrange(p,self.n+p) for k in xrange(j,self.n+j)] for j in xrange(0,self.row,self.n) for p in xrange(0,self.row,self.n)]
        if not all(set(i) == all_set for i in all_littles):
            return False
        return True


# goodSudoku1 = Sudoku([
#     [7, 8, 4, 1, 5, 9, 3, 2, 6],
#     [5, 3, 9, 6, 7, 2, 8, 4, 1],
#     [6, 1, 2, 4, 3, 8, 7, 5, 9],
#
#     [9, 2, 8, 7, 1, 5, 4, 6, 3],
#     [3, 5, 7, 8, 4, 6, 1, 9, 2],
#     [4, 6, 1, 9, 2, 3, 5, 8, 7],
#
#     [8, 7, 6, 3, 9, 4, 2, 1, 5],
#     [2, 4, 3, 5, 6, 1, 9, 7, 8],
#     [1, 9, 5, 2, 8, 7, 6, 3, 4]
# ])
#
# print goodSudoku1.is_valid()
#
#
# # Invalid Sudoku
# badSudoku1 = Sudoku([
#     [0, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9],
#     [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ])

import numpy as np


class Sudoku(object):
    def __init__(self, theArray):
        self.grid = np.array(theArray)
        self.listgrid = theArray

        self.N = len(theArray)
        self.M = len(theArray[0])

    def has_valid_size(self):

        if isinstance(self.listgrid[0][0], bool): return False
        if self.grid.shape == (1, 1):
            return True
        for i in self.listgrid:
            if len(i) != self.N: return False
        return True

    # your code here
    def is_valid(self):
        if not self.has_valid_size():
            return False

        seqs2check = [self.getRowsIterator(), self.getColsIterator(), self.getSquaresIterator()]
        for it in seqs2check:
            for seq in it:
                if self.checkSeq(seq) == False:
                    return False
        return True

    def getRowsIterator(self):
        for i in range(self.N):
            yield self.grid[i, :]

    def getColsIterator(self):
        for i in range(self.N):
            yield self.grid[:, i]

    def getSquaresIterator(self):
        squareSize = int(np.sqrt(self.N))
        for i in range(squareSize):
            for j in range(squareSize):
                ix1 = i * squareSize
                ix2 = j * squareSize
                yield self.grid[ix1:ix1 + squareSize, ix2:ix2 + squareSize].flatten()

    def checkSeq(self, seq):
        return sorted(seq) == range(1, self.N + 1)