from LinkedList import LinkedList

def main():
    # Create a linked List with the following values in sequence: 3, 7, 5, 12, and 15

    linkedlist = LinkedList()
    linkedlist.setNodeData(0, 3)
    linkedlist.appendNewNode(7)
    linkedlist.appendNewNode(5)
    linkedlist.appendNewNode(12)
    linkedlist.appendNewNode(15)
    linkedlist.appendNewNode(17)
    linkedlist.appendNewNode(20)

    # Split the linkedlist in half and return the first linkedlist reference to lst1 and
    # the second linkedlist reference to lst2
    lst1, lst2 = linkedlist.splitInhalf()
    print("The number of nodes in the lst1: ", lst1.getNumNodes())
    print("LinkedList 1 Values: ")
    for i in range(lst1.getNumNodes()):
        print(lst1.getNodeData(i))

    print()

    print("The number of nodes in the lst2: ", lst2.getNumNodes())
    print("LinkedList 2 Values: ")
    for i in range(lst2.getNumNodes()):
        print(lst2.getNodeData(i))

if __name__ == "__main__":
    main()