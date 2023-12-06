from enum import Enum


class Kind(Enum):
    DOG = 1
    CAT = 2
    BIRD = 3


class Pet:
    def __init__(self, name, breed, age, greeting, mass, kind):
        self.name = name
        self.breed = breed
        self.age = age
        self.greeting = greeting
        self.mass = mass
        self.kind = kind

    def is_polite(self):
        return True if 'Hello' in self.greeting else False


class Home:
    def __init__(self):
        self.pets = []

    def add_pet(self, pet):
        self.pets.append(pet)

    def are_friends(self, pet_1, pet_2):
        return abs(pet_1.age - pet_2.age) < 2

    def sort_by_age(self):
        self.pets.sort(key=lambda x: x.age)


def main():
    dog = Pet("Kuzya", "Burmese", 3, "Myav, myav!", 4, Kind.CAT)
    cat = Pet("Barsik", "Labrador", 5, "Hello, I'm Barsik!", 15, Kind.DOG)
    bird = Pet("Kikins", "Crow", 2, "I`m a bird!", 1, Kind.BIRD)

    home = Home()

    home.add_pet(dog)
    home.add_pet(cat)
    home.add_pet(bird)

    home.sort_by_age()

    for pet in home.pets:
        print(f"Name: {pet.name}, Breed: {pet.breed}, Age: {pet.age}, Greeting: {pet.greeting}, Mass: {pet.mass}, Kind: {pet.kind}")

    for i in range(len(home.pets)):
        for j in range(i + 1, len(home.pets)):
            if home.are_friends(home.pets[i], home.pets[j]):
                print(f"{home.pets[i].name} and {home.pets[j].name} are friends!")


if __name__ == "__main__":
    main()