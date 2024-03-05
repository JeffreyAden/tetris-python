import pygame, sys
from game import Game
from colors import Colors

# initalize the program
pygame.init()

title_font = pygame.font.Font(None, 40)
score_surface = title_font.render("Score", True, Colors.white)
next_surface = title_font.render("Next", True, Colors.white)
game_over_surface = title_font.render("GAME OVER", True, Colors.white)

score_rect = pygame.Rect(320, 55, 170, 60) # the pygame rect obj will now appear on the screen
next_rect = pygame.Rect(320, 215, 170, 180)

# let's create and initalize the dimensions
# of our display screen surface for our game

screen = pygame.display.set_mode((500, 640))
pygame.display.set_caption("Tetris")

# add a variable to control the frame rate of the game
clock = pygame.time.Clock()
game = Game()

# let's create a custom event that will be triggered when certain
# conditions are met.In our case, we want to use this event(GAME_UPDATE) to slow
# down the speed of our blocks' decent to 200ms using 'set_time' method
GAME_UPDATE = pygame.USEREVENT
pygame.time.set_timer(GAME_UPDATE, 200)

while True:
    # get all the events in the program, put them in a list and loop over them
    # this should go on unless the game is over in which case terminate everything
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  # if the event is quit, the exit the loop
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            # add a restart option so that we can restart the game immediately if we want to
            if game.game_over == True:
                game.game_over = False
                game.reset()
            if event.key == pygame.K_LEFT and game.game_over == False:
                game.move_left()
            if event.key == pygame.K_RIGHT and game.game_over == False:
                game.move_right()
            if event.key == pygame.K_DOWN and game.game_over == False:
                game.move_down()
                game.update_score(0, 1)
            # rotate the blocks counter-clockwise
            if event.key == pygame.K_UP and game.game_over == False:
                game.rotate()
        if event.type == GAME_UPDATE and game.game_over == False:
            game.move_down()

    # Drawing the program's events....

    # because the score will be dynamic (always changing)
    # the screen surface for the score must also be different
    # the score is an int so it must be converted to a string to be displayed
    score_value_surface = title_font.render(str(game.score), True, Colors.white)

    screen.fill(Colors.dark_blue)
    screen.blit(score_surface, (365, 20, 50, 50))
    screen.blit(next_surface, (375, 180, 50, 50))
    # only display the game over message when we finish the game
    if game.game_over == True:
        screen.blit(game_over_surface, (320, 450, 50, 50))

    pygame.draw.rect(screen, Colors.light_blue, score_rect, 0, 15)
    screen.blit(score_value_surface,
                score_value_surface.get_rect(centerx=score_rect.centerx, centery=score_rect.centery))
    pygame.draw.rect(screen, Colors.light_blue, next_rect, 0, 15)
    game.draw(screen)
    pygame.display.update()  # show a black screen after exiting the game
    clock.tick(60) # the program should run at 60fps

