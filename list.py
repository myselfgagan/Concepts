# creating list with function
mylist = list()
# or
mylist = []

# adding elements at last
mylist.append("apple")

# adding element at specific position
mylist.insert(0, "lemon")

# removing last item
item = mylist.pop()

# to remove particular item
item = mylist.remove("apple")

# to remove all items
item = mylist.clear()

# to sort original list
mylist.sort()

# to sort list as new list
new_list = sorted(mylist)

# to reverse the list
rev_list = mylist.reverse()
# or
rev_list = mylist[::-1]

copy_list = mylist
# this will not create new list, both points to same list

# to copy list
copy_list = mylist.copy()
# or
copy_list = list(mylist)
# or
copy_list = mylist[:]

# list comprehension
mylist = [1, 2, 3, 4, 5, 6]
new_list = [i*i for i in mylist]

# to count particular item
total = mylist.count("lemon")

# to get first appearance of item
mylist.index("lemon")

# *** Slicing is possible for tuple ***

# creating tuple
mytuple = (1, 2, 3, 4)
# or
mytuple = (1,) # comma should be added at last if there is only one element
# or
mytuple = tuple([1, 2, 3, 4])