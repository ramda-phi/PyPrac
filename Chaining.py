class HashTable:
    class Cell:
        def __init__(self, key, value, cp=None):
            self.key = key
            self.value = value
            self.next = cp

    def __init__(self, func, size):
        self.size = 0
        self.hash_size = size
        self.hash_table = [None] * size
        self.hash_func = func

    def _hash_func(self, x):
        return self.hash_func(x) % self.hash_size

    def _search(self, key):
        n = self._hash_func(key)
        cp = self.hash_table[n]
        while cp:
            if cp.key == key:
                return (True, cp)
            cp = cp.next
        return (False, n)

    def search(self, key):
        x, y = self._search(key)
        if x:
            return y.value
        return None

    def insert(self, key, value):
        x, y = self._search(key)
        if x:
            y.value = value
        else:
            cp = HashTable.Cell(key, value, self.hash_table[y])
            self.hash_table[y] = cp
            self.size += 1
        return value

    def delete(self, key):
        n = self._hash_func(key)
        cp = self.hash_table[n]
        value = None
        if cp:
            if cp.key == key:
                value = cp.value
                self.hash_table[n] = cp.next
                self.size -= 1
            else:
                while cp.next:
                    if cp.next.key == key:
                        value = cp.next.value
                        cp.next = cp.next.next
                        self.size -= 1
                        break
                    cp = cp.next
        return value

    def traverse(self):
        for cp in self.hash_table:
            while cp:
                yield (cp.key, cp.value)
                cp = cp.next

    def __len__(self):
        return self.size


if __name__ == '__main__':
    import random
    hs = 11

    def hf(key):
        value = 0
        for x in key:
            value = (value << 3) + x
        return value

    ht = HashTable(hf, hs)
    count = 1
    keys = [(random.randint(0, 255), random.randint(0, 255))
            for x in xrange(15)]
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
