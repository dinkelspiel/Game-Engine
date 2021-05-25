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
        if component not in self.components:
            self.components.remove(self.components.index(component))

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