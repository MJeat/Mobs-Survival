# Mobs-Survival
This is a project for my Computer Science A course. 

Instruction on how to run the code application:

First, install pygame by writing pip install pygame in the Vscode terminal.
Second, after running the code, you should see the home screen of the game. Read the tips in the home screen carefully since the enemies are quite fast.
Third, after clicking play, the default weapon is the gun and the sword is the secondary weapon. Click and hold your right mouse to shoot bullets. Click 1 or 2 to switch weapons. Both weapons are revolved around the player and not moving with the mouse cursor.
Fourth, click p to pause the game.
Fifth, know that you cannot leave the game because your cursor is connected to the weapons. One way to leave the game is to get touched by the mobs.
Note: Each time you kill a mob, you get one point for your score located on the top left corner of the screen.
Note: This game is only developed using pygame in Vscode only. No external platforms. 


1. Project Title: Mobs Survival

2. Project issue, problem to be solved:
Since this is a game-based project, its objective is to survive. The game is about surviving hordes after hordes of different mobs. There is no winning. You will eventually die. Do your best to survive and aim for the highest scores you could get.
 
3. Current progress (PDLC: Problem analysis, design, etc..)
Ideation: Started brainstorming ideas with a pencil and paper. And eventually, I realized that I have always wanted to make a pixel game. 
Planning: Started preparing the schedule, and started to visualize on what kind of game I wanted. Then, I began searching on YT for references. It was a shooting game.
Implementation: The game itself is imported from pygame module. I started writing what the internet said. However, I made 4 key changes to the character in the game, including switching weapons, pausing the game, scoreboard, home screen, and game over screen.
Deployment: After 1 week of developing the game, I published it on GitHub and ran the code. It works as planned.

4. Project Functions/Features:
The game itself has 5 main files:
main.py is the main file that is used to run the game. This file has one class called Game that contains all essential functions to begin the game, such as __init__ and run functions/methods.
player.py is the file that controls the player's movement, shooting, and interaction with mobs/enemies and objects within the game.
sprites.py is the file that has 5 classes, such as Sprites, Enemies, CollisionSprites, Bullet, and Gun. All of these classes determined the functionalities of mobs, objects, bullets of the gun, and the gun itself.
groups.py is the file that creates a more realistic feature with objects. When the player walks behind the rocks or trees, the player's character will be behind those objects. The same goes for when the player is in front.
settings.py is just a file that determines the screen and the game map width and height.

5. Expected No. of Pages:
There are 3 pages: Home screen, in-game screen, and game over screen.

6. Project reference: HERELinks to an external site.

