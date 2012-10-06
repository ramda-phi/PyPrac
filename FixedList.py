from LinkedList import LinkedList
#import Enumerable


class FixedList(LinkedList):
    def __init__(self, limit, *args):
        self.limit = limit
        self.size = 0
        LinkedList.__init__(self, *args[:limit])

    def insert(self, n, x):
        if self.size < self.limit:
            result = LinkedList.insert(self, n, x)
            if result is not None:
                self.size += 1
            return result
        return None

    def delete(self, n):
        if self.size > 0:
            result = LinkedList.delete(self, n)
            if result is not None:
                self.size -= 1
            return result
        return None
