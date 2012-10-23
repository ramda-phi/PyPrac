class HashTable2:
    def __init__(self, func, size):
        self.size = 0
        self.hash_size = size
        self.hash_func = func
        self.hash_table = [None] * size

    def _hash_func(self, key):
        return self.hash_func(key) % self.hash_size

    def _search_key(self, key):
        n = self._hash_func(key)
        count = 0
        while count < self.hash_size:
            data = self.hash_table[n]
            if data is None:
                break
            if data and data[0] == key:
                return n
            #linear probing
            n = (n + 1) % self.hash_size
            count += 1
        return -1

    def search(self, key):
        n = self._search_key(key)
        if n >= 0:
            return self.hash_table[n][1]
        return None

    def insert(self, key, value):
        n = self._search_key(key)
        if n < 0:
            n = self._hash_func(key)
            count = 0
            while count < self.hash_size:
                if not self.hash_table[n]:
                    self.size += 1
                    break
                # linear probing
                n = (n + 1) % self.hash_size
                count += 1
            else:
                raise IndexError
        # insert
        self.hash_table[n] = (key, value)
        return value

    def delete(self, key):
        n = self._search_key(key)
        value = None
        if n >= 0:
            value - self.hash_table[n][1]
            self.hash_table[n] = ()
            self.size -= 1
        return value

    def traverse(self):
        for data in self.hash_table:
            if data:
                yield data

    def __len__(self):
        return self.size
