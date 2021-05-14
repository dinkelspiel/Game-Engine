import pygame, os, json, pyautogui, sys, time

from .modules.input import Input
from .modules.language import Language_Handler
from .modules.colors import Color_Handler
from .modules.sound import Sound_Handler
from .modules.image import image
from .modules.math_utils import math_utils
from .modules.renderer import renderer
from .modules.fonts import font_handler

from .modules.screens.screen_1 import screen_1
from .modules.screens.screen_2 import screen_2
from .modules.screens.screen_3 import screen_3
from .modules.screens.screen_4 import screen_4

class Game:

    game_speed = 1
    clock = pygame.time.Clock()

    running = True
    title = "Game"

    current_assetpack = "main"

    def stop(self):
        self.running = False

    def change_title(self, title):
        self.title = title
        pygame.display.set_caption(title)

    def __init__(self):
        self.input = Input()
        self.language_handler = Language_Handler(self)
        self.color_handler = Color_Handler(self)
        self.sound_handler = Sound_Handler(self)
        self.image = image(self)
        self.math = math_utils()
        self.renderer = renderer(self)
        self.font_handler = font_handler(self)

        self.previous_time = time.time()

        self.input.set_input_state('general')

        with open(os.path.join("src", "properties.json"), "r") as file:
            self.properties = json.load(file)

        self.change_title(self.properties["id"])
        icon = pygame.image.load(os.path.join("src", "resources", self.current_assetpack, "assets", "icon.png"))
        pygame.display.set_icon(icon)

    def initialize(self):
        self.change_title(self.properties["id"])
        self.input.input_state = "general"

        sscreen_1 = screen_1(self)
        sscreen_2 = screen_2(self)
        sscreen_3 = screen_3(self)
        sscreen_4 = screen_4(self)
        self.renderer.load_screen(sscreen_1, 'screen_1')
        self.renderer.load_screen(sscreen_2, 'screen_2')
        self.renderer.load_screen(sscreen_3, 'screen_3')
        self.renderer.load_screen(sscreen_4, 'screen_4')
        self.renderer.switch_screen('screen_1')

        self.screen = 1

    def update(self):
        # Calculate Delta Time
        now = time.time()
        self.delta_time = now - self.previous_time
        self.previous_time = now

        self.input.any_key_pressed = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.stop()
            if event.type == pygame.KEYDOWN:
                self.input.any_key_pressed = True

        if self.input.is_just_pressed('LEFT'):
            self.screen -= 1
        if self.input.is_just_pressed('RIGHT'):
            self.screen += 1

        self.screen = min(4, max(self.screen, 1))
        if self.renderer.current_screen != 'screen_' + str(self.screen):
            self.renderer.switch_screen('screen_' + str(self.screen))

        # Screens
        self.renderer.update()

    def end_update(self):
        self.input.check_keys()
        self.input.mouse_button_last_frame = self.input.is_mouse_button_pressed()

    def render(self):  
        self.renderer.render()

    def end_render(self):  
        pass