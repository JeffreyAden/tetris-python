from colors import Colors
import pygame
from positions import Position

class Block:
    def __init__(self, id):
        self.id = id # unique
        # create a unique method that'll represent all types of blocks throughout the program
        self.cells = {}
        self.cell_size = 30  # size in px
        self.row_offset = 0
        self.column_offset = 0
        self.rotation_state = 0
        # colors of the blocks
        self.colors = Colors.get_cell_colors()

    # create a fxn to move the blocks around
    def move(self, rows, columns):
        self.row_offset += rows
        self.column_offset += columns

    # introduce another fxn that keeps track of the blocks' positions
    def get_cell_positions(self):
        tiles = self.cells[self.rotation_state]
        moved_tiles = [] # get and store the new positions of the blocks here
        for position in tiles:
            position = Position(position.row + self.row_offset, position.column + self.column_offset)
            moved_tiles.append(position)
        return moved_tiles

    # let's create a rotate function for our game
    def rotate(self):
        self.rotation_state += 1
        #if the rotation reaches the maximum state, reset back to 0
        if self.rotation_state == len(self.cells):
            self.rotation_state = 0
    # create an undo-rotate method for the cases where the blocks aren't on our screen window
    def undo_rotation(self):
        self.rotation_state -= 1
        if self.rotation_state == 0:
            self.rotation_state = len(self.cells) - 1

    def draw(self, screen, offset_x, offset_y):
        tiles = self.get_cell_positions()
        for tile in tiles:
            tile_rect = pygame.Rect(offset_x + tile.column*self.cell_size, offset_y + tile.row*self.cell_size,
                                    self.cell_size - 1, self.cell_size - 1)
            pygame.draw.rect(screen, self.colors[self.id], tile_rect)


