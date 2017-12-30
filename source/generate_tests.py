import random

file = open("../tests/14.txt", "w")
file.write("# тест на добавление 10 элементов в дерамиду с индексом 2\n")
file.write("add_treap\n")
file.write("# Wait...\n")
for i in range(10):
    file.write("insert 2 "+ str(int(random.random()*100))+" 1\n")


# for j in range(9999):
#     file.write("delete 1 1 \n")

# file.write("split 1 300\n")
# file.write("split 3 300\n")
# file.write("size 4")
