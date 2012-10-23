# None: etmpty$
# (): delete$
# data: (key, value)$


class HashTable3:
    def __init__(self, func, size):
        self.size = 0
        self.hash_size = size
        self.hash_func = func
        self.hash_table = [None] * size

    def _hash_func(self, key):
        n = self.hash_func(key)
        return (n % self.hash_size, 7 - n % 7)

    def _search_key(self, key):
        n, i = self._hash_func(key)
        count = 0
        while count < self.hash_size:
            data = self.hash_table[n]
            if data is None:
                break
            if data and data[0] == key:
                return n
            # double hashing
            n = (n + i) % self.hash_size
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
            n, i = self._hash_func(key)
            count = 0
            while count < self.hash_size:
                    if not self.hash_table[n]:
                        self.size += 1
                        break
                    # double hashing
                    n = (n + i) % self.hash_size
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
            value = self.hash_table[n][1]
            self.hash_table[n] = ()
        return value

    def traverse(self):
        for data in self.hash_table:
            if data:
                yield data

    def __len__(self):
        return self.size
