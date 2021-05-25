## Imports

import pygame, pyautogui

## Class for making you unable to register a non screen

class Screen:
    pass

## A Camera that pans around and moves object that has the Camera_Relative_Component component

class Camera:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

## Main Renderer Handler

class renderer:

    ## Initialize

    def __init__(self, game):

        self.game = game

        ## Initialize camera for renderer

        self.camera = Camera()

        ## Create variables

        self.screens = {}
        self.current_screen = ''

        ## Sizes

        self.original_size = (1280, 720)

        ## Start Surfaces

        self.screen = pygame.display.set_mode((1280, 720), pygame.RESIZABLE)
        self.main_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)

    ## Functions

    # Getter for screen size to Vector2 Tuple

    def get_screen_size(self):
        return (self.screen.get_width(), self.screen.get_height())

    # Initializes a screen to be able to be used in renderer

    def load_screen(self, screen: Screen, screen_id):
        screen_add = screen
        self.screens[screen_id] = screen_add

    # Switches to a initialized screen

    def switch_screen(self, screen_id):
        self.current_screen = screen_id

    ## Update Method

    def update(self):
        
        # Clear main surface for drawing

        self.main_surface = pygame.Surface((self.screen.get_width(), self.screen.get_height()), pygame.SRCALPHA)

        # Update the currently selected screen

        self.screens[self.current_screen].update()

    ## Render Method

    def render(self):

        # Render the current screen

        self.screens[self.current_screen].render()

        # Render the debug view

        self.game.debug.render()

        # Update the screen

        self.screen.blit(self.main_surface, (0, 0))
        pygame.display.update()