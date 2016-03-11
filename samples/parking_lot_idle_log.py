Python 3.4.3+ (default, Oct 14 2015, 16:03:50) 
[GCC 5.2.1 20151010] on linux
Type "copyright", "credits" or "license()" for more information.
>>> 
=== RESTART: /home/cpenick/Documents/python_repo/python_oo/parking_app.py ===
yo, welcome to parking!
p = park, l = list cars
What you want?p
License Plate?abc123
>>> lot1
<parking.ParkingLot object at 0x7f6055eb4400>
>>> lot1._spaces
{'j9': <parking.Vehicle object at 0x7f6050cdb128>}
>>> lot1.park(p.Vehicle('def456'),'a1')
>>> lot1._spaces
{'a1': <parking.Vehicle object at 0x7f6050cd7a90>, 'j9': <parking.Vehicle object at 0x7f6050cdb128>}
>>> lot1._spaces.keys()
dict_keys(['a1', 'j9'])
>>> list(lot1._spaces.keys())
['a1', 'j9']
>>> list(lot1._spaces.keys()).sort(reverse = True)
>>> x = list(lot1._spaces.keys()).sort(reverse = True)
>>> x
>>> list(lot1._spaces.keys())
['a1', 'j9']
>>> x = list(lot1._spaces.keys())
>>> x
['a1', 'j9']
>>> x.sort(reverse = True)
>>> x
['j9', 'a1']
>>> 
