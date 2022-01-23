def greeting(f):
    def welcome():
        print("welcome")
        f()
    return welcome

# @greeting
# def hello():
#     print("hello")

def hi():
    print("hi")

# this means same as:
new_hi = greeting(hi)
hi = new_hi

# hello()
hi()