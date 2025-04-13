PROJECT OVERVIEW
My game is a simple maze game with a player, and end goal, and obstacles such as walls. Its purpose is to entertain and to be my computer science project. Its key features are a player controlled by the arrow keys, walls to prevent the player from reaching the end point, and endpoint, an enemy, and pushable blocks.

INSTRUCTIONS
Have the current version of python and pygame. Open any level file of your choosing. Run the level file. Control the white player and make the player sprite reach the green endpoint sprite. Once you reach the end, a "YOU WON" message will print to tell you that you won. Avoid obstacles such as the black walls and red enemy, and push the blue pushable blocks out of the way.
( i can't get any screenshots right now because there is an error with the python interpreter, ignore this if i fix the error and get screenshots but forget to delete this)

REQUIREMENTS REFERENCE
Deliverables 1 and 2 required the project to have three levels, with each level adding new obstacles, going from walls to pushables, then to enemies. The order was changed for gameplay purposes but the requirements were met other than that. The deliverables also needed the project to have a wall class from which all the other classes would inherit from, such as the player class inheriting the collision method from the wall class. This was done and all the classes rely on the wall class for the check_for_collision, draw, and get_rect methods.

CREDITS AND ACKNOWLEDGEMENTS
- Mr Sullivan for helping fix my pushable class
- copilot for fixing minor mistakes and helping with small problems
- copilot, chatgpt, deepseek for adding debugging to my pushable and trying to fix my pushable

NOTES
- everything except the pushable works, i think either it is the player not colliding with the pushable, or the pushable not changing positions, or both
- also have to make the level selection menu, and make the enemy make the player go back to the menu when the enemy catches the player
- treat level1 as a an integration testing example, will make real levels by placing the walls around in different locations
- i think that the pushable doesn't work because the player sprite isn't colliding with the pushable's sprite, the enemy collides and i assume the walls also collide. the player sprite is overlapping the pushable sprite, it just doesnt do the collision
