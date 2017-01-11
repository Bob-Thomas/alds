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

    def __repr__(self):  # voor afdrukken
        return str(self.data)

    def __lt__(self, other):  # voor sorteren
        return self.data < other.data


INFINITY = float("inf")  # float("inf")


def vertices(G):
    return sorted(G)


def edges(G):
    return [(u, v) for u in vertices(G) for v in G[u]]


v = [Vertex(i) for i in range(8)]

G = {v[0]: [v[1], v[4]],
     v[1]: [v[0], v[5]],
     v[2]: [v[3], v[5], v[6]],
     v[3]: [v[2], v[6], v[7]],
     v[4]: [v[0]],
     v[5]: [v[1], v[2], v[6]],
     v[6]: [v[2], v[3], v[5], v[7]],
     v[7]: [v[3], v[6]]}

print("vertices(G):", vertices(G))
print("edges(G):", edges(G))


def clear(G):
    for v in vertices(G):
        k = [e for e in vars(v) if e != 'data']
        for e in k:
            delattr(v, e)


def BFS(G, s):
    V = vertices(G)
    s.predecessor = None  # s krijgt het attribuut 'predecessor'
    s.distance = 0  # s krijgt het attribuut 'distance'
    for v in V:
        if v != s:
            v.distance = INFINITY  # v krijgt het attribuut 'distance'
    no_cycle = True
    q = myqueue()
    q.enqueue(s)  # plaats de startnode in de queue
    while q:
        u = q.dequeue()
        for v in G[u]:
            if v.distance == INFINITY:  # v is nog niet bezocht
                v.distance = u.distance + 1
                v.predecessor = u  # v krijgt het attribuut 'predecessor'
                q.enqueue(v)  # plaats de buren van v in de queue
            elif u.predecessor != v:
                no_cycle = False
    return no_cycle


# print("q:", q)
BFS(G, v[1])


def show_tree_info(G):
    print('tree:', end=' ')
    for v in vertices(G):
        print('(' + str(v), end='')
        if hasattr(v, 'distance'):
            print(',d:' + str(v.distance), end='')
        if hasattr(v, 'predecessor'):
            print(',p:' + str(v.predecessor), end='')
        print(')', end=' ')
    print()


show_tree_info(G)


def show_sorted_tree_info(G):
    print('sorted tree:')
    V = vertices(G)
    #    V = [v for v in V if hasattr(v,'distance') and hasattr(v,'predecessor')]
    V.sort(key=lambda x: (x.distance, x.predecessor))
    d = 0
    for v in V:
        if v.distance > d:
            print()
            d += 1
        print('(' + str(v) + ',d:' + str(v.distance) + ',p:'
              + str(v.predecessor), end='')
        print(')', end=' ')
    print()


show_sorted_tree_info(G)


def path_BFS(G, u, v):
    BFS(G, u)
    a = []
    if hasattr(v, 'predecessor'):
        current = v
        while current:
            a.append(current)
            current = current.predecessor
        a.reverse()
    return a


def is_connected(G):
    BFS(G,  list(G.keys())[0])
    for s in G:
        if s.distance == INFINITY:
            return False
    return True


def no_cycles(G):
    return BFS(G, list(G.keys())[0])


# diconnected graph - http://i.imgur.com/lSFqJkT.png
v = [Vertex(i) for i in range(8)]

G = {
    v[0]: {v[4], v[5]},
    v[1]: {v[4], v[5], v[6]},
    v[2]: {v[4], v[5], v[6]},
    v[3]: {v[7]},
    v[4]: {v[0], v[1], v[5]},
    v[5]: {v[0], v[1], v[2]},
    v[6]: {v[1], v[2]},
    v[7]: {v[3]}
}
print("disconnected graaf", is_connected(G))

# connnected graph with cycles - http://i.imgur.com/rMNJ1UM.png
v = [Vertex(i) for i in range(8)]
G = {
    v[0]: [v[4], v[5]],
    v[1]: [v[4], v[5], v[6]],
    v[2]: [v[4], v[5], v[6]],
    v[4]: [v[0], v[1], v[2], v[5]],
    v[5]: [v[4], v[0], v[1], v[2]],
    v[6]: [v[1], v[2]],
}
print("Graaf is connected", is_connected(G))
print("graaf heeft wel cycles:", no_cycles(G))
clear(G)

# disconnnected graph without cycles - http://i.imgur.com/BuiHpLU.png

v = [Vertex(i) for i in range(8)]
G = {
    v[0]: [v[4], v[1]],
    v[1]: [v[4], v[6]],
    v[2]: [v[5]],
    v[3]: [v[7]],
    v[4]: [v[0], v[1]],
    v[5]: [v[0], v[2]],
    v[6]: [v[1]],
    v[7]: [v[3]],
}

print("graaf heeft geen cycles:", no_cycles(G))



clear(G)
