class Queue:
    # define Cell
    class Cell:
        def __init__(self, x, y=None):
            self.data = x
            self.next = y

    def __init__(self):
        self.size = 0
        self.rear = None

    def enqueue(self, x):
        if self.size == 0:
            self.rear = Queue.Cell(x)
            self.rear.next = self.rear  # <- Circular List
        else:
            new_cell = Queue.Cell(x, self.rear.next)
            self.rear.next = new_cell
            self.rear = new_cell
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError
        front = self.rear.next
        self.rear.next = front.next
        self.size -= 1
        if self.size == 0:
            self.rear = None
        return front.data

    def rotate(self, n=1):
        if self.size == 0 or n < 1:
            raise IndexError
        while n > 0:
            self.rear = self.rear.next
            n -= 1

    def isEmpty(self):
        return self.size == 0

    def peek(self):
        if self.size == 0:
            raise IndexError
        return self.rear.next.data

    def __str__(self):
        if self.size == 0:
            return 'Queue()'
        cp = self.rear.next
        n = self.size
        buff = 'Queue('
        while n > 1:
            buff += '%s, ' % cp.data
            cp = cp.next
            n -= 1
        buff += '%s)' % cp.data
        return buff


if __name__ == '__main__':
    q = Queue()
    print q.isEmpty()
    for x in range(5):
        q.enqueue(x)
    print q
    q.rotate()
    print q.peek()
    q.rotate()
    print q.peek()
    q.rotate()
    print q.peek()
    q.rotate()
    print q.peek()
    q.rotate()
    print q.peek()
    while not q.isEmpty():
        print q.dequeue()
        print q
    print q
