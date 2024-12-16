from TreeNode import TreeNode

class DungeonTree:
    """
    Represents the tree structure of the dungeon map.
    
    Methods:
        add_room(parent_room, new_room): Adds a new room as a child of the parent room.
        print_map(): Prints the dungeon map as a tree.
    """
    def __init__(self, root_room):
        self.root = TreeNode(root_room)

    def add_room(self, parent_room, new_room):
        """
        Adds a new room as a child of the specified parent room.
        """
        def find_room(node, room_name):
            if node.data.name == room_name:
                return node
            for child in node.children:
                result = find_room(child, room_name)
                if result:
                    return result
            return None

        parent_node = find_room(self.root, parent_room.name)
        if parent_node:
            parent_node.add_child(TreeNode(new_room))
        else:
            print(f"Parent room '{parent_room.name}' not found!")

    def print_map(self, node=None, level=0):
        """
        Prints the dungeon map as a tree structure.
        """
        if node is None:
            node = self.root
        print(" " * level * 4 + f"Room: {node.data.name} - {node.data.description}")
        for child in node.children:
            self.print_map(child, level + 1)
