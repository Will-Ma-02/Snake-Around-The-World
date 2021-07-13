package SnakeGame;

import java.awt.Color;
import java.util.*;

public class Snake {
	
	private ArrayList<Segment> segments = new ArrayList<Segment>(0);
	private int length;
	private char direction;
	
	/* Creates a new snake with the following properties: 
	 * - The snake's head is at the center of the screen. 
	 * - The snake's tail is one segment long and is below the head.
	 * - The snake's length is 2.
	 * - The snake's direction is up. */
	public Snake() {
		this.segments.add(new Segment(Game.SIZE / 2, Game.SIZE / 2));
		this.segments.add(new Segment(Game.SIZE / 2, (Game.SIZE / 2) + Game.UNIT));
		this.length = 2;
		this.direction = 'U';
	}
	
	/* Returns a specified segment. */
	public Segment getSegment(int i) {
		return this.segments.get(i);
	}
	
	/* Returns the segment that is currently first. */
	public Segment getHead() {
		return this.segments.get(0);
	}
	
	/* Returns the segment that is currently last. */
	public Segment getEndOfTail() {
		return this.segments.get(this.length - 1);
	}
 	
	/* Removes the segment that is currently last. */
	public void removeLastSegmentOfTail() {
		this.segments.remove(this.length - 1);
	}
	
	/* Adds a segment that becomes the new head. */
	public void addNewSegmentToHead(Segment segment) {
		this.segments.add(0, segment);
	}
	
	/* Adds a segment to the end of the tail. */
	public void addNewSegmentToEndOfTail(Segment segment) {
		this.segments.add(segment);
		this.length++;
	}
	
	/* Returns the number of segments. */
	public int getLength() {
		return this.length;
	}
	
	/* Returns the direction. */
	public char getDirection() {
		return this.direction;
	}
	
	/* Sets the direction to something new. */
	public void setDirection(char direction) {
		this.direction = direction;
	}
	
	/* Returns the color of the snake. */
	public static Color snakeColor() {
		return Color.GREEN;
	}
}
