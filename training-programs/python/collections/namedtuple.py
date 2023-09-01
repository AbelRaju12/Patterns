from collections import namedtuple

Point = namedtuple('Point', 'x,y,z')
pt = Point(5, 6, 7)
print(pt)
print(pt.y)