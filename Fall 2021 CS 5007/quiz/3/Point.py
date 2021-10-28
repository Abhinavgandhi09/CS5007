class Point:

    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_x(self,x):
        self.__x = x

    def get_x(self):
        return self.__x

    def set_y(self,y):
        self.__y = y

    def get_y(self):
        return self.__y

    def toString(self):
        s = "\nThe coordinate of the point is (" + str(self.__x) + "," + str(self.__y) + ")"
        return s

    def increaseOneOnX(self):
        inc_x = self.get_x() + 1
        return self.set_x(inc_x)

    def increaseOneOnY(self):
        inc_y = self.get_y() + 1
        return self.set_y(inc_y)


point_obj = Point()
