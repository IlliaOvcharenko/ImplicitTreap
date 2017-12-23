from source.implicit_treap import ImplicitTreap
import graphviz as gv
import random
import tkinter as tk


class GUI:
    def __init__(self):
        tree = ImplicitTreap(array=[1,2,3,4,5,6])
        first, second = tree.divide(0)
        second, third = second.divide(5)
        self.implicit_treap = second

        graph = self.implicit_treap.get_graph()
        data = graph.pipe()
        self.root = tk.Tk()
        self.root.title("Implicit Treap")
        self.root.geometry("1300x750")
        self.root.resizable(width=False, height=False)
        image = tk.PhotoImage(data=data, format="gif")
        self.frame = tk.Frame(self.root, bd=0, relief=tk.FLAT)

        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)

        xscrollbar = tk.Scrollbar(self.frame, orient=tk.HORIZONTAL)
        xscrollbar.grid(row=1, column=0, sticky=tk.E + tk.W)

        yscrollbar = tk.Scrollbar(self.frame)
        yscrollbar.grid(row=0, column=1, sticky=tk.N + tk.S)

        self.cnv = tk.Canvas(self.frame, bd=0, width=900, height=750,
                             xscrollcommand=xscrollbar.set,
                             yscrollcommand=yscrollbar.set)
        self.cnv.create_image(0, 0, image=image, anchor="nw")

        self.cnv.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.cnv.config(scrollregion=self.cnv.bbox(tk.ALL))

        xscrollbar.config(command=self.cnv.xview)
        yscrollbar.config(command=self.cnv.yview)
        self.frame.pack(side="right")
        self.label_name = tk.Label(self.root, text="Implicit Treap")
        self.label_name.config(font=("American Typewriter", 44))
        self.label_name.pack(side="top", pady=100)
        self.label_name = tk.Label(self.root, text="Node value")
        self.label_name.pack()
        self.entry_add_node_val = tk.Entry(self.root)
        self.entry_add_node_val.pack()
        self.label_name = tk.Label(self.root, text="Node index")
        self.label_name.pack()
        self.entry_add_node_index = tk.Entry(self.root)
        self.entry_add_node_index.pack()
        self.btn_add_node = tk.Button(self.root, command=self.add_node, text="Add node")
        self.btn_add_node.pack()
        self.btn_add_random = tk.Button(self.root, command=self.add_random, text="Add random node")
        self.btn_add_random.pack(pady=16)
        self.btn_clean = tk.Button(self.root, command=self.clean, text="Clean")
        self.btn_clean.pack(pady=16)
        self.label_description = tk.Label(self.root, text="V - value, P - priority\n "
                                                          "left edge is blue, right edge is red")
        self.label_description.pack(side="bottom")
        self.root.mainloop()

    def clean(self):
        self.implicit_treap = ImplicitTreap([])
        self.update_graph()

    def add_random(self):
        self.implicit_treap[0] = int(random.random() * 100)
        self.update_graph()

    def add_node(self):
        new_val = int(self.entry_add_node_val.get())
        new_index = int(self.entry_add_node_index.get())
        self.implicit_treap[new_index] = new_val
        self.update_graph()

    def update_graph(self):
        self.cnv.delete("all")
        graph = self.implicit_treap.get_graph()
        data = graph.pipe()
        image_update = tk.PhotoImage(data=data, format="gif")
        self.cnv.create_image(0, 0, image=image_update, anchor="nw")
        self.cnv.image = image_update
        self.cnv.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.cnv.config(scrollregion=self.cnv.bbox(tk.ALL))
        self.cnv.update()
