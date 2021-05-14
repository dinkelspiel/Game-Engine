import pygame, os
pygame.font.init()

class font_handler:
    def __init__(self, game) -> None:
        self.game = game

    def render(self, text, font, size, color):
        font_file = pygame.font.Font(os.path.join('src', 'resources', self.game.current_assetpack, 'assets', 'fonts', font + '.ttf'), size) 
        return font_file.render(text, True, color)


