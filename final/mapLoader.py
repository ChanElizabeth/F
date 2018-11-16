class MapLoader:
    def __init__(self, mapFile):
        self.mapFile = open(mapFile, "r").readlines()
        self.mapFile = [x.strip() for x in self.mapFile]
        #self.mapSecs = []
        self.mapKeys = []
        for i in self.mapFile:
            x = i.split("-")
            #self.mapSecs.append(x[0])
            self.mapKeys.append(x[1])

    def getKeys(self, time):
        return self.mapKeys[time].split(",")



    #def getSecs(self):
    #    return self.mapSecs


# map = MapLoader("maps/easy.txt")
#
# print(map.getKeys("00:07"))
