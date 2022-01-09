import ADT
g = ADT.Graph()
g.addVertex("A", "B", "C", "D", "E")
g.addEdge("A", 6, "B")
g.addEdge("A", 1, "D")
g.addEdge("D", 2, "B")
g.addEdge("D", 1, "E")
g.addEdge("B", 2, "E")
g.addEdge("C", 5, "B", "E")

def dijkstra(G, start):
    table = dict.fromkeys(G.vertices, (none, None))
    visited = []
    unvisited = G.vertices
    table[start] = (0, None)
    curretnVertex = G[start]
    while currentVertex != None and len(unvisited) > 1:
        closestNeighbor = None
        for n in currentVertex.neighbors:
            if n not in visited:
                if G.edge(currentVertex, n) != None and table[n.id] != None:
                    distance = table[currentVertex.id][0] + G.edge(currentVertex, n)
                    if table[n.id][0] == None or distance < table[n.id][0]:
                        table[n.id] = (distance, currentVertex.id)
                        closestNeighbor = n
                    visited.append(currentVertex)
                    if currentVertex.id in unvisited:
                        del unvisited[currentVertex.id]
        currentVertex = closeestNeighbor
    return table

d = dijkstra(g, "A")
print(d ["C"])



