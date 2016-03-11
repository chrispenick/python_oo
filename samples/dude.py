import random

class Character:
    universe = 'DnD'
    def __init__(self, kind, *values):
        self._kind = kind
        self._lives = values[0]
        self._health = values[1]
        self._hits = values[2]

        
class Monster(Character):
    monsters = dict(dragon=[3,3,3],ogre=[2,1,2],snake=[1,1,1])
    def __init__(self):
        pick = random.choice(list(Monster.monsters.keys()))
        super().__init__(pick, *Monster.monsters[pick])
        self._alignment = 'chaotic evil'
