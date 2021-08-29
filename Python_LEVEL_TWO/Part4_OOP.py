# INHERITANCE
class Animal:
    def __init__(self):
        print("ANIMAL CREATED")

    def whoAmI(self):
        print("ANIMAL")

    def eat(self):
        print("EATING")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        print("DOG CREATED")

    def bark(self):
        print("WOOF")

    def eat(self):
        print("DOG EATING")

# my_d = Dog()
# my_d.whoAmI()
# my_d.eat()
# my_d.bark()

# SPECIAL METHODS
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed!")


b = Book("Python", "Daniil", 200)
del b
