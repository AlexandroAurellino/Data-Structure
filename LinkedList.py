from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def add_Head(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        self.size += 1
    
    def add_Tail(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

        self.size += 1
    
    def add_by_index(self, index, data):
        if index < 0 or index > self.size:
            raise IndexError("Index out of range")

        new_node = Node(data)

        if index == 0:
            self.add_Head(data)
        elif index == self.size:
            self.add_Tail(data)
        else:
            helper = self.head
            for i in range(index-1):
                helper = helper.next
            new_node.next = helper.next
            helper.next = new_node

            self.size += 1

    def remove_head(self):
        if self.head is None:
            raise IndexError("List is empty")

        self.head = self.head.next

        if self.head is None:
            self.tail = None

        self.size -= 1

    def remove_tail(self):
        if self.head is None:
            raise IndexError("List is empty")
        
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            helper = self.head
            while helper.next.next is not None:
                helper = helper.next
            helper.next = None
            self.tail = helper

        self.size -= 1

    def remove_by_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        if index == 0:
            self.remove_head()
        elif index == self.size:
            self.remove_tail()
        else:
            helper = self.head
            for i in range(index - 1):
                helper = helper.next
            helper.next = helper.next.next

            self.size -= 1

    def print_list(self):
        helper = self.head
        while helper is not None:
            print(helper.data)
            helper = helper.next

    def get_size(self):
        return self.size
    
    def get_head(self):
        return self.head
    
    def get_tail(self):
        return self.tail
    
    def get_by_index(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index out of range")

        helper = self.head
        for i in range(index):
            helper = helper.next
        return helper
    
    def clear(self):
        self.head = None
        self.tail = None
        self.size = 0

        print("List cleared")