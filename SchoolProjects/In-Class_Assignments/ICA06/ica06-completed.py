# ICA06 - Functions Review
# Complete the code as instructed below and add (push) to your
# private class repo.



# Q1: Create a function called fun1 that accepts two values and returns
# the the result of the multiplication of these two values.
def fun1(x, y):
    return x * y



# Q2: Create a function called fun2 that accepts two values, a and b, and returns a
# function (closure) that takes one parameter x and returns a * x + b.
def fun2(a, b):
    def f(x):
        return a * x + b
    return f
    



# This section of code only runs when this file is called directly.
# It calls each of the above functions fun1 and fun2 and
# prints the values returned - along with
# a message that indicates the function and paramaters used to make the call.
if __name__ == '__main__':
    print("Q1: Called fun1(100, 200) and got back a value of:", fun1(100, 200))
    fx = fun2(100, 200)
    print("Q2: Called fx=fun2(100, 200), then called fx(300) and got back a value of:", fx(300))