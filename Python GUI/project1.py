import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius
    
    def get_diameter(self):
        return 2 * self.radius
    
    def get_circumference(self):
        return 2 * math.pi * self.radius
    
    def get_volume(self):
        return (4/3) * math.pi * (self.radius ** 3)

# Example usage
radius = float(input("Enter the radius of the sphere: "))
my_sphere = Sphere(radius)

diameter = my_sphere.get_diameter()
circumference = my_sphere.get_circumference()
volume = my_sphere.get_volume()

print("Diameter:", diameter)
print("Circumference:", circumference)
print("Volume:", volume)
