adjacent = ((1, 2),  #  A
        (0, 2, 3),  #  B
        (0, 1, 4),  #  C
        (1, 4, 5),  #  D
        (2, 3, 6),  #  E
        (3,),  #  F
        (1,))  #  G


def search(goal, path):
    n = path[len(path) - 1]
    if n == goal:
        print path
    else:
        for x in adjacent[n]:
            if x not in path:
                path.append(x)
                search(goal, path)
                path.pop()


search(6, [0])
print '-----'
search(6, [0, 1])
