# Build Linked List class
# Create class called Node so that whenever LinkedList class wants to do anything to item it calls this class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None



class LinkedList:
    # Constructor Method
    # Initialize linked list
    def __init__(self, value):
        # Create new node
        new_node = Node(value)
        self.head = new_node # points to new node
        self.tail = new_node # points to new node
        self.length = 1
    
    # def append(self, value):
    #     # Create new Node
    #     # Add new node to the end

    # def prepend(self, value):
    #     # Create new Node
    #     # Add new node to the beginning
    
    # def insert(self, value):
    #     # Create new Node
    #     # Insert node wherever requested

my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
print(my_linked_list.tail.value)
print(my_linked_list.length)



