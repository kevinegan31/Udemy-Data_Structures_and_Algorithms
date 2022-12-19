# One for loop, inside of another for loop
# O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            print(i,j) 

print_items(10) # prints nxn to get all combinations -- 100 items printed out

# Add another level to the function
# O(n^3) but simplified to O(n^2)
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k) 

print_items(10) # prints nxnxn to get all combinations -- 1000 items printed out

# Add another separate loop to the function
# O(n^2+n) becomes O(n^2) because standalone n is very small proportion of operations
def print_items(n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                print(i,j,k)
    # add another for loop
    for k in range(n):
        print(k)

print_items(10) # prints nxnxn to get all combinations -- 1000 items printed out
