# Base class: Superhero
class Superhero:
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def show_power(self):
        print(f"{self.name} has the power: {self.power}")

# Inherited class: FlyingSuperhero
class FlyingSuperhero(Superhero):
    def __init__(self, name, power, speed):
        super().__init__(name, power)
        self.speed = speed

    def show_power(self):
        print(f"{self.name} has the power: {self.power} and can fly at {self.speed} km/h")

# Polymorphism example
class Superman(Superhero):
    def move(self):
        print("Superman is flying 🦸‍♂️")

class Spiderman(Superhero):
    def move(self):
        print("Spiderman is swinging 🕷️")

# Create objects
hero1 = FlyingSuperhero("Iron Man", "Powered Armor", 250)
hero2 = Superman("Superman", "Super Strength")
hero3 = Spiderman("Spiderman", "Web Slinging")

# Show powers
hero1.show_power()
hero2.show_power()
hero3.show_power()

# Demonstrate polymorphism
heroes = [hero2, hero3]
for hero in heroes:
    hero.move()
