## Interactive Fiction

Write an interactive fiction game. It may be as deep or shallow as you like, though obviously greater care in execution will result in a better grade. It should be possible to beat the game given the following instructions:

	GET ALL
	OPEN DOOR
	EAST
	GET EDELWEISS
	UP
	ENTER CAVE
	LIGHT FIRE
	WAIT
	PUT EDELWEISS IN FIRE
	PUT HELMET IN STATUE
	PUT PRISM IN PICKLE
	EXIT CAVE
	NORTH
	GET MEANING OF LIFE
	
The following verbs must be supported:

	LIGHT x
	EXAMINE x
	GET/TAKE x
	DROP x
	PUT x IN y
	NORTH
	WEST
	SOUTH
	EAST
	UP
	DOWN
	WAIT
	ENTER x
	EXIT x
	OPEN X

Though other paths to victory are, naturally, preferred. This must be a game with a parser, not a simple hyperlink game (such as one made with Twine http://twinery.org/2/).

Case of commands does not matter.

Call the program `journey.py`. Place the program in a repo as `interfic`.
