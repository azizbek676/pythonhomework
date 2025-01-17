import math

class Vector:
    def __init__(self, components):
        """Initialize the vector with a list of components."""
        self.components = components
        self.dimension = len(components)

    def __add__(self, other):
        """Add two vectors."""
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for addition.")
        return Vector([a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        """Subtract two vectors."""
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for subtraction.")
        return Vector([a - b for a, b in zip(self.components, other.components)])

    def dot(self, other):
        """Calculate the dot product of two vectors."""
        if self.dimension != other.dimension:
            raise ValueError("Vectors must have the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def __mul__(self, scalar):
        """Multiply the vector by a scalar."""
        return Vector([a * scalar for a in self.components])

    def magnitude(self):
        """Calculate the magnitude (length) of the vector."""
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        """Normalize the vector (return the unit vector)."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector([a / mag for a in self.components])

    def __str__(self):
        """Return a string representation of the vector."""
        return f"Vector({self.components})"

    def __repr__(self):
        """Return an unambiguous string representation of the vector."""
        return f"Vector({repr(self.components)})"

v1 = Vector([1, 2, 3])
v2 = Vector([4, 5, 6])
print(v1 + v2)  
print(v1 - v2)  
print(v1.dot(v2)) 
print(v1 * 3) 
print(v1.magnitude()) 
print(v1.normalize()) 
