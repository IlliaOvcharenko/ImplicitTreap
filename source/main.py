import sys
sys.path.append("../")
import source.gui as gui
from source.implicit_treap import ImplicitTreap
from source.test_interpreter import TestInterpreter

mode = "console"
if len(sys.argv) > 1:
    mode = sys.argv[1]

# mode = "gui"
if mode == "gui":
    interface = gui.GUI()
else:
    print("Interactive mode")
    answer = input("Read test from file (type Y to agree) ")
    if answer == "Y":
        file_name = input("Enter file name: ")
        it = [ImplicitTreap(root=None)]
        TestInterpreter.file_mode(file_name, it)
        TestInterpreter.console_mode(treap_array=it)
    else:
        TestInterpreter.console_mode()

