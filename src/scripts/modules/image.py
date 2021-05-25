## Imports

import pygame, os

## Class

class image:
    def __init__(self, game):
        self.game = game

    ## Loads image from the current active image folder using the current Assetpack

    def load(self, image):
        return pygame.image.load(os.path.join('src', 'resources', self.game.current_assetpack, 'assets', 'images', image))