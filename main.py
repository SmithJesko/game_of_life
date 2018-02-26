# Conway's Game of Life by Smith Jesko
# This is a cellular automata simulation

## RULES
# Any live cell with fewer than two live neighbours dies, as if caused by underpopulation.
# Any live cell with two or three live neighbours lives on to the next generation.
# Any live cell with more than three live neighbours dies, as if by overpopulation.
# Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.

import pyglet
from game_of_life import GameOfLife
from config import width, height, fill_percent, cell_size, export

i = 0

class Window(pyglet.window.Window):

    def __init__(self):
        super().__init__(width, height)
        self.gameOfLife = GameOfLife(self.get_size()[0],
                                     self.get_size()[1],
                                     cell_size,
                                     fill_percent)
        pyglet.clock.schedule_interval(self.update, 1.0/24.0)
        self.i = 0

    def on_draw(self):
        self.clear()
        self.gameOfLife.draw()
        
    def update(self, dt):
        self.i += 1
        self.gameOfLife.run_rules()
        
        if export:
            self.export_loop()
        
    def export_loop(self):
        pyglet.image.get_buffer_manager().get_color_buffer().save('img/screenshot{}.png'.format(self.i))
        

if __name__ == "__main__":
    window = Window()
    pyglet.app.run()