# http://www.geocities.jp/m_hiroi/light/pyalgo27.html


import RingBuffer


adjacent = (
        (1, 3),  # 0
        (0, 2, 4),  # 1
        (1, 5),  # 2
        (0, 4, 6),  # 3
        (1, 3, 5, 7),  # 4
        (2, 4, 8),  # 5
        (3, 7),  # 6
        (4, 6, 8),  # 7
        (5, 7)  # 8
        )

GOAL = [1, 2, 3, 4, 5, 6, 7, 8, 0]
SIZE = 181440


# Breadth-First Search
class State:
    def __init__(self, board, space, prev):
        self.board = board
        self.space = space
        self.prev = prev


def bf_search(start):
    r = RingBuffer
    q = r.Queue(SIZE)
    q.enqueue(State(start, start.index(0), None))
    table = {}
    table[tuple(start)] = True
    while not q.isEmpty():
        a = q.dequeue()
        for x in adjacent[a.space]:
            b = a.board[:]
            b[a.space] = b[x]
            b[x] = 0
            key = tuple(b)
            if key in table:
                continue
            c = State(b, x, a)
            if b == GOAL:
                print_answer(c)
                return
            q.enqueue(c)
            table[key] = True


def print_answer(x):
    if x is not None:
        print_answer(x.prev)
        print x.board


#if __name__ == '__main__':
#    bf_search([8, 6, 7, 2, 5, 4, 3, 0, 1])


# bi_directional search
FORE = 1
BACK = 0


class State0:
    def __init__(self, board, space, prev, dir):
        self.board = board
        self.space = space
        self.prev = prev
        self.dir = dir


def bi_search(start):
    r = RingBuffer
    q = r.Queue(SIZE)
    table = {}
    a = State0(start, start.index(0), None, FORE)
    q.enqueue(a)
    table[tuple(start)] = a
    a = State0(GOAL, GOAL.index(0), None, BACK)
    q.enqueue(a)
    table[tuple(GOAL)] = a
    while not q.isEmpty():
        a = q.dequeue()
        for x in adjacent[a.space]:
            b = a.board[:]
            b[a.space] = b[x]
            b[x] = 0
            key = tuple(b)
            if key in table:
                c = table[key]
                if c.dir != a.dir:
                    # Found!
                    print_answer1(a, c)
                    return
            else:
                c = State0(b, x, a, a.dir)
                q.enqueue(c)
                table[key] = c


def print_answer_goal(a):
    while a is not None:
        print a.board
        a = a.prev


def print_answer1(a, b):
    if a.dir == FORE:
        print_answer(a)
        print_answer_goal(b)
    else:
        print_answer(b)
        print_answer_goal(a)


#if __name__ == '__main__':
#    bi_search([8, 6, 7, 2, 5, 4, 3, 0, 1])


#  the longest


class State00:
    def __init__(self, board, space, prev, move):
        self.board = board
        self.space = space
        self.prev = prev
        self.move = move


def search_longest_move():
    buff = [None] * SIZE
    a = State00(GOAL, GOAL.index(0), None, 0)
    buff[0] = a
    front = 0
    rear = 1
    table = {}
    table[tuple(GOAL)] = a
    while front < rear:
        a = buff[front]
        for x in adjacent[a.space]:
            b = a.board[:]
            b[a.space] = b[x]
            b[x] = 0
            key = tuple(b)
            if key in table:
                continue
            c = State00(b, x, a, a.move + 1)
            buff[rear] = c
            rear += 1
            table[key] = c
        front += 1
    n = SIZE - 1
    move = buff[n].move
    print 'move=', move
    while buff[n].move == move:
        print buff[n].board
        n -= 1


#if __name__ == '__main__':
#    search_longest_move()


# Iterative Deeping


board = [8, 6, 7, 2, 5, 4, 3, 0, 1]
move_piece = [None] * 32


def id_search(limit, move, space):
    if move == limit:
        if board == GOAL:
            global count
            count += 1
            print move_piece[1:]
    else:
        for x in adjacent[space]:
            p = board[x]
            if move_piece[move] == p:
                continue
            # move piece
            board[space] = p
            board[x] = 0
            move_piece[move + 1] = p
            id_search(limit, move + 1, x)
            # reset
            board[space] = 0
            board[x] = p


count = 0
#import time
#s = time.clock()
#for x in xrange(1, 32):
#    print 'move ', x
#    id_search(x, 0, board.index(0), [-1])
#    if count > 0:
#        break
#e = time.clock()
#print "%.3f" % (e - s)


# Lower Bound


distance = (
        (),
        (0, 1, 2, 1, 2, 3, 2, 3, 4),
        (1, 0, 1, 2, 1, 2, 3, 2, 3),
        (2, 1, 0, 3, 2, 1, 4, 3, 2),
        (1, 2, 3, 0, 1, 2, 1, 2, 3),
        (2, 1, 2, 1, 0, 1, 2, 1, 2),
        (3, 2, 1, 2, 1, 0, 3, 2, 1),
        (2, 3, 4, 1, 2, 3, 0, 1, 2),
        (3, 2, 3, 2, 1, 2, 1, 0, 1)
        )


def get_distance(board):
    v = 0
    for x in xrange(9):
        p = board[x]
        if p == 0:
            continue
        v += distance[p][x]
    return v


def id_lower_search(limit, move, space, lower):
    if move == limit:
        if board == GOAL:
            global count
            count += 1
            print move_piece[1:]
    else:
        for x in adjacent[space]:
            p = board[x]
            if move_piece[move] == p:
                continue
            # move piece
            board[space] = p
            board[x] = 0
            move_piece[move + 1] = p
            new_lower = lower - distance[p][x] + distance[p][space]
            # lower-bound search
            if new_lower + move <= limit:
                id_lower_search(limit, move + 1, x, new_lower)
            # reverse
            board[space] = 0
            board[x] = p


count = 0
import time
s = time.clock()
n = get_distance(board)
for x in xrange(n, 32):
    print 'move', x
    id_lower_search(x, 0, board.index(0), n)
    if count > 0:
        break
e = time.clock()
print "%.3f" % (e - s)
