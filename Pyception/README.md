# Pyception! by William Ma 
- Version: 1.2
- Github: Will-Ma-02
- Repository: https://github.com/Will-Ma-02/Snake-Around-The-World
- Please read this throughly before you start playing!
- 
#### WARNING: This is a personal project made for my own (and your) entertainment. This game is
#### not copyrighted or trademarked, and has no intent to be profitable. The fonts used in the game
#### are also not owned by me, nor do I have the rights to them, so please DO NOT use it outside 
#### of its intended purpose. Read the README in the Fonts folder for more information.

## Pyception! · An Overview 
Hooray! This project was a huge success for me. It was by far one of my biggest projects 
ever. With different menu screens, the ability to save and customize settings and data, 
and some pixelated text, this game ended up being a massive success! 

The biggest challenges by far were trying to make a working settings screen, and reading
and writing to the .ini file that stores data. It was my first time dealing with file
I/O in Python as well as .ini files in general, so getting this to work was a huge deal for
me! 

The base of the game wasn't anything much. I used an object-oriented approach to design
this game, as well as for ease of future updates and easy debugging. If you want to learn
more about how I designed this game, I will be releasing more details soon!

By the way, the name for this game is sort of ironic. I made the snake game in a programming
lanugage named after a snake. Hence the name "Pyception": A Python in Python.

## Pyception! · A Tutorial 
With that out of the way, let me show you how to play the game. If you're unfamiliar with 
the rules of Snake, they are as follows:

1. You control a snake which moves in a 1 of 4 directions (up, down, left, right) that can be 
changed using the arrow keys. Changing direction changes where your head (the leading part of
your body) goes. All other segments follow behind it.
2. Every time you eat food (the only other non-snake object), your score goes up by 1 and the 
snake grows 1 segment longer. The food moves to a new location.
3. If you hit a wall (any of the edges) or eat yourself (your head touches any part of your 
tail), it's game over. The longer the game goes on, the harder it gets!

The goal of the game is to get the highest score possible while not hitting a wall or eating
yourself. 

In my game, I've implemented these rules in the following way:
1. When you start a new game, the snake and the food spawn in random locations. The snake 
starts out at a size of 1 segment and the snake's inital direction is "None", meaning it will 
be stationary until you hit an arrow key.
2. You can't instantly change to the direction opposite yours. This means if you are going up, 
you can't change your direction to down, and vice versa. Same goes for left and right. This is 
to avoid accidentally losing by telescoping into yourself!
3. To help with confusion, I've added some eyes to the head of the snake to avoid confusion
over which segment is the head. They even change direction based on which direction the snake
is moving!
4. There is a score tracker on either the top or bottom of the screen, depending on the setting.
This tracks what your current score is and is updated every time you eat more food.
5. I've made it so your high score is saved. You can see your high score in the menu screen and
in the end screen after a game over. Your high score is saved in the Saved_Data.ini file, which
I will go over in more detail shortly.


## Pyception! · Running The Game
There are lots of ways to run the game, depending on what IDE (if any) you are using. Here are a
few:
- If you're using VSCode, you can click the play button in the top right to automatically execute the
Python script for you. Make sure you are in the script "Game.py" before you click the button. If this
doesn't work, make sure you have the VSCode Python 3 interpreter extension installed.
- Another way is to open a terminal and navigate to the Pyception folder. You can do this by using
cd commands. If you're not sure how to navigate using cd commands, look up a tutorial on Google. Once 
inside, type "python3 Game.py" and the game should start. If this doesn't work, make sure you have 
Python installed on your computer. To do this, type "pip3 install python" in the terminal.
- If you're using any other IDE other than VSCode, look up a tutorial of how to run python scripts in 
their environment. You may need to install a couple extensions to do so.
- If you have any other questions or find an alternative method to the ones I described that works, let
me know through a DM!

## Pyception! · Settings 
You can change your setting by navigating to the settings menu by pressing Tab in the start menu. Once 
inside, use the number keys to select a setting. Use the left and right arrow keys to cycle through the 
settings. That's it, you're good to go! As mentioned earlier, your settings will be saved to the 
Saved_Data.ini file. This means your settings will be saved even after you close the game, and will
be loaded in once you run it again. Your high score is saved in here too, but in a different section.

## Pyception! · A Conclusion
That's it from me for now! If I have any more updates, I will update this README as well as the repo.
Again, this has been one of my biggest projects, so thank you for all the support! 
