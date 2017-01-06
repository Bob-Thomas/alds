class myqueue(list):
    def __init__(self, a=[]):
        list.__init__(self, a)

    def dequeue(self):
        return self.pop(0)

    def enqueue(self, x):
        self.append(x)


class Vertex:
    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return str(self.data)

    def __lt__(self, other):
        return self.data < other.data


import math

INFINITY = math.inf  # float("inf")


def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]


v = [Vertex(i) for i in range(8)]


def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
    for e in k:
        delattr(v, e)


def BFS(G, s):  # breadth first search
    V = vertices(G)
    s.predecessor = None
    s.distance = 0
    for v in V:
        if v != s:
            v.distance = INFINITY
        q = myqueue()
        q.enqueue(s)
    while q:
        u = q.dequeue()
    for v in G[u]:
        if v.distance == INFINITY:
            v.distance = u.distance + 1
    v.predecessor = u
    q.enqueue(v)


def identical_elements(a):
    b = a[0]
    for i in a:
        if i != b:
            return False
    return True


def _identical_elements(a):
    if len(a) <= 1:
        return True
    else:
        return a[0] == a[1] and identical_elements(a[1::])


def contains_None_data_node(n):
    return n is not None and (n.data is None or contains_None_data_node(n.next))


def _contains_None_data_node(n):
    while n is not None:
        if n.data is None:
            return True
        n = n.next
    return False


def count(n, x):
    if n == None:
        return 0
    else:
        if n.data == x:
            return 1 + count(n.left, x) + count(n.right, x)
        else:
            return count(n.left, x) + count(n.right, x)1




a = [4, 4, 4, 4, 4]

print(identical_elements(a))
print(_identical_elements(a))
