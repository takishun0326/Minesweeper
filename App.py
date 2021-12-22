import tkinter
from tkinter import ttk

from Frame import Frame

WIDTH = 500
HEIGHT = 500



if __name__ == '__main__':

    main_win = tkinter.Tk()
    main_win.title("MineSweeper")
    main_win.geometry(str(WIDTH)+'x'+str(HEIGHT))


    # Menu

    # Frame
    Frame.Frame(main_win)



    main_win.mainloop()
    