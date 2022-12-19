# print items function
# pass it a number n and have a for loop that runs n times
# print i from the for loop
def print_items(n):
    for i in range(n):
        print(i)

print_items(10) # 10 items printed

# O(n) here - n is the number of operations

# Add for loop with j
def print_items(n):
    for i in range(n):
        print(i)
    for j in range(n):
        print(j)

print_items(10) # prints 10 items twice from [0-9]
# second code runs n + n times or O(2n) = O(n)
