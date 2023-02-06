'''recursive binary search'''
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
    def __init__(self):
        # empty tree would be self.root = None and insert would be adding into empty tree
        self.root = None
    def __r_contains(self, current_node, value):
        '''recursive binary search'''
        # Empty tree
        # we pass the root, if it is none, return false
        if current_node == None:
            return False
        # if the value is equal to the currentnode value, return true
        if current_node.value == value:
            return True
        # if the value is less than the current node value, go left
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        # if the value is greater than the current node value, go right
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)
        
        
    def r_contains(self, value):
        '''recursive binary search'''
        # call the recursive function
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        '''recursive insert'''
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        '''recursive insert'''
        if self.root == None:
            self.root = Node(value)
        # call the recursive function
        self.__r_insert(self.root, value)
        
# Constructor test
my_tree = BinarySearchTree()

print(my_tree.root)

# Insert test
my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)
print('Root: ', my_tree.root.value)
print('Root --> Left: ', my_tree.root.left.value)
print('Root --> Right: ', my_tree.root.right.value)
