class Thing:
    shared_item = 'Something that we can all reference.'
    def __init__(self, year):
        self._year = year

    def __str__(self):
        return str(self._year)
        
class SubThing(Thing):
    def __init__(self, year, month):
        super().__init__(year)
        self._month = month
