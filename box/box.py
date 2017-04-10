    # Create a class that represents a cuboid:
    # It should take its three dimensions as constructor parameters (numbers)
    # It should have a method called `get_surface` that returns the cuboid's surface
    # It should have a method called `get_volume` that returns the cuboid's volume

class Cuboid(object):
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.length = length

    def get_surface(self):
        surface = 0
        surface = 2 * (self.width * self.height) + 2 * (self.height * self.length) + 2 * (self.width * self.length)
        return surface

    def get_volume(self):
        volume = 0
        volume = self.width * self.height * self.length
        return volume

box = Cuboid(10, 20, 30)
print(box.get_surface()) # should print 2200
print(box.get_volume()) # should print 6000
