package SnakeGame;

import java.awt.*;
import java.awt.event.*;

import javax.swing.*;
import javax.swing.Timer;

import java.util.*;

public class Game extends JPanel implements ActionListener, KeyListener {
	
	// IGNORE THIS
	private static final long serialVersionUID = 1L;
	
	// Constants for the game
	public static final int SIZE = 800;
	public static final int UNIT = 25;
	public static final int TICK_SPEED = 100;
	
	// Key Constants
	private static final int UP_ARROW = 38;
	private static final int DOWN_ARROW = 40;
	private static final int LEFT_ARROW = 37;
	private static final int RIGHT_ARROW = 39;
	private static final int SPACE = 32;
	private static final int R_KEY = 82;
	
	// String constants
	private static final String GAME_NAME = "Snake By Mr8Bit";
	private static final String TITLE_TEXT = "Press space to start | Press R for rules";
	private static final String GAME_OVER_STRING = "GAME OVER";
	private static final String GAME_OVER_TEXT = "Press space to play again";
	private static final String RULES1 = "The objective of Snake is to eat as many red circles (food)";
	private static final String RULES2 = "as you can without eating yourself (head touches tail) or";
	private static final String RULES3 = "hitting a wall. The snake will get longer each time it eats a red";
	private static final String RULES4 = "circle. You will start in the center facing and heading up.";
	private static final String RULES5 = "Use the arrow keys to change direction. Press space to start.";
	
	// Booleans 
	boolean inStartScreen = true;
	boolean inRulesScreen = false;
	boolean play = false;
	boolean inGameOverScreen = false;
	
	// Score counter
	int score = 0;
	
	// Important objects
	Timer timer;
	Timer rules;
	Random random = new Random();
	Food food = new Food(random.nextInt((int) (SIZE / UNIT)) * UNIT, random.nextInt((int) (SIZE / UNIT)) * UNIT);
	Snake snake = new Snake();
	
	// Fonts
	Font fontBig = new Font("Courier New Bold", Font.BOLD, 50);
	FontMetrics fontMetricsBig = getFontMetrics(fontBig);
	
	Font fontSmall = new Font("Courier New Bold", Font.BOLD, 20);
	FontMetrics fontMetricsSmall = getFontMetrics(fontSmall);
	
	/* Instantiates a new game. */
	public Game() {
		this.setPreferredSize(new Dimension(SIZE, SIZE));
		this.setBackground(Color.BLACK);
		this.setFocusable(true);
		this.addKeyListener(this);
	}
	
	/* Important function for Graphics. */
	public void paintComponent(Graphics g) {
		super.paintComponent(g);
		draw(g);
	}
	
