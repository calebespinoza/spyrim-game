from spyrim_map import SpyrimMap
import random

class ExpertMap(SpyrimMap):
    def __init__(self, x, y):
        self.__map = []
        self.__dragons_quantity = 10
        super().__init__(x, y)
    
    def create_map (self):
        for j in range(super().y):
            self.__map.append([])
            for i in range(super().x):
                self.__map[j].append(f"spyrim")
                
        self.set_ragnar_mountain()
        self.set_frostfall_village()
        self.set_whiterun_village()
        self.set_woods()
        self.set_river()
        self.set_talos_lake()
        self.set_soltitude_village()
        self.set_sovngarde_village()
        self.set_jerall_mountains()
        self.set_dragons(self.__dragons_quantity)
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
        self.__map[15][7] = "woods"
        self.__map[15][10] = "woods"
        self.__map[15][13] = "woods"
        self.__map[15][14] = "woods"
        self.__map[15][15] = "woods"
        self.__map[16][6] = "woods"
        self.__map[16][14] = "woods"
        self.__map[16][15] = "woods"
        self.__map[17][7] = "woods"
    
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
    
    def set_talos_lake(self):
        self.__map[0][15] = "talos lake"
        self.__map[0][17] = "talos lake"
        self.__map[0][18] = "talos lake"
        self.__map[1][15] = "talos lake"
        self.__map[1][17] = "talos lake"
        self.__map[1][18] = "talos lake"
        self.__map[1][19] = "talos lake"
        self.__map[2][16] = "talos lake"
        self.__map[2][17] = "talos lake"
        self.__map[2][18] = "talos lake"
        self.__map[2][19] = "talos lake"
        self.__map[3][15] = "talos lake"
        self.__map[3][16] = "talos lake"
        self.__map[3][17] = "talos lake"
        self.__map[3][18] = "talos lake"
        self.__map[3][19] = "talos lake"
        self.__map[4][16] = "talos lake"
        self.__map[4][17] = "talos lake"
        self.__map[4][18] = "talos lake"
        self.__map[4][19] = "talos lake"
        self.__map[5][16] = "talos lake"
        self.__map[5][19] = "talos lake"
    
    def set_soltitude_village(self):
        self.__map[7][18] = "soltitude"
        self.__map[8][18] = "soltitude"
        self.__map[9][18] = "soltitude"
        self.__map[10][18] = "soltitude"
        self.__map[11][18] = "soltitude"
        self.__map[12][18] = "soltitude"
        self.__map[13][18] = "soltitude"
        self.__map[14][18] = "soltitude"
        self.__map[15][18] = "soltitude"
        self.__map[16][18] = "soltitude"
        self.__map[7][17] = "soltitude"
        self.__map[9][19] = "soltitude"
        self.__map[10][19] = "soltitude"
        self.__map[11][17] = "soltitude"
        self.__map[11][19] = "soltitude"
        self.__map[13][16] = "soltitude"
        self.__map[13][17] = "soltitude"
        self.__map[13][19] = "soltitude"
        self.__map[14][17] = "soltitude"
        self.__map[14][19] = "soltitude"
        self.__map[15][19] = "soltitude"
    
    def set_sovngarde_village(self):
        self.__map[16][10] = "sovngarde"
        self.__map[17][9] = "sovngarde"
        self.__map[17][10] = "sovngarde"
        self.__map[18][8] = "sovngarde"
        self.__map[18][9] = "sovngarde"
        self.__map[18][10] = "sovngarde"
        self.__map[18][11] = "sovngarde"
        self.__map[19][8] = "sovngarde"
        self.__map[19][9] = "sovngarde"
        self.__map[19][10] = "sovngarde"
        self.__map[19][11] = "sovngarde"
        self.__map[19][12] = "sovngarde"
    
    def set_jerall_mountains(self):
        self.__map[15][1] = "jerall mountains"
        self.__map[16][1] = "jerall mountains"
        self.__map[16][2] = "jerall mountains"
        self.__map[16][3] = "jerall mountains"
        self.__map[17][1] = "jerall mountains"
        self.__map[17][2] = "jerall mountains"
        self.__map[17][3] = "jerall mountains"
        self.__map[18][1] = "jerall mountains"
        self.__map[18][2] = "jerall mountains"
        self.__map[18][3] = "jerall mountains"
        self.__map[18][4] = "jerall mountains"
        self.__map[19][2] = "jerall mountains"
        self.__map[19][3] = "jerall mountains"

    def set_dragons(self, quantity):
        for i in range(quantity):
            x = random.randint(0, super().x - 1)
            y = random.randint(0, super().y - 1)
            self.__map[y][x] = "DRAGON"
