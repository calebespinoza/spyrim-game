class SpyrimMap:
    def __init__(self, x, y):
        self.__x_axis = x
        self.__y_axis = y
        self.__map = []
    
    def create_map (self):
        for j in range(self.__y_axis):
            self.__map.append([])
            for i in range(self.__x_axis):
                self.__map[j].append(f"{j}-{i}")
        return self.__map
    
    def print_map (self, spyrim_map):
        for row in range(len(spyrim_map)):
            print(spyrim_map[row])
    #        for col in len(spyrim_map[row]):
    #            print()

#if __name__ == '__main__':
#    spyrim_map = SpyrimMap()
#    my_map = spyrim_map.create_map()
#    spyrim_map.print_map(my_map)