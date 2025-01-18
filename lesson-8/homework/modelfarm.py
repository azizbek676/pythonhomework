class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def eat(self):
        """Simulate eating behavior."""
        print(f"{self.name} is eating.")

    def sleep(self):
        """Simulate sleeping behavior."""
        print(f"{self.name} is sleeping.")

    def make_sound(self):
        """General method for making a sound."""
        print(f"{self.name} is making a sound.")

class Cow(Animal):
    def __init__(self, name, species, milk_production):
        super().__init__(name, species)
        self.milk_production = milk_production

    def moo(self):
        """Cow-specific sound."""
        print(f"{self.name} says Moo!")

    def milk(self):
        """Simulate milking the cow."""
        print(f"{self.name} produces {self.milk_production} liters of milk per day.")

class Sheep(Animal):
    def __init__(self, name, species, wool_amount):
        super().__init__(name, species)
        self.wool_amount = wool_amount

    def baa(self):
        """Sheep-specific sound."""
        print(f"{self.name} says Baa!")

    def shear(self):
        """Simulate shearing the sheep."""
        print(f"{self.name} has {self.wool_amount} kg of wool to shear.")

class Dog(Animal):
    def __init__(self, name, species, breed):
        super().__init__(name, species)
        self.breed = breed

    def bark(self):
        """Dog-specific sound."""
        print(f"{self.name} barks Woof!")

    def fetch(self):
        """Simulate fetching behavior."""
        print(f"{self.name} is fetching the ball!")

cow = Cow("Bessie", "Cow", 25)
sheep = Sheep("Dolly", "Sheep", 5)
dog = Dog("Rex", "Dog", "Labrador")
print("\nInteracting with animals on the farm:")

cow.eat()
cow.sleep()
cow.make_sound()
cow.moo()
cow.milk()

sheep.eat()
sheep.sleep()
sheep.make_sound()
sheep.baa()
sheep.shear()

dog.eat()
dog.sleep()
dog.make_sound()
dog.bark()
dog.fetch()
