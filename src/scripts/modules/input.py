## Imports

from re import L
import pygame

## Class

class Input:

    ## Start vars

    input_state = "main"

    key_signature = False

    # All keys recognized by the script

    record_keys = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z",
                   "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
                   "UP", "DOWN", "LEFT", "RIGHT", 
                   "SPACE", "LCTRL", "LSHIFT", "LALT", "RETURN", "ESCAPE", "TAB", "BACKSPACE",
                   "PERIOD", "MINUS"]

    ## Setter for the input state

    def set_input_state(self, state):
        self.input_state = state

    ## Initialize

    def __init__(self):
        self.any_key_pressed = False
        
        # Create the last_frame_keys and pressed_keys using a for loop for the length of self.record_keys

        self.last_frame_keys = []
        self.pressed_keys = []
        for i in self.record_keys:
            self.pressed_keys.append(False)
            self.last_frame_keys.append(False)

        self.mouse_button_last_frame = False

    ## Returns if a keys is pressed

    def is_pressed(self, key, input_state=""):

        # Gets the key signature in pygame using this terribleness
        # I wish i could just use the keyboard module but that doesnt work on unix based operating systems ;-;

        keys = pygame.key.get_pressed()
        code = "self.key_signature = pygame.K_" + key
        exec(code)

        # Returns a bool wether the key is pressed the window is focused and based on the func params if the input state is the current one

        if input_state != "":
            return bool(keys[self.key_signature] and pygame.mouse.get_focused() and input_state == self.input_state)
        else:
            return bool(keys[self.key_signature] and pygame.mouse.get_focused())

    ## Check what keys are pressed this frame

    def check_keys(self):
        for i, key in enumerate(self.record_keys):
            self.last_frame_keys[i] = self.is_pressed(key)

    ## Returns true if a key was pressed this frame not if its held

    def is_just_pressed(self, key, input_state=""):

        # Same terribleness as in is_pressed()

        keys = pygame.key.get_pressed()
        code = "self.key_signature = pygame.K_" + key
        exec(code)

        # Same thing as in is_pressed() except now theres a check for wether or not it was pressed last frame too in which it returns false

        if input_state != "":
            return bool(keys[self.key_signature] and not self.last_frame_keys[self.record_keys.index(key)] and pygame.mouse.get_focused() and input_state == self.input_state)
        else:
            return bool(keys[self.key_signature] and not self.last_frame_keys[self.record_keys.index(key)] and pygame.mouse.get_focused())

    ## Returns if any key is pressed

    def is_any_key_pressed(self):
        return self.any_key_pressed

    ## Returns if mb_left is pressed

    def is_mouse_button_pressed(self):
        return pygame.mouse.get_pressed()[0]
    
    ## Returns if mb_left was pressed this frame

    def is_mouse_button_just_pressed(self):
        return pygame.mouse.get_pressed()[0] and not self.mouse_button_last_frame