from tkinter import *
from module.fruit_reader import read_fruit_list
from components import SelectionFrame, DetailFrame


class App:
    def __init__(self, root):
        self.fruit_list = read_fruit_list("../fruit.csv")
        self.root = root
        self.selection_ui = SelectionFrame(fruit_list=self.fruit_list, master=root)
        self.selection_ui.pack()
        self.detail_frame = DetailFrame(fruit_list=self.fruit_list, master=root)
        self.detail_frame.pack()

        self.selection_ui.set_select_callback(self.detail_frame.select_fruit)  # set callback

    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    master = Tk()
    master.title("pokemmo-fruit")
    master.geometry("300x400")
    app = App(master)
    app.start()
