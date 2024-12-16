class TreeNode:
    """
    Represents a node in a tree.
    
    Attributes:
        data (any): The data stored in the node.
        children (list): A list of child nodes.
    """
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        """
        Adds a child node to this node.
        """
        self.children.append(child_node)

    def remove_child(self, child_node):
        """
        Removes a child node from this node.
        """
        self.children = [child for child in self.children if child != child_node]

    def get_children(self):
        """
        Returns the list of children.
        """
        return self.children
