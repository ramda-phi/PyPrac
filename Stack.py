from LinkedList import LinkedList


class Stack:
    def __init__(self):
        self.content = LinkedList()

    def push(self, x):
        self.content.insert(0, x)

    def pop(self):
        return self.content.delete(0)

    def top(self):
        return self.content[0]

    def isEmpty(self):
        return self.content.isEmpty()
