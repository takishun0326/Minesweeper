import random

class Game:
    def __init__(self):
        self.is_gamestart = False

    def gameStart(self, clicked_x, clicked_y):

        self.is_gamestart = True
        # Mine n%
        per = 15

        # map作成 15x15のすべて値が0
        self.map = [[0 for i in range(15)] for j in range(15)]
        for i in range(15):
            for j in range(15):
                # クリックした場所なら
                if not (i==clicked_x and j==clicked_y):
                    rand = random.randint(0,100)
                    if rand <= per:
                        # per % の確率でヒットした座標を地雷にする(-1)
                        self.map[i][j] = -1
                        
        print (self.map)
        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]

        for i in range(15):
            for j in range(15):

                if self.map[i][j] != -1:
                    # 画面外へはアクセスしない
                    for k in range(8):
                        if (i+dx[k]>=0) and (i+dx[k]<15) and (j+dy[k]>=0) and (j+dy[k]<15) :
                            if self.map[i+dx[k]][j+dy[k]] == -1:
                                # 地雷の数をカウント
                                self.map[i][j] += 1
                    
        

        

    


