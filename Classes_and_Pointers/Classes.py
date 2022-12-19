# Creating Classes
class Cookie:
    # Constructor
    # If self is a keyword, it is a method rather than a function.
    # Color is the variable passed to the constructor
    # Allows us to create new cookies
    def __init__(self, color):
        self.color = color # color passed and is applied to self.color
    # Method to get the color of the cookie
    def get_color(self):
        return self.color
    # method to set the color of the cookie
    def set_color(self, color):
        self.color = color


# creates a green cookie
# this particular cookie is calling itself green
cookie_one = Cookie('green')
# this particular cookie is calling itself blue
cookie_two = Cookie('blue')


print('Cookie one is', cookie_one.get_color())
print('Cookie two is', cookie_two.get_color())

cookie_one.set_color('yellow')

print('\nCookie one is now', cookie_one.get_color()) # \n creates a new line
print('Cookie two is still', cookie_two.get_color())


# Create class for linked list
# class LinkedList:
#     def __init__(self,value):
#         self.value = value
    
#     def append(self, value):
#         value.append(value)
    
#     def pop(self):
#         return self.value
    
#     def prepend(self, value): # put on the beginning
#         value.prepend(value)

#     def insert(self, index, value):
    
#     def remove(self, index):