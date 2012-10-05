# from www.geocities.jp/m_hiroi/light/python05.html
#
# Usage:
#
#   import .../LinkedList
#   a = LinkedList.LinkedList()


class LinkedList:

    class Cell:
        def __init__(self, data, link=None):
            self.data = data
            self.link = link

    def __init__(self, *args):
        self.top = LinkedList.Cell(None)  # header cell
        for x in reversed(args):
            self.insert(0, x)

    # look for _nth element
    def _nth(self, n):
        i = -1
        cp = self.top
        while cp is not None:
            if i == n:
                return cp
            i += 1
            cp = cp.link
        return None

    # look for nth element
    def at(self, n):
        cp = self._nth(n)
        if cp is not None:
            return cp.data
        return None

    # Insert data
    def insert(self, n, x):
        cp = self._nth(n - 1)
        if cp is not None:
            cp.link = LinkedList.Cell(x, cp.link)
            return x
        return None

    # Delete data
    def delete(self, n):
        cp = self._nth(n - 1)
        if cp is not None and cp.link is not None:
            data = cp.link.data
            cp.link = cp.link.link
            return data
        return None

    # Empty or not
    def isEmpty(self):
        cp = self._nth(0)
        if cp is None:
            return True
        else:
            return False

    # init iterator
    def __iter__(self):
        self.index = self.top.link
        return self

    # 'next' method
    def next(self):
        if self.index is None:
            raise StopIteration
        data = self.index.data
        self.index = self.index.link
        return data

    # iter => generator
    def each(self):
        cp = self.top.link
        while cp is not None:
            yield cp.data
            cp = cp.link

    # Overload 'len()'
    def __len__(self):
        n = 0
        for _ in self.each():
            n += 1
        return n

    # Overload 'print'
    def __str__(self):
        if self.top.link is None:
            return 'LList()'
        s = 'LList('
        for x in self.each():
            s += '%s, ' % x
        return s[:-2] + ')'

    # Overload 'L[n]'
    def __getitem__(self, n):
        cp = self._nth(n)
        if cp is not None:
            return cp.data
        raise IndexError

    # Overload 'L[n] = x'
    def __setitem__(self, n, x):
        cp = self._nth(n)
        if cp is not None:
            cp.data = x
            return None
        raise IndexError

    # Overload 'del L[n]'
    def __delitem__(self, n):
        if self.delete(n) is None:
            raise IndexError

    # Overload 'x + y'
    def __add__(x, y):
        # copy list
        def copy(a):
            if not a:
                return None
            return LinkedList.Cell(a.data, copy(a.link))

        # link list
        def append(a, b):
            if a is None:
                return copy(b)
            return LinkedList.Cell(a.data, append(a.link, b))

        if not isinstance(y, LinkedList):
            raise NotImplementedError
        z = LinkedList()
        z.top.link = append(x.top.link, y.top.link)
        return z
