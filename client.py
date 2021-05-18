import pygame, time
from src.scripts.game_manager import Game_Manager

game = Game_Manager()

game.initialize()

while game.running:
    ## Update

    update_start_time = time.time()
    game.update()
    game.end_update()
    update_end_time = time.time()

    ## Render

    render_start_time = time.time()
    game.render()
    game.end_render()
    render_end_time = time.time()

    game.debug.send_stats(update_end_time - update_start_time, render_end_time - render_start_time)

pygame.quit()