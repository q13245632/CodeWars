# -*- coding:utf-8 -*-
# author: yushan
# date: 2017-03-27

from itertools import tee, islice

def times(n, generator):
    for i in generator:
        yield n * i

def merge(gen1, gen2):
    ngen1 = gen1.next()
    ngen2 = gen2.next()
    while 1:
        if ngen1 < ngen2:
            yield ngen1
            ngen1 = gen1.next()
        elif ngen2 < ngen1:
            yield ngen2
            ngen2 = gen2.next()
        else:
            yield ngen1
            ngen1 = gen1.next()
            ngen2 = gen2.next()

def hamming(n):
    def _hamming():
        yield 1
        for n in merge(times(2, m2),
                       merge(times(3, m3),
                             times(5, m5))):
            yield n
    m1 = _hamming()
    m2, m3, m5, mres = tee(m1, 4)
    return next(islice(mres, n-1, None), None)


def hamming(n):
    bases = [2, 3, 5]
    expos = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[expos[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            expos[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]


test.expect(hamming(1) == 1, "hamming(1) should be 1");
test.expect(hamming(2) == 2, "hamming(2) should be 2");
test.expect(hamming(3) == 3, "hamming(3) should be 3");
test.expect(hamming(4) == 4, "hamming(4) should be 4");
test.expect(hamming(5) == 5, "hamming(5) should be 5");
test.expect(hamming(6) == 6, "hamming(6) should be 6");
test.expect(hamming(7) == 8, "hamming(7) should be 8");
test.expect(hamming(8) == 9, "hamming(8) should be 9");
test.expect(hamming(9) == 10, "hamming(9) should be 10");
test.expect(hamming(10) == 12, "hamming(10) should be 12");
test.expect(hamming(11) == 15, "hamming(11) should be 15");
test.expect(hamming(12) == 16, "hamming(12) should be 16");
test.expect(hamming(13) == 18, "hamming(13) should be 18");
test.expect(hamming(14) == 20, "hamming(14) should be 20");
test.expect(hamming(15) == 24, "hamming(15) should be 24");
test.expect(hamming(16) == 25, "hamming(16) should be 25");
test.expect(hamming(17) == 27, "hamming(17) should be 27");
test.expect(hamming(18) == 30, "hamming(18) should be 30");
test.expect(hamming(19) == 32, "hamming(19) should be 32");