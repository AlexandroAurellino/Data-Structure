from BinaryTreeNode import BinaryTreeNode

class CombatBinaryTree:
    """
    Represents a binary tree for combat decisions.
    """
    def __init__(self):
        self.root = None

    def build_tree(self):
        """
        Builds a predefined combat tree for decision-making.
        """
        self.root = BinaryTreeNode("Start Combat")
        self.root.left = BinaryTreeNode("Attack")
        self.root.right = BinaryTreeNode("Defend")
        self.root.left.left = BinaryTreeNode("Critical Hit!")
        self.root.left.right = BinaryTreeNode("Missed Attack")
        self.root.right.left = BinaryTreeNode("Successful Block")
        self.root.right.right = BinaryTreeNode("Took Damage")

    def traverse(self, node):
        """
        Traverses the combat tree based on player's choices.
        """
        if node is None:
            return
        print(node.data)
        if node.left and node.right:
            choice = input("Choose (left: Attack / right: Defend): ").strip().lower()
            if choice == "left":
                self.traverse(node.left)
            elif choice == "right":
                self.traverse(node.right)
