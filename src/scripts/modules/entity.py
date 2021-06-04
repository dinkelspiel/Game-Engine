## Transform class for a entity

class Transform:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

## Base Entity

class Entity:

    ## Add component to entity

    def add_component(self, component):
        if component not in self.components:
            self.components.append(component)

    ## Remove component from entity

    def remove_component(self, component):
        if component in self.components:
            self.components.remove(self.components.index(component))

    ## Get component

    def get_component(self, component):
        yes = False
        for index, item in enumerate(self.components):
            if type(item) == component:
                yes = True
                num = index
                break
        
        if yes == True:
            return self.components[num]

    ## Contains Component

    def contains_component(self, component):
        if component in self.components:
            return True
        return False

    ## Use the update method in all the components

    def update(self):
        for component in self.components:
            component.update()

    ## Use the render method in all the components

    def render(self):
        for component in self.components:
            component.render()

## Base Components

# Base component for making the entity camera relative

class Camera_Relative_Component():
    def __init__(self, game, parent) -> None:
        self.game = game    
        self.parent = parent

    def update(self):
        self.parent.camera_relative_x = self.parent.transform.x - self.game.renderer.camera.x
        self.parent.camera_relative_y = self.parent.transform.y - self.game.renderer.camera.y

    def render(self):
        pass

class Sprite_Renderer_Component():
    def __init__(self, game, parent) -> None:
        self.game = game    
        self.parent = parent

        self.surface = None
        self.sprite = None

    def update(self):
        pass

    def render(self):
        if self.sprite != None and self.surface != None:
            if self.parent.contains_component(Camera_Relative_Component(self.game, self.parent)):
                self.surface.blit(self.sprite, (self.parent.camera_relative_x, self.parent.camera_relative_y))
            else:
                self.surface.blit(self.sprite, (self.parent.transform.x, self.parent.transform.y))