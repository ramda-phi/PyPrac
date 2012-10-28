adjacent = ((1, 2),  #  A
        (0, 2, 3),  #  B
        (0, 1, 4),  #  C
        (1, 4, 5),  #  D
        (2, 3, 6),  #  E
        (3,),  #  F
        (1,))  #  G


def id_search(limit, goal, path):
    n = len(path)
    m = path[n - 1]
    if n == limit:
        if m == goal:
            print path
    else:
        for x in adjacent[m]:
            if x not in path:
                path.append(x)
                id_search(limit, goal, path)
                path.pop()


print '-----'
for x in range(1, 8):
    print x, 'moves'
    id_search(x, 6, [0])
