import time
import random
from source.implicit_treap import ImplicitTreap, ImplicitTreapNode
memory = []
durt = [100, 1000, 5000, 10000, 50000, 100000, 500000, 100000, 200000]
for dur in durt:
    start_time = time.time()
    # list = ImplicitTreap.innit(array=[0])
    # for i in range(dur):
    #     node = ImplicitTreapNode(17, random.random())
    #     list = ImplicitTreap.insert(list, node, 1)
    list = []
    for i in range(dur):
        list.insert(0, 17)
    # print(list.size)
    end_time = time.time()
    duration = end_time - start_time
    memory.append(duration)
print(memory)
# print("Duration is " + str(duration))
