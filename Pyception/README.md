# Pyception! by William Ma 
- Version: 1.2
- Github: Will-Ma-02
- Repository: https://github.com/Will-Ma-02/Snake-Around-The-World
- If you aren't sure about something, please read this throughly!

## Pyception! · An Overview 
Hooray! This project was a huge success for me. It was by far my biggest project yet. 
With different menu screens, the ability to save and customize settings and data, 
and some pixelated text, this game ended up being a massive success! 

The biggest challenges by far were trying to make a working settings screen, and reading
and writing to the .ini file that stores data. It was my first time dealing with file
I/O in Python as well as .ini files in general, so getting this to work was a huge deal for
me! 

The base of the game wasn't anything much. I used an object-oriented approach to design
this game, as well as for ease of future updates and easy debugging. If you want to learn
more about how I designed this game, I will be releasing more details soon!

## Pyception! · A Tutorial 
With that out of the way, let me show you how to play the game. If you're unfamiliar with 
the rules of Snake, they are as follows:

1. You control a snake which moves in a 1 of 4 directions (up, down, left, right) that can be 
changed using the arrow keys. Changing direction changes where your head goes.
2. Every time you eat food (the only other non-snake object), your score goes up by 1 and the 
snake grows 1 unit longer. The food moves to a new location.
3. If you hit a wall (any of the edges) or eat yourself (your head touches any part of your 
tail), it's game over. The longer the game goes on, the harder it gets!

The goal of the game is to get the highest score possible while not hitting a wall or eating
yourself. 

In my game, I've implemented these rules in the following way:
1. When you start a new game, the snake and the food spawn in random locations. The snake 
starts out at a size of 1 unit and the snake's inital direction is "None", meaning it will 
be stationary until you hit an arrow key.
2. You can't instantly change to the direction opposite yours. This means if you are going up, 
you can't change your direction to down, and vice versa. Same goes for left and right. This is 
to avoid accidentally losing by telescoping into yourself!
3. There is a score tracker on either the top or bottom of the screen, depending on the setting.
This tracks what your current score is and is updated every time you eat more food.
4. I've made it so your high score is saved. You can see your high score in the menu screen and
in the end screen after a game over. Your high score is saved in the Saved_Data,ini file, which
I will go over in more detail shortly.





