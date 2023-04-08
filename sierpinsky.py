from random import choice, random


def select_random_point(points_x: list[int], points_y: list[int]):
    rand_x = random()
    rand_y = random()
    
    new_x =  rand_x * max(points_x)
    new_y = rand_y * max(points_y)

    return new_x, new_y

def select_half_way(current_x, current_y, starting_points_x, starting_points_y):
    chosen_vertex = choice([0,1,2])
    points_x = starting_points_x
    points_y = starting_points_y
    vertex_x = points_x[chosen_vertex]
    vertex_y = points_y[chosen_vertex]

    new_x = (vertex_x + current_x)/2
    new_y = (vertex_y + current_y)/2

    return new_x, new_y