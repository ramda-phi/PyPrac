class Queue:
    def __init__(self, size):
        self.size = size
        self.buff = [None] * size
        self.front = 0
        self.rear = 0
        self.count = 0

    def enqueue(self, x):
        if self.count >= self.size:
            raise IndexError
        self.buff[self.rear] = x
        self.rear += 1
        self.count += 1
        if self.rear == self.size:
            self.rear = 0

    def dequeue(self):
        if self.count <= 0:
            raise IndexError
        x = self.buff[self.front]
        self.front += 1
        self.count -= 1
        if self.front == self.size:
            self.front = 0
        return x

    def isEmpty(self):
        return self.count == 0


#if __name__ == '__main__':
#    a = Queue(10)
#    for x in xrange(10):
#        a.enqueue(x)
#    while not a.isEmpty():
#        print a.dequeue()
