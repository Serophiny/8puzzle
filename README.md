# 8puzzle & 15puzzle
Python solver for the 8puzzle & 15puzzle game

[Link to Game](http://www.mypuzzle.org/sliding)

Python Version tested: Python 2.7.15+

---

Settings:

INITIAL_BOARD, your start Board

WINNING_BOARD, the winning board, mostly [1, 2, 3, 4, 5, 6, 7, 8, 0] or [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 0]

MANHATTAN == True uses Manhattan distance heuristic

MISPLACED == True uses Misplaced (out of tile) heuristic


May Solve 8Puzzle & 15Puzzle. (15Puzzle will probably need MANHATTAN == True).


IMPORTANT:

Printed boards must be read from bottom to top!
