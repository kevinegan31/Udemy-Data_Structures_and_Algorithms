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

    # print list
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    # Add new node to the end of list
    def append(self, value):
        # Create new Node
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    # Remove node from linked list
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        # while loop to move pre and temp to end of list
        while (temp.next): # or while temp.next is not None
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None # removes the last node from the list
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    # Add item ot the begnining of a list
    def prepend(self, value):
        # Create new Node
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    # Remove the first item from the list
    def pop_first(self):
        if self.length == 0: # checks if there are any items
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0: # applies when you started with one item
            self.tail = None
        return temp

    # Return the node at the index
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        # perform for loop to go through range up to index
        # _ since we do not use the variable in the for loop
        for _ in range(index):
            temp = temp.next
        return temp
    
    # Set a value for the node
    def set_value(self, index, value):
        temp = self.get(index) # Will either return None or a node
        if temp is not None: # or if temp:
            temp.value = value
            return True
        return False # if temp is None

    # Insert a node that has a particular value into our linked list
    def insert(self, index, value):
        # if index is out of range, return false
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            # once this prepend method runs, we're done
            # running this on this particular index of the linked list
            return self.prepend(value)
        if index == self.length:
            # add to the end
            return self.append(value)
        # Create new Node
        new_node = Node(value)
        # use get to return the node at the index
        # then move it to -1
        temp = self.get(index - 1)
        new_node.next = temp.next
        # move arrow to point to the new node
        temp.next = new_node
        self.length += 1
        return True

        
        # Insert node wherever requested


my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
print(my_linked_list.tail.value)
print(my_linked_list.length)

# Add node
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()

# Remove node
my_linked_list.print_list()
# (2) Items - Returns 2 Node
print(my_linked_list.pop())
# (1) Item - Returns 1 Node
print(my_linked_list.pop())
# (0) Items - Returns None
print(my_linked_list.pop())

# Add node to the beginning of list
my_linked_list = LinkedList(2)
my_linked_list.append(3)
my_linked_list.print_list()
my_linked_list.prepend(1)
my_linked_list.print_list()

# Pop first item off of the linked list
my_linked_list = LinkedList(2)
my_linked_list.append(1)

# (2) Items - Returns 2 Node
print(my_linked_list.pop_first())
# (1) Item - Returns 1 Node
print(my_linked_list.pop_first())
# (0) Items - Returns None
print(my_linked_list.pop_first())

# Get node at the index
my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

print(my_linked_list.get(2))

# Set node at index
my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)

my_linked_list.set_value(1,4) # sets value at the index of 1 to 4
print(my_linked_list.print_list())


# Insert a new node
my_linked_list = LinkedList(0)
my_linked_list.append(2)
my_linked_list.insert(1, 1)
print(my_linked_list.print_list())