	/* The method that draws the whole game. */
	public void draw(Graphics g) {
		if (inStartScreen) {
			// Draw the game title
			g.setColor(Color.WHITE);
			g.setFont(fontBig);
			g.drawString(GAME_NAME, 
			(SIZE - fontMetricsBig.stringWidth(GAME_NAME)) / 2, (SIZE / 2) - (2 * UNIT));
			
			// Draw the title instructions
			g.setColor(Color.WHITE);
			g.setFont(fontSmall);
			g.drawString(TITLE_TEXT, 
			(SIZE - fontMetricsSmall.stringWidth(TITLE_TEXT)) / 2, SIZE / 2);
			
		} else if (inRulesScreen) {
			// Draw the rules
			g.setColor(Color.WHITE);
			g.setFont(fontSmall);
			g.drawString(RULES1, 
			(SIZE - fontMetricsSmall.stringWidth(RULES1)) / 2, (SIZE / 2) - (4 * UNIT));
			
			g.setColor(Color.WHITE);
			g.setFont(fontSmall);
			g.drawString(RULES2, 
			(SIZE - fontMetricsSmall.stringWidth(RULES2)) / 2, (SIZE / 2) - (2 * UNIT));
			
			g.setColor(Color.WHITE);
			g.setFont(fontSmall);
			g.drawString(RULES3, 
			(SIZE - fontMetricsSmall.stringWidth(RULES3)) / 2, (SIZE / 2));
			
			g.setColor(Color.WHITE);
			g.setFont(fontSmall);
			g.drawString(RULES4, 
			(SIZE - fontMetricsSmall.stringWidth(RULES4)) / 2, (SIZE / 2) + (2 * UNIT));
			
			g.setColor(Color.WHITE);
			g.setFont(fontSmall);
			g.drawString(RULES5, 
			(SIZE - fontMetricsSmall.stringWidth(RULES5)) / 2, (SIZE / 2) + (4 * UNIT));
			
		} else if (play){
			// Draw the score
			g.setColor(Color.WHITE);
			g.setFont(fontSmall);
			g.drawString("Score: " + score, 
			(SIZE - fontMetricsSmall.stringWidth("Score: " + score)) / 2, 2 * UNIT);
			
			// Draw the food
			g.setColor(Food.foodColor());
			g.fillOval(food.getX(), food.getY(), food.getSize(), food.getSize());
			
			// Draw each segment of the snake
			for (int i = 0; i < snake.getLength(); i++) {
				g.setColor(Snake.snakeColor());
				g.fillRect(snake.getSegment(i).getX(), snake.getSegment(i).getY(), UNIT, UNIT);
			}	
			
		} else if (inGameOverScreen){
			// Draw the game over text
			g.setColor(Color.RED);
			g.setFont(fontBig);
			g.drawString(GAME_OVER_STRING, 
			(SIZE - fontMetricsBig.stringWidth(GAME_OVER_STRING)) / 2, (SIZE / 2) - (2 * UNIT));
			
			// Draw the game over score
			g.setColor(Color.WHITE);
			g.setFont(fontSmall);
			g.drawString("Your score was: " + score, 
			(SIZE - fontMetricsSmall.stringWidth("Your score was: " + score)) / 2, (SIZE / 2));
			
			// Draw the game over instructions
			g.setColor(Color.WHITE);
			g.setFont(fontSmall);
			g.drawString(GAME_OVER_TEXT, 
			(SIZE - fontMetricsSmall.stringWidth(GAME_OVER_TEXT)) / 2, (SIZE / 2) + (2 * UNIT));
		} 
	}
	
	/* Begins a new timer if the player chooses to view the rules. */
	public void rules() {
		rules = new Timer(1, this);
		rules.start();
	}
	
	/* Begins a new game from the rules screen. */
	public void startFromRules() {
		rules.removeActionListener(this);
		generateFood();
		play = true;
		timer = new Timer(TICK_SPEED, this);
		timer.start();
	}
	
	/* Begins a new game. */
	public void start() {
		generateFood();
		play = true;
		timer = new Timer(TICK_SPEED, this);
		timer.start();
	}
	
	/* Restarts the game. */
	public void restart() {
		Snake newSnake = new Snake();
		snake = newSnake;
		generateFood();
		score = 0;
		play = true;
		timer.restart();
	}
	
	/* Moves the food to a random location. */
	public void generateFood() {
		Random random = new Random();
		food.setX(random.nextInt((int) (SIZE / UNIT)) * UNIT); 
		food.setY(random.nextInt((int) (SIZE / UNIT)) * UNIT);
	}
	
	/* Moves the snake based on its direction. */
	public void move() {
		char dir = snake.getDirection();
		switch (dir) {
		case 'U':
			// Removes the last segment of the tail and creates a new head above current head
			snake.removeLastSegmentOfTail();
			Segment newHeadUP = new Segment(snake.getHead().getX(), snake.getHead().getY() - UNIT);
			snake.addNewSegmentToHead(newHeadUP);
			break;
			
		case 'D':
			// Removes the last segment of the tail and creates a new head below current head
			snake.removeLastSegmentOfTail();
			Segment newHeadDOWN = new Segment(snake.getHead().getX(), snake.getHead().getY() + UNIT);
			snake.addNewSegmentToHead(newHeadDOWN);
			break;
			
		case 'L':
			// Removes the last segment of the tail and creates a new head to the left of current head
			snake.removeLastSegmentOfTail();
			Segment newHeadLEFT = new Segment(snake.getHead().getX() - UNIT, snake.getHead().getY());
			snake.addNewSegmentToHead(newHeadLEFT);
			break;
			
		case 'R':
			// Removes the last segment of the tail and creates a new head to the right of current head
			snake.removeLastSegmentOfTail();
			Segment newHeadRIGHT = new Segment(snake.getHead().getX() + UNIT, snake.getHead().getY());
			snake.addNewSegmentToHead(newHeadRIGHT);
			break;
		}			
	}
	
