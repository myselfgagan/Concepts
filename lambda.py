a = [1, 2, 3, 4, 5, 6]

add10 = lambda x: x+10
mult = lambda x,y: x*y

b = map(lambda x: x*2, a)
print(list(b))


c = filter(lambda x: x%2 == 0, a)
print(list(c))