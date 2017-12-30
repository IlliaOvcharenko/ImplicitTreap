"""
Класс-наследник обычного неаяного декартового дерева с функциями построения графа в graphviz
Для использования (сейчас неожиданность :) ) необходимо наличие данной библиотеки
В этом проекте используется только в gui
"""

from source.implicit_treap import *
import graphviz as gv


class GuiImplicitTreap(ImplicitTreap):
    def get_graph(self, format_type="gif"):
        graph = gv.Graph(format=format_type)
        graph = GuiImplicitTreap.create_graph(self._root, graph)[0]
        return graph

    @staticmethod
    def create_graph(tree: ImplicitTreapNode, graph: gv.Graph, add: int = 0):
        if tree is None:
            return graph, None
        current_key = add + ImplicitTreapNode.get_left_size(tree)
        label = "V: %s, P: %s" % (tree.val, round(tree.priority, 3))
        graph.node(str(current_key), label=label)
        first_key = GuiImplicitTreap.create_graph(tree.left, graph, add)[1]
        new_add = add + 1 + ImplicitTreapNode.get_left_size(tree)
        second_key = GuiImplicitTreap.create_graph(tree.right, graph, new_add)[1]
        if first_key is not None:
            graph.edge(str(current_key), str(first_key), color="blue")
        if second_key is not None:
            graph.edge(str(current_key), str(second_key), color="red")
        return graph, current_key

    @staticmethod
    def from_implicit_treap(tree: ImplicitTreap):
        new_tree = GuiImplicitTreap()
        new_tree._root = tree._root
        return new_tree