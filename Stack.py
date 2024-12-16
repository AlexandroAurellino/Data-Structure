class Stack:
    """
    Represents a stack data structure.
    
    Attributes:
        items (list): Internal list to store stack elements.
    """
    def __init__(self):
        self.items = []

    def push(self, item):
        """
        Adds an item to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Removes and returns the top item from the stack.
        """
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()

    def peek(self):
        """
        Returns the top item without removing it.
        """
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """
        Checks if the stack is empty.
        """
        return len(self.items) == 0

    def size(self):
        """
        Returns the number of items in the stack.
        """
        return len(self.items)
