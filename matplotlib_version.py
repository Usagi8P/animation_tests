import matplotlib.pyplot as plt # type: ignore
from matplotlib import animation
from sierpinsky import select_random_point, select_half_way
import copy

def plt_artist_anim():
    n_itertions = 1000

    points_x = [0,2,4]
    points_y = [0,3,0]

    starting_points_x = copy.deepcopy(points_x)
    starting_points_y = copy.deepcopy(points_y)

    new_x, new_y = select_random_point(points_x, points_y)

    points_x.append(new_x)
    points_y.append(new_y)

    fig, axs = plt.subplots()
    ims = []

    for _ in range(n_itertions):
        new_x, new_y = select_half_way(points_x[-1], points_y[-1], starting_points_x, starting_points_y)
        points_x.append(new_x)
        points_y.append(new_y)
        frame = axs.plot(points_x,points_y,marker=".",ls='None',color='black')
        ims.append(frame)

    anim = animation.ArtistAnimation(fig, ims, interval = 10, repeat_delay=1000)

    plt.show()

if __name__ == "__main__":
    plt_artist_anim()