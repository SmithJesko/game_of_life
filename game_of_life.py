import pyglet
import random as rnd
from config import cell_color

class GameOfLife:

    def __init__(self, window_width, window_height, cell_size, percent_fill):
        self.grid_width = int(window_width / cell_size)
        self.grid_height = int(window_height / cell_size)
        self.cell_size = cell_size
        self.percent_fill = percent_fill
        self.cells = []
        self.generate_cells()


    def generate_cells(self):
        for row in range(0, self.grid_height):
            self.cells.append([])
            for col in range(0, self.grid_width):
                if rnd.random() < self.percent_fill:
                    self.cells[row].append(1)
                else:
                    self.cells[row].append(0)
    

    def run_rules(self):
        temp = []
        for row in range(0, self.grid_height):
            temp.append([])
            for col in range(0, self.grid_width):
                cell_sum = sum([self.get_cell_value(row - 1, col),
                                self.get_cell_value(row - 1, col - 1),
                                self.get_cell_value(row, col -1),
                                self.get_cell_value(row + 1, col - 1),
                                self.get_cell_value(row + 1, col),
                                self.get_cell_value(row + 1, col + 1),
                                self.get_cell_value(row, col + 1),
                                self.get_cell_value(row - 1, col + 1)])

                if self.cells[row][col] == 0 and cell_sum == 3:
                    temp[row].append(1)
                elif self.cells[row][col] == 1 and (cell_sum == 3 or cell_sum == 2):
                    temp[row].append(1)
                else:
                    temp[row].append(0)
        self.cells = temp
    

    def get_cell_value(self, row, col):
        if row >= 0  and row < self.grid_height and \
           col >= 0 and col < self.grid_width:
           return self.cells[row][col]
        return 0


    def draw(self):
        for row in range(0, self.grid_height):
            for col in range(0, self.grid_width):
                if self.cells[row][col] == 1:
                    #(0, 0) (0, 20) (20, 0) (20, 20)
                    square_coords = (row * self.cell_size, col * self.cell_size,
                                     row * self.cell_size, col * self.cell_size + self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size,
                                     row * self.cell_size + self.cell_size, col * self.cell_size + self.cell_size)

                    pyglet.gl.glColor3f(cell_color[0], cell_color[1], cell_color[2])

                    pyglet.graphics.draw_indexed(4, pyglet.gl.GL_TRIANGLES,
                                        [0, 1, 2, 1, 2, 3],
                                        ('v2i', square_coords))