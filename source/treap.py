"""
Простое декартово дерево, без выкрутасов
"""

import random
import copy


class TreapNode:
    def __init__(self, key, priority):
        self.key = key
        self.priority = priority
        self.left = None
        self.right = None


class Treap:
    @staticmethod
    def innit(array=None) -> TreapNode:
        tree = None
        for i in array:
            node = TreapNode(i, random.random())
            tree = Treap.insert(tree, node)
        return tree

    @staticmethod
    def insert(tree: TreapNode, node: TreapNode):
        if tree is None:
            return node

        if node.priority > tree.priority:
            node.left, node.right = Treap.split(tree, node.key)
            return node

        if tree.key > node.key:
            tree.left = Treap.insert(tree.left, node)
            return tree
        else:
            tree.right = Treap.insert(tree.right, node)
            return tree

    @staticmethod
    def split(origin_tree: TreapNode, key: int):
        tree = copy.deepcopy(origin_tree)

        if tree is None:
            return None, None

        if tree.key < key:
            first_tree, second_tree = Treap.split(tree.right, key)
            tree.right = first_tree
            return tree, second_tree
        else:
            first_tree, second_tree = Treap.split(tree.left, key)
            tree.left = second_tree
            return first_tree, tree

    @staticmethod
    def merge(first_tree: TreapNode, second_tree: TreapNode) -> TreapNode:
        """
        сливает два дерева только если все ключи дерева first_tree меньше
        ключей дерева second_tree
        """
        if first_tree is None:
            return second_tree
        if second_tree is None:
            return first_tree

        if first_tree.priority > second_tree.priority:
            first_tree.right = Treap.merge(first_tree.right, second_tree)
            return first_tree
        else:
            second_tree.left = Treap.merge(first_tree, second_tree.left)
            return second_tree

    @staticmethod
    def print_tree(tree: TreapNode):
        if tree is None:
            return
        Treap.print_tree(tree.left)
        print("Node with key: %s and priority: %s\n" % (tree.key, tree.priority))
        Treap.print_tree(tree.right)


