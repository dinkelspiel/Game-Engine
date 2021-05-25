## Imports

import pygame

## All constraints that can be used

# Rectangle Constraints

class rect_constraints():
    pass

class center_constraint(rect_constraints):
    pass

class aspect_constraint(rect_constraints):
    def __init__(self, aspect_ratio) -> None:
        self.value = aspect_ratio

class percentage_constraint(rect_constraints):
    def __init__(self, percentage):
        self.value = percentage

class pixel_constraint(rect_constraints):
    def __init__(self, pixel):
        self.value = pixel

# Text constraints

class text_size_constraint:
    pass

class resize_constraint:
    pass

class samesize_constraint:
    pass

## Gui Rectangle Class

class gui_rect:

    # Start Vars for everything

    x_constraint = None
    y_constraint = None
    width_constraint = None
    height_constraint = None

    x = 0
    y = 0

    tween = False
    tween_x = 0
    tween_y = 0
    tween_mult = 0

    tween_s = False
    tween_width = 0
    tween_height = 0
    tween_s_mult = 0

    tween_c = False
    tween_color_rgb = (0, 0, 0)

    tmp_width = 0
    tmp_height = 0

    width = 0
    height = 0

    border_radius = 0
    outline = 0

    color = (0, 0, 0)

    parent = None

    image = 0
    image_rotation = 0

    ## Set Constraints

    # Position Constraints

    def set_x_constraint(self, x_constraint):
        self.x_constraint = x_constraint

    def set_y_constraint(self, y_constraint):
        self.y_constraint = y_constraint

    # Size Constraints

    def set_width_constraint(self, width_constraint):
        self.width_constraint = width_constraint

    def set_height_constraint(self, height_constraint):
        self.height_constraint = height_constraint

    # Misc to rect

    def set_border_radius(self, radius):
        self.border_radius = radius

    def set_outline_radius(self, outline):
        self.outline = outline

    def set_draw_color(self, rgb):
        self.color = rgb

    # Tools

    def is_touching_mouse(self):
        mx, my = pygame.mouse.get_pos()
        if self.game.math.in_rect(mx, my, self.x, self.y , self.width, self.height):
            return True
        return False

    def tween_to(self, x, y, mult):
        self.tween = True
        self.tween_x = x
        self.tween_y = y
        self.tween_mult = mult

    def tween_size(self, width, height, mult):
        self.tween_s = True
        self.tween_width = width
        self.tween_height = height
        self.tween_s_mult = mult

    def tween_color(self, colorrgb, mult):
        self.tween_c = True
        self.tween_color_rgb = colorrgb
        self.tween_color_mult = mult

    def __init__(self, game, parent=None) -> None:
        self.game = game
        self.parent = parent
        self.visible = True
        self.show_rect = True
        self.show_image = True

        self.has_initialized = False

    def initialize(self):
        if self.parent == None:
            self.parent = self.game.renderer.screen_rect

    ## Update thingy

    def update(self):

        if not self.has_initialized:
            self.initialize()

        ## Set Position thing

        if not self.tween:
            # Set X Constraints

            if self.x_constraint != None:
                class_use = type(self.x_constraint)
                if class_use == center_constraint:
                    self.x = self.parent.x + (self.parent.width / 2) - (int(self.width) / 2)
                elif class_use == percentage_constraint:
                    self.x = self.parent.x + (self.parent.width * self.x_constraint.value)
                elif class_use == pixel_constraint:
                    self.x = self.parent.x + self.x_constraint.value

            # Set Y Constraints

            if self.y_constraint != None:
                class_use = type(self.y_constraint)
                if class_use == center_constraint:
                    self.y = self.parent.y + (self.parent.height / 2) - (int(self.height) / 2)
                elif class_use == percentage_constraint:
                    self.y = self.parent.y + (self.parent.height * self.y_constraint.value)
                elif class_use == pixel_constraint:
                    self.y = self.parent.y + self.y_constraint.value

        ## Set size thingy

        if not self.tween_s:

            # Set Width Constraints

            if self.width_constraint != None:
                class_use = type(self.width_constraint)
                if class_use == percentage_constraint:
                    self.width = self.parent.width * self.width_constraint.value
                elif class_use == aspect_constraint:
                    self.width = self.height * self.width_constraint.value
                elif class_use == pixel_constraint:
                    self.width = self.width_constraint.value

            # Set Height Constraints

            if self.height_constraint != None:
                class_use = type(self.height_constraint)
                if class_use == percentage_constraint:
                    self.height = self.parent.height * self.height_constraint.value
                elif class_use == aspect_constraint:
                    self.height = self.width * self.height_constraint.value()
                elif class_use == pixel_constraint:
                    self.height = self.height_constraint.value

        # Tween Position

        if self.tween:
            tmp_x = 0
            tmp_y = 0
            class_use = type(self.tween_x)
            if class_use == center_constraint:
                tmp_x = self.parent.x + (self.parent.width / 2) - (int(self.width) / 2)
            elif class_use == percentage_constraint:
                tmp_x = self.parent.x + (self.parent.width * self.tween_x.value)
            elif class_use == pixel_constraint:
                tmp_x = self.parent.x + self.tween_x.value

            class_use = type(self.tween_y)
            if class_use == center_constraint:
                tmp_y = self.parent.y + (self.parent.height / 2) - (int(self.height) / 2)
            elif class_use == percentage_constraint:
                tmp_y = self.parent.y + (self.parent.height * self.tween_y.value)
            elif class_use == pixel_constraint:
                tmp_y = self.parent.y + self.tween_y.value

            self.x += (tmp_x - self.x) / ((self.tween_mult * self.game.delta_time) * 600)
            self.y += (tmp_y - self.y) / ((self.tween_mult * self.game.delta_time) * 600) 

        # Tween Size

        if self.tween_s:
            class_use = type(self.tween_width)
            if class_use == percentage_constraint:
                self.tmp_width = self.parent.width * self.tween_width.value
            elif class_use == aspect_constraint:
                self.tmp_width = self.tmp_height
            elif class_use == pixel_constraint:
                self.tmp_width = self.tween_width.value

            class_use = type(self.tween_height)
            if class_use == percentage_constraint:
                self.tmp_height = self.parent.height * self.tween_height.value
            elif class_use == aspect_constraint:
                self.tmp_height = self.tmp_width
            elif class_use == pixel_constraint:
                self.tmp_height = self.tween_height.value
                    
            self.width += (self.tmp_width - self.width) / self.tween_s_mult
            self.height += (self.tmp_height - self.height) / self.tween_s_mult
        
        if self.tween_c:
            self.color = (self.color[0] + (self.tween_color_rgb[0] - self.color[0]) / self.tween_color_mult,
                          self.color[1] + (self.tween_color_rgb[1] - self.color[1]) / self.tween_color_mult, 
                          self.color[2] + (self.tween_color_rgb[2] - self.color[2]) / self.tween_color_mult)

    def render(self):
        if self.visible:
            if self.show_rect:
                pygame.draw.rect(self.game.renderer.main_surface, self.color, ((self.x, self.y), (self.width, self.height)), self.outline, self.border_radius)
            if self.image != 0 and self.show_image:
                image = pygame.transform.scale(self.image, (int(self.width), int(self.height)))
                img, rect = self.game.math.rotate_center(image, self.image_rotation, self.x + self.width / 2, self.y + self.height / 2)
                self.game.renderer.main_surface.blit(img, rect)

