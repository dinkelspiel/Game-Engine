## Imports

import pygame, os
pygame.font.init()

## Class

class font_handler:
    def __init__(self, game) -> None:
        self.game = game

    ## Returns a render of the designated font and text using the designated font from the current assetpack

    def render(self, text, font, size, color):
        font_file = pygame.font.Font(os.path.join('src', 'resources', self.game.current_assetpack, 'assets', 'fonts', font + '.ttf'), size) 
        return font_file.render(text, True, color)


