from tkinter import *
from app.fruit_reader import read_fruit_list
import app.components as comp


class App:
    def __init__(self, root):
        self.fruit_list = read_fruit_list("fruit.csv")
        self.root = root
        # init selection view
        self.selection_ui = comp.SelectionFrame(
            fruit_list=self.fruit_list, master=root)
        self.selection_ui.pack()
        # init detail view
        self.detail_frame = comp.DetailFrame(
            fruit_list=self.fruit_list, master=root)
        self.detail_frame.pack(pady=15)
        # bind change image callback to TreeView
        self.selection_ui.set_select_callback(self.detail_frame.select_fruit)
        # default selection

    def start(self):
        self.root.mainloop()


def start():
    master = Tk()
    master.title("pokemmo-fruit")
    master.geometry("300x370")
    master.resizable(width=False, height=False)
    app = App(master)
    app.start()


if __name__ == '__main__':
    start()
