package SnakeGame;

import java.awt.Color;

public class Food {
	
	private int x;
	private int y;
	private final int size;
	
	/* Creates a new food in the specified location with a radius of one game unit. */
	public Food(int x, int y) {
		this.x = x;
		this.y = y;
		this.size = Game.UNIT;
	}
	
	/* Returns the X value of the food. */
	public int getX() {
		return this.x;
	}
	
	/* Sets the X value of the food to something new. */
	public void setX(int x) {
		this.x = x;
	}
	
	/* Returns the Y value of the food. */
	public int getY() {
		return this.y;
	}
	
	/* Sets the Y value of the food to something new. */
	public void setY(int y) {
		this.y = y;
	}
	
	/* Returns the radius of the food. */
	public int getSize() {
		return this.size;
	}
	
	/* Returns the color of the food. */
	public static Color foodColor() {
		return Color.RED;
	}
}
