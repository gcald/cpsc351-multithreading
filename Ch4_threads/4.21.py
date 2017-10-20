import threading
import logging
import sys

# logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)  # use to view debug statements
values = [90, 81, 78, 95, 79, 72, 85]
values_average = 0
values_min = 0
values_max = 0


def get_input():
    global values
    print("Please input numbers to calculate average, min and max: ")
    values = (input())
    values = values.split()


def average():
    global values
    global values_average
    logging.debug("\n%s starting..." % threading.currentThread().getName())
    values_average = int(sum(values)/len(values))
    logging.debug("%s exiting..." % threading.currentThread().getName())


def minimum():
    global values
    global values_min
    logging.debug("\n%s starting..." % threading.currentThread().getName())
    values_min = min(values)
    logging.debug("%s exiting..." % threading.currentThread().getName())


def maximum():
    global values
    global values_max
    logging.debug("\n%s starting..." % threading.currentThread().getName())
    values_max = max(values)
    logging.debug("%s exiting..." % threading.currentThread().getName())


t = threading.Thread(target=average())
t1 = threading.Thread(target=minimum())
t2 = threading.Thread(target=maximum())

t.start()
t1.start()
t2.start()
print("The average value is %d\nThe minimum value is %d\nThe maximum values is %d" %
      (values_average, values_min, values_max))
