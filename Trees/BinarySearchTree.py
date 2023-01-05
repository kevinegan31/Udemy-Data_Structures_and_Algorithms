# Trees
# Create Node class
class Node:
    def __init__(self, value):
        # Add value to node
        self.value = value
        # Node pointing left
        self.left = None
        # Node Pointing right
        self.right = None

class BinarySearchTree:
    # def __init__(self):
    #     # Create new node
    #     new_node = Node(value)
    #     # Create a root variable which acts like head from linked list
    #     self.root = new_node
    #     # empty tree would be self.root = None and insert would be adding into empty tree
    #     # self.root = None 
    '''
    Create constructor for empty binary search tree
    With this method, we can add nodes with insert()
    '''
    def __init__(self):
        # empty tree would be self.root = None and insert would be adding into empty tree
        self.root = None
    # Insert new node
    def insert(self, value):
        # Create new node
        new_node = Node(value)
        # If its an empty tree, return new_node
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        # Run through while(True) loop
        while(True):
            # Need to specify values, nodes cannot be equal
            if new_node.value == temp.value:
                return False
            # Need to check values left
            if new_node.value < temp.value:
                # If the spot is open, set it as the new_node
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            # Need to check values right if greater than temp.value
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    # Check if tree contains a particular value
    def contains(self, value):
        # If root is empty, return False
        if self.root is None:
            return False
        # create temporary variable
        temp = self.root
        # Return False if number is not in the tree
        while temp is not None:
            # If less than, move left
            if value < temp.value:
                temp = temp.left
            # If greater than, move left
            elif value > temp.value:
                temp = temp.right
            # Return true if we've found our value
            else:
                return True
        return False


# Constructor test
my_tree = BinarySearchTree()

print(my_tree.root)

# Insert test
my_tree = BinarySearchTree()
my_tree.insert(2)
my_tree.insert(1)
my_tree.insert(3)

"""
    THE LINES ABOVE CREATE THIS TREE:
                 2
                / \
               1   3
"""


print('Root:', my_tree.root.value)            
print('Root->Left:', my_tree.root.left.value)        
print('Root->Right:', my_tree.root.right.value)        

# Contains test
my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)

print('BST Contains 27:')
print(my_tree.contains(27))

print('\nBST Contains 17:')
print(my_tree.contains(17))
