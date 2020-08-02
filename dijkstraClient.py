from dijkstra import Vertex
from dijkstra import Edge
from dijkstra import calculateShortestPath

# code here
vertices = []
vertices.append(Vertex('A'))
vertices.append(Vertex('B'))
vertices.append(Vertex('C'))
vertices.append(Vertex('D'))
vertices.append(Vertex('E'))

edges = []
edges.append(Edge('A', 'B', 6))
edges.append(Edge('A', 'D', 1))
edges.append(Edge('B', 'C', 5))
edges.append(Edge('D', 'B', 2))
edges.append(Edge('E', 'B', 2))
edges.append(Edge('C', 'E', 5))
edges.append(Edge('D', 'E', 1))

startVertex = 'A'
endVertex = 'C'
verticesResult = calculateShortestPath(vertices, edges, startVertex, endVertex)

# print result
resultVertex = verticesResult.where(lambda v: v.name == startVertex)[0]
while(True):   
    if(resultVertex.nextVertex == ''):
        print(f'{resultVertex.name}({resultVertex.calculatedDistance})')
        break
    else:
        print(f'{resultVertex.name}({resultVertex.calculatedDistance}) => ', end = '')
    resultVertex = verticesResult.where(lambda v: v.name == resultVertex.nextVertex)[0]
