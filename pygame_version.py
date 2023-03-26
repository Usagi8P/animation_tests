import pygame
from pygame.locals import *

class Point(pygame.sprite.Sprite):
    def __init__(self,x_loc, y_loc,surface):
        super().__init__()
        self.surface = pygame.Surface((50,50))
        self.shape = pygame.draw.circle(surface, (0,0,0), center=(x_loc, y_loc), radius = 1)
        # self.rect = self.surface.get_rect(center=(x_loc, y_loc))

def pygame_anim():
    pygame.init()

    frames_per_sec = 60

    frame_rate = pygame.time.Clock()
    screen = pygame.display.set_mode((480, 480), pygame.SCALED)
    pygame.display.set_caption("Sierpinski Triangle")

    p1 = Point(100,100, screen)
    p2 = Point(50,50,screen)
    p3 = Point(100,50, screen)

    all_points = pygame.sprite.Group()
    all_points.add(p1)
    all_points.add(p2)
    all_points.add(p3)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            
        screen.fill((255,255,255))

        for point in all_points:
            screen.blit(point.surface, point.shape)

        pygame.display.update()
        frame_rate.tick(frames_per_sec)


if __name__ == "__main__":
    pygame_anim()
