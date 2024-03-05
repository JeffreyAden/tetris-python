# This grid is the definitive layout for all the tetris blocks
import pygame
from colors import Colors

class Grid:
    def __init__(self):
        self.num_rows = 20
        self.num_cols = 10
        self.cell_size = 30  # each cell in the grid is 30px

        # create a nested list (2D array) to represent every cell in the grid
        # use list comprehension to create the 2D array
        self.grid = [[0 for j in range(self.num_cols)] for i in range(self.num_rows)]
        self.colors = Colors.get_cell_colors()

    def print_grid(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                # print all row-columns on a new line
                print(self.grid[row][column], end=" ")
            print()

    def is_inside(self, row, column):
        if row >= 0 and row < self.num_rows and column >= 0 and column < self.num_cols:
            return True
        return False

    # let's avoid collisions between blocks by using a method to check whether or not
    # some parts of the grid are empty or not. If a position in the gird is empty return
    # True otherwise return False.
    def is_empty(self, row, column):
        if self.grid[row][column] == 0:
            return True
        return False

    # check whether or not the row is full and if so, then clear it
    def is_row_full(self, row):
        for column in range(self.num_cols):
            if self.grid[row][column] == 0:
                return False
        return True

    # clear the bottom screen rows whenever we finish filling it up
    def clear_row(self, row):
        for column in range(self.num_cols):
            self.grid[row][column] == 0

    # move the grid rows down by a certain amount
    def move_row_down(self, row, num_rows):
        for column in range(self.num_cols):
            self.grid[row + num_rows][column] = self.grid[row][column]
            self.grid[row][column] = 0

    # use a method that will handle the top-bottom checking
    # and updating of all completed rows in the grid
    def clear_full_rows(self):
        completed = 0
        # from the bottom to the near top, loop and check of any and all completed rows
        for row in range(self.num_rows-1, 0, -1):
            if self.is_row_full(row):
                self.clear_row(row)
                completed += 1
            elif completed > 0:
                self.move_row_down(row, completed)
        return completed

    def reset(self):
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                self.grid[row][column] = 0

    # let's add a draw grid fxn
    def draw(self, screen):
        # iterate through each and every cell in the grid and assign their value to a variable
        for row in range(self.num_rows):
            for column in range(self.num_cols):
                cell_value = self.grid[row][column]
                # create a Rect object that'll render as colorful blocks come runtime
                cell_rect = pygame.Rect(column*self.cell_size + 11, row*self.cell_size + 11,
                                        self.cell_size - 1, self.cell_size - 1) # (x, y, w, h)

                # to draw the blocks we need to pass in the following args
                # (surface, color, rect)
                pygame.draw.rect(surface=screen, color=self.colors[cell_value], rect=cell_rect)
