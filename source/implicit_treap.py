"""
Неявное декартовое дерево - радномизированное дерево поиска

Ведет себя как динамический массив с очень неплохой ассимптотикой для некоторых операций:
    insert() - O(log n) - вставка
    get_item() - O(log n) - получение элемента по индексу
    innit() - O(n log n) - создание дерево из массива
    get_sum() - O(log n) - сумма на отрезке
Глвный недостаток - большой расход по памяти по сравнению с обычним массивом
TODO не работает delete!
"""
import graphviz as gv
import random
import copy


class ImplicitTreapNode:
    def __init__(self, val, priority):
        self.val = val
        self.priority = priority
        self.left = None
        self.right = None
        self.size = 1
        self.reverse = False
        self.segment_sum = val

    def copy(self, new_node):

        self.val = new_node.val
        self.priority = new_node.priority
        self.left = new_node.left
        self.right = new_node.right
        self.size = new_node.size
        self.segment_sum = new_node.segment_sum

    @staticmethod
    def update_segment_sum(node):
        if node is not None:
            left_sum = 0 if node.left is None else node.left.segment_sum
            right_sum = 0 if node.right is None else node.right.segment_sum
            node.segment_sum = left_sum + node.val + right_sum

    @staticmethod
    def update_size(node):
        if node is not None:
            left_size = 0 if node.left is None else node.left.size
            right_size = 0 if node.right is None else node.right.size
            node.size = left_size + 1 + right_size

    @staticmethod
    def get_left_size(node):
        return 0 if node.left is None else node.left.size


