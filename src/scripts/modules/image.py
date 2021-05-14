import pygame, os

class image:
    def __init__(self, game):
        self.game = game

    def load(self, image):
        return pygame.image.load(os.path.join('src', 'resources', self.game.current_assetpack, 'assets', 'images', image))