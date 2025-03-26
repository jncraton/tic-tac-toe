Tic tac toe
===========

This project creates an AI agent to play games of [Tic-tac-toe](https://en.wikipedia.org/wiki/Tic-tac-toe).

Learning Objectives
-------------------

After completing this experience, students will be able to:

- Map game playing to search problems
- Implement minimax

![Move sequence](https://upload.wikimedia.org/wikipedia/commons/1/1b/Tic-tac-toe-game-1.svg)

The included `my_agent` function should be modified to return an appropriate move for a given board position. Additional implementation details are described in `play.py`.

Algorithms
----------

Tic-tac-toe is a short, perfect information game with a known optimal solution. Perfect play results in every game ending in a draw.

On modern hardware, exhaustive search using [minimax](https://en.wikipedia.org/wiki/Minimax) should be possible to achieve optimal play. Other approaches, such as [Monte Carlo Tree Search](https://en.wikipedia.org/wiki/Monte_Carlo_tree_search) should also produce good results while using much less compute.
