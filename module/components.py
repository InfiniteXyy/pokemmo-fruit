from tkinter import *
from tkinter.ttk import Treeview, Scrollbar
import models
import PIL.Image
import PIL.ImageTk


class SelectionFrame(Frame):
    def __init__(self, fruit_list, **kw):
        # init drop down
        super().__init__(**kw)
        self.fruit_list = fruit_list
        self.type_select = StringVar(self)
        type_options = OptionMenu(self, self.type_select, *models.TYPES, command=self.set_group)
        type_options.config(width=20)
        type_options.grid(row=0, column=0, pady=10)
        # init treeView
        self.tree = Treeview(self, columns=["名称", "效果"], show="headings")
        self.tree.column("名称", width=50, anchor='center')
        self.tree.column("效果", width=150, anchor='center')
        self.tree.heading("名称", text="名称")
        self.tree.heading("效果", text="效果")
        self.tree.grid(row=1, column=0)
        self.tree.bind("<Double-1>", self.select_item)
        self.select_item_callback = lambda x: x
        vbar = Scrollbar(self, orient=VERTICAL, command=self.tree.yview)
        self.tree.configure(yscrollcommand=vbar.set)
        vbar.grid(row=1, column=1, sticky=NS)
        # default value
        self.set_group(models.TYPES[0])

    def set_group(self, group):
        self.type_select.set(group)
        x = self.tree.get_children()
        for item in x:
            self.tree.delete(item)

        for x in self.fruit_list:
            if x.get_type() == group:
                self.tree.insert("", END, value=(x.name, x.description))

    def select_item(self, event):
        item = self.tree.selection()[0]
        name = self.tree.item(item, "value")[0]
        self.select_item_callback(next(filter(lambda x: x.name == name, self.fruit_list)))

    def set_select_callback(self, callback):
        self.select_item_callback = callback


class DetailFrame(Frame):
    def __init__(self, fruit_list, **kw):
        super().__init__(**kw)
        self.fruit_list = fruit_list
        panel = Label(self)
        self.image_panel = panel
        panel.grid(row=0, column=0)
        self.descriptionVar = StringVar(self)
        self.seedVar = StringVar(self)
        self.nameVar = StringVar(self)
        Label(self, textvariable=self.nameVar, font=("Ping Fang", 16, "bold"), fg="#4a4a4a").grid(row=0, column=1)
        Label(self, textvariable=self.descriptionVar, font=("Ping Fang", 16), fg="#9b9b9b").grid(row=0, column=2)
        Label(self, textvariable=self.seedVar, font=("Ping Fang", 14), fg="#4a4a4a").grid(row=2, column=0, columnspan=3)

    def select_fruit(self, fruit):
        img = PIL.Image.open("../assets/imgs/{}.png".format(fruit.name))
        photo = PIL.ImageTk.PhotoImage(img)
        self.image_panel.config(image=photo)
        self.image_panel.image = photo
        self.nameVar.set(fruit.get_name())
        self.descriptionVar.set(fruit.get_description())
        self.seedVar.set(fruit.get_seeds())
