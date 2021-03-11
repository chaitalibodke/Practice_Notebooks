# ------------------------------------
#  Lists in Python
# ------------------------------------

# Declare and Initialise a list
list1 = ["Jitesh", "John", "Alia"]

# Access the element of a list
print(list1[2])


# -------------------------------
# Basic Operations on list
# -------------------------------

# Add an element to a list using Append
list1.append("Lise")

# Update an element
list1[1] = "Frans"

# Delete an element
del list1[2]

# Get the length of a list
len(list1)

# Concatenate two lists
list2 = ["a", "b", "c"]

conlist = list1 + list2

# Sort the content of the list
list1.sort()


# Multidimensional lists
twoDlist = [["Jitesh", "Frans", "Lise"], [123, 456, 345]]

print(twoDlist[0][1])


# Slicing of the multidimensional list
sublist = []

for list1 in twoDlist:
    sublist.append(list1[1:3])
















