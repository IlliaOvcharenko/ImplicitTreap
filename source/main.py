from source.implicit_treap import ImplicitTreap


imp_treap = ImplicitTreap([1, 2, 3, 4, 5])
# imp_treap[1] = 100
# imp_treap[5] = 17
# imp_treap[1] = 17

imp_treap.print()
print(imp_treap.size())
print(imp_treap[4])
print(imp_treap.get_sum(1, 4))
imp_treap[1] = 17

print(imp_treap.get_sum(0, 5))
# imp_treap.print()
# print(imp_treap.size())
# print(imp_treap[2])
ImplicitTreap.delete(imp_treap._root, 2)
imp_treap.print()

# print(imp_treap[2])