class ImplicitTreap:
    def __init__(self, array=None, root=None):
        if root is not None:
            self._root = root
        elif array is not None:
            self._root = ImplicitTreap.innit(array=array)
        else:
            self._root = None

    def divide(self, index: int):
        first_root, second_root = ImplicitTreap.split(self._root, index)
        return ImplicitTreap(root=first_root), ImplicitTreap(root=second_root)

    def union(self, tree):
        root = ImplicitTreap.merge(self._root, tree._root)
        return ImplicitTreap(root=root)

    def __setitem__(self, key, value):
        node = ImplicitTreapNode(value, random.random())
        self._root = ImplicitTreap.insert(self._root, node, key)

    def __getitem__(self, item):
        item = ImplicitTreap.get_item(self._root, item)
        return None if item is None else item.val

    def size(self):
        return ImplicitTreap.get_size(self._root)

    def print(self, list=None):
        ImplicitTreap.print_tree(self._root, list)

    def get_sum(self, left, right):
        return ImplicitTreap.get_segment_sum(self._root, left, right)

    def get_graph(self, format_type="gif"):
        graph = gv.Graph(format=format_type)
        graph = ImplicitTreap.create_graph(self._root, graph)[0]
        return graph

    def erase(self, index):
        ImplicitTreap.delete(self._root, index)

    def invert(self, left, right):
        ImplicitTreap.reverse(self._root, left, right)

    @staticmethod
    def get_size(tree: ImplicitTreapNode):
        return tree.size

    @staticmethod
    def get_item(tree: ImplicitTreapNode, index: int, add: int = 0):
        if tree is None:
            return None
        current_key = add + ImplicitTreapNode.get_left_size(tree)
        if current_key == index:
            return tree

        if current_key < index:
            new_add = add + 1 + ImplicitTreapNode.get_left_size(tree)
            return ImplicitTreap.get_item(tree.right, index, new_add)
        else:
            return ImplicitTreap.get_item(tree.left, index, add)

    @staticmethod
    def reverse(tree, left, right):
        if right < left:
            left, right = right, left
        first_tree, second_tree = ImplicitTreap.split(tree, left)
        second_tree, third_tree = ImplicitTreap.split(second_tree, right - left + 1)
        second_tree.reverse = bool(True ^ second_tree.reverse)
        ImplicitTreap.merge(first_tree, ImplicitTreap.merge(second_tree, third_tree))

    @staticmethod
    def push_reverse(tree: ImplicitTreapNode):
        if tree is not None:
            if tree.reverse:
                tree.left, tree.right = tree.right, tree.left
                tree.reverse = False
                if tree.left is not None:
                    tree.left.reverse = bool(True ^ tree.left.reverse)
                if tree.right is not None:
                    tree.right.reverse = bool(True ^ tree.right.reverse)


    @staticmethod
    def get_segment_sum(tree: ImplicitTreapNode, left: int, right: int):
        if right < left:
            left, right = right, left
        first_tree, second_tree = ImplicitTreap.split(tree, left)
        second_tree, third_tree = ImplicitTreap.split(second_tree, right - left + 1)
        result = second_tree.segment_sum
        tree = ImplicitTreap.merge(ImplicitTreap.merge(first_tree, second_tree), third_tree)
        return result

    @staticmethod
    def innit(array=None) -> ImplicitTreapNode:
        tree = None
        for index, elem in enumerate(array):
            node = ImplicitTreapNode(elem, random.random())
            tree = ImplicitTreap.insert(tree, node, index)
        return tree

    @staticmethod
    def insert(origin_tree: ImplicitTreapNode, node: ImplicitTreapNode, index: int):
        first_tree, second_tree = ImplicitTreap.split(origin_tree, index)
        return ImplicitTreap.merge(ImplicitTreap.merge(first_tree, node), second_tree)

    @staticmethod
    def delete(tree, index, add=0):
        """
        TODO нужен ли здесь push_reverse? вот в чем вопрос
        """
        if tree is None:
            return
        current_key = add + ImplicitTreapNode.get_left_size(tree)
        new_add = current_key + 1
        left_key = float("inf")
        right_key = float("inf")
        if tree.left is not None:
            left_key = add + ImplicitTreapNode.get_left_size(tree.left)
        if tree.right is not None:
            right_key = new_add + ImplicitTreapNode.get_left_size(tree.right)
        if current_key == index:
            try:
                new_node = ImplicitTreap.merge(tree.left, tree.right)
                tree.copy(new_node)
                ImplicitTreapNode.update_size(tree)
                ImplicitTreapNode.update_segment_sum(tree)
            except Exception:
                raise Exception("Delete last item in array")

        elif left_key == index:
            new_node = ImplicitTreap.merge(tree.left.left, tree.left.right)
            tree.left = new_node

            ImplicitTreapNode.update_size(tree)
            ImplicitTreapNode.update_segment_sum(tree)

        elif right_key == index:
            new_node = ImplicitTreap.merge(tree.right.left, tree.right.right)
            tree.right = new_node

            ImplicitTreapNode.update_size(tree)
            ImplicitTreapNode.update_segment_sum(tree)

        else:
            if current_key < index:
                ImplicitTreap.delete(tree.right, index, new_add)
                ImplicitTreapNode.update_size(tree)
                ImplicitTreapNode.update_segment_sum(tree)
            else:
                ImplicitTreap.delete(tree.left, index, add)
                ImplicitTreapNode.update_size(tree)
                ImplicitTreapNode.update_segment_sum(tree)


        # if current_key < index:
        #     return ImplicitTreap.get_item(tree.right, index, new_add)
        # else:
        #     return ImplicitTreap.get_item(tree.left, index, add)
        # node = ImplicitTreap.get_item(tree, index)
        # new_node = ImplicitTreap.merge(node.left, node.right)
        # if new_node is None:
        #     node = None
        #     del node
        # else:
        #     node.copy(new_node)

    @staticmethod
    def split(tree: ImplicitTreapNode, key: int, add: int=0):

        if tree is None:
            return None, None

        ImplicitTreap.push_reverse(tree)
        current_key = add + ImplicitTreapNode.get_left_size(tree)
        if current_key < key:
            new_add = add + 1 + ImplicitTreapNode.get_left_size(tree)
            first_tree, second_tree = ImplicitTreap.split(tree.right, key, new_add)
            tree.right = first_tree
            ImplicitTreapNode.update_size(tree)
            ImplicitTreapNode.update_size(second_tree)
            ImplicitTreapNode.update_segment_sum(tree)
            ImplicitTreapNode.update_segment_sum(second_tree)

            return tree, second_tree
        else:
            first_tree, second_tree = ImplicitTreap.split(tree.left, key, add)
            tree.left = second_tree
            ImplicitTreapNode.update_size(tree)
            ImplicitTreapNode.update_size(first_tree)
            ImplicitTreapNode.update_segment_sum(tree)
            ImplicitTreapNode.update_segment_sum(first_tree)

            return first_tree, tree

    @staticmethod
    def merge(first_tree: ImplicitTreapNode, second_tree: ImplicitTreapNode) -> ImplicitTreapNode:
        """
        сливает два дерева только если все ключи дерева first_tree меньше
        ключей дерева second_tree
        """
        ImplicitTreap.push_reverse(first_tree)
        ImplicitTreap.push_reverse(second_tree)
        if first_tree is None:
            return second_tree
        if second_tree is None:
            return first_tree

        if first_tree.priority > second_tree.priority:
            first_tree.right = ImplicitTreap.merge(first_tree.right, second_tree)
            ImplicitTreapNode.update_size(first_tree)
            ImplicitTreapNode.update_segment_sum(first_tree)
            return first_tree
        else:
            second_tree.left = ImplicitTreap.merge(first_tree, second_tree.left)
            ImplicitTreapNode.update_size(second_tree)
            ImplicitTreapNode.update_segment_sum(second_tree)
            return second_tree


    @staticmethod
    def print_tree(tree: ImplicitTreapNode, list=None):
        if tree is None:
            return
        ImplicitTreap.push_reverse(tree)
        ImplicitTreap.print_tree(tree.left, list=list)
        print("Node with value: %s and priority: %s\n" % (tree.val, tree.priority))
        if list is not None:
            list.append(tree.val)
        ImplicitTreap.print_tree(tree.right, list=list)

    @staticmethod
    def create_graph(tree: ImplicitTreapNode, graph: gv.Graph, add: int = 0):
        if tree is None:
            return graph, None
        current_key = add + ImplicitTreapNode.get_left_size(tree)
        label = "V: %s, P: %s" % (tree.val, round(tree.priority, 3))
        graph.node(str(current_key), label=label)
        first_key = ImplicitTreap.create_graph(tree.left, graph, add)[1]
        new_add = add + 1 + ImplicitTreapNode.get_left_size(tree)
        second_key = ImplicitTreap.create_graph(tree.right, graph, new_add)[1]
        if first_key is not None:
            graph.edge(str(current_key), str(first_key), color="blue")
        if second_key is not None:
            graph.edge(str(current_key), str(second_key), color="red")
        return graph, current_key

