class Dog:

    # CLASS OBJECT ATTRIBUTE
    species = "mammal"

    def __init__(self, breed, name):
        self.breed = breed
        self.name = name


my_dog = Dog("Lab", "Sammy")
print(my_dog.breed)
print(my_dog.name)
print(my_dog.species)


class Circle:
    pi = 3.14

    def __init__(self, radius=1):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * Circle.pi

    def set_radius(self, new_r):
        self.radius = new_r


my_circle = Circle(3)
my_circle.set_radius(100)
print(my_circle.radius)
print(my_circle.area())
