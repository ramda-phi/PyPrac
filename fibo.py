class Fibo():
    def __init__(self):
        self.a1 = 0
        self.a2 = 1

    def __call__(self):
        n = self.a1 + self.a2
        self.a2 = self.a1
        self.a1 = n
        return n
