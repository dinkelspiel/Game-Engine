import pygame, time
from src.scripts.game_manager import Game_Manager
from src.scripts.project import *

game = Game_Manager()

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