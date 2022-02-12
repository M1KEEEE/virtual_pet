class Pet:
    def __init__(
        self, 
        name, 
        fullnes, 
        health, 
        mood, 
        cleannes, 
        energy
    ):
        self.name = name
        self.fullnes = fullnes
        self.health = health
        self.mood = mood
        self.cleannes = cleannesnes
        self.energy = energy
        self.fullnes_change = -1
        self.health_change = -1
        self.mood_change = -1
        self.cleannes_change = -1
        self.energy_change = -1

    def feed(self, num):
        self.fullnes += num
        print("self")