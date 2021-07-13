package SnakeGame;

public class Segment {
	
	private int x;
	private int y;
	private final int size;
	
	/* Creates a new segment in the specified location with side lengths of one game unit. */
	public Segment(int x, int y) {
		this.x = x;
		this.y = y;
		this.size = Game.UNIT;
	}
	
	/* Returns the X value of a segment. */
	public int getX() {
		return this.x;
	}
	
	/* Sets the X value of a segment to something new. */
	public void setX(int x) {
		this.x = x;
	}
	
	/* Returns the Y value of a segment. */
	public int getY() {
		return this.y;
	}
	
	/* Sets the Y value of a segment to something new. */
	public void setY(int y) {
		this.y = y;
	}
	
	/* Returns the side length of a segment. */
	public int getSize() {
		return this.size;
	}
}
