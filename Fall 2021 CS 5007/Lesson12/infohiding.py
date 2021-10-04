class InfoHiding:
    def __init__(self):
        self.visible = "Look at me"
        self._alsoVisible = "Look at me too"
        self.__invisible = "Do not look at me directly"

    def print_visible(self):
        print(self.visible)

    def _print_also_visible(self):
        print(self._alsoVisible)

    def __print_invisible(self):
        print(self.__invisible)


def main():
    test = InfoHiding()
    print(test.visible)
    print(test._alsoVisible)
    # print(test.__invisible)

    print()

    test.print_visible()
    test._print_also_visible()
    # test.__print_invisible()


if __name__ == "__main__":
    main()

# Private instance variables should have getter and setter functions
# Recommend 1 class 1 file
# filename = name of class

# from Filename import ClassName

# Set default values for objects in constructors
