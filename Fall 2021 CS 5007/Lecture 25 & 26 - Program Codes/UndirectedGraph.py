from UndirectedGraphVertex import Vertex

class Graph:
    def __init__(self):
        self.__vertList = {} # Key: Vertex Object
        self.__numVertices = 0

    def getKeyVertList(self):
        return self.__vertList

    def setKeyVertList(self, vertList):
        self.__vertList = vertList

    def getNumVertices(self):
        return self.__numVertices

    def setNumVertices(self, numVertices):
        self.__numVertices = numVertices

    def addVertex(self, key):
        newVertex = Vertex(key)
        self.getKeyVertList()[key] = newVertex
        self.setNumVertices(self.getNumVertices() + 1)

    def getVertex(self, key):
        if key in self.getKeyVertList():
            return self.getKeyVertList()[key]
        else:
            return None

    def containVertex(self, key):
        return key in self.getKeyVertList()

    def addEdge(self, v1, v2, weight=0): #**#
        if v1 not in self.getKeyVertList():
            self.addVertex(v1)

        if v2 not in self.getKeyVertList():
            self.addVertex(v2)

        self.getKeyVertList()[v1].addNeighbor(v2, weight) #**#
        self.getKeyVertList()[v2].addNeighbor(v1, weight) #**#

    def getVerticeKey(self):
        return self.getKeyVertList().keys()

    def getVerticeNode(self):
        return self.getKeyVertList().values()