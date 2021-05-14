import pygame, math

class math_utils:
    def rotate_center(self, image, angle, x, y):
        rotated_image = pygame.transform.rotate(image, angle)
        new_rect = rotated_image.get_rect(center = image.get_rect(center = (x, y)).center)

        return rotated_image, new_rect
    
    def distance_between_points(self, x1, y1, x2, y2):
        return math.hypot(x2 - x1, y2 - y1)

    def direction_between_points(self, x1, y1, x2, y2):
        radians = math.atan2(y2-y1, x2-x1)
        return(math.degrees(radians))

    def lengthdir_x(self, length, angle):
        radian_angle = angle * math.pi / 180
        return length * math.cos(radian_angle)

    def lengthdir_y(self, length, angle):
        radian_angle = angle * math.pi / 180
        return length * math.sin(radian_angle)

    def in_rect(self, x, y, rectx, recty, width, height):
        if x > rectx and x < rectx + width:
            if y > recty and y < recty + height:
                return True
        return False