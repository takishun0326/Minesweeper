import tkinter
from tkinter import ttk

from Game import Game

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



    def pushed_grid(self,i,j):
        def disable_button():
            self.game.gameStart(i,j)
            # 押されたマスを押された状態で保持された物へ変更
            self.buttons[i][j].destroy()
            self.buttons[i][j] = tkinter.Button(self.main_win,text='0', relief='sunken')
            self.buttons[i][j].place(x=20*i+100, y=20*j+100, width=20, height=20)
            print("pushed " + str(i) + str(j))

        return disable_button

    # widgets 準備
    def widgets(self):
        self.buttons = []
        for i in range(15):
            button = []
            for j in range(15):
                button.append(tkinter.Button(self.main_win,text=i, command=self.pushed_grid(i,j)))
            
            self.buttons.append(button)

    # widgets 配置
    def position(self):
        for i in range(15):
            for j in range(15):
                self.buttons[i][j].place(x=20*i+100, y=20*j+100, width=20, height=20)
