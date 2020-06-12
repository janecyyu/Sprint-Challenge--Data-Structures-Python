"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from collections import deque


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # 1. if no root
        if self is None:
            # if isn't, create the node and park it there
            self = BSTNode(value)
        # 2. there is a root
        else:
            # comparer the value
            if value < self.value:
                # go left
                # if another node on this side
                if self.left:
                    self.left.insert(value)
                else:
                    self.left = BSTNode(value)

            else:
                # else go right
                # Return True if the tree contains the value
                # False if it does not
                if self.right:
                    self.right.insert(value)
                else:
                    self.right = BSTNode(value)

    def contains(self, target):
        # if root equals target, return true
        if self.value == target:
            return True
        else:
            # if target greater than self's value, go right
            if target > self.value:
                if self.right:
                    # repeat again the previous steps
                    return self.right.contains(target)
                # if no more elements means not found
                else:
                    return False
            # if target less than self's value, go left
            else:
                if self.left:
                    # repeat again the previous steps
                    return self.left.contains(target)
                # if no more elements means not found
                else:
                    return False

    def get_max(self):

        if not self.right:
            return self.value
        return self.right.get_max()

        # # if no self, return none:
        # if self is None:
        #     return None

        # # only one element
        # if self.left is None and self.right is None:
        #     return self.value

        # res = self.value
        # # set left nad right max are zero at the begining, in case left or right side is empty
        # left_max = 0
        # right_max = 0

        # if self.left:
        #     left_max = self.left.get_max()
        # if self.right:
        #     right_max = self.right.get_max()

        # if (left_max > res):
        #     res = left_max
        # if (right_max > res):
        #     res = right_max
        # return res

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.for_each(fn)
        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------
    def depth_first_for_each(self, fn):
        fn(self.value)
        if self.left:
            self.left.depth_first_for_each(fn)
        if self.right:
            self.right.depth_first_for_each(fn)

    def iter_depth_first_search(self, fn):
        stack = []
        stack.append(self)
        while len(stack) > 0:
            # pop off the stack
            current_node = stack.pop()
            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)
            fn(current_node.value)

    def iter_breadth_first_search(self, fn):
        q = deque()
        q.append(self)

        while len(q) > 0:
            current_node = q.popleft()
            if current_node.left:
                q.append(current_node.left)
            if current_node.right:
                q.append(current_node.right)
            fn(current_node.value)

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        if node is None:
            return

        self.in_order_print(node.left)
        print(node.value)
        self.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        if node is None:
            return
        # print(self.value)
        self.iter_breadth_first_search(print)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        if node is None:
            return
        # print(self.value)
        self.iter_depth_first_search(print)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT

    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
