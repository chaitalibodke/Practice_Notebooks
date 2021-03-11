# ------------------------------
# Python Dictionary
# ------------------------------

# Define and initialise a dictionary
Address = {'Street'  : '180 Adams Street', \
           'City'    : 'Chicago',          \
           'State'   : 'IL',               \
           'Country' : 'USA'}

# Access the value
print(Address['Street'])


# Update the value using key
Address['Street'] = '181 Adams Street'


# Add a key-value pair to existing dictionary
Address['Zip'] = 60611


# Delete a key-value pair
del Address['Zip']


# Get the length of the dictionary
len(Address)


# Convert the dictionary into a string
str(Address)


# Get the list of all the keys of dictionary
print(Address.keys())

# Get all the values
print(Address.values())
















