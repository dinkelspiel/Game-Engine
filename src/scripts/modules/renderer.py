import pygame, pyautogui

class Screen:
    pass

class Camera:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

class renderer:
    def __init__(self, game):
        self.game = game
        self.camera = Camera()

        self.screens = {}
        self.current_screen = ''

        self.original_size = (1280, 720)
        self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        self.main_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)

    def get_screen_size(self):
        return (self.screen.get_width(), self.screen.get_height())

    def load_screen(self, screen: Screen, screen_id):
        screen_add = screen
        self.screens[screen_id] = screen_add

    def switch_screen(self, screen_id):
        self.current_screen = screen_id

    def update(self):
        self.main_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)
        self.screens[self.current_screen].update()

    def render(self):
        self.screens[self.current_screen].render()

        self.game.debug.render()

        self.screen.blit(self.main_surface, (0, 0))

        pygame.display.update()