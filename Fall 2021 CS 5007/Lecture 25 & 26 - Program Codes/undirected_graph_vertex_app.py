from UndirectedGraphVertex import Vertex

def main():
    vertex1 = Vertex(1)
    vertex1.addNeighbor(2, 2.4)
    vertex1.addNeighbor(3, 4.5)
    print(vertex1)

if __name__ == "__main__":
    main()