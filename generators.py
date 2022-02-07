def mygenerator():   # returns object that can be iterated
    yield 1
    yield 2
    yield 3
    
g = mygenerator()

# getting all values from yield
for i in g:
    print(i)
    
# running function yield to yield statement
value = next(g)  # runs till 1st yield
print(value)

value = next(g) # continues from 1st yeald and runs till 2nd yield
print(value)

# we can use inbuild iterator functions
print(sum(g))
print(sorted(g))



# execution example
def countdown(num):
    print("Starts")
    while num > 0:
        yield num
        num -= 1
        
cd = countdown(5)   # object created - nothing prints

value = next(cd)    # prints starting and 5

print(next(cd))     # prints 4




# difference between normal function and generator
def first(n):    # takes memory to store numbers in "nums" list
    nums = []
    num = 0
    while num < n:
        nums.append(num)
        num += 1
    return nums

print(first(10))
print(sum(first(10)))        

def first_generator(n):  # takes less memory as no list is required
    num = 0
    while num < n:
        yield num
        num += 1
        
fg = first_generator(10)
for i in fg:
    print(i)
print(sum(first_generator(10)))

# fibonacci example
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a
        a, b = b, a+b
        
fib = fibonacci(30)
for i in fib:
    print(i)
    



# generator comprehension (same as list comprehensions)
mygenerator = (i for i in range(10) if i%2 == 0)    # generator comprehensions take less space then list comprehension
for i in mygenerator:
    print(i)