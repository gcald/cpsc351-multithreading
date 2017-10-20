import multiprocessing  # python's version of openMP
import math
from random import uniform

num_of_procs = 1  # can be used for testing number of processes
num_of_points = int(1000000/num_of_procs)  # the original amount of points in 4.22 divided by number of processes
points_in_circle = 0

x_points = []
y_points = []


def distance(x, y):
    return math.sqrt((x - 0)**2 + (y - 0)**2)


def random_point():
    global points_in_circle
    global num_of_procs
    # print(multiprocessing.current_process().name) # prints the name of the process
    for i in range(num_of_points):
        dist = 0
        x_points.append(uniform(-1, 1))  # generates random float numbers
        y_points.append(uniform(-1, 1))
        dist = distance(x_points[i], y_points[i])
        if dist < 1:
            points_in_circle += 1


def calculate_pi():
    global num_of_points
    global points_in_circle
    print("pi =", (4*points_in_circle)/(num_of_points*num_of_procs))


if __name__ == "__main__":
    jobs = []
    for j in range(0, num_of_procs):  # used to create multiple processes
        process = multiprocessing.Process(target=random_point())
        jobs.append(process)
    for k in jobs:
        k.start()
    for k in jobs:
        k.join()
    calculate_pi()

