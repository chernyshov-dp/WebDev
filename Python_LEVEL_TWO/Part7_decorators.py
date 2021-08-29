# s = "GLOBAL VARIABLE"
#
#
# def func():
#     my_local = 10
#     print(locals())
#     print(globals()["s"])
#
# func()


# def hello(name="Daniil"):
#     return "Hello, " + name
#
#
# print(hello())
#
# my_new_greet = hello()
# print(my_new_greet)


# def hello(name="Daniil"):
#     print("THE HELLO() FUNCTION HAS BEEN RUN!")
#
#     def greet():
#         return "THIS STRING IS INSIDE GREET()"
#
#     def welcome():
#         return "THIS STRING IS INSIDE WELCOME()"
#
#     if name == "Daniil":
#         return greet
#     else:
#         return welcome
#
#
# x = hello()
# print(x())


# def hello():
#     return "Hi Daniil!"
#
#
# def other(func):
#     print("HELLO")
#     print(func())
#
#
# other(hello)


def new_decorator(func):

    def wrap_func():
        print("CODE HERE BEFORE EXECUTING FUNC")
        func()
        print("FUNC() HAS BEEN CALLED")

    return wrap_func


# func_needs_decorator = new_decorator(func_needs_decorator)
@new_decorator
def func_needs_decorator():
    print("THIS FUNCTION IS IN NEED OF A DECORATOR!")


func_needs_decorator()
