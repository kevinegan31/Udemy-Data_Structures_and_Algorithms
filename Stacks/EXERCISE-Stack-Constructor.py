class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    ## WRITE NODE CONSTRUCTOR HERE ##
    #                               #
    #                               #
    #                               #
    #                               #
    #################################
        
class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    ## WRITE STACK CONSTRUCTOR HERE ##
    #                                #
    #                                #
    #                                #
    #                                #
    ##################################




my_stack = Stack(4)

print('Top:', my_stack.top.value)
print('Height:', my_stack.height)



"""
    EXPECTED OUTPUT:
    ----------------
    Top: 4
    Height: 1

"""