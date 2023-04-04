import pygame
from pygame.locals import *

class Point(pygame.sprite.Sprite):
    def __init__(self,x_loc, y_loc, radius):
        super().__init__()
        self.image = pygame.Surface((radius*2,radius*2),flags=pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = (x_loc, y_loc))
        self.image.fill((255,255,255,0.0))
        pygame.draw.circle(self.image, (0,0,0), center=(radius, radius), radius = radius)

def pygame_anim():
    pygame.init()

    frames_per_sec = 60
    window = (480,480)

    frame_rate = pygame.time.Clock()
    screen = pygame.display.set_mode(window, pygame.SCALED)
    pygame.display.set_caption("Sierpinski Triangle")

    radius = 5
    p1 = Point(100,100, radius)
    p2 = Point(200,200,radius)
    p3 = Point(105,102, radius)

    all_points = pygame.sprite.Group()
    all_points.add(p1)
    all_points.add(p2)
    all_points.add(p3)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            
        screen.fill((255,255,255))

        all_points.draw(screen)

        pygame.display.flip()
        frame_rate.tick(frames_per_sec)


if __name__ == "__main__":
    pygame_anim()
