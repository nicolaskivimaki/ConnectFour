
## Connect Four in Python with Pygame

This repository contains the code for an implementation of the classic Connect Four game in Python. The game utilizes the Pygame library for its user interface and includes an AI opponent that uses the Minimax algorithm with Alpha-Beta pruning.

### Project Structure

The application is currently divided into three classes: 
* Game - handles the game loop and graphical user interface
* Board - keeps track of the game state and handles changes to it
* AI_engine - handles the minimax algorithm and heuristic function for evaluating possible moves

### Time and Space Complexity

The time complexity for the game is O(n). The space complexity is also O(n), as the game state is represented using a 2D array, and a new game state is stored on each iteration of the minimax algorithm.

### What can be improved:

* The heuristic evaluation function could be further developed as it is currently relatively primitive and does not take into account all of the factors that affect how good a position is.
* The graphical user interface could be developed further to improve the gameplay experience.

### Sources

* https://tiralabra.github.io/2023_alkukesa/fi/aiheet/minimax.pdf
* https://en.wikipedia.org/wiki/Minimax
* https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
* https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