class gui_text:
    def set_x_constraint(self, constraint):
        self.x_constraint = constraint

    def set_y_constraint(self, constraint):
        self.y_constraint = constraint

    def set_size_constraint(self, constraint):
        self.size_constraint = constraint

    def set_color(self, rgb):
        self.color = rgb

    def __init__(self, game) -> None:
        self.game = game

        self.text = ""
        self.draw_text = self.text
        self.parent = None

        self.x, self.y = 0, 0

        self.x_constraint = None
        self.y_constraint = None
        self.size_constraint = None

        self.size = 12

        self.color = (0, 0, 0)

    def update(self):
        if self.parent == None:
            print('Parent of text field must be set')
            return

        self.draw_text = self.text
        self.draw_text += '\n'
        self.draw_text = self.draw_text.split('\n')
        self.draw_text = self.draw_text[0: -1]

        self.longest_length = 0
        for i in self.draw_text:
            length = self.game.font_handler.render(i, 'default', self.size, (0, 0, 0)).get_width()
            self.longest_length = max(self.longest_length, length)

        class_use = type(self.x_constraint)
        if class_use == center_constraint:
            self.x = self.parent.x + (self.parent.width / 2)
        elif class_use == percentage_constraint:
            self.x = self.parent.x + (self.parent.width * self.x_constraint.value)
        elif class_use == pixel_constraint:
            self.x = self.parent.x + self.x_constraint.value

        class_use = type(self.y_constraint)
        if class_use == center_constraint:
            self.y = self.parent.y + (self.parent.height / 2) - (self.size * (len(self.draw_text) - 1)) / 2
        elif class_use == percentage_constraint:
            self.y = self.parent.y + (self.parent.width * self.y_constraint.value)
        elif class_use == pixel_constraint:
            self.y = self.parent.y + self.y_constraint.value

        class_use = type(self.size_constraint)
        if class_use == resize_constraint:
            pass
        if class_use == percentage_constraint:
            self.size = int((self.parent.height * self.size_constraint.value) / len(self.draw_text))

    def render(self):
        for i, item in enumerate(self.draw_text):
            img, rect = self.game.math.rotate_center(self.game.font_handler.render(item, 'default', self.size, self.color), 0, self.x, (self.y + self.size * i))
            self.game.renderer.main_surface.blit(img, rect)

