import random

class Game:
    def __init__(self):
        self.is_gamestart = False

    def gameStart(self, clicked_x, clicked_y):

        dx = [1, 1, 1, 0, 0, -1, -1, -1]
        dy = [1, 0, -1, 1, -1, 1, 0, -1]

        self.is_gamestart = True
        # Mine n%
        per = 20

        # map作成 15x15のすべて値が0, 訪れたマス状況
        self.map = [[0 for j in range(15)] for j in range(20)]
        self.map_visit = [[0 for j in range(15)] for i in range(20)]

        for i in range(20):
            for j in range(15):
                # クリックした場所なら
                if i==clicked_x and j==clicked_y:
                    self.map[i][j] = 0
                else:
                    rand = random.randint(0,100)
                    if rand <= per:
                        # per % の確率でヒットした座標を地雷にする(-1)
                        self.map[i][j] = -1
                    
        for k in range(8):
            new_x = clicked_x+dx[k]
            new_y = clicked_y+dy[k]
            if (new_x>=0) and (new_x<20) and (new_y>=0) and (new_y<15):
                print(new_x,new_y)
                self.map[new_x][new_y] = 0

                        
        print (self.map)

        for i in range(20):
            for j in range(15):

                if self.map[i][j] != -1:
                    # 画面外へはアクセスしない
                    for k in range(8):
                        if (i+dx[k]>=0) and (i+dx[k]<20) and (j+dy[k]>=0) and (j+dy[k]<15) :
                            if self.map[i+dx[k]][j+dy[k]] == -1:
                                # 地雷の数をカウント
                                self.map[i][j] += 1
        
        print(self.map)
                    
    # 押した場所から地雷0は全部開放する    
    def get_expandAreaPos(self, x, y):

        result = [[x,y]]

        dx = [1,1,1,0,0,-1,-1,-1]
        dy = [1,0,-1,1,-1,1,0,-1]

        # そのマスを訪れた
        self.map_visit[x][y] = 1

        queue = [[x,y]]        
        
        while len(queue) != 0:

            tmp = queue.pop(0)
            for k in range(8):
                new_x = tmp[0] + dx[k]
                new_y = tmp[1] + dy[k]

                if new_x>=0 and new_x<20 and new_y>=0 and new_y<15:
                    # まだ訪れていないかつマスが0なら
                    if self.map_visit[new_x][new_y] == 0:

                        if self.map[new_x][new_y] == 0:
                            self.map_visit[new_x][new_y] = 1
                            queue.append([new_x,new_y])
                            result.append([new_x,new_y])
                            
                        # 数字が割り振られているマスなら and 元のマスが0なら
                        elif self.map[new_x][new_y] > 0 and self.map[tmp[0]][tmp[1]] == 0:
                            self.map_visit[new_x][new_y] = 1
                            result.append([new_x,new_y])

        return result

        

        

    


