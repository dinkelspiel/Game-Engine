## Imports

import pygame, os
pygame.mixer.init()

## Class

class Sound_Handler:

    def __init__(self, game):
        self.game = game

    ## Loads sound from current active sound folder following the current Assetpack

    def load(self, sound_file):
            return pygame.mixer.Sound(os.path.join("src", "resources", self.game.current_assetpack, "assets", "sounds", sound_file))