class gui_toggle_button:
    def __init__(self, game) -> None:
        self.game = game
        self.rect = gui_rect(game)
    
        self.hover = False
        self.toggled = False

    def update(self):
        self.rect.update()
        if self.rect.is_touching_mouse():
            self.hover = True
        else:
            self.hover = False

        if self.hover and self.game.input.is_mouse_button_just_pressed():
            self.toggled = not self.toggled

    def render(self):
        self.rect.render()

class gui_press_button:
    def __init__(self, game) -> None:
        self.game = game
        self.rect = gui_rect(game)
    
        self.hover = False
        self.pressed = False

    def update(self):
        self.rect.update()
        if self.rect.is_touching_mouse():
            self.hover = True
        else:
            self.hover = False

        if self.hover and self.game.input.is_mouse_button_just_pressed():
            self.pressed = True
        else:
            self.pressed = False

    def render(self):
        self.rect.render()

class gui_slider:
    def __init__(self, game, val_start, val_end) -> None:
        self.game = game
        self.slider_body = gui_rect(game)
        self.slider_head = gui_rect(game)

        self.value = 0
        self.value_range = (val_start, val_end)

    def update(self):
        self.slider_body.update()
        self.slider_head.update()

        slider_bigger_bounding_box = ((self.slider_body.x, self.slider_body.y - 10), (self.slider_body.width, self.slider_body.height + 30))

        self.slider_head.x = max(self.slider_body.x, min(self.slider_head.x, self.slider_body.x + self.slider_body.width))

        if self.slider_head.tween:
            self.value = (self.slider_head.x - self.slider_body.x) / (self.slider_body.width / self.value_range[1]) * 1.01

        mx, my = pygame.mouse.get_pos()
        if self.game.math.in_rect(mx, my, slider_bigger_bounding_box[0][0], slider_bigger_bounding_box[0][1], slider_bigger_bounding_box[1][0], slider_bigger_bounding_box[1][1]) and self.game.input.is_mouse_button_pressed():
            self.slider_head.tween_to(pixel_constraint(mx - self.slider_head.parent.x - self.slider_head.width / 2), center_constraint(), 3)

    def render(self):
        self.slider_body.render()
        self.slider_head.render()