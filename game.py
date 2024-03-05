
from grid import Grid
from blocks import *
import random
import pygame

class Game:

    def __init__(self):
        self.grid = Grid()
        self.blocks = [IBlock(), JBlock(), LBlock(), ZBlock(), TBlock(), SBlock(), OBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.game_over = False
        self.score = 0
        self.rotate_sound = pygame.mixer.Sound("Sounds/rotate.ogg")
        self.clear_sound = pygame.mixer.Sound('Sounds/clear.ogg')
        pygame.mixer.music.load("Sounds/music.ogg")
        pygame.mixer.music.play(-1) # -1 means loop indefinitely
    # we'll update the score as follows: 100pts for 1 line cleared, 200 pts for 2 lines and so on
    def update_score(self, lines_cleared, move_down_points):
        if lines_cleared == 1:
            self.score += 100
        elif lines_cleared == 2:
            self.score += 300
        elif lines_cleared == 3:
            self.score += 500
        self.score += move_down_points

    def get_random_block(self):
        if len(self.blocks) == 0:
            self.blocks = [IBlock(), JBlock(), LBlock(), ZBlock(), TBlock(), SBlock(), OBlock()]
        block = random.choice(self.blocks)
        self.blocks.remove(block)
        return block

    # the move is invalid if the block is outside the screen or
    # if it fits but also goes out of screen bounds for left, right moves and rotation
    def move_left(self):
        self.current_block.move(0, -1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0, 1)

    def move_right(self):
        self.current_block.move(0, 1)
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.move(0,-1)

    def move_down(self):
        self.current_block.move(1, 0)
        if self.block_inside()== False or self.block_fits()== False:
            self.current_block.move(-1, 0)
            self.lock_block()

    # when the block reaches the screen's bottom, lock it in place via a method
    def lock_block(self):
        tiles = self.current_block.get_cell_positions()
        for position in tiles:
            self.grid.grid[position.row][position.column] = self.current_block.id
        # now fetch the next block as the previous one is stuck at the bottom
        self.current_block = self.next_block
        self.next_block = self.get_random_block()
        rows_cleared = self.grid.clear_full_rows()

        # sound off whenever a row is cleared
        if rows_cleared > 0:
            self.clear_sound.play()
            self.update_score(rows_cleared, 0)

        # if a new block can't fit inside the grid, we end the game
        if self.block_fits() == False:
            self.game_over = True

    # use a method to restart and rest the game once its finished
    def reset(self):
        self.grid.reset() # for reset to work, the grid class must have this method
        self.blocks = [IBlock(), JBlock(), LBlock(), ZBlock(), TBlock(), SBlock(), OBlock()]
        self.current_block = self.get_random_block()
        self.next_block = self.get_random_block()
        self.score = 0


    # check if the block is on top of an empty grid or not
    # if the position is empty, the block can move to that position
    def block_fits(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_empty(tile.row, tile.column) == False:
                return False
        return True

    def rotate(self):
        self.current_block.rotate()
        # if the block is rotating outside of our screen window, undo said rotation
        if self.block_inside() == False or self.block_fits() == False:
            self.current_block.undo_rotation()
        else:
            self.rotate_sound.play()
    # check to see if the blocks are inside or outside the grid
    # if they are, bring them back in
    def block_inside(self):
        tiles = self.current_block.get_cell_positions()
        for tile in tiles:
            if self.grid.is_inside(tile.row, tile.column) == False:
                return False
        return True

    def draw(self, screen):
        self.grid.draw(screen)
        self.current_block.draw(screen,11, 11)

        if self.next_block.id == 3:
            self.next_block.draw(screen, 255, 290)
        elif self.next_block.id == 4:
            self.next_block.draw(screen, 255, 280)
        else:
            self.next_block.draw(screen, 270, 270)