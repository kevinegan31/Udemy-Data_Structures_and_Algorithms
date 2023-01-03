# Queues
# Build Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Build queue class
class Queue:
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    # Print queue
    def print_queue(self):
        # Creates temporary value
        temp = self.first
        # While loop to determine where value is in list
        while temp is not None:
            # prints value
            print(temp.value)
            # Moves temp to next position to print next value
            temp = temp.next
    # Build Enqueue by adding item ot the end of the queue
    def enqueue(self, value):
        # create new node
        new_node = Node(value)
        # if node is empty, point to new node
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            # last.next points to new node
            self.last.next = new_node
            # Last becomes new node
            self.last = new_node
        self.length += 1
        return True
    # Build dequeue by removing first from queue
    def dequeue(self):
        # if queue is empty, return none
        if self.length == 0:
            return None
        # set temp to first
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp


# Constructor test
my_queue = Queue(4)

my_queue.print_queue()

# Enqueue test
my_queue = Queue(1)

print('Queue before enqueue(2):')
my_queue.print_queue()

my_queue.enqueue(2)

print('\nQueue after enqueue(2):')
my_queue.print_queue()

# Dequeue test
my_queue = Queue(1)
my_queue.enqueue(2)

# (2) Items - Returns 2 Node
print(my_queue.dequeue().value)
# (1) Item -  Returns 1 Node
print(my_queue.dequeue().value)
# (0) Items - Returns None
print(my_queue.dequeue())