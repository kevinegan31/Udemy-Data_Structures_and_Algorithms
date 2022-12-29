# Linked List Constructor 2
# class to create new node
class Node:
    # Create constructor method
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    # Create constructor method
    # Create new node
    # Constructor passes a value so that we can assign it to a node
    def __init__(self, value):
        # pass a value, so it calls the Node class to pass the value
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
    # Append item to the end of the list
    def append(self, value):
        # create new node
        new_node = Node(value)
        # if head does not exist
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            # if head does exist
        else:
            # tail.next points to new node
            self.tail.next = new_node
            # tail points to new node
            self.tail = new_node
        # length adds 1
        self.length += 1
        # optional
        return True
    # Remove last item from list
    def pop(self):
        # Check if list is empty
        if self.length == 0:
            return None
        # If not, create temporary value equal to head
        temp = self.head
        # Create pre tail value equal to head
        pre = self.head
        # While temp exists, move pre to temp and temp to point next
        while temp.next is not None:
            pre = temp
            temp = temp.next
        # Save tail as the pre value at the end of list
        self.tail = pre
        # Move tail.next to be temp pointer which removes item
        self.tail.next = None
        # Length subtracts
        self.length -=1
        # If we removed the only item in the list, head and tail = 
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    # Add item to beginning of the linked list
    def prepend(self, value):
        # Create new node
        new_node = Node(value)
        # if there is nothing in the node, head and tail become new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        # else: the new node points to head and head changes to new node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    # Pop the first item off of the list
    def pop_first(self):
        # If node is empty, return None
        if self.length == 0:
            return None
        # temporarily create variable = head
        temp = self.head
        # Move head to next postiion
        self.head = self.head.next
        # change temp.next to None to remove Node from list
        temp.next = None
        # Subtract 1 from length
        self.length -= 1
        # If length is zero, tail also equal to None
        if self.length == 0:
            self.tail = None
        return temp
    # Get item from list
    def get(self, index):
        # test for valid index
        if index < 0 or index >= self.length:
            return None
        # Create temp variable pointing to head
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    # Set item to value in the list
    def set_value(self, index, value):
        # Gets index and calls it temp
        temp = self.get(index)
        # If temp is not None, change the value to value
        if temp is not None:
            temp.value = value
            return True
        return False
    # Insert item to list
    def insert(self, index, value):
        # test for valid index
        if index < 0 or index >= self.length:
            return False
        # if index is 0, add node to the beginning of the list
        if index == 0:
            return self.prepend(value)
        # if index == length, put at the end of the list
        if index == self.length:
            return self.append(value)
        # Create new node
        new_node = Node(value)
        # Have temp point to index - 1
        temp = self.get(index - 1)
        # New node points to temp.next, which is where it is to be inserted
        new_node.next = temp.next
        # change temp.next now to new node
        temp.next = new_node
        # add length 1
        self.length += 1
        return True
    # Remove an item at a particular index
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        # if index is 0, add node to the beginning of the list
        if index == 0:
            return self.pop_first()
        # if index == length, put at the end of the list
        if index == self.length - 1:
            return self.pop()
        # get index - 1 from temp
        prev = self.get(index - 1)
        # O(1) get prev.next for temp
        temp = prev.next
        # Moves arrow to next from temp
        prev.next = temp.next
        # Remove temp by stating temp.next = None
        temp.next = None
        self.length -= 1
        return temp
    # Reverse list
    def reverse(self):
        # set temp = head
        temp = self.head
        # head = tail
        self.head = self.tail
        # tail = head
        self.tail = temp
        # variable on the right side of temp
        after = temp.next
        # variable before temp
        before = None
        # for loop that goes through the length of the list
        for _ in range(self.length):
            # after moves to temp.next
            # must come first
            after = temp.next
            # temp.next turns around to point to before
            # now you have a gap in the list
            temp.next = before
            # before needs to be moved to temp, before moving temp to after
            before = temp
            # move temp to after
            temp = after






my_linked_list = LinkedList(4)
print(my_linked_list.head.value)
my_linked_list.print_list()

my_linked_list.append(7)

my_linked_list.print_list()

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.print_list()
my_linked_list.pop()
my_linked_list.print_list()
my_linked_list.pop()
print(my_linked_list.print_list())

my_linked_list = LinkedList(1)
my_linked_list.prepend(2)
my_linked_list.prepend(3)
my_linked_list.prepend(4)
my_linked_list.print_list()


my_linked_list = LinkedList(4)
my_linked_list.append(1)

print(my_linked_list.pop_first())
print(my_linked_list.pop_first())
print(my_linked_list.pop_first())

my_linked_list = LinkedList(0)
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)
print(my_linked_list.get(2))

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.set_value(1, 4)
my_linked_list.print_list()



print(my_linked_list.set_value(2,4))

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.insert(1, 4)
my_linked_list.print_list()

my_linked_list = LinkedList(11)
my_linked_list.append(3)
my_linked_list.append(23)
my_linked_list.append(7)
my_linked_list.remove(2)
my_linked_list.print_list()


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()
my_linked_list.print_list()

