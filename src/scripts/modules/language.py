## Imports

import json, os

## Class

class Language_Handler:

    ## Current language

    current_language_id = "en_US"

    ## Initialize

    def __init__(self, game):
        self.game = game

        ## Load language file

        with open(os.path.join("src", "resources", self.game.current_assetpack, "data", "lang", self.current_language_id + ".json"), "r") as lang_file:
            self.lang_json = json.load(lang_file)
    
    ## Return the translated text taken from the link 
    ## If no text is found translated in the current language the id will be given

    def translatable_text(self, lang_file_link):
        if lang_file_link in self.lang_json:
            text = self.lang_json[lang_file_link]
            return text
        else:
            return lang_file_link
        


    