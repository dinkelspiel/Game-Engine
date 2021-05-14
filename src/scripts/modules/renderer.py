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

        self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)

    def get_screen_size(self):
        return (self.screen.get_width(), self.screen.get_height())

    def load_screen(self, screen: Screen, screen_id):
        screen_add = screen
        self.screens[screen_id] = screen_add

    def switch_screen(self, screen_id):
        self.current_screen = screen_id

    def update(self):
        self.screens[self.current_screen].update()

    def render(self):
        self.screens[self.current_screen].render()
        pygame.display.update()