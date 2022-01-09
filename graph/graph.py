import ADT
class Vertex:
    def __init__(self, key):
        self.id = key
        self.neighbors = []

    def addNeighbor(self, vertex, directed = False):
        if vertex not in self.neighbors:
            self.neighbors.append(vertex)
        if not directed:
            if self not in vertex.neighbors:
                vertex.addNeighbor(self)

class Graph:
    def __init__(self, directed = False):
        self.vertices = {}
        self.directed = directed

    def size(self):
        return len(self.vertices)

    def __getitem__(self, key):
        return self.vertices[key]

    def __contains__(self, key):
        return key in self.vertices

    def addVertex(self, *v):
        for key in v:
            if key not in self:
                self.vertices[key] = Vertex(key)

    def addEdge(self, start, *end):
        for key in end:
            if key in self:
                self[start].addNeighbor(self[key], self.directed)

    def edges(self):
        output = []
        for key in self.vertices.keys():
            for vertex in self.vertices[key].neighbors:
                kvp = (key, vertex.id)
                if kvp not in output and tuple(reversed(kvp)) not in output:
                    output.append(kvp)
            return output

    def __iter__(self):
        return iter(self.vertices.values())


g = ADT.Graph()
g.addVertex(0,1,2,3,4,5,6,7,8,9,10,11,12,13)
g.addEdge(0,6,8,4)
g.addEdge(6,7)
g.addEdge(7,3)
g.addEdge(3,2)
g.addEdge(2,1)
g.addEdge(1,8,5,9)
g.addEdge(5,4)
g.addEdge(9,11,12)
g.addEdge(12,13)

order =[]
marked = [False] * g.size()
def dfs(G, start):
    order.append(G[start].id)
    marked[start] = True
    for w in G[start].neighbors:
        if not marked[w.id]:
            dfs(G,w.id)

#dfs(g, 1)
#print(order)

def bfs(G, start, end = None):
    queue = [G[start]]
    while len(queue) > 0:
        v = queue.pop(0)
        if not marked[v.id]:
            order.append(v.id)
            if v.id == end:
                return v
            marked[v.id] = True
            for w in v.neighbors:
                if not marked[w.id]:
                    queue.append(w)
    return None

#Looking for a path
node = bfs(g, 1, 8)
if node != None:
    print(node.id)
else:
    print("Not found")
print(order)