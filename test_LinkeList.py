from LinkedList import LinkedList

# Initialize LinkedList
ll = LinkedList()

# Add elements to the head
ll.add_Head(10)
ll.add_Head(20)
ll.add_Head(30)
print("After adding to head:")
ll.print_list()

# Add elements to the tail
ll.add_Tail(40)
ll.add_Tail(50)
print("\nAfter adding to tail:")
ll.print_list()

# Add element by index
ll.add_by_index(2, 25)
print("\nAfter adding 25 at index 2:")
ll.print_list()

# Remove head
ll.remove_head()
print("\nAfter removing head:")
ll.print_list()

# Remove tail
ll.remove_tail()
print("\nAfter removing tail:")
ll.print_list()

# Remove by index
ll.remove_by_index(2)
print("\nAfter removing element at index 2:")
ll.print_list()

# Get size
print("\nSize of LinkedList:", ll.get_size())

# Get element by index
print("\nElement at index 2:", ll.get_by_index(2))

# Clear the list
ll.clear()
print("\nAfter clearing the list:")
ll.print_list()
