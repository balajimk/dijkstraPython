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

Vertices = []
Edges = []

def calculateShortestPath(startVertex, endVertex):
    vertices = Enumerable(Vertices)
    edges = Enumerable(Edges)
    unvisitedVertices = vertices.where(lambda v: v.visited == False)
    currentVertex = None
    while unvisitedVertices.count() > 0:
        if (currentVertex == None):
            currentVertex = vertices.where(lambda v: v.name == startVertex)[0]
        else:
            currentVertex = vertices.where(lambda v: v.calculatedDistance > 0 and v.visited == False).order_by(lambda v: v.calculatedDistance)[0]
        currentVertex.visited = True
        unvisitedVertices = vertices.where(lambda v: v.visited == False)
        
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
