import random
import Double_Hashing


hs = 11


def hf(key):
    value = 0
    for x in key:
        value = (value << 3) + x
    return value

ht = Double_Hashing.HashTable3(hf, hs)
count = 1
keys = [(random.randint(0, 255), random.randint(0, 255)) for x in xrange(11)]
print keys
for x in keys:
    if not ht.search(x):
        ht.insert(x, count)
        count += 1
for x, y in ht.traverse():
    print x, y
print '-----'
for x in keys:
    ht.insert(x, count)
    count += 1
for x, y in ht.traverse():
    print x, y
print '-----'
for x in keys:
    print ht.search(x),
    print ht.delete(x),
    print ht.search(x),
    print len(ht)
