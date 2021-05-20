from re import L
import pygame

class Input:

    input_state = "main"

    key_signature = False

    record_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                   "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                   "UP", "DOWN", "LEFT", "RIGHT", 
                   "SPACE", "LCTRL", "LSHIFT", "LALT", "RETURN", "ESCAPE", "TAB", "BACKSPACE",
                   "PERIOD", "MINUS"]

    def set_input_state(self, state):
        self.input_state = state

    def __init__(self):
        self.any_key_pressed = False
        
        self.last_frame_keys = []
        self.pressed_keys = []
        for i in self.record_keys:
            self.pressed_keys.append(False)
            self.last_frame_keys.append(False)

        self.mouse_button_last_frame = False

    def is_pressed(self, key, input_state=""):
        keys = pygame.key.get_pressed()
        code = "self.key_signature = pygame.K_" + key
        exec(code)
        if input_state != "":
            return bool(keys[self.key_signature] and pygame.mouse.get_focused() and input_state == self.input_state)
        else:
            return bool(keys[self.key_signature] and pygame.mouse.get_focused())

    def check_keys(self):
        for i, key in enumerate(self.record_keys):
            self.last_frame_keys[i] = self.is_pressed(key)

    def is_just_pressed(self, key, input_state=""):
        keys = pygame.key.get_pressed()
        code = "self.key_signature = pygame.K_" + key
        exec(code)
        if input_state != "":
            return bool(keys[self.key_signature] and not self.last_frame_keys[self.record_keys.index(key)] and pygame.mouse.get_focused() and input_state == self.input_state)
        else:
            return bool(keys[self.key_signature] and not self.last_frame_keys[self.record_keys.index(key)] and pygame.mouse.get_focused())

    def is_any_key_pressed(self):
        return self.any_key_pressed

    def is_mouse_button_pressed(self):
        return pygame.mouse.get_pressed()[0]
    
    def is_mouse_button_just_pressed(self):
        return pygame.mouse.get_pressed()[0] and not self.mouse_button_last_frame