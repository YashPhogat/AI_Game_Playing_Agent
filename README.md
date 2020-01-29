# AI_Game_Playing_Agent


Halma is a famous old Victorian game in which the objective is not to capture your opponent's pieces but instead to hop over them in an effort to get to the opposite side first. Similar to Chinese Checkers but with more depth and added complexity as there are 8 directions of movement instead of 6.

In this project, we will play the game of Halma, an adversarial game with some similarities to checkers. The game uses a 16x16 checkered gameboard. Each player starts with 19 game pieces clustered in diagonally opposite corners of the board. To win the game, a player needs to transfer all of their pieces from their starting corner to the opposite corner, into the positions that were initially occupied by the opponent. Note that this original rule of the game is subject to spoiling, as a player may choose to not move some pieces at all, thereby preventing the opponent from occupying those locations. Note that the spoiling player cannot win either (because some pieces remain in their original corner and thus cannot be used to occupy all positions in the opposite corner). Here, to prevent spoiling, we modify the goal of the game to be to occupy all of the opponent’s starting positions which the opponent is not still occupying.

1. Created an AI agent that can play HALMA against other AI agents or human players.

2. Used the the classical Minimax game playing algorithm along with alpha-beta pruning.

3. Handled more complicated rules to avoid spoiling by either player.


NOTE: I am not entirely sure if posting the code may violate some of my course rules since this was a class project so I will not be posting any code here. Please reach out to me personally if you want to understand the logic or other details.
