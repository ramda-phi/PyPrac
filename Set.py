class Set:
    class Cell:
        def __init__(self, x, next=None):
            self.item = x
            self.next = next

    def __init__(self, data=None):
        self.top = Set.Cell(None)  # Header Cell
        if data:
            for x in data:
                if not self.member(x):
                    self.top.next = Set.Cell(x, self.top.next)

    def member(self, x):
        cp = self.top.next
        while cp:
            if cp.item == x:
                return True
            cp = cp.next
        return False

    def insert(self, x):
        if not self.member(x):
            self.top.next = Set.Cell(x, self.top.next)

    def issubset(self, x):
        cp = self.top.next
        while cp:
            if not x.member(cp.item):
                return False
            cp = cp.next
        return True

    def isequal(self, x):
        return self.issubset(x) and x.issubset(self)

    def union(self, x):
        def _union(cp):
            if cp is None:
                return x.top.next
            elif x.member(cp.item):
                return _union(cp.next)
            else:
                return Set.Cell(cp.item, _union(cp.next))

        s = Set()
        s.top.next = _union(self.top.next)
        return s

    def intersection(self, x):
        def _intersection(cp):
            if cp is None:
                return None
            elif x.member(cp.item):
                return Set.Cell(cp.item, _intersection(cp.next))
            else:
                return _intersection(cp.next)
        s = Set()
        s.top.next = _intersection(self.top.next)
        return s

    def difference(self, x):
        def _difference(cp):
            if cp is None:
                return None
            elif x.member(cp.item):
                return _difference(cp.next)
            else:
                return Set.Cell(cp.item, _difference(cp.next))
        s = Set()
        s.top.next = _difference(self.top.next)
        return s

    def remove(self, x):
        def _remove(cp):
            if cp is None:
                return None
            elif cp.item == x:
                return cp.next
            else:
                return Set.Cell(cp.item, _remove(cp.next))
        self.top.next = _remove(self.top.next)

    def traverse(self):
        cp = self.top.next
        while cp:
            yield cp.item
            cp = cp.next

    def __len__(self):
        n = 0
        cp = self.top.next
        while cp:
            n += 1
            cp = cp.next
        return n

    def __str__(self):
        cp = self.top.next
        if cp is None:
            return 'Set([])'
        buff = 'Set(['
        while cp.next:
            buff += '%s, ' % cp.item
            cp = cp.next
        buff += '%s)]' % cp.item
        return buff
