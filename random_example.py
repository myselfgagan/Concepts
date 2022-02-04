import  random

# prints random float from 0-1
a = random.random()

# prints random float from range 1-10
a = random.uniform(1, 10)

# prints random integer from range 1-10, icluding 10
a = random.randint(1, 10)

# prints random integer from range 1-10, excluding 10
a = random.randrange(1, 10)



mylist = list("ABCDEFG")

# select any element randomly from list
a = random.choice(mylist)

# select multiple elements from the list, unique elements
a = random.sample(mylist, 3)

# select multiple elements from the list, repeat elements
a = random.choices(mylist, k=3)

# shuffle the list
a = random.shuffle(mylist)