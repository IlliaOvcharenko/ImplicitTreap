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
    interp = TestInterpreter()
    interp.console_mode()

