class Queue:
    class Cell:
        def __init__(self, data, link=None):
            self.data = data
            self.link = link

    def __init__(self):
        self.size = 0
        self.front = None
        self.rear = None

    def enqueue(self, x):
        if self.size == 0:
            self.front = self.rear = Queue.Cell(x)
        else:
            new_cell = Queue.Cell(x)
            self.rear.link = new_cell
            self.rear = new_cell
        self.size += 1

    def dequeue(self):
        if self.size == 0:
            raise IndexError
        value = self.front.data
        self.front = self.front.link
        self.size -= 1
        if self.size == 0:
            self.rear = None
        return value

    def isEmpty(self):
        return self.size == 0
