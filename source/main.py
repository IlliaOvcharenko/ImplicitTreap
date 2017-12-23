import sys
sys.path.append("../")
import source.gui as gui
from source.implicit_treap import ImplicitTreap

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
        try:
            file = open(file_name, 'r')
            # for comm in file:

        except:
            print("No such file.\nexit")
    else:
        treap_array = [ImplicitTreap(array=[1, 2, 3, 4, 5])]
        print("For exit type 'exit'")
        print("If you need some help type 'help'")
        print("You have already treap with index 1 and values [1, 2, 3, 4, 5]")
        comm = input("Enter command ")
        while comm != "exit":
            try:
                comm_arr = comm.split(" ")
                if comm_arr[0] == "size":
                    treap_index = int(comm_arr[1]) - 1
                    print("Size is " + str(treap_array[treap_index].size()))

                elif comm_arr[0] == "insert":
                    treap_index = int(comm_arr[1]) - 1
                    value = int(comm_arr[2])
                    index = int(comm_arr[3])
                    treap_array[treap_index][index] = value

                elif comm_arr[0] == "delete":
                    treap_index = int(comm_arr[1]) - 1
                    index = int(comm_arr[2])
                    treap_array[treap_index].erase(index)

                elif comm_arr[0] == "get_sum":
                    treap_index = int(comm_arr[1]) - 1
                    left = int(comm_arr[2])
                    right = int(comm_arr[3])
                    print("Sum is " + str(treap_array[treap_index].get_sum(left, right)))

                elif comm_arr[0] == "split":
                    treap_index = int(comm_arr[1]) - 1
                    index = int(comm_arr[2])
                    first, second = treap_array[treap_index].divide(index)
                    treap_array.append(first)
                    treap_array.append(second)
                    length = len(treap_array)
                    print("First part index is %s, second part index is %s" % (length - 1, length - 2))

                elif comm_arr[0] == "add_treap":
                    values = map(int, comm_arr[1:])
                    treap_array.append(ImplicitTreap(array=values))
                    index_of_new_item = len(treap_array)
                    print("New treap index is %s" % index_of_new_item)

                elif comm_arr[0] == "merge":
                    first_treap_index = int(comm_arr[1]) - 1
                    second_treap_index = int(comm_arr[2]) - 1
                    treap_array.append(
                        treap_array[first_treap_index].union(treap_array[second_treap_index]))

                    index_of_new_item = len(treap_array)
                    print("New treap index is %s" % index_of_new_item)

                elif comm_arr[0] == "reverse":
                    treap_index = int(comm_arr[1]) - 1
                    left = int(comm_arr[2])
                    right = int(comm_arr[3])
                    treap_array[treap_index].invert(left, right)

                elif comm_arr[0] == "print":
                    treap_index = int(comm_arr[1]) - 1
                    treap_array[treap_index].print()

                elif comm_arr[0] == "get_item":
                    treap_index = int(comm_arr[1]) - 1
                    index = int(comm_arr[2])
                    print(treap_array[treap_index][index])

                elif comm_arr[0] == "help":
                    answer = """
    Functions:
        size <index_of_treap>
        insert <index_of_treap> <index_in_treap> <value>
        delete <index_of_treap> <index_of_item_in_treap>
        get_sum <index_of_treap> <left_bound> <right_bound>
        split <index_of_treap> <index_to_spit>
        add_treap [ <values_to_add> ]
        merge <index_of_first_treap> <index_of_second_treap>
        reverse <index_of_treap> <left_bound> <right_bound>
        print <index_of_treap>
        get_item <index_of_treap> <index_of_item_in_treap>
        help - you are here :)
                    """
                    print(answer)
            except:
                print("Wrong command, try one more time")
            comm = input("Enter command ")
    # arr = ImplicitTreap(array=[1, 2, 3, 4, 5])
    # arr.erase(1)
    # print(arr.size())
    # arr.erase(1)
    # arr.print()
    # print(arr.size())
