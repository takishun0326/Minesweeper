import tkinter
from tkinter import ttk

#from ..Game import Game

WIDTH = 500
HEIGHT = 500

class Frame:
    def __init__(self, main_win):
        self.main_win = main_win

        self.frame = tkinter.Frame(main_win, width=500, height=500)
        self.frame.pack()

        self.widgets()
        self.position()



    def pushed_grid(self,i,j):
        def tmp():
            print("pushed " + str(i) + str(j))
        return tmp


    def widgets(self):
        self.buttons = []
        for i in range(15):
            button = []
            for j in range(15):
                button.append(tkinter.Button(self.main_win,text=i, command=self.pushed_grid(i,j)))
            
            self.buttons.append(button)

    def position(self):
        for i in range(15):
            for j in range(15):
                self.buttons[i][j].place(x=20*i+100, y=20*j+100, width=20, height=20)
