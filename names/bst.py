import sys
sys.path.append('../queue_and_stack')
from dll_queue import Queue
from dll import Stack


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Left subtree - nodes with keys lesser than the nodes key
        if value < self.value:
            if self.left:
                self.left.insert(value)
            if not self.left:
                self.left = BinarySearchTree(value)

        if value >= self.value:
            if self.right:
                self.right.insert(value)
            if not self.right:
                self.right = BinarySearchTree(value)

    def contains(self, target):
        # check containment
        if self.value == target:
            return True
        if target > self.value:
            if not self.right:
                return False
            return self.right.contains(target)

        if target < self.value:
            if not self.left:
                return False
            return self.left.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        if not self:
            return None

        if not self.right:
            # current value is already max so just return it
            return self.value
        # return max value in right sub tree
        return self.right.get_max()

    # Call the function `cb` on the value of each node
    # You may use a recursive or iterative approach
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)

    # DAY 2 Project -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        pass

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        pass

    # STRETCH Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self, node):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self, node):
        pass
