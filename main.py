# -*- coding: utf-8 -*-

class Animal:
    hunger = 'hungry'
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        self.hunger = 'full'
        print(f'{self.name}: покормили!')

    def voices(self):
        print(self.voice)

    def __gt__(self, other):
        return self.weight > other.weight

    def __add__(self, other):
        return Animal('',self.weight + other.weight)

    def __radd__(self, other):
        if other == 0:
            return self
        else:
            return self.__add__(other)

class Milk:
    def get_milk(self):
        print(f'{self.name}: подоили!')

class Egg:
    def get_eggs(self):
        print(f'{self.name}: собрали яйца!')

class Wool:
    def get_wool(self):
        print(f'{self.name}: постригли!')

class Goose(Animal, Egg):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Га!'

class Cow(Animal, Milk):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Муу!'

class Sheep(Animal, Wool):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Бее!'

class Chiken(Animal, Egg):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Ко!'

class Goat(Animal, Milk):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Бее!'

class Duck(Animal, Egg):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Кря!'

animals = []

goose1 = Goose('Серый', 3000)
animals.append(goose1)
goose2 = Goose('Белый', 2500)
animals.append(goose2)

cow1 = Cow('Манька', 400000)
animals.append(cow1)

sheep1 = Sheep('Барашек', 100000)
animals.append(sheep1)
sheep2 = Sheep('Кудрявый', 90000)
animals.append(sheep2)

chiken1 = Chiken('Ко-Ко', 1000)
animals.append(chiken1)
chiken2 = Chiken('Кукареку', 800)
animals.append(chiken2)

goat1 = Goat('Рога', 60000)
animals.append(goat1)
goat2 = Goat('Копыта', 65000)
animals.append(goat2)

duck1 = Duck('Кряква', 1600)
animals.append(duck1)

goose1.feed()
goose2.feed()
cow1.feed()
sheep1.feed()
sheep2.feed()
chiken1.feed()
chiken2.feed()
goat1.feed()
goat2.feed()
duck1.feed()

cow1.get_milk()
sheep1.get_wool()
chiken1.get_eggs()


total_weight = sum(animals)
print(f'Общий вес животных: {total_weight.weight} грамм')

max_animal = max(animals)
print(f'Наибольший вес имеет: {max_animal.name}')



