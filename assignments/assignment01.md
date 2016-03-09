Dungeon Dudes
===
For this assignment, you'll create a simple role-playing game. This game will include:
*	Heroes
*	Monsters
*	Treasures
*	A Quest or Adventure
Game Play
---
A hero will make their way through the adventure. The adventure will have rooms, caves, or glens in a forest but each is a distinct location. You should describe the location as the hero enters. 

In each location the hero is met with various monsters. The monsters may attack first or the heroes may get the jump on the monsters. When you enter a location the hero and the monsters roll for Initiative. Highest roll on a d6 attacks first. There may be more than one monster in any location. Use this fact to adjust the difficulty of the game.

Attack mechanics:
---
A hero rolls dice for combat. A hero will roll three dice (d6). Monsters roll from one to three dice (d6) depending on the size and strength of the monster. If the attacker's highest die equals or exceeds the defender's highest die then the attack hits.

A hero can attack a monster and a monster can attack a hero. 

Example attack:
The hero is attacking.
The hero rolls the following dice: 5, 3, 6
The monster rolls: 2, 5, 1. This monster takes two hits to be defeated.
The hero's (attacker's) 5 is greater than or equal to the monster's (defender's) 5 so the hero's attack is successful. Some monsters take more than one successful attack to be completely knocked out. Monsters may take from one to three hits.

The hero has 10 hits before the hero has lost completely. In some locations the hero may discover a treasure after defeating the monster. The appearance of treasures is random. The treasure should be added to the hero's loot bag.

Provide the hero with a menu of choices. At any time the hero should be able to:
*	list items in the loot bag
*	move to the next location
*	list out their number of hits left (health)
*	list out the number of hits left for a monster
*	attack the monster
Once a hero moves to a location the roll for initiative is automatic for the monster and the hero.
Requirements
---
The name of your github repository should be called dungeon_dudes. The name of the program should be called dungeon_dudes. The game should implement all the basic mechanics described in Attack Mechanics. The game should be written in Python 3.4. You should be able to start the game from the command line.
Optional Flourishes
---
One of the treasures can be an attack enhancing potion. Give the hero the choice to use this in one battle. If the hero uses the potion it gives the hero one more die (d6) to use in an attack. Once the potion has been used in a battle it is expended and cannot be used again.

Give the hero the ability to run away from a battle. You will need to provide more than one pathway through a map. A sketch of the area and a Map object may help you here.

Allow our hero to save the game state and start again later from that same point.
