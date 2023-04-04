import matplotlib.pyplot as plt
from matplotlib import animation
from random import choice, random

def plt_artist_anim():
    n_itertions = 500

    points_x = [0,2,4]
    points_y = [0,3,0]

    new_x, new_y = select_random_point(points_x, points_y)

    points_x.append(new_x)
    points_y.append(new_y)

    fig, axs = plt.subplots()
    ims = []

    for _ in range(n_itertions):
        new_x, new_y = select_half_way(points_x[-1], points_y[-1])
        points_x.append(new_x)
        points_y.append(new_y)
        frame = axs.plot(points_x,points_y,marker=",",ls='None',color='black')
        ims.append(frame)

    anim = animation.ArtistAnimation(fig, ims, interval = 10, repeat_delay=1000)

    plt.show()

def select_random_point(points_x, points_y):
    rand_x = random()
    rand_y = random()
    
    new_x =  rand_x * max(points_x)
    new_y = rand_y * max(points_y)

    return new_x, new_y

def select_half_way(current_x, current_y):
    chosen_vertex = choice([0,1,2])
    points_x = [0,2,4]
    points_y = [0,3,0]
    vertex_x = points_x[chosen_vertex]
    vertex_y = points_y[chosen_vertex]

    new_x = (vertex_x + current_x)/2
    new_y = (vertex_y + current_y)/2

    return new_x, new_y

if __name__ == "__main__":
    plt_artist_anim()