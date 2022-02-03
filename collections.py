from collections import Counter, namedtuple, defaultdict, deque

# Counter
text = "aaaaabbbbccc"
my_counter = Counter(text)
print(my_counter)
print(my_counter.items())
print(my_counter.keys())
print(my_counter.values())
print(my_counter.most_common(1)) # argument - 1st n common values
print(list(my_counter.elements())) # returns all elements as list


# namedtuple
Point = namedtuple("Point", "x, y")
pt = Point(1, 4)
print(pt)
print(pt.x, pt.y)

# defaultdict
d = defaultdict(int)  # provided default type
d["a"] = 1
d["b"] = 2
print(d["a"])  # print value of a
print(d["c"])  # print default value of int, i.e. "0"

# deque
d = deque()
d.append(1)
d.append(2)
d.appendleft(3)
d.extend([4, 5, 6])
d.extendleft([7, 8, 9])
d.rotate(3)
d.rotate(1)
d.rotate(-2)