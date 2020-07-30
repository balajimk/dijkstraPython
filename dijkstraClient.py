import dijkstra

# code here
vertices = []
vertices.append(dijkstra.Vertex('A'))
vertices.append(dijkstra.Vertex('B'))
vertices.append(dijkstra.Vertex('C'))
vertices.append(dijkstra.Vertex('D'))
vertices.append(dijkstra.Vertex('E'))
dijkstra.Vertices = vertices

edges = []
edges.append(dijkstra.Edge('A', 'B', 6))
edges.append(dijkstra.Edge('A', 'D', 1))
edges.append(dijkstra.Edge('B', 'C', 5))
edges.append(dijkstra.Edge('D', 'B', 2))
edges.append(dijkstra.Edge('E', 'B', 2))
edges.append(dijkstra.Edge('C', 'E', 5))
edges.append(dijkstra.Edge('D', 'E', 1))
dijkstra.Edges = edges

startVertex = 'A'
endVertex = 'C'
vertices = dijkstra.calculateShortestPath(startVertex, endVertex)

# print result
resultVertex = vertices.where(lambda v: v.name == startVertex)[0]
while(True):   
    if(resultVertex.nextVertex == ''):
        print(f'{resultVertex.name}({resultVertex.calculatedDistance})')
        break
    else:
        print(f'{resultVertex.name}({resultVertex.calculatedDistance}) => ', end = '')
    resultVertex = vertices.where(lambda v: v.name == resultVertex.nextVertex)[0]
