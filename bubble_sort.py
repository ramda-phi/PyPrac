import random


def bubble_sort(buff):
    k = len(buff) - 1
    for i in xrange(k):
        for j in xrange(k, i, -1):
            if buff[j - 1] > buff[j]:
                temp = buff[j]
                buff[j] = buff[j - 1]
                buff[j - 1] = temp


x = 8000

# random
a = [random.randint(0, 100000) for y in xrange(x)]
b = range(x)
c = range(x, 0, -1)
d = range(x / 2) + range(x / 2, 0, -1)
