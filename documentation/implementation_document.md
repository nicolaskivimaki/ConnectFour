
## Connect Four in Python with Pygame

This repository contains the code for an implementation of the classic Connect Four game in Python. The game utilizes the Pygame library for its user interface and includes an AI opponent that uses the Minimax algorithm with Alpha-Beta pruning.

### Project Structure

The application is currently divided into three classes: 
* Game - handles the game loop and graphical user interface
* Board - keeps track of the game state and handles changes to it
* AI_engine - handles the minimax algorithm and heuristic function for evaluating possible moves

### AI and data structures

The AI opponent uses the minimax algorithm with alpha-beta pruning and the game state is stored in a two-dimensional array, representing the game board's slots. 

The Minimax algorithm is a recursive, decision-making algorithm that is often used to make decisions in turn-based or zero-sum games like Connect Four, Chess, Tic Tac Toe, etc. The algorithm works by generating a tree of potential game states with the root being the current state and branches being possible moves. It simulates turns between the AI and the human player, always maximizing the AI's score while minimizing the human's. A heuristic function calculates a numerical score for each state, based on looking at windows of four slots and analyzing how promising the slot looks. The AI then makes a decision based on minimizing the worst-case scenario that the opponent can force, assuming optimal play from its opponent. 

Alpha-Beta Pruning is a technique used to optimize the algorithm. Essentially, it 'prunes' the branches of the tree that do not need to be searched because we already know they will not influence the final decision, thus speeding up the decision-making process.

### Time and Space Complexity

The time complexity for the game is O(n). The space complexity is also O(n), as the game state is represented using a 2D array, and a new game state is stored on each iteration of the minimax algorithm.

### Graphical User Interface

The graphical user interface was developed using the Pygame library. The player is able to choose a column to drop their token in simply by clicking on the desired column. The player is able to choose their desired token color as well as the difficulty of the opponent. The difficulty of the opponent (2, 4 or 6) is the depth that will be used by the minimax algorithm.

<img width="694" alt="Screenshot 2023-07-05 at 2 56 18" src="https://github.com/nicolaskivimaki/tiralabra_K23/assets/86207135/c6efef9e-6570-445e-b3f4-395fd2e99cf3">

<img width="697" alt="Screenshot 2023-07-05 at 2 42 55" src="https://github.com/nicolaskivimaki/tiralabra_K23/assets/86207135/9e929b7f-c2f1-47ff-a3a3-1b456df6d527">

### What can be improved:

* The heuristic evaluation function could be further developed as it is currently relatively primitive and does not take into account all of the factors that affect how good a position is.
* The graphical user interface could be developed further to improve the gameplay experience.

### Sources

* https://tiralabra.github.io/2023_alkukesa/fi/aiheet/minimax.pdf
* https://en.wikipedia.org/wiki/Minimax
* https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
* https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/
