import dijkstra

# code here
vertices = []
vertices.append(dijkstra.Vertex('A'))
vertices.append(dijkstra.Vertex('B'))
vertices.append(dijkstra.Vertex('C'))
vertices.append(dijkstra.Vertex('D'))
vertices.append(dijkstra.Vertex('E'))

edges = []
edges.append(dijkstra.Edge('A', 'B', 6))
edges.append(dijkstra.Edge('A', 'D', 1))
edges.append(dijkstra.Edge('B', 'C', 5))
edges.append(dijkstra.Edge('D', 'B', 2))
edges.append(dijkstra.Edge('E', 'B', 2))
edges.append(dijkstra.Edge('C', 'E', 5))
edges.append(dijkstra.Edge('D', 'E', 1))

startVertex = 'A'
endVertex = 'C'
verticesResult = dijkstra.calculateShortestPath(vertices, edges, startVertex, endVertex)

# print result
resultVertex = verticesResult.where(lambda v: v.name == startVertex)[0]
while(True):   
    if(resultVertex.nextVertex == ''):
        print(f'{resultVertex.name}({resultVertex.calculatedDistance})')
        break
    else:
        print(f'{resultVertex.name}({resultVertex.calculatedDistance}) => ', end = '')
    resultVertex = verticesResult.where(lambda v: v.name == resultVertex.nextVertex)[0]
