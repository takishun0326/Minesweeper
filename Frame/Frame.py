import tkinter
from tkinter import ttk

from Game import Game
from functools import partial 

WIDTH = 500
HEIGHT = 500

class Frame:
    def __init__(self, main_win):
        self.main_win = main_win
        self.game = Game.Game()

        self.frame = tkinter.Frame(main_win, width=500, height=500)
        self.frame.pack()

        self.widgets()
        self.position()

    # 押された後のボタンの状態  x, y, text
    def disable_button(self, i, j, num):
            
            # 押されたマスを押された状態で保持された物へ変更
            self.buttons[i][j].destroy()
            self.buttons[i][j] = tkinter.Button(self.main_win, text=num , relief='sunken')
            self.buttons[i][j].place(x=20*i+100, y=20*j+100, width=20, height=20)
            # print("pushed " + str(i) + str(j))

    def put_flg(self,event, i, j):
        # gameがスタートしているか
        if self.game.is_gamestart:
            flg_img = tkinter.PhotoImage(file = 'Flag.png')
            self.small_flg_img = flg_img.subsample(30, 30)
            event.widget["image"] = self.small_flg_img

    def pushed_grid(self,i,j):
        def expanding_pushed_button():
            # ゲームスタートしていないとき
            
            if not self.game.is_gamestart:
                self.game.gameStart(i,j)
                expand_area_pos = self.game.get_expandAreaPos(i,j)
                for pos in expand_area_pos:
                    self.disable_button(pos[0], pos[1], self.game.map[pos[0]][pos[1]])
            else :
                # 爆弾をタッチしたら
                if self.game.map[i][j] == -1:
                    self.game.map_visit[i][j] = 1
                    self.buttons[i][j].destroy()
                    bomb_img = tkinter.PhotoImage(file = 'Bomb.png')
                    self.small_bomb_img = bomb_img.subsample(30, 30)
                    self.buttons[i][j] = tkinter.Button(self.main_win, image = self.small_bomb_img, relief='sunken')
                    self.buttons[i][j].place(x=20*i+100, y=20*j+100, width=20, height=20)

                else :
                    # print(self.game.map[i][j])
                    expand_area_pos = self.game.get_expandAreaPos(i,j)
                    for pos in expand_area_pos:
                        self.disable_button(pos[0], pos[1], self.game.map[pos[0]][pos[1]])
                
        return expanding_pushed_button

    # widgets 準備
    def widgets(self):
        self.buttons = []
        for i in range(15):
            button = []
            for j in range(15):
                b = tkinter.Button(self.main_win, command=self.pushed_grid(i,j))
                b.bind("<Button-3>", lambda event: self.put_flg(event,i,j))                 
                button.append(b)
            
            self.buttons.append(button)
        

    # widgets 配置
    def position(self):
        for i in range(15):
            for j in range(15):
                self.buttons[i][j].place(x=20*i+100, y=20*j+100, width=20, height=20)
