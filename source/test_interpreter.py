import sys
import time
import psutil
sys.path.append("../")
from source.implicit_treap import ImplicitTreap


class TestInterpreter:
    def __init__(self, treap_array=None):
        if treap_array is not None:
            self.treap_array = treap_array
        else:
            self.treap_array = [ImplicitTreap()]

    def get_treap_array(self):
        return self.treap_array

    def command_execute(self, com):
        try:
            com = com.strip()
            comm_arr = com.split(" ")
            if comm_arr[0] == "size":
                treap_index = int(comm_arr[1]) - 1
                print("Size is " + str(self.treap_array[treap_index].size()))

            elif comm_arr[0] == "insert":
                treap_index = int(comm_arr[1]) - 1
                index = int(comm_arr[3])
                value = int(comm_arr[2])
                self.treap_array[treap_index][index] = value

            elif comm_arr[0] == "delete":
                treap_index = int(comm_arr[1]) - 1
                index = int(comm_arr[2])
                self.treap_array[treap_index].erase(index)

            elif comm_arr[0] == "get_sum":
                treap_index = int(comm_arr[1]) - 1
                left = int(comm_arr[2])
                right = int(comm_arr[3])
                print("Sum is " + str(self.treap_array[treap_index].get_sum(left, right)))

            elif comm_arr[0] == "split":
                treap_index = int(comm_arr[1]) - 1
                index = int(comm_arr[2])
                first, second = self.treap_array[treap_index].divide(index)
                self.treap_array.append(first)
                self.treap_array.append(second)
                length = len(self.treap_array)
                print("First part index is %s, second part index is %s" % (length - 1, length))

            elif comm_arr[0] == "add_treap":
                values = map(int, comm_arr[1:])
                self.treap_array.append(ImplicitTreap(array=values))
                index_of_new_item = len(self.treap_array)
                print("New treap index is %s" % index_of_new_item)

            elif comm_arr[0] == "merge":
                first_treap_index = int(comm_arr[1]) - 1
                second_treap_index = int(comm_arr[2]) - 1
                self.treap_array.append(
                    self.treap_array[first_treap_index].union(self.treap_array[second_treap_index]))

                index_of_new_item = len(self.treap_array)
                print("New treap index is %s" % index_of_new_item)

            elif comm_arr[0] == "reverse":
                treap_index = int(comm_arr[1]) - 1
                left = int(comm_arr[2])
                right = int(comm_arr[3])
                self.treap_array[treap_index].invert(left, right)

            elif comm_arr[0] == "full_print":
                treap_index = int(comm_arr[1]) - 1
                print("")
                self.treap_array[treap_index].print()

            elif comm_arr[0] == "print":
                treap_index = int(comm_arr[1]) - 1
                array_of_items = []
                print("")
                self.treap_array[treap_index].print(list=array_of_items, console_print=False)
                print(array_of_items)
                print("")

            elif comm_arr[0] == "number_of_treaps":
                num = len(self.treap_array)
                print("There are %s treaps" % num)

            elif comm_arr[0] == "get_item":
                treap_index = int(comm_arr[1]) - 1
                index = int(comm_arr[2])
                print(self.treap_array[treap_index][index])

            elif comm_arr[0] == "read_file":
                file_name = comm_arr[1]
                # try:
                #     file = open(file_name, 'r')
                #     for comm in file:
                #         TestInterpreter.command_execute(comm, tp_arr)
                #
                # except:
                #     print("No such file")
                proc = psutil.Process()
                start_time = time.time()
                start_memory = proc.memory_info()[0]
                self.file_mode(file_name)
                end_time = time.time()
                end_memory = proc.memory_info()[0]
                print("Execution time is " + str(end_time - start_time))
                print("Memory usage is around " + str(end_memory - start_memory) + " bytes")

            elif comm_arr[0] == "#":
                print("")
                print(" ".join(comm_arr[1:]))
                print("")

            elif comm_arr[0] == "clean":
                self.treap_array = [ImplicitTreap()]

            elif comm_arr[0] == "test":
                file_name = "tests/" + comm_arr[1] + ".txt"
                command = "read_file " + file_name
                self.command_execute(command)

            elif comm_arr[0] == "help":
                answer = """
Functions:

    size <index_of_treap> - получить размер указанной дерамиды с индексом index_of_treap.

    insert <index_of_treap> <index_in_treap> <value> 
    Вставить в дерамиду с индексом index_of_treap
    значение value на позицию index_in_treap, при этом элемент который находится там не удаляется, 
    а сдвигается влево.

    delete <index_of_treap> <index_of_item_in_treap>
    Удалить элемент с индексом 
    index_of_item_in_treap из дерамиды с индексом index_of_treap, элементы сдигаются вправо, тем 
    самым заполняя экзистенциальную пустоту внутри.
    АХТУНГ! Не удалять последний элемент, так как это корень дерева.
    
    get_sum <index_of_treap> <left_bound> <right_bound> 
    Получить сумму на отрезке 
    [left_bound, right_bound] (левая и правая границы включительно) в дерамиде с индексом 
    index_of_treap .
    
    split <index_of_treap> <index_to_spit> 
    Разбить дерамиду с индексом index_of_treap на две по индексу index_to_spit, выводит индексы 
    полученных дерамид. 
    АХТУНГ! Входящая дерамиды поменяет поменять свое содержимое (в ней останется первая 
    часть, так как дерамида передается по ссылке, а не копируется; дерамида не персистентная)
     
    add_treap [ <values_to_add> ]
    Добавить новую дерамиду с элементами [ <values_to_add> ] (элементы для добавления можно 
    перечислять через пробел), выводит индекс нового дерева.
    
    merge <index_of_first_treap> <index_of_second_treap> 
    Слить две дерамиды с индексами index_of_first_treap и index_of_second_treap в одну дерамиду,
    выводит индекс новой дерамиды. 
    АХТУНГ! Не стоит сливать одинаковые куски одной и той же дерамид, так как
    это приведет к бесконечной рекурсии; всходящие дерамиды могут поменять свое содержимое (дерамиды
    передаются по ссылке, а не копируется; дерамида не персистентная)
    
    reverse <index_of_treap> <left_bound> <right_bound>
    Развернуть элементы на отрезке [left_bound, right_bound] (левая и правая границы включительно) 
    в дерамиде с индексом index_of_treapв обратном порядке.
    
    print <index_of_treap>
    Вывести содержимое дерамиды с индексом index_of_treap в виде массива
    
    full_print <index_of_treap>
    Вывести значение элементов и их приоритеты для дерамиды с индексом index_of_treap 
    
    get_item <index_of_treap> <index_of_item_in_treap> 
    Получить элемент из дерамиды index_of_treap с индексом index_of_item_in_treap.
    
    number_of_treaps
    Вывести текущее количестов дерамид к которым можно обратиться.
    
    read_file <file_name>
    Выполняет тест из файли с именем file_name.
    
    test <test_name>
    Выполняет команду read_file для теста test_name (test_name - название файла в папке tests без 
    указания расширения .txt, эта информация подставляется автоманически)
    
    # <string>
    Выводит входящюю строку без изменений.
    
    clean
    Удаляет все дерамиды, создается пустая дерамида с индексом 1. 
    АХТУНГ! Используется в тестах.
    
    help
    Получить справку. Ты тут :)
                            """
                print(answer)
            else:
                print("No such command, try one more time")

        except Exception as ex:
            print("Wrong command, try one more time")
            # print(ex)

    def file_mode(self, file_name):
        try:
            file = open(file_name, 'r')
            for comm in file:
                self.command_execute(comm)
        except:
            print("No such file.\nexit")

    def console_mode(self):
        # str = ""
        # if self.treap_array is None:
        self.treap_array = [ImplicitTreap(array=[1, 2, 3, 4, 5])]
        str = "1, 2, 3, 4, 5"
        print("For exit type 'exit'")
        print("If you need some help type 'help'")
        print("You have already treap with index 1 and values ["+ str +"]")
        comm = input("Enter command: ")
        while comm.strip() != "exit":
            self.command_execute(comm)
            comm = input("Enter command: ")
