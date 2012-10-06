class Enumerable:
    # Search
    def member(self, func):
        for x in self.each():
            if func(x):
                return x
        return False

    # Position
    def position(self, func):
        n = 0
        for x in self.each():
            if func(x):
                return n
            n += 1
        return -1

    # Count
    def count(self, func):
        a = []
        for x in self.each():
            if func(x):
                a.append(x)
        return n

    # Map
    def map(self, func):
        a = []
        for x in self.each():
            a.append(func(x))
        return a

    # Filter
    def filter(self, func):
        a = []
        for x in self.each():
            if func(x):
                a.append(x)
        return a

    # Fold
    def fold(self, func, init):
        a = init
        for x in self.each():
            a = func(a, x)
        return a
