class BinaryTreeNode:
    """
    Represents a node in a binary tree.
    
    Attributes:
        data (any): The data stored in the node.
        left (BinaryTreeNode): The left child.
        right (BinaryTreeNode): The right child.
    """
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
