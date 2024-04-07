
class Node(object):

    def __init__(self, data='', left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self, level=0):
        """Return a string representation (of the tree with root self).

        Left-to-right tree-wise is top-to-bottom in the output string.
        Note: For instances of the PrefixCodeTree class below, one can
        read off the map from bitstrings to letters from this string.
        """
        s = '      '*level + str(self.data) + "\n"
        for child in [self.left, self.right]:
            if child is not None:
                s += child.__str__(level+1)
        return s

class PrefixCodeTree:

    def __init__(self, debug = False):
        self.root = Node('-root-') if debug else Node()
        self.debug = debug

    def add_code(self, char, code):
        """Add char to the tree in position determined by code."""
        node = self.root
        for bit in code[:-1]:
            if bit == '1':
                if node.right is None:
                    node.right = Node('`--1--') if self.debug else Node()
                node = node.right
            if bit == '0':
                if node.left is None:
                    node.left = Node('`--0--') if self.debug else Node()
                node = node.left
        if code[-1] == '1':
            node.right = Node('`--1-- ' + char) if self.debug else Node(char)
        if code[-1] == '0':
            node.left = Node('`--0-- ' + char) if self.debug else Node(char)

    def decode(self, bitstring):
        pass

