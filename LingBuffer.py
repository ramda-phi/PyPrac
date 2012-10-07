class LingBuffer:
    def __init__(self, n=16):
        self.size = n
        self.buff = [None] * n
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, x):
        if self.count == self.size:
            raise IndexError
        self.buff[self.rear] = x
        self.rear += 1
        if self.rear == self.size:
            self.rear = 0
        self.count += 1

    def dequeue(self):
        if self.count == 0:
            raise IndexError
        data = self.buff[self.front]
        self.front += 1
        if self.front == self.size:
            self.front = 0
        self.count -= 1
        return data

    def peek(self):
        if self.count == 0:
            raise IndexError
        return self.buff[self.front]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size

    def __str__(self):
        if self.count == 0:
            return 'Queue()'
        buff = 'Queue('
        n = self.count
        i = self.front
        while n > 1:
            buff += '%s, ' % self.buff[i]
            i += 1
            if i == self.size:
                i = 0
            n -= 1
        buff += '%s)' % self.buff[i]
        return buff


if __name__ == '__main__':
    q = LingBuffer(8)
    x = 0
    while not q.isFull():
        q.enqueue(x)
        x += 1
    while not q.isEmpty():
        print q.dequeue()
        print q
