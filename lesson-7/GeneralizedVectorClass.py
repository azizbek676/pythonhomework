import math

class Vector:
    def __init__(self, *components):
        """Initialize the vector with given components."""
        if len(components) == 0:
            raise ValueError("A vector must have at least one component.")
        self.components = components

    def __add__(self, other):
        """Add two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for addition.")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        """Subtract two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for subtraction.")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def dot(self, other):
        """Calculate the dot product of two vectors."""
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must be of the same dimension for dot product.")
        return sum(a * b for a, b in zip(self.components, other.components))

    def scalar_multiply(self, scalar):
        """Multiply the vector by a scalar."""
        return Vector(*(a * scalar for a in self.components))

    def magnitude(self):
        """Compute the magnitude (length) of the vector."""
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        """Return the unit vector (normalized vector)."""
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return self.scalar_multiply(1 / mag)

    def __str__(self):
        """Return a string representation of the vector."""
        return f"Vector({', '.join(map(str, self.components))})"

    def __repr__(self):
        """Return a detailed string representation of the vector."""
        return f"Vector({', '.join(map(str, self.components))})"
if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)

    print("Vector v1:", v1)
    print("Vector v2:", v2)

    print("Addition:", v1 + v2)
    print("Subtraction:", v1 - v2)
    print("Dot Product:", v1.dot(v2))
    print("Magnitude of v1:", v1.magnitude())
    print("Normalized v1:", v1.normalize())