# Pointers
# Integers
num1 = 11
num2 = num1

# Print values of num1 and num2
print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

# Gives the address where num1 and num2 are stored
# They actually point to the same address
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2))

# Test if changing num2 means we use a different adderss to allocate num2
num2 = 22

# Print values of num1 and num2
print("Before num2 value is updated:")
print("num1 =", num1)
print("num2 =", num2)

# Gives the address where num1 and num2 are stored
# They point to different addresses
print("\nnum1 points to:", id(num1))
print("num2 points to:", id(num2)) 
#################################################################################
#################################################################################
#################################################################################
# Dictionaries
# Both values of dict1 and dict2 will point to the same dictionary
dict1 = {
    'value': 11 # this variable is going to point at a dictionary in memory
}
dict2 = dict1
# Print values of dict1 and dict2
print("Before value value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

# Gives the address where dict1 and dict2 are stored
# They actually point to the same address
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))
# Now they will be pointed to different locations
dict2['value'] = 22

# Print values of dict1 and dict2
print("Before value value is updated:")
print("dict1 =", dict1)
print("dict2 =", dict2)

# Gives the address where dict1 and dict2 are stored
# They actually point to the same address since dict1 takes on the value of dict2
print("\ndict1 points to:", id(dict1))
print("dict2 points to:", id(dict2))

dict3 = {
    'value': 33
}
# Now dictionary 2 points to dict3
dict2=dict3

# Now all three variables point to the same dictionary
dict1=dict2

# If you don't have a variable pointing to original dictionary, there is no way to access it.
# Python removes it through a process called 'garbage collection'