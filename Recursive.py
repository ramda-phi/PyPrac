tarai = {}


class Memoize:
    def __init__(self, func):
        self.table = {}
        self.f = func

    def __call__(self, *args):
        if not args in self.table:
            self.table[args] = self.f(*args)
        return self.table[args]


@Memoize
def tarai(x, y, z):
    if x <= y:
        return y
    return tarai(tarai(x - 1, y, z),
            tarai(y - 1, z, x),
            tarai(z - 1, x, y))


# Lazy Evaluation with closure
def tarai_d(x, y, z):
    if x <= y:
        return y
    zz = z()
    return tarai_d(tarai_d(x - 1, y, lambda: zz),
            tarai_d(y - 1, zz, lambda: x),
            lambda: tarai(zz - 1, x, lambda: y))


# Lazy Evaluation
def tarai_lazy(x, y, xx, yy, zz):
    if x <= y:
        return y
    z = tarai_le(xx, yy, zz)
    return tarai_lazy(tarai(x - 1, y, z),
            tarai_le(y - 1, z, x),
            z - 1, x, y)


def tarai_le(x, y, z):
    if x <= y:
        return y
    return tarai_lazy(tarai_le(x - 1, y, z),
            tarai_le(y - 1, z, x),
            z - 1, x, y)
