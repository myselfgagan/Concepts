# creating error class
class ValueTooHighError(Exception):
    pass

class ValueTooLowError(Exception):
    def __init__(self, message, value):
        self.message = message
        self.value = value

def test_value(x):
    if x > 100:
        raise ValueTooHighError("Value is too high")
    if x < 5:
        raise ValueTooLowError("valaue is too small, x")

try:
    test_value(200)
    test_value(1)
except ValueTooHighError as e:
    print(e)
except ValueTooLowError as e:
    print(e.message, e.value)




# raising an error
try:                          # statement
    a = 5/1      
    b = a + "10"

except TypeError as e:        # error message
    print(e)
except:
    print("an error occured")
else:
    print("all good")

finally:                      # this always run
    print("This will run at all cost")