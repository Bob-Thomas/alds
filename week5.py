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
    a = list(G.keys())
    a.sort()
    return a


def edges(G):
    a = []
    for u in vertices(G):
        for v in G[u]:
            a.append((u, v))
    return a


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
    V = vertices(G)
    BFS(G, V[0])
    #loop through the graph and check if a node his distance is infinity which means it hasn't been found.
    #which means it's  disconnected from the path
    for s in G:
        if s.distance == INFINITY:
            return False
    return True


def no_cycles(G):
    #updated BFS to avoid duplicate code
    #BFS returns true or false based on the relation ship between the node and predecessor
    V = vertices(G)
    return BFS(G, V[0])


def get_bridges(G):
    bridges = []
    for e in edges(G):
        # Remove the edges
        G[e[0]].remove(e[1])
        G[e[1]].remove(e[0])
        # if it broke the connection it's a bridge
        if not is_connected(G):
            bridges.append(e)
        # restore the edges
        G[e[0]].append(e[1])
        G[e[1]].append(e[0])
    return bridges


def is_strongly_connected(G):
    # check if it's fully connected else return
    if not is_connected(G):
        return False
    second_graph = {}
    # reverse the graph
    for edge in edges(G):
        if edge[0] in second_graph.keys():
            second_graph[edge[0]].append(edge[1])
        else:
            second_graph[edge[0]] = [edge[1]]
    # check if everything is still connected if not it isn't strongly connected
    return is_connected(second_graph)


def is_euler_graph(G):
    for l in G.values():
        if len(l) % 2 != 0: #if has a modulo of 2 in the length of his paths
            return False
    return True


def get_euler_circuit(G, s):
    #first check if euler graph
    if not is_euler_graph(G):
        return
    #add the first step
    steps = [s]
    #loop through the steps inside the node
    while (G[s]):
        for t in G[s]:
            k = t #temp save the value
            if (s, t) not in get_bridges(G):#if it's not a bridge stop and add the step
                break
        #add the steps and remove the traversed nodes from each other
        steps.append(k)
        G[s].remove(k)
        G[k].remove(s)
        s = k

    return steps


# diconnected graph - http://i.imgur.com/lSFqJkT.png
v = [Vertex(i) for i in range(8)]

G = {
    v[0]: [v[4], v[5]],
    v[1]: [v[4], v[5], v[6]],
    v[2]: [v[4], v[5], v[6]],
    v[3]: [v[7]],
    v[4]: [v[0], v[1], v[5]],
    v[5]: [v[0], v[1], v[2]],
    v[6]: [v[1], v[2]],
    v[7]: [v[3]]
}
print("disconnected graaf", is_connected(G))
clear(G)
# connnected graph with cycles - http://i.imgur.com/rMNJ1UM.png
v = [Vertex(i) for i in range(7)]
G = {
    v[0]: [v[5], v[4]],
    v[1]: [v[4], v[5], v[6]],
    v[2]: [v[4], v[5], v[6]],
    v[4]: [v[0], v[1], v[2], v[5]],
    v[5]: [v[1], v[2], v[4], v[0]],
    v[6]: [v[1], v[2]],
}

print("Graaf is connected", is_connected(G))
print("graaf heeft wel cycles:", no_cycles(G))
clear(G)

# disconnnected graph without cycles - http://i.imgur.com/BuiHpLU.png

v = [Vertex(i) for i in range(8)]
G = {v[0]: [v[5], v[4]],
     v[1]: [v[4], v[6]],
     v[2]: [v[5]],
     v[3]: [v[7]],
     v[4]: [v[0], v[1]],
     v[5]: [v[0], v[2]],
     v[6]: [v[1]],
     v[7]: [v[3]]}
clear(G)
print("graaf heeft geen cycles:", no_cycles(G))
clear(G)

v = [Vertex(i) for i in range(8)]
G = {
    v[0]: [v[1], v[3]],
    v[1]: [v[0], v[2]],
    v[2]: [v[1], v[4], v[3]],
    v[3]: [v[2], v[0]],
    v[4]: [v[2], v[5], v[6]],
    v[5]: [v[4], v[6]],
    v[6]: [v[5], v[4], v[7]],
    v[7]: [v[6]]
}
print("Bridges ", get_bridges(G))
clear(G)

v = [Vertex(i) for i in range(3)]
G = {v[0]: [v[1]],
     v[1]: [v[2]],
     v[2]: [v[0]]}
print("Should be true cause it's strong", is_strongly_connected(G))
clear(G)

v = [Vertex(i) for i in range(3)]
G = {v[0]: [v[1]],
     v[1]: [],
     v[2]: [v[0], v[1]]}
print("should be false cause it's not strong:", is_strongly_connected(G))
clear(G)

v = [Vertex(i) for i in range(8)]
G = {v[0]: [v[1], v[2]],
     v[1]: [v[0], v[3]],
     v[2]: [v[0], v[3]],
     v[3]: [v[1], v[2], v[4], v[6]],
     v[4]: [v[3], v[5], v[6], v[7]],
     v[5]: [v[4], v[6]],
     v[6]: [v[3], v[4], v[5], v[7]],
     v[7]: [v[4], v[6]]}
print("Euler: ", is_euler_graph(G))
print("Euler: ", get_euler_circuit(G, v[0]))
clear(G)
