class Transform:
    def __init__(self) -> None:
        self.x = 0
        self.y = 0

class Entity:
    def add_component(self, component):
        if component not in self.components:
            self.components.append(component)

    def remove_component(self, component):
        if component not in self.components:
            self.components.remove(self.components.index(component))

    def update(self):
        for component in self.components:
            component.update()

    def render(self):
        for component in self.components:
            component.render()

class Camera_Relative_Component():
    def __init__(self, game, parent) -> None:
        self.game = game    
        self.parent = parent

    def update(self):
        self.parent.camera_relative_x = self.parent.transform.x - self.game.renderer.camera.x
        self.parent.camera_relative_y = self.parent.transform.y - self.game.renderer.camera.y

    def render(self):
        pass