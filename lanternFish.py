class lanternFish:
    def __init__(self, timer):
        self.timer = timer
    def tick(self):
        if self.timer == 0:
            #reproduce new lanternfish
            self.timer = 6
            return lanternFish(8)
        else:
            self.timer -= 1
            return None

