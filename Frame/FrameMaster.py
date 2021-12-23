import tkinter
from tkinter import ttk

from Frame import Frame

class FrameMaster:
    def __init__(self, main_win):
        self.main_win = main_win
        self.frame = Frame.Frame(self.main_win)
        

        smile_img = tkinter.PhotoImage(file = 'Smile.png')
        self.s_smile_img = smile_img.subsample(10,10)
        self.restart_button = tkinter.Button(self.main_win, image=self.s_smile_img, command=self.game_restart)
        self.restart_button.place(x=170, y=20, width=60, height=60)
    def game_restart(self):
        self.frame = Frame.Frame(self.main_win)