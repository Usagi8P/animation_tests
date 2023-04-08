import pygame
from pygame.locals import *
from sierpinsky import select_random_point, select_half_way

class Point(pygame.sprite.Sprite):
    def __init__(self,x_loc: int, y_loc: int, radius: int):
        super().__init__()
        self.x_loc = x_loc
        self.y_loc = y_loc
        self.image = pygame.Surface((radius*2,radius*2),flags=pygame.SRCALPHA)
        self.rect = self.image.get_rect(center = (self.x_loc, self.y_loc))
        self.image.fill((255,255,255,0.0))
        pygame.draw.circle(self.image, (0,0,0), center=(radius, radius), radius = radius)

def pygame_anim():
    pygame.init()

    frames_per_sec = 60
    window = (480,480)

    frame_rate = pygame.time.Clock()
    screen = pygame.display.set_mode(window, pygame.SCALED)
    pygame.display.set_caption("Sierpinski Triangle")

    radius = 1
    offset = 40
    iterations = 100000
    iteration_count = 0

    p1 = Point(0+offset,0+offset, radius)
    p2 = Point(200+offset,300+offset,radius)
    p3 = Point(400+offset,0+offset, radius)

    all_points = pygame.sprite.Group()
    all_points.add(p1)
    all_points.add(p2)
    all_points.add(p3)

    starting_points = pygame.sprite.Group()
    starting_points.add(p1)
    starting_points.add(p2)
    starting_points.add(p3)

    points_x: list[int] = []
    points_y: list[int] = []
    for point in all_points:
        points_x.append(point.x_loc)
        points_y.append(point.y_loc)

    starting_points_x: list[int] = []
    starting_points_y: list[int] = []
    for starting_point in starting_points:
        starting_points_x.append(starting_point.x_loc)
        starting_points_y.append(starting_point.y_loc)

    new_x, new_y = select_random_point(points_x,points_y)
    p4 = Point(new_x,new_y,radius)
    most_recent_p = p4
    all_points.add(p4)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()

        if iteration_count < iterations:
            new_x, new_y = select_half_way(most_recent_p.x_loc, most_recent_p.y_loc, starting_points_x, starting_points_y)
            all_points.add(Point(new_x, new_y, radius))
            most_recent_p = Point(new_x, new_y, radius)
            iteration_count += 1

        screen.fill((255,255,255))

        all_points.draw(screen)

        pygame.display.flip()
        frame_rate.tick(frames_per_sec)


if __name__ == "__main__":
    pygame_anim()
