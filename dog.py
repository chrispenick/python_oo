import random

class Dog:
    def __init__(self, name, breed, size, gender, health = 100,
                 bark = 'Woof', age = 0):
        self._name = name
        self._breed = breed
        self._size = size
        self._age = age
        self._gender = gender
        self._bark = bark
        self._health = health

    def bark(self, times = 1):
        return self._bark * times

    def breed(self, other):
        genders = ['male','female']
        gender = random.choice(genders)
        breed = self._breed + other._breed
        return Dog('dog',breed,'small',gender)

class PoliceDog(Dog):
    def __init__(self, name, breed, size, gender, badge):
        super().__init__(name, breed, size, gender)
        self._badge = badge

    def attack(self, other):
        other._health = other._health - 5

    @property
    def badge(self):
        return self._badge

    @badge.setter
    def badge(self, badge_num):
        if len(badge_num) >= 6:
            self._badge = badge_num
