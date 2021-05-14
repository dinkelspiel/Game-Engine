import pygame, time
from src.scripts.game import Game
from src.scripts.project import *

game = Game()

game.initialize()

while game.running:
    ## Update

    update_start_time = time.time()
    game.update()
    update()
    game.end_update()
    update_end_time = time.time()

    ## Render

    render_start_time = time.time()
    game.render()
    render()
    game.end_render()

    render_end_time = time.time()

pygame.quit()