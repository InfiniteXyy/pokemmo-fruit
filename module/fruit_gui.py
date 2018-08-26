from tkinter import *
from tkinter.ttk import Treeview, Scrollbar
from module.fruit_reader import read_fruit_list
from module.models import *
import PIL.Image
import PIL.ImageTk


class App:
    def __init__(self, root):
        self.fruit_list = read_fruit_list("../fruit.csv")
        self.root = root
        self.init_selection_window()
        self.init_detail_frame()

    def init_selection_window(self):
        div = Frame(self.root)
        div.grid(row=0, column=0, padx=10)
        # init drop down
        type_select = StringVar(div)
        type_select.set(TYPES[0])  # default value
        type_options = OptionMenu(div, type_select, *TYPES, command=self.select_type)
        type_options.grid(row=0, column=0, ipady=10)
        # init treeView
        self.tree = Treeview(div, columns=["名称", "效果"], show="headings")
        self.tree.column("名称", width=50, anchor='center')
        self.tree.column("效果", width=150, anchor='center')
        self.tree.heading("名称", text="名称")
        self.tree.heading("效果", text="效果")
        self.select_type(TYPES[0])
        self.tree.grid(row=1, column=0)
        self.tree.bind("<Double-1>", self.select_item)
        vbar = Scrollbar(div, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vbar.set)
        vbar.grid(row=1, column=1, sticky=NS)

    def select_type(self, fruit_type):
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

        for x in self.fruit_list:
            if x.get_type() == fruit_type:
                self.tree.insert("", END, value=(x.name, x.description))

    def init_detail_frame(self):
        img = PIL.Image.open("../assets/imgs/木子果.png")
        photo = PIL.ImageTk.PhotoImage(img, size=(200, 200))
        panel = Label(self.root, image=photo, width=84, height=84)
        panel.image = photo
        self.image_panel = panel
        panel.grid(row=0, column=1)

    def select_item(self, event):
        item = self.tree.selection()[0]
        print("you clicked on", self.tree.item(item, "value")[0])
        img = PIL.Image.open("../assets/imgs/{}.png".format(self.tree.item(item, "value")[0]))
        photo = PIL.ImageTk.PhotoImage(img, size=(200, 200))
        self.image_panel.config(image=photo)
        self.image_panel.image = photo


    def start(self):
        self.root.mainloop()


if __name__ == '__main__':
    master = Tk()
    master.title("pokemmo-fruit")
    master.geometry("500x400")
    app = App(master)
    app.start()
