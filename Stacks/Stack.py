# Stack
# Build Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Build stack class
class Stack:
    def __init__(self, value):
        # Create new node
        new_node = Node(value)
        # Similar to head, but refer to it as top of stack pointing to new_node
        self.top = new_node
        # Height is like length, now = 1
        self.height = 1
    # Print stack
    def print_stack(self):
        # Creates temporary value
        temp = self.top
        # While loop to determine where value is in list
        while temp is not None:
            # prints value
            print(temp.value)
            # Moves temp to next position to print next value
            temp = temp.next
    # Add item to beginning of the stack
    def push(self, value):
        # Create new node
        new_node = Node(value)
        # if there is nothing in the stack, top and bottom become new node
        if self.top is None:
            self.top = new_node
        # else: the new node points to head and head changes to new node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    # Pop item off list
    def pop(self):
        # If height is zero, return None
        if self.height == 0:
            return None
        # Create variable to point to top node
        temp = self.top
        # Move top to next item down
        self.top = self.top.next
        # Remove temp from stack
        temp.next = None
        # Subtract 1 from height
        self.height -= 1
        return temp



# Constructor test
my_stack = Stack(4)
my_stack.print_stack()
print('Top:', my_stack.top.value)
print('Height:', my_stack.height)

# Push test
my_stack = Stack(2)

print('Stack before push(1):')
my_stack.print_stack()

my_stack.push(1)

print('\nStack after push(1):')
my_stack.print_stack()

# Pop test
my_stack = Stack(4)
my_stack.push(3)
my_stack.push(2)
my_stack.push(1)

print('Stack before pop():')
my_stack.print_stack()

print('\nPopped node:')
print(my_stack.pop().value)

print('\nStack after pop():')
my_stack.print_stack()
