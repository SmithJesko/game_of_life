# Game of Life
### A cellular automata simulation

> The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970.

>The "game" is a zero-player game, meaning that its evolution is determined by its initial state, requiring no further input. One interacts with the Game of Life by creating an initial configuration and observing how it evolves, or, for advanced "players", by creating patterns with particular properties.

I made this cellular automata simulation based off of John Conway's Game of Life using Python 3.6 and pyglet

---

### Rules
+ Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
+ Any live cell with two or three live neighbours lives on to the next generation.
+ Any live cell with more than three live neighbours dies, as if by overpopulation.
+ Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

### To use
1. Make sure you have Python 3 installed
2. Use `pip install pyglet`
3. Clone this repository
4. Edit the `config.py` file
5. Run `main.py`

### Example
![example](https://github.com/SmithJesko/game_of_life/blob/master/example.gif)
