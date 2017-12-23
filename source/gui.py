import sys
sys.path.append("../")
from source.implicit_treap import ImplicitTreap
from source.test_interpreter import TestInterpreter
import graphviz as gv
import random
import tkinter as tk


class GUI:
    def __init__(self):
        tree = ImplicitTreap(array=[1, 2, 3, 4, 5, 6])
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
        self.label_name.pack(side="top", pady=50)
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

        self.entry_add_from_file = tk.Entry(self.root)
        self.entry_add_from_file.pack()
        self.btn_add_from_file = tk.Button(self.root, command=self.add_from_file, text="Add from file")
        self.btn_add_from_file.pack()

        self.entry_delete = tk.Entry(self.root)
        self.entry_delete.pack()
        self.btn_delete = tk.Button(self.root, command=self.delete,
                                           text="Delete item by index")
        self.btn_delete.pack()
        self.entry_reverse = tk.Entry(self.root)
        self.entry_reverse.pack()
        self.btn_reverse = tk.Button(self.root, command=self.reverse,
                                    text="Reverse")
        self.btn_reverse.pack()

        self.btn_add_random = tk.Button(self.root, command=self.add_random, text="Add random node")
        self.btn_add_random.pack(pady=16)
        self.btn_clean = tk.Button(self.root, command=self.clean, text="Clean")
        self.btn_clean.pack(pady=16)


        self.label_description = tk.Label(self.root, text="V - value, P - priority\n "
                                                          "left edge is blue, right edge is red")
        self.label_description.pack(side="bottom")

        self.label_size = tk.Label(self.root, text="size")
        self.label_size.pack(side="bottom")
        txt_frm = tk.Frame(self.root, width=600, height=600)
        txt_frm.pack(fill="both", expand=True)
        txt_frm.grid_propagate(False)
        txt_frm.grid_rowconfigure(0, weight=1)
        txt_frm.grid_columnconfigure(0, weight=1)

        self.txt = tk.Text(txt_frm, bd=0, borderwidth=0, relief="sunken")
        self.txt.config(font=("consolas", 18), undo=True, wrap='word')
        self.txt.grid(row=0, column=0, sticky="nsew", padx=2, pady=2)

        scrollb = tk.Scrollbar(txt_frm, command=self.txt.yview)
        scrollb.grid(row=0, column=1, sticky='nsew')
        self.txt['yscrollcommand'] = scrollb.set
        self.update_graph()
        self.root.mainloop()

    def delete(self):
        index = int(self.entry_delete.get())
        self.implicit_treap.erase(index)
        self.update_graph()

    def reverse(self):
        first, second = list(map(int, self.entry_reverse.get().strip().split("-")))
        self.implicit_treap.invert(first, second)
        self.implicit_treap.print()
        self.update_graph()



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

    def add_from_file(self):
        arr = [ImplicitTreap(root=None)]
        file_name = self.entry_add_from_file.get()
        TestInterpreter.file_mode(file_name, arr)
        self.implicit_treap = arr[0]
        self.update_graph()


    def update_graph(self):
        if self.implicit_treap._root is not None:
            self.label_size["text"] = "Size is %s" % self.implicit_treap.size()
        else:
            self.label_size["text"] = "Size is 0"

        array = []
        self.implicit_treap.print(list=array)
        self.txt.delete('1.0', tk.END)
        self.txt.insert(tk.INSERT, str(array))
        self.cnv.delete("all")
        graph = self.implicit_treap.get_graph()
        data = graph.pipe()
        image_update = tk.PhotoImage(data=data, format="gif")
        self.cnv.create_image(0, 0, image=image_update, anchor="nw")
        self.cnv.image = image_update
        self.cnv.grid(row=0, column=0, sticky=tk.N + tk.S + tk.E + tk.W)
        self.cnv.config(scrollregion=self.cnv.bbox(tk.ALL))
        self.cnv.update()
