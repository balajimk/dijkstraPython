from py_linq import Enumerable

class Vertex(object):
    def __init__(self, name):
        super().__init__()
        self.name = name
        self.calculatedDistance = 0
        self.previousVertex = ''
        self.nextVertex = ''
        self.visited = False

class Edge(object):
    def __init__(self, v1, v2, distance):
        super().__init__()
        self.v1 = v1
        self.v2 = v2
        self.distance = distance
        self.used = False

def calculateShortestPath(verticesList, edgesList, startVertex, endVertex):
    vertices = Enumerable(verticesList)
    edges = Enumerable(edgesList)
    unvisitedVerticesCount = vertices.where(lambda v: v.visited == False).count()
    currentVertex = None

    while unvisitedVerticesCount > 0:
        if (currentVertex == None):
            currentVertex = vertices.where(lambda v: v.name == startVertex)[0]
        else:
            currentVertex = vertices.where(lambda v: v.calculatedDistance > 0 and v.visited == False).order_by(lambda v: v.calculatedDistance)[0]
        
        connectingEdges = edges.where(lambda e: (e.v1 == currentVertex.name or e.v2 == currentVertex.name) and e.used == False)
        for currentEdge in connectingEdges:
            currentNeighborName = ''
            if (currentEdge.v1 == currentVertex.name):
                currentNeighborName = currentEdge.v2
            else:
                currentNeighborName = currentEdge.v1
            currentNeighbor = vertices.where(lambda v: v.name == currentNeighborName)[0]

            tempDistance = 0
            tempDistance = currentVertex.calculatedDistance + currentEdge.distance
            if (currentNeighbor.calculatedDistance == 0 or tempDistance < currentNeighbor.calculatedDistance):
                currentNeighbor.calculatedDistance = tempDistance
                currentNeighbor.previousVertex = currentVertex.name
            
            currentEdge.used = True
        # for loop ends here
        currentVertex.visited = True
        unvisitedVerticesCount = vertices.where(lambda v: v.visited == False).count()
    # while loop ends here

    # set next values for forward traversing
    nVertex = vertices.where(lambda v: v.name == endVertex)[0]
    valueToSetAsNext = ''
    while(True):
        valueToSetAsNext = nVertex.name
        if (nVertex.previousVertex == ''):
            break
        nVertex = vertices.where(lambda v: v.name == nVertex.previousVertex)[0]
        nVertex.nextVertex = valueToSetAsNext

    return (vertices)
