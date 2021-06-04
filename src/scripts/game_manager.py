## Imports

# Non Local Modules

import pygame, os, json, pyautogui, sys, time

# Local Modules

from .modules.input import Input
from .modules.language import Language_Handler
from .modules.colors import Color_Handler
from .modules.sound import Sound_Handler
from .modules.image import image
from .modules.math_utils import math_utils
from .modules.renderer import renderer
from .modules.fonts import font_handler
from .modules.debug import Debug

# Screens

from .screens.engine_main_screen import engine_main_screen
from .screens.game_screen import game_screen

## Game Manager Class

class Game_Manager:

    def stop(self):
        self.running = False

    def change_title(self, title):
        self.title = title
        pygame.display.set_caption(title)

    def __init__(self):
        ## Set asset pack (Needs to be done before modules)

        self.current_assetpack = "main"

        ## Initialize all modules

        self.input = Input()
        self.language_handler = Language_Handler(self)
        self.color_handler = Color_Handler(self)
        self.sound_handler = Sound_Handler(self)
        self.image = image(self)
        self.math = math_utils()
        self.renderer = renderer(self)
        self.font_handler = font_handler(self)
        self.debug = Debug(self)

        ## Time

        self.delta_time = 1
        self.game_speed = 1
        self.clock = pygame.time.Clock()

        ## General Info and Data

        self.running = True
        self.title = "Game"

        with open(os.path.join("src", "properties.json"), "r") as file:
            self.properties = json.load(file)

        self.change_title(self.properties["id"])
        icon = pygame.image.load(os.path.join("src", "resources", self.current_assetpack, "assets", "icon.png"))
        pygame.display.set_icon(icon)

        ## Start debug 

        self.previous_time = time.time()

        ## Set input state

        self.input.set_input_state('general')

    ## Set to default settings

    def initialize(self):
        self.change_title(self.properties["id"])
        self.input.input_state = "general"

        self.renderer.load_screen(engine_main_screen(self), "engine_main")
        self.renderer.load_screen(game_screen(self), "game_screen")
        self.renderer.switch_screen("game_screen")

    ## Main Update Method

    def update(self):
        ## Calculate Delta Time

        now = time.time()
        self.delta_time = now - self.previous_time
        self.previous_time = now

        ## Input

        self.input.any_key_pressed = False
        for i, item in enumerate(self.input.pressed_keys):
            self.input.pressed_keys[i] = False

        ## Events

        keys = pygame.key.get_pressed()
        for event in pygame.event.get():
            
            # Stop if quit called

            if event.type == pygame.QUIT:
                self.stop()

            # Input 

            if event.type == pygame.KEYDOWN:
                self.input.any_key_pressed = True
                for i, key in enumerate(self.input.record_keys):
                    key_signature = 0
                    exec("key_signature = pygame.K_" + key)
                    self.input.pressed_keys[i] = keys[key_signature]
                        
        ## Screens

        self.renderer.update()

        self.debug.update()

    ## Trail update method

    def end_update(self):
        self.input.check_keys()
        self.input.mouse_button_last_frame = self.input.is_mouse_button_pressed()

    ## Main Renderer Method

    def render(self):  
        self.renderer.render()

    ## Trail renderer method

    def end_render(self):  
        pass