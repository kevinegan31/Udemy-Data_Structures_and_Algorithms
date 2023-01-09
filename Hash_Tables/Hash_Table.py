# Hash Table
class HashTable:
    # Build list 0-6
    def __init__(self, size=7):
        # Call empty list data_map equal to the size
        self.data_map = [None] * size
    # Hash method
    # Pass key to determine address where we store key/value pair
    def __hash(self, key):
        # start at 0
        my_hash = 0
        # Loop through the letters in the key
        for letter in key:
            '''
            my_hash + ordinal of the letter (ASCII numerical value for each letter)
            multiply by 23 (prime number), then use modulo to get the remainder as we divide
            So the remainder will be anywhere from 0-6
            '''
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash
    # Print hash table
    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)
    # Set item in hash table
    def set_item(self, key, value):
        # Create index to compute address
        index = self.__hash(key)
        # Need to check if index is none
        if self.data_map[index] == None:
            # Create data map
            self.data_map[index] = []
        # Add key/value pair to list in hash table if it already exists
        self.data_map[index].append([key, value])
    # Get address based on key
    def get_item(self, key):
        # Set variable to index in the hash
        index = self.__hash(key)
        if self.data_map[index] is not None:
            # Loop through list that is at that index
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    # Put Keys into a list and return the list
    def keys(self):
        all_keys = []
        # Create for loop that loops through data_map list
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    # Then add keys to the all_keys list
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

        



# Constructor Test
my_hash_table = HashTable()

my_hash_table.print_table()

# Set item Test
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

my_hash_table.print_table()

# Get item test
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)

print('Bolts:', my_hash_table.get_item('bolts'))
print('Washers:', my_hash_table.get_item('washers'))
print('Lumber:', my_hash_table.get_item('lumber'))

# Keys Test
my_hash_table = HashTable()

my_hash_table.set_item('bolts', 1400)
my_hash_table.set_item('washers', 50)
my_hash_table.set_item('lumber', 70)

print(my_hash_table.keys())
