class Settings:
    def __init__(self):
        self.difficulties = [("EASY", 10), ("MEDIUM", 15), ("HARD", 25)]
        self.map_sizes = [("SMALL", 20, 25),
                          ("MEDIUM", 20, 50), ("LARGE", 20, 100)]
        self.soundString = ["OFF", "ON"]
        self.difficultyId = 0
        self.mapId = 1
        self.fruit_count = 2
        self.sound = 1

    def difficultySwitch(self):
        self.difficultyId = (self.difficultyId + 1) % len(self.difficulties)

    def getMap(self):
        return self.map_sizes[self.mapId]

    def getDifficulty(self):
        return self.difficulties[self.difficultyId]

    def mapSwitch(self):
        self.mapId = (self.mapId + 1) % len(self.map_sizes)

    def getSound(self):
        return self.soundString[self.sound]

    def soundSwitch(self):
        self.sound = (self.sound + 1) % len(self.soundString)

    def fruitAdd(self):
        self.fruit_count = self.fruit_count + 1

    def fruitRemove(self):
        self.fruit_count = self.fruit_count - 1
