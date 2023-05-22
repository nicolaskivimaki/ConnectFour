# Project Specification

This project will be coded in Python. I can do peer evaluations in Python only. The project documentation will be in English.

Bachelor's degree in Computer Science.

## Connect Four

The goal of this project is to create a Connect Four game using the Python programming language. The game will have a graphical user interface and will adhere to the standard rules of Connect Four.

The game will utilize the Pygame library for handling graphics and input events.

The game state will be represented using a 2D grid structure. Each element in the grid will represent a cell on the Connect Four board, and the value (0, 1 or 2) stored in that element will indicate the player occupying that cell, if any.

The program will handle user input through the graphical user interface, allowing players to select columns for dropping their tokens. The program will validate the players' moves and enforce the rules of Connect Four, including checking for wins and detecting a draw.

The AI opponent will use the minimax algorithm with alpha-beta pruning to make calculated decisions. It will evaluate possible moves and select the optimal one based on the current game state and depth used by the algorithm.

The time complexity for the game should be O(n), where n is the total number of possible moves in a given position. The space complexity should be O(1), as the game state will be represented using a 2D array.

## References:

* https://www.askpython.com/python/examples/connect-four-game
* https://oscarnieves100.medium.com/programming-a-connect-4-game-on-python-f0e787a3a0cf
* https://www.youtube.com/watch?v=NkmYfTl2L_Y
