import math

class Vector:
    def __init__(self, *components):
        """Initialize the vector with given components."""
        if len(components) == 0:
            components = input("Please enter the vector components separated by spaces: ").split()
            components = [float(component) for component in components]
        self.components = components

    def __add__(self, other):
        """Add two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for addition.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))