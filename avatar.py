
class Avatar(object):
    def __init__(self, x, y):
        self.__guns = ["Wooden", "Silver", "Ebony"]
        self.__shields = ["Wooden", "Silver", "Ebony"]
        self.__armors = ["Leather", "Silver", "Ebony"]
        self.__x_position = x
        self.__y_position = y
    
    @property
    def guns(self):
        return self.__guns
    
    @property
    def shields(self):
        return self.__shields

    @property
    def armors(self):
        return self.__armors
    
    @property
    def x_position(self):
        return self.__x_position
    
    @property
    def y_position(sefl):
        return sefl.__y_position
    
    @x_position.setter
    def x_position(self, value):
        self.__x_position = value
    
    @y_position.setter
    def y_position(self, value):
        self.__y_position = value