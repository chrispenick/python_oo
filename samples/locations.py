import random
class Location:
    descriptions = ['basement','my garage', "teacher's conference"]
    loot = ['bowling ball', 'cat', 'Micky Mantle baseball card']
    def __init__(self):
        self._description = random.choice(Location.descriptions)
        self._loot = random.choice(Location.loot)


class Quest:
    def __init__(self, title, rooms):
        self._title = title
        self._room_map = []
        for r in range(rooms):
            self._room_map.append(Location())
