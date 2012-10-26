import Set


s = Set
a = s.Set([1, 2, 3, 4, 5])
b = s.Set([4, 5, 6, 7, 8])
print a
print b
c = a.union(b)
print c
d = a.intersection(b)
print d
e = a.difference(b)
print e
print a.issubset(c)
print c.issubset(a)
print a.isequal(a)
a.insert(1)
print a
a.insert(10)
print a
b.remove(5)
print b
print c
print '-----'
f = b.union(a)
