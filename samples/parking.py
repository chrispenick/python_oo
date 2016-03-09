class Vehicle:
    def __init__(self, tag):
        self._tag = tag
    
class ParkingLot():
    def __init__(self):
        rows = 'abcdefghij'
        self._labels = []
        for row in rows:
            for num in range(1,11):
                self._labels.append(row + str(num))
                
        self._spaces = {}

    def park(self, vehicle, space):
        if space in self._labels \
           and space not in self._spaces.keys():
            self._spaces[space] = vehicle
            
        

