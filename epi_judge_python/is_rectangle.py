import collections

Point = collections.namedtuple('Point', ('x', 'y'))

import collections
import math

Point = collections.namedtuple("Point", ("x", "y"))

def is_rectangle(p1: Point, p2: Point, p3: Point, p4: Point) -> bool:
    points = [p1, p2, p3, p4]

    cx = sum(p.x for p in points) / 4.0
    cy = sum(p.y for p in points) / 4.0

    points.sort(key=lambda p: math.atan2(p.y - cy, p.x - cx))

    def vec(a, b):
        return (b.x - a.x, b.y - a.y)

    v1 = vec(points[0], points[1])
    v2 = vec(points[1], points[2])
    v3 = vec(points[2], points[3])
    v4 = vec(points[3], points[0])

    def dot(u, v):
        return u[0]*v[0] + u[1]*v[1]

    def length2(v):
        return v[0]**2 + v[1]**2

    if not (dot(v1, v2) == 0 and dot(v2, v3) == 0 and dot(v3, v4) == 0 and dot(v4, v1) == 0):
        return False

    if not (length2(v1) == length2(v3) and length2(v2) == length2(v4)):
        return False

    return True


if __name__ == '__main__':
    p1 = Point(0, 0)
    p2 = Point(2, 0)
    p3 = Point(2, 1)
    p4 = Point(0, 1)
    # → True
    print(is_rectangle(p1, p2, p3, p4))

    p1 = Point(1, 1)
    p2 = Point(4, 1)
    p3 = Point(4, 4)
    p4 = Point(1, 4)
    # → True
    print(is_rectangle(p1, p2, p3, p4))


    p1 = Point(0, 0)
    p2 = Point(1, 1)
    p3 = Point(4, 1)
    p4 = Point(3, 0)
    # → False
    print(is_rectangle(p1, p2, p3, p4))

    p1 = Point(0, 0)
    p2 = Point(2, 1)
    p3 = Point(4, 1)
    p4 = Point(2, 0)
    # → False
    print(is_rectangle(p1, p2, p3, p4))

    p1 = Point(0, 0)
    p2 = Point(3, 0)
    p3 = Point(2, 1)
    p4 = Point(0, 1)
    # → False
    print(is_rectangle(p1, p2, p3, p4))

    p1 = Point(0, 0)
    p2 = Point(2, 0)
    p3 = Point(1, 2)
    p4 = Point(0, 1)
    # → False
    print(is_rectangle(p1, p2, p3, p4))

