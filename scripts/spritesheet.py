import pygame
class SpriteSheet():
    def __init__(self, image):
        self.sheet = image

    def get_image(self, frame, width, height, scale):
        # very much stolen from a tutorial, coding with russ is amazing for pygame
        self.image = pygame.Surface((width, height), pygame.SRCALPHA).convert_alpha()
        self.image.blit(self.sheet, (0, 0), (frame * width, 0, width, height))
        self.image = pygame.transform.scale(self.image, (width * scale, height * scale))
        return self.image