## Imports

import json, os
from colormap import hex2rgb

## Class

class Color_Handler:
    def __init__(self, game):
        self.game = game
    
    ## Returns the hex value of the given link from the current assetpack

    def get_hex(self, color_link):
        with open(os.path.join("src", "resources", self.game.current_assetpack, "assets", "colors.json"), "r") as color_file:
            color_json = json.load(color_file)
        if color_link in color_json:
            return color_json[color_link]
        else:
            return "#00000"

    ## Returns the rgb value of the given link from the current assetpack

    def get_rgb(self, color_link):
        with open(os.path.join("src", "resources", self.game.current_assetpack, "assets", "colors.json"), "r") as color_file:
            color_json = json.load(color_file)
        if color_link in color_json:
            return hex2rgb(color_json[color_link])
        else:
            return (0, 0, 0)
        
