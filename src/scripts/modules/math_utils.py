## Imports

import pygame, math

## Class

class math_utils:

    ## Function for rotating a image around its center in pygame

    def rotate_center(self, image, angle, x, y):

        # Rotate the image

        rotated_image = pygame.transform.rotate(image, angle)

        # Center the image to its designated x and y coordinate to couteract the wierd rotation in pygame

        new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

        return rotated_image, new_rect
    
    ## Pythagoras Theorem that returns the hypotenus

    def distance_between_points(self, x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)

    ## Gets the direction from one Vector2 to another Vector2 in degrees

    def direction_between_points(self, x1, y1, x2, y2):
        radians = math.atan2(y2-y1, x2-x1)
        return(math.degrees(radians))

    ## Gets the difference between angles

    def angle_difference(self, x, y):
        return math.atan2(math.sin(x-y), math.cos(x-y))

    ## Two functions that return the Vector2 from (0, 0) if you were to go at an angle at a speed for example 
    ## length=2 and angle=45 would go to (1.4, 1.4)
    ## This is useful for example cars in topdown that usually move in a 360 direction

    def lengthdir_x(self, length, angle):
        radian_angle = angle * math.pi / 180
        return length * math.cos(radian_angle)

    def lengthdir_y(self, length, angle):
        radian_angle = angle * math.pi / 180
        return length * math.sin(radian_angle)

    ## Returns if a Vector2 is in a rectangle

    def in_rect(self, x, y, rectx, recty, width, height):
        if x > rectx and x < rectx + width:
            if y > recty and y < recty + height:
                return True
        return False