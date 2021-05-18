import pygame, os, json, pyautogui, sys, time

from .modules.input import Input
from .modules.language import Language_Handler
from .modules.colors import Color_Handler
from .modules.sound import Sound_Handler
from .modules.image import image
from .modules.math_utils import math_utils
from .modules.renderer import renderer
from .modules.fonts import font_handler
from .modules.debug import Debug

from .screens.screen_main_menu import screen_main_menu
from .screens.screen_game import screen_game
from .screens.screen_settings import screen_settins
from .screens.screen_lose import screen_lose
from .screens.screen_win import screen_win
from .screens.gui_test import gui_test

class Game_Manager:

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
        self.debug = Debug(self)

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

        game_screen = screen_game(self)
        main_menu_screen = screen_main_menu(self)
        screen_gui_test = gui_test(self)
        settings_screen = screen_settins(self)
        lose_screen = screen_lose(self)
        win_screen = screen_win(self)
        self.renderer.load_screen(screen_gui_test, 'gui_test')
        self.renderer.load_screen(game_screen, 'game')
        self.renderer.load_screen(main_menu_screen, 'main_menu')
        self.renderer.load_screen(settings_screen, 'settings')
        self.renderer.load_screen(lose_screen, 'lose')
        self.renderer.load_screen(win_screen, 'win')
        self.renderer.switch_screen('main_menu')

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

        # Screens
        self.renderer.update()

        self.debug.update()

    def end_update(self):
        self.input.check_keys()
        self.input.mouse_button_last_frame = self.input.is_mouse_button_pressed()

    def render(self):  
        self.renderer.render()

    def end_render(self):  
        pass