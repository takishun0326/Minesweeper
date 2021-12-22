import random

class Game:
    def __init__(self):
        
        # Mine n%
        per = 20

        self.mines = []
        for i in range(15):
            for j in range(15):
                rand = random.randint(0,100)
                if rand <= per:
                    # per % の確率でヒットした座標を記録
                    self.mines.append(list((i,j)))
        




