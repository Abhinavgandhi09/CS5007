from BinarySearchTree import BinarySearchTree


def printBinaryTree(tree):
    # Print the parent of each node
    print()
    tree.printParentNode()

    # Print leaves and non-leaves
    print()
    print("The number of leaves of this tree is " + str(tree.countLeaves()))
    print()
    print("The number of non-leaves of this tree is " + str(tree.countNonLeaves()))


def createBinaryTree():
    tree = BinarySearchTree()

    newNode = True

    while newNode:
        val = int(input("Enter value of node: "))
        tree.insertNode(val)

        user_input = input("Is there another node? Please enter Y or N: ")
        while user_input.upper() != 'Y' and user_input.upper() != 'N':
            print("Incorrect entry.")
            user_input = input("Is there another node? Please enter Y or N: ")

        if user_input.upper() == 'Y':
            newNode = True
        elif user_input.upper() == 'N':
            newNode = False

    return tree


def main():
    newTree = True

    while newTree:
        tree = createBinaryTree()
        printBinaryTree(tree)

        user_input = input("Is there another tree? Enter Y or N: ")

        while user_input.upper() != 'Y' and user_input.upper() != 'N':
            print("Incorrect input entered. Please enter Y or N.")
            user_input = input("Is there another tree? Enter Y or N: ")

        if user_input.upper() == 'Y':
            newTree = True
        elif user_input.upper() == 'N':
            newTree = False

    print()
    print("Thank You for Using My Application")

    return 0


if __name__ == "__main__":
    main()
