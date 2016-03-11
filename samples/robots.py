class Robot:
    __counter = 0

    @staticmethod
    def get_counter():
        return Robot.__counter
    
    def __init__(self, designation, purpose, three_law = False):
        self._designation = designation
        self._purpose = purpose
        self._three_law = three_law
        Robot.__counter += 1

    def __del__(self):
        Robot.__counter -= 1
        
