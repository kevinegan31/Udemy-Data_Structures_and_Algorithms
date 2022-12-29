class Node:
    def __init__(self, value):
        # set value
        self.value = value
        # set next
        self.next = None
        # set prev
        self.prev = None
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################

class DoublyLinkedList:
    def __init__(self,value):
        # create new node
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        # set temp value
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    ## WRITE DLL CONSTRUCTOR HERE ##
    #                              #
    #                              #
    #                              #
    #                              #
    ################################
  



my_doubly_linked_list = DoublyLinkedList(7)

print('Head:', my_doubly_linked_list.head.value)
print('Tail:', my_doubly_linked_list.tail.value)
print('Length:', my_doubly_linked_list.length)



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 7
    Tail: 7
    Length: 1

"""
