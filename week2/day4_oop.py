class Person:

    def __init__(self, name):
        self.name = name


class Bike:

    def __init__(self, speeds, owner):  # self is the instance of the class just created
        # self.speed = 1
        self.speed = speeds
        self.owner = owner
        self.color = "red"
        self._layers = 1

    def set_color(self, new_color):
        self.color = new_color
        self._layers += 1

    def get_layers(self):  # the ._ and creating a function allows this to not be changed by anyone
        return self._layers

joel = Person("Joel")
danielle = Person("Danielle")
bike = Bike(18, joel)  # creates bike, calling __init__
danielles_bike = Bike(18, danielle)

print("OWNERS========")
print(bike.owner.name)
print(danielles_bike.owner.name)

print("color before we change it")
print(bike.speed)
print(bike.color)
print(bike.get_layers())

print("color after we change it")
bike.set_color("purple")
print(bike.color)
print(bike.get_layers())
print("color of danielles bike")
print(danielles_bike.color)

for x in range(100):
    bike.set_color("red")
print(bike.get_layers())
