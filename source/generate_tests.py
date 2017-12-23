import random

file = open("08.txt", "w")
for i in range(500):
    file.write("insert 1 "+ str(int(random.random()*100))+" 1\n")
# for j in range(9999):
#     file.write("delete 1 1 \n")

# file.write("split 1 300\n")
# file.write("split 3 300\n")
# file.write("size 4")
