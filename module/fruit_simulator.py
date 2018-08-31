from tkinter import *
import module.components as comp


class Simulator(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("680x500")
        self.resizable(width=False, height=False)
        self.title("模拟器")
        self.init_left()
        self.init_right()

    def init_left(self):
        left_frame = Frame(self)
        top_list = comp.ListFrame(master=left_frame, title="启动资源")
        bottom_list = comp.ListFrame(master=left_frame, title="当前资源")
        top_list.pack(fill=X)
        bottom_list.pack(fill=X)
        left_frame.place(relx=0, rely=0, relwidth=0.3, relheight=1.0)

    def init_right(self):
        rightFrame = Frame(self)
        display = comp.DisplayFrame(master=rightFrame)
        buttons = comp.ButtonGroup(master=rightFrame)
        display.pack(fill=X)
        buttons.pack(fill=X)
        rightFrame.place(relx=0.3, rely=0, relwidth=0.7, relheight=1.0)


if __name__ == '__main__':
    simulator = Simulator()
    simulator.mainloop()
