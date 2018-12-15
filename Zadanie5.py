class Plant:
    def __init__(self, breeding, wild):
        self.breeding = breeding
        self.wild = wild

    def __eq__(self, other):
        return self.breeding == other.breeding and self.wild == other.wild


print("******")
plant1 = Plant("TAK", "NIE")
plant2 = Plant("NIE", "TAK")

print(plant1 == plant2)
print("******")


class BreedingPlant(Plant):
    def __init__(self, water, growtime):
        self.water = water
        self.growtime = growtime

    def __eq__(self, other):
        return self.water == other.water and self.growtime == other.growtime


breedingPlant1 = BreedingPlant("litr dziennie", "6 miesiecy")
breedingPlant2 = BreedingPlant("litr dziennie", "6 miesiecy")

print(breedingPlant1 == breedingPlant2)
print("******")


class WildPlant(Plant):
    def __init__(self, water, growtime):
        self.water = water
        self.growtime = growtime

    def __eq__(self, other):
        return self.water == other.water and self.growtime == other.growtime


wildPlant1 = WildPlant("litr dziennie", "6 miesiecy")
wildPlant2 = WildPlant("litr dziennie", "6 miesiecy")

print(wildPlant1 == wildPlant2)
print("******")


class Wheat(BreedingPlant):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __eq__(self, other):
        return self.name == other.name and self.height == other.height


wheat1 = Wheat("Pszenica", 65)
wheat2 = Wheat("Pszenica", 65)
wheat3 = Wheat("Pszenica", 65)

print(wheat1 == wheat2)
print(wheat2 == wheat3)
print(wheat1 == wheat3)
print("******")


class Rye(BreedingPlant):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __eq__(self, other):
        return self.name == other.name and self.height == other.height


rye1 = Rye("Zyto", 65)
rye2 = Rye("Zyto", 65)
rye3 = Rye("Zyto", 65)

print(rye1 == rye2)
print(rye2 == rye3)
print(rye1 == rye3)
print("******")


class BlueBerry(WildPlant):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __eq__(self, other):
        return self.name == other.name and self.height == other.height


blueBerry1 = BlueBerry("Jagoda mala", 56)
blueBerry2 = BlueBerry("Jagoda mala", 56)
blueBerry3 = BlueBerry("Jagoda duza", 77)

print(blueBerry1 == blueBerry2)
print(blueBerry2 == blueBerry3)
print(blueBerry1 == blueBerry3)
print("******")


class BlackBerry(WildPlant):
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __eq__(self, other):
        return self.name == other.name and self.height == other.height


blackBerry1 = BlackBerry("Jezynka", 56)
blackBerry2 = BlackBerry("Jezyneczka", 77)
blackBerry3 = BlackBerry("Jezynka", 56)

print(blackBerry1 == blackBerry2)
print(blackBerry2 == blackBerry3)
print(blackBerry1 == blackBerry3)
print("******")
