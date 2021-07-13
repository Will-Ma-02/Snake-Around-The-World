package SnakeGame;

import javax.swing.*;

public class Frame extends JFrame {
	
	// IGNORE THIS
	private static final long serialVersionUID = 1L;
	
	/* Instantiates the window in which the game is played. */
	public Frame() {
		this.add(new Game());
		this.setTitle("Snake By Mr8Bit");
		this.setVisible(true);
		this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		this.pack();
		this.setLocationRelativeTo(null);
	}
}
