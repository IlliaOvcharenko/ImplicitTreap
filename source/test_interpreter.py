import sys
sys.path.append("../")
from source.implicit_treap import ImplicitTreap


class TestInterpreter:

    @staticmethod
    def command_execute(com, tp_arr):
        try:
            com = com.strip()
            comm_arr = com.split(" ")
            if comm_arr[0] == "size":
                treap_index = int(comm_arr[1]) - 1
                print("Size is " + str(tp_arr[treap_index].size()))

            elif comm_arr[0] == "insert":
                treap_index = int(comm_arr[1]) - 1
                value = int(comm_arr[2])
                index = int(comm_arr[3])
                tp_arr[treap_index][index] = value

            elif comm_arr[0] == "delete":
                treap_index = int(comm_arr[1]) - 1
                index = int(comm_arr[2])
                tp_arr[treap_index].erase(index)

            elif comm_arr[0] == "get_sum":
                treap_index = int(comm_arr[1]) - 1
                left = int(comm_arr[2])
                right = int(comm_arr[3])
                print("Sum is " + str(tp_arr[treap_index].get_sum(left, right)))

            elif comm_arr[0] == "split":
                treap_index = int(comm_arr[1]) - 1
                index = int(comm_arr[2])
                first, second = tp_arr[treap_index].divide(index)
                tp_arr.append(first)
                tp_arr.append(second)
                length = len(tp_arr)
                print("First part index is %s, second part index is %s" % (length - 1, length))

            elif comm_arr[0] == "add_treap":
                values = map(int, comm_arr[1:])
                tp_arr.append(ImplicitTreap(array=values))
                index_of_new_item = len(tp_arr)
                print("New treap index is %s" % index_of_new_item)

            elif comm_arr[0] == "merge":
                first_treap_index = int(comm_arr[1]) - 1
                second_treap_index = int(comm_arr[2]) - 1
                tp_arr.append(
                    tp_arr[first_treap_index].union(tp_arr[second_treap_index]))

                index_of_new_item = len(tp_arr)
                print("New treap index is %s" % index_of_new_item)

            elif comm_arr[0] == "reverse":
                treap_index = int(comm_arr[1]) - 1
                left = int(comm_arr[2])
                right = int(comm_arr[3])
                tp_arr[treap_index].invert(left, right)

            elif comm_arr[0] == "print":
                treap_index = int(comm_arr[1]) - 1
                tp_arr[treap_index].print()

            elif comm_arr[0] == "number_of_treaps":
                num = len(tp_arr)
                print("There are %s treaps" % num)

            elif comm_arr[0] == "get_item":
                treap_index = int(comm_arr[1]) - 1
                index = int(comm_arr[2])
                print(tp_arr[treap_index][index])

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
    number_of_treaps
    help - you are here :)
                            """
                print(answer)
        except Exception:
            print("Wrong command, try one more time")

    @staticmethod
    def file_mode(file_name, treap_array):
        try:
            file = open(file_name, 'r')
            for comm in file:
                TestInterpreter.command_execute(comm, treap_array)
        except:
            print("No such file.\nexit")

    @staticmethod
    def console_mode(treap_array=None):
        str = ""
        if treap_array is None:
            treap_array = [ImplicitTreap(array=[1, 2, 3, 4, 5])]
            str = "1, 2, 3, 4, 5"
        print("For exit type 'exit'")
        print("If you need some help type 'help'")
        print("You have already treap with index 1 and values ["+ str +"]")
        comm = input("Enter command ")
        while comm != "exit":
            TestInterpreter.command_execute(comm, treap_array)
            comm = input("Enter command ")
