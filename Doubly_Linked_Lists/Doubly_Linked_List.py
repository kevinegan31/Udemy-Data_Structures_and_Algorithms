# Doubly Linked List
# Node Constructor
class Node:
    def __init__(self, value):
        # Set value of node
        self.value = value
        # Set next pointer as none
        self.next = None
        # Set previous pointer to none
        self.prev = None
# Doubly Linked List Constructor
class DoublyLinkedList:
    def __init__(self, value):
        # Create new node
        new_node = Node(value)
        # Head now points to new node
        self.head = new_node
        # Tail now points to new node
        self.tail = new_node
        # Node length is equal to 1
        self.length = 1
    # Method to print the list
    def print_list(self):
        # Creates temporary value
        temp = self.head
        # While loop to determine where value is in list
        while temp is not None:
            # prints value
            print(temp.value)
            # Moves temp to next position to print next value
            temp = temp.next
    # Appdend to new node
    def append(self, value):
        # Create new node
        new_node = Node(value)
        # If value does not exist
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # if head does exist
        else:
            # tail.next points to new node
            self.tail.next = new_node
            # New node points to tail
            new_node.prev = self.tail
            # tail points to new node
            self.tail = new_node
        # length adds 1
        self.length += 1
        # Insert requires boolean, we use append in insert
        return True
    # Remove item off the end
    def pop(self):
        # No items in the doubly linked list
        if self.length == 0:
            return None
        # Create temporary variable pointing to tail
        temp = self.tail
        # Check if there is anything left in list
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # Move tail to previous
            self.tail = self.tail.prev
            # Next for new tail is now none
            self.tail.next = None
            # Removing item by stating temp.prev is now None
            temp.prev = None
        self.length -= 1
        return temp
    # Add item at the beginning of the list
    def prepend(self, value):
        # Create new node
        new_node = Node(value)
        # Check if list is empty and point to new node
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            # New node points to head
            new_node.next = self.head
            # Head points back at new node
            self.head.prev = new_node
            # Head becomes new node
            self.head = new_node
        self.length += 1
        return True
    # Remove first item
    def pop_first(self):
        # Check if there are any items in list
        if self.length == 0:
            return None
        # temp variable points to head
        temp = self.head
        # Check if only 1 item in list
        if self.length == 1:
            # Head and tail now point to none
            self.head = None
            self.tail = None
        else:
            # Move head to next
            self.head = self.head.next
            # Remove previous pointer from head
            self.head.prev = None
            # Remove temp.next pointer and node
            temp.next = None
        self.length -= 1
        return temp
    # Get item from list
    def get(self, index):
        # Test for valid index
        if index < 0 or index >= self.length:
            return None
        # Create temp variable pointing to head
        temp = self.head
        # If index is in first half of list
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            # set temp to tail to start at tail
            temp = self.tail
            # Start at length - 1, decrement by 1 everytime we loop through
            for _ in range(self.length - 1, index, -1):
                # move to the left
                temp = temp.prev
        return temp
    # Set item to value in the list
    def set_value(self, index, value):
        # Create temp variable
        temp = self.get(index)
        # If temp exists, pass value to node
        if temp is not None:
            temp.value = value
            return True
        return False
    # Insert node into list
    def insert(self, index, value):
        # Test for valid index
        if index < 0 or index > self.length:
            return False
        # If index is 0, add node to the begging of the list
        if index == 0:
            return self.prepend(value)
        # if index == length, put at the end of the list
        if index == self.length:
            return self.append(value)
        # Create new node
        new_node = Node(value)
        # Create before variable pointing at index - 1
        before = self.get(index - 1)
        # Create after variable pointing at next index
        after = before.next
        # point prev of new node to before
        new_node.prev = before
        # point new node to after
        new_node.next = after
        # point before to new_node
        before.next = new_node
        # point after back to new node
        after.prev = new_node
        # increment list length by 1
        self.length += 1
        return True
    # Remove an item at a particular index
    def remove(self, index):
        # Check if index exists
        if index < 0 or index >= self.length:
            return None
        # If index is 0, add node to the beginning of the list
        if index == 0:
            return self.pop_first()
        # If index == length, put at end of the list
        if index == self.length - 1:
            return self.pop()
        temp = self.get(index)
        before = temp.prev
        after = temp.next
        before.next = after
        after.prev = before
        temp.next = None
        temp.prev = None
        self.length -= 1
        return temp



my_doubly_linked_list = DoublyLinkedList(7)

print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length)

my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)


# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop())

# (0) Items - Returns None
print(my_doubly_linked_list.pop())


my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(3)

print('Before prepend():')
print('----------------')
print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')
print('Doubly Linked List:')
my_doubly_linked_list.print_list()


my_doubly_linked_list.prepend(1)


print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length, '\n')
print('Doubly Linked List:')
my_doubly_linked_list.print_list()

my_doubly_linked_list = DoublyLinkedList(2)
my_doubly_linked_list.append(1)


# (2) Items - Returns 2 Node
print(my_doubly_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_doubly_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_doubly_linked_list.pop_first())

# Get
my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)

print('Get node from first half of DLL:')
print(my_doubly_linked_list.get(1).value)

print('\nGet node from second half of DLL:')
print(my_doubly_linked_list.get(2).value)

# Set
my_doubly_linked_list = DoublyLinkedList(11)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(23)
my_doubly_linked_list.append(7)

print('DLL before set_value():')
my_doubly_linked_list.print_list()

my_doubly_linked_list.set_value(1,4)

print('\nDLL after set_value():')
my_doubly_linked_list.print_list()

# Insert
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(3)


print('DLL before insert():')
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(1,2)

print('\nDLL after insert(2) in middle:')
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(0,0)

print('\nDLL after insert(0) at beginning:')
my_doubly_linked_list.print_list()


my_doubly_linked_list.insert(4,4)

print('\nDLL after insert(4) at end:')
my_doubly_linked_list.print_list()

# Remove
my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)

print('DLL before remove():')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() in middle:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(0).value)
print('DLL after remove() of first node:')
my_doubly_linked_list.print_list()

print('\nRemoved node:')
print(my_doubly_linked_list.remove(2).value)
print('DLL after remove() of last node:')
my_doubly_linked_list.print_list()


my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)

print(my_doubly_linked_list.remove(1))

my_doubly_linked_list.print_list()