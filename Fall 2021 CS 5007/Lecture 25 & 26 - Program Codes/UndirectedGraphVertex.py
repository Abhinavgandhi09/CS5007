class Vertex:
    def __init__(self, key):
        self.__id = key
        self.__connectedTo = {} # Vertex Object (Key): Weight

    def getId(self):
        return self.__id

    def setId(self, key):
        self.__id = key

    def getConnections(self):
        return self.__connectedTo

    def setConnections(self, connectedTo):
        self.__connectedTo = connectedTo

    def addNeighbor(self, nbrKey, weight=0):
        vertex = Vertex(nbrKey)
        self.getConnections()[vertex] = weight

    def getWeight(self, vertex):
        return self.getConnections()[vertex]

    def __str__(self):
        return "Node " + str(self.getId()) + " Connected To: " + \
               str({str(x.getId()) + " : " + str(self.getWeight(x)) for x in self.getConnections().keys()})