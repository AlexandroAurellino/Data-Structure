from LinkedList import LinkedList
from Room import Room
from Stack import Stack

class Dungeon:
    """
    Manages the Linked List of rooms and player navigation.

    Attributes:
        room_list (LinkedList): A linked list of rooms.
        current_node (Node): The node the player is currently in.
        movement_stack (Stack): A stack to track player movement history.

    Methods:
        add_room(room: Room): Adds a new room to the dungeon.
        remove_room(index: int): Removes a room by index.
        navigate_forward(): Moves the player to the next room.
        navigate_backward(): Moves the player to the previous room.
        backtrack(): Moves the player back to the previous room in history.
        inspect_room(): Returns details of the current room.
    """

    def __init__(self):
        self.room_list = LinkedList()
        self.current_node = None
        self.movement_stack = Stack()  # Track movement history

    def add_room(self, room):
        """
        Adds a room to the dungeon.

        Args:
            room (Room): The room to add.
        """
        self.room_list.add_Tail(room)
        # Set the current node to the head if it's the first room
        if self.room_list.get_size() == 1:
            self.current_node = self.room_list.get_head()

    def navigate_forward(self):
        """
        Moves the player to the next room.
        """
        if self.current_node and self.current_node.next:
            # Push the current room onto the stack
            self.movement_stack.push(self.current_node)
            self.current_node = self.current_node.next
        else:
            print("You can't go forward. This is the last room.")

    def navigate_backward(self):
        """
        Moves the player to the previous room.
        """
        if self.current_node == self.room_list.get_head():
            print("You can't go backward. This is the first room.")
        else:
            # Traverse the list to find the previous node
            temp = self.room_list.get_head()
            while temp.next != self.current_node:
                temp = temp.next
            self.movement_stack.push(self.current_node)  # Push current to history
            self.current_node = temp

    def backtrack(self):
        """
        Moves the player back to the last room they visited (via stack).
        """
        if not self.movement_stack.is_empty():
            self.current_node = self.movement_stack.pop()
            print("You backtracked to the previous room.")
        else:
            print("No previous rooms to backtrack to.")

    def inspect_room(self):
        """
        Returns details of the current room.

        Returns:
            str: Details of the current room.
        """
        if self.current_node:
            room = self.current_node.data
            return f"Room: {room.name}\nDescription: {room.description}\nItems: {', '.join(room.items) if room.items else 'None'}"
        else:
            return "No rooms available."

    def remove_room(self, index):
        """
        Removes a room by index.
        """
        self.room_list.remove_by_index(index)
        # Update the current node if necessary
        self.current_node = self.room_list.get_head()

    

    