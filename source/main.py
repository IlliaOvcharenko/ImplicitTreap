import sys
sys.path.append("../")
import source.gui as gui
from source.implicit_treap import ImplicitTreap

mode = "console"
if len(sys.argv) > 1:
    mode = sys.argv[1]

if mode == "gui":
    interface = gui.GUI()
else:
    print("interactive mode")
    arr = ImplicitTreap(array=[1, 2, 3, 4, 5])
    first, second = arr.divide(3)
    new = second.union(first)
    new.print()
