# creating dict using dict function
mydict = {"name" : "Gagan", "age" : 25, "city": "Jabalpur"}

# adding new pair
mydict["email"] = "gagan@123.com"

# deleting a pair
del mydict["name"]
# or
mydict.pop("age")

# to delete the last pair
mydict.popitem()

# to access all keys
for key in mydict.keys():
    print(key)

# to access all values
for value in mydict.values():
    print(value)

# to access both key, value pair
for key, value in mydict.items():
    print(key, value)

# copy a dictionary
mydict_copy = mydict.copy()
# or
mydict_copy = dict(mydict)

# to update a dictionary with other dictionary
mydict = {"name" : "Gagan", "age" : 25, "city" : "Jabalpur"}
mydict2 = {"name" : "Gagan", "age" : 26, "email" : "gagan@123.com"}
mydict.update(mydict2)


# **** SETS ****

# for empty set, set() should be used
myset = {1, 2, 3, 4}
# or
myset = set([1, 2, 3, 4])
# or
myset = set("1234")

# to add element
myset.add(5)

# to remove element
myset.remove(5) # gives error if element is not present
# or
myset.discard(5) # gives no error at all

# to return random value from set
value = myset.pop() # returns a random value

# to delete all values
myset.clear()

# mathematical operations
odd = {1, 3, 5, 7, 9}
even = {0, 2, 4, 6, 8}
prime = {2, 3, 5, 7}

# Union
u = even.union(odd)

# Intersection
i = even.intersection(prime)

# difference
d = even.difference(prime)
# d = {0, 4, 6, 8}

# symetric difference - returns non common values from both sets
sd = even.symetric_difference(prime)
# sd = {0, 4, 6, 8, 3, 5, 7}

# update the set with another
odd.update(prime)
# {1, 2, 3, 5, 7, 9}

# to return common values from both
odd.symetric_update(prime)
# {3, 5, 7}

# check subset
odd.issubset(even)

# check superset
odd.issuperset(even)

# check disjoint (no common elements)
odd.isdisjoint(even)

# copy a set
myset_copy = myset.copy()
# or
myset_copy = set(myset)

# frozenset - it is not mutable(cannot add values once created)
fset = frozenset([1, 2, 3, 4])