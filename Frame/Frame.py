import tkinter
from tkinter import ttk

from Game import Game
from functools import partial 
from Frame import Clock

WIDTH = 400
HEIGHT = 400

class Frame:
    def __init__(self, main_win):
        self.main_win = main_win
        self.game = Game.Game()

        self.flgs = []
        self.bombs = []

        self.frame = tkinter.Frame(self.main_win, width=WIDTH, height=HEIGHT)
        self.frame.pack()

        self.clock = Clock.Clock(self.main_win)

        self.widgets()
        self.position()

    # 押された後のボタンの状態  x, y, text
    def disable_button(self, i, j, num):
            
        # 押されたマスを押された状態で保持された物へ変更
        self.buttons[i][j].destroy()
        if num == 0:
            self.buttons[i][j] = tkinter.Button(self.main_win, relief='sunken')
        else :    
            self.buttons[i][j] = tkinter.Button(self.main_win, text=num , relief='sunken')
        self.buttons[i][j].place(x=20*i, y=20*j+100, width=20, height=20)
        # print("pushed " + str(i) + str(j))

    # 右クリックで旗を置く
    def put_flg(self,event):
        # gameがスタートしているか
        if self.game.is_gamestart:
            # 旗を立てる
            if event.widget["image"] == '':
                flg_img = tkinter.PhotoImage(file = 'Flag.png')
                self.flgs.append(flg_img.subsample(30, 30))
                event.widget["image"] = self.flgs[-1]
            # 旗状態解除
            else :
                event.widget["image"] = ''


    def pushed_grid(self,x,y):
        def expanding_pushed_button():
            # ゲームスタートしていないとき
            
            if not self.game.is_gamestart:
                # Timer start
                self.clock.start_timer()
                # Map 生成
                self.game.gameStart(x,y)
                expand_area_pos = self.game.get_expandAreaPos(x,y)
                for pos in expand_area_pos:
                    self.disable_button(pos[0], pos[1], self.game.map[pos[0]][pos[1]])
                       
            
            # 爆弾をタッチしたら
            if self.game.map_visit[x][y] != 1 :
                if self.game.map[x][y] == -1:

                    self.buttons[x][y].destroy()
                    bomb_img = tkinter.PhotoImage(file = 'Bomb.png')

                    # Timer Stop
                    self.clock.game_over()

                    # 爆弾をすべて掘り起こす
                    for i in range(20):
                        for j in range(15):
                            self.game.map_visit[i][j] = 1
                            if self.game.map[i][j] == -1:
                                self.bombs.append(bomb_img.subsample(30, 30))
                                self.buttons[i][j] = tkinter.Button(self.main_win, image = self.bombs[-1], relief='sunken')
                                self.buttons[i][j].place(x=20*i, y=20*j+100, width=20, height=20)

                else:  
                    expand_area_pos = self.game.get_expandAreaPos(x,y)
                    for pos in expand_area_pos:
                        self.disable_button(pos[0], pos[1], self.game.map[pos[0]][pos[1]])

            # game clear  判定      
            if self.game.is_game_clear():
                # すべて訪れたことにする
                for i in range(20):
                    for j in range(15):
                        self.game.map_visit[i][j] = 1
                # Timer Stop
                self.clock.game_clear()
                
        return expanding_pushed_button


    # widgets 準備
    def widgets(self):
        
        self.buttons = []
        for i in range(20):
            button = []
            for j in range(15):
                # ボタンの設定
                b = tkinter.Button(self.main_win, command=self.pushed_grid(i,j))
                b.bind("<Button-3>", lambda event: self.put_flg(event))                 
                button.append(b)
            
            self.buttons.append(button)
        

    # widgets 配置
    def position(self):

        for i in range(20):
            for j in range(15):
                self.buttons[i][j].place(x=20*i, y=20*j+100, width=20, height=20)
