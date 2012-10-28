adjacent = ((1, 2),  #  A
        (0, 2, 3),  #  B
        (0, 1, 4),  #  C
        (1, 4, 5),  #  D
        (2, 3, 6),  #  E
        (3,),  #  F
        (1,))  #  G


def bf_search(start, goal):
    q = [[start]]
    while len(q) > 0:
        #  Deque
        path = q.pop(0)
        n = path[len(path) - 1]
        if n == goal:
            print path
        else:
            for x in adjacent[n]:
                if x not in path:
                    new_path = path[:]
                    new_path.append(x)
                    #  Enqueue
                    q.append(new_path)


print '-----'
bf_search(0, 6)