	/* Checks if the snake hit a border or ate itself. */
	public void snakeHitBorderOrAteItself() {
		int snakeHeadX = snake.getHead().getX();
		int snakeHeadY = snake.getHead().getY();
		
		// Checks if snake ate itself
		for (int i = snake.getLength() - 1; i > 0; i--) {
			if (snakeHeadX == snake.getSegment(i).getX() && snakeHeadY == snake.getSegment(i).getY()) {
				play = false;
			}
		}
		// Checks if snake hit left border
		if (snakeHeadX < 0) {
			play = false;
			
		// Checks if snake hit right border
		} else if (snakeHeadX > SIZE - UNIT) {
			play = false;
			
		// Checks if snake hit top border
		} else if (snakeHeadY < 0) {
			play = false;
			
		// Checks if snake hit bottom border
		} else if (snakeHeadY > SIZE - UNIT) {
			play = false;
		}
		inGameOverScreen = true;
	}
	
	/* Controls what happens when the snake eats the food. */
	public void snakeEatFood() {
		int snakeHeadX = snake.getHead().getX();
		int snakeHeadY = snake.getHead().getY();
		
		if (snakeHeadX == food.getX() && snakeHeadY == food.getY()) {
			char dir = snake.getDirection();
			switch (dir) {
			case 'U':
				// Attaches a new segment onto the snake below its tail
				Segment newTailUP = new Segment(snake.getEndOfTail().getX(), snake.getEndOfTail().getY() + UNIT);
				snake.addNewSegmentToEndOfTail(newTailUP);
				break;
				
			case 'D':
				// Attaches a new segment onto the snake above its tail
				Segment newTailDOWN = new Segment(snake.getEndOfTail().getX(), snake.getEndOfTail().getY() - UNIT);
				snake.addNewSegmentToEndOfTail(newTailDOWN);
				break;
				
			case 'L':
				// Attaches a new segment onto the snake to the right of its tail
				Segment newTailLEFT = new Segment(snake.getEndOfTail().getX() + UNIT, snake.getEndOfTail().getY());
				snake.addNewSegmentToEndOfTail(newTailLEFT);
				break;
				
			case 'R':
				// Attaches a new segment onto the snake to the left of its tail
				Segment newTailRIGHT = new Segment(snake.getEndOfTail().getX() - UNIT, snake.getEndOfTail().getY());
				snake.addNewSegmentToEndOfTail(newTailRIGHT);
				break;
			}
			score++;
			generateFood();
		}
	}
	
	/* Unused method. */
	@Override
	public void keyTyped(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}
	
	/* Controls the key actions of the game. */
	@Override
	public void keyPressed(KeyEvent e) {
		int key = e.getKeyCode();
		if (inStartScreen) {
			if (key == SPACE) {
				start();
				inStartScreen = false;
			} else if (key == R_KEY) {
				rules();
				inRulesScreen = true;
				inStartScreen = false;
			}
		} else if (inRulesScreen) {
			if (key == SPACE) {
				startFromRules();
				inRulesScreen = false;
			}
		} else if (play) {
			switch (key) {
			case UP_ARROW:
				if (snake.getDirection() != 'D') {
					snake.setDirection('U');
				}
				break;
			case DOWN_ARROW:
				if (snake.getDirection() != 'U') {
					snake.setDirection('D');
				}
				break;
			case LEFT_ARROW:
				if (snake.getDirection() != 'R') {
					snake.setDirection('L');
				}
				break;
			case RIGHT_ARROW:
				if (snake.getDirection() != 'L') {
					snake.setDirection('R');
				}
				break;
			}
		} else if (inGameOverScreen) {
			if (key == SPACE) {
				restart();
				inGameOverScreen = false;
			}
		}
	}
	
	/* Unused method. */
	@Override
	public void keyReleased(KeyEvent e) {
		// TODO Auto-generated method stub
		
	}
	
	/* Main animation method. */
	@Override
	public void actionPerformed(ActionEvent e) {
		if (play) {
			move();
			snakeHitBorderOrAteItself();
			snakeEatFood();
		}
		repaint();
	}

}
