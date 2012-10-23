import random
import time
import OpenAddress


hs = 10007


def hf(key):
    value = 0
    for x in key:
        value = (value << 3) + x
    return value


def make_data(n):
    ht = OpenAddress.HashTable2(hf, hs)
    while len(ht) < n:
        key = (random.randint(0, 255), random.randint(0, 255),
                random.randint(0, 255))
        ht.insert(key, True)
    return ht

for x in [5000, 6000, 7000, 8000, 9000, 10000]:
    start = time.clock()
    make_data(x)
    print x, time.clock() - start
