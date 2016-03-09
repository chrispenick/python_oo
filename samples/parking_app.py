import parking as p
import random

##def main():
print("yo, welcome to parking!")
lot1 = p.ParkingLot()
print("p = park, l = list cars")
choice = input("What you want?")
if choice == 'p':
    tag = input("License Plate?")
    space = random.choice(lot1._labels)
    lot1.park(p.Vehicle(tag),space)
    
