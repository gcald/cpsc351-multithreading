import threading
import math
from random import uniform

num_of_points = 1000000
points_in_circle = 0

x_points = []
y_points = []


def distance(x, y):
    return math.sqrt((x - 0)**2 + (y - 0)**2)


def random_point():
    global points_in_circle
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
    print("pi =", (4*points_in_circle)/num_of_points)


t = threading.Thread(target=random_point())
t.start()
calculate_pi()
