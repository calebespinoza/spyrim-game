from spyrim_map import SpyrimMap
import random

class BegineerMap(SpyrimMap):
    def __init__(self, x, y):
        self.__map = []
        super().__init__(x, y)
    
    def create_map (self):
        for j in range(super().y):
            self.__map.append([])
            for i in range(super().x):
                self.__map[j].append(f"{j}-{i}")

        self.set_ragnar_mountain()
        self.set_frostfall_village()
        self.set_whiterun_village()
        self.set_woods()
        self.set_river()
        self.set_dragons(4)
        SpyrimMap.map=self.__map
    
    def set_ragnar_mountain(self):
        self.__map[5][7] = "ragnar mountain"
        self.__map[5][8] = "ragnar mountain"
        self.__map[6][6] = "ragnar mountain"
        self.__map[6][7] = "ragnar mountain"
        self.__map[6][8] = "ragnar mountain"
        self.__map[7][6] = "ragnar mountain"
        self.__map[7][7] = "ragnar mountain"
        self.__map[8][7] = "ragnar mountain"
        self.__map[8][8] = "ragnar mountain"
    
    def set_frostfall_village(self):
        self.__map[1][11] = "frostfall"
        self.__map[1][12] = "frostfall"
        self.__map[1][13] = "frostfall"
        self.__map[2][12] = "frostfall"
        self.__map[2][13] = "frostfall"
        self.__map[3][11] = "frostfall"
        self.__map[3][12] = "frostfall"
        self.__map[3][13] = "frostfall"
        self.__map[4][11] = "frostfall"
        self.__map[4][12] = "frostfall"
        self.__map[5][12] = "frostfall"
    
    def set_whiterun_village(self):
        self.__map[5][2] = "whiterun"
        self.__map[5][3] = "whiterun"
        self.__map[6][1] = "whiterun"
        self.__map[6][2] = "whiterun"
        self.__map[6][3] = "whiterun"
        self.__map[7][2] = "whiterun"
        self.__map[7][3] = "whiterun"
        self.__map[8][1] = "whiterun"
        self.__map[8][2] = "whiterun"
        self.__map[8][3] = "whiterun"
        self.__map[9][2] = "whiterun"
        self.__map[9][3] = "whiterun"
        self.__map[10][3] = "whiterun"
    
    def set_woods(self):
        self.__map[10][6] = "woods"
        self.__map[10][7] = "woods"
        self.__map[10][8] = "woods"
        self.__map[10][10] = "woods"
        self.__map[10][12] = "woods"
        self.__map[10][13] = "woods"
        self.__map[11][8] = "woods"
        self.__map[11][10] = "woods"
        self.__map[11][11] = "woods"
        self.__map[11][13] = "woods"
        self.__map[11][14] = "woods"
        self.__map[12][5] = "woods"
        self.__map[12][6] = "woods"
        self.__map[12][7] = "woods"
        self.__map[12][8] = "woods"
        self.__map[12][9] = "woods"
        self.__map[12][10] = "woods"
        self.__map[12][11] = "woods"
        self.__map[12][12] = "woods"
        self.__map[12][13] = "woods"
        self.__map[12][14] = "woods"
        self.__map[13][6] = "woods"
        self.__map[13][7] = "woods"
        self.__map[13][8] = "woods"
        self.__map[13][9] = "woods"
        self.__map[13][10] = "woods"
        self.__map[13][11] = "woods"
        self.__map[13][12] = "woods"
        self.__map[13][13] = "woods"
        self.__map[13][14] = "woods"
        self.__map[14][7] = "woods"
        self.__map[14][8] = "woods"
        self.__map[14][9] = "woods"
        self.__map[14][10] = "woods"
        self.__map[14][11] = "woods"
        self.__map[14][12] = "woods"
        self.__map[14][13] = "woods"
        self.__map[14][14] = "woods"
    
    def set_river(self):
        self.__map[2][0] = "river"
        self.__map[2][1] = "river"
        self.__map[2][2] = "river"
        self.__map[1][2] = "river"
        self.__map[1][3] = "river"
        self.__map[1][4] = "river"
        self.__map[2][4] = "river"
        self.__map[2][5] = "river"
        self.__map[2][6] = "river"
        self.__map[1][6] = "river"
        self.__map[0][6] = "river"

    def set_dragons(self, quantity):
        for i in range(quantity):
            x = random.randint(0, super().x - 1)
            y = random.randint(0, super().y - 1)
            self.__map[y][x] = "DRAGON"
