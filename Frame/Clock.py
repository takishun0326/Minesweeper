import time
from tkinter import ttk
import tkinter

class Clock:
    def __init__(self,main_win):

        self.main_win = main_win

        self.sec = 0
        
        self.is_game_finished = False

        # Timer
        self.timer_min_label = tkinter.StringVar()
        self.timer_sec_label = tkinter.StringVar()

        # Timer
        self.timer_min_label.set('00 ：')
        self.timer_sec_label.set('00')
        self.timer_min = tkinter.Label(self.main_win, textvariable=self.timer_min_label)
        self.timer_sec = tkinter.Label(self.main_win, textvariable=self.timer_sec_label)

        self.timer_min.place(x=280,y=20, anchor=tkinter.NW, width=70, height = 60)
        self.timer_sec.place(x=330,y=20, anchor=tkinter.NW, width=40, height=60)


    def timer(self):
        # ゲーム中なら
        if not self.is_game_finished:
            self.main_win.after(1000, self.timer)
            self.sec += 1
            self.timer_min_label.set(format(int(self.sec/60), '02') + ' ：')
            self.timer_sec_label.set(format((self.sec%60), '02'))

    def start_timer(self):
        self.timer()           

    def game_over(self):
        self.timer_min['fg'] = 'red'
        self.timer_sec['fg'] = 'red'
        self.is_game_finished = True

    def game_clear(self):
        self.timer_min['fg'] = 'green2'
        self.timer_sec['fg'] = 'green2'
        self.is_game_finished = True