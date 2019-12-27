# -*- coding: utf-8 -*-

class Animal:
    hunger = 'hungry'
    voice = ''

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def feed(self):
        self.hunger = 'full'
        print(f'{self.name} is fed!')

    def voices(self):
        print(self.voice)

class Diary:
    pass

class LayEgg:
    pass

class Wool:
    pass

class Goose(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Honk!'

class Cow(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Moo!'

class Sheep(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Baa!'

class Chiken(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Cluck!'

class Goat(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Baa!'

class Duck(Animal):
    def __init__(self, name, weight):
        super().__init__(name, weight)
        self.voice = 'Quack!'


goose1 = Goose('Серый', 3000)
goose2 = Goose('Белый', 2500)

cow1 = Cow('Манька', 400000)

sheep1 = Sheep('Барашек', 100000)
sheep2 = Sheep('Кудрявый', 90000)

chiken1 = Chiken('Ко-Ко', 1000)
chiken2 = Chiken('Кукареку', 800)

goat1 = Goat('Рога', 60000)
goat2 = Goat('Копыта', 65000)

duck1 = Duck('Кряква', 1600)

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


