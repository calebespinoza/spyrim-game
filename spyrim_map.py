
class SpyrimMap(object):

    def __init__(self, x, y):
        self._map = []
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x

    @x.setter
    def x (self, value):
        self._x = value

    @property
    def y(self):
        return self._y

    @x.setter
    def y (self, value):
        self._y = value
    
    @property
    def map(self):
        return self._map
    
    @map.setter
    def map(self, value):
        self._map.append = value
    
    def create_map (self):
        pass

    def print_map (self, spyrim_map):
        for row in range(len(spyrim_map)):
            print(spyrim_map[row])
    

#if __name__ == '__main__':
#    spyrim_map = SpyrimMap("begineer")
#    my_map = spyrim_map.create_map()
#    spyrim_map.print_map(my_map)