class Settings:
    def __init__(self):
        self.difficulties = [("easy", 10), ("medium", 15), ("hard", 25)]
        self.map_sizes = [("small", 20, 20),
                          ("medium", 20, 40), ("large", 20, 80)]
        self.difficultyId = 0
        self.mapId = 1

    def difficultySwitch(self):
        self.difficultyId = (self.difficultyId + 1) % len(self.difficulties)

    def getMap(self):
        return self.map_sizes[self.mapId]

    def getDifficulty(self):
        return self.difficulties[self.difficultyId]

    def mapSwitch(self):
        self.mapId = (self.mapId + 1) % len(self.map_sizes)
