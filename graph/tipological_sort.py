import ADT

courses = ADT.Graph(True)
courses.addVertex(0,1,2,3,4,5,6,7,8,9)
courses[0].value = "MATH-151"
courses[1].value = "CS-150"
courses[2].value = "CS-220"
courses[3].value = "CS-151"
courses[4].value = "CS-250"
courses[5].value = "CS-230"
courses[6].value = "CS-466"
courses[7].value = "CS-360"
courses[8].value = "CS-460"
courses[9].value = "CS-477"
courses.addEdge(0,2)
courses.addEdge(1,2,3)
courses.addEdge(2,7,9)
courses.addEdge(7,8)
courses.addEdge(9,8)
courses.addEdge(3,4,5)
courses.addEdge(5,6)



def tops(G):
    output = []
    startVertices = []
    for vertex in G:
        if len(vertex.predecessors) == 0:
            startVertices.append(vertex)

    for vertex in startVertices:
        marked = [False] * G.size()
        stack = [vertex] 
        while len(stack) > 0:
            v = stack.pop()
            if not marked[v.id]:
                addToOutput = True
                for p in v.predecessors:
                    addToOutput = addToOutput and p.id in output
                if adToOutput:
                    output.append(v.id)
                    marked[v.id] = True 
                    for w in neighbors:
                        if not marked[w.id]:
                            stack.append(w.id)
        return output

t = tops(courses)
print(t)

for i in t:
    print(course[i].value)
