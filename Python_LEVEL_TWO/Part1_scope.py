# LOCAL
lambda x: x**2

# Enclosing function locals
name = "This is a global name!"


def greet():
    name = "Sammy"

    def hello():
        print(f"Hello, {name}!")

    hello()


greet()
print(name)

x = 50


def func():
    # global x
    x = 1000
    return x


print(f"Before function call, x is: {x}")
x = func()
print(f"After function call, x is: {x}")
