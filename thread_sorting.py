# Ch.4 Multithreaded Sorting Sorting by George Calderon
import threading
import logging
import sys
from copy import deepcopy

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG) #  use to view debug statements
num_list = [12, 5, 55, 19, 8, 4, 7, 3, 17, 10]
final_list = []
list_num = 1

print("Starting List: %s" % num_list)


def sort_list(start_index, end_index):
    global list_num
    logging.debug("\n%s starting..." % threading.currentThread().getName())  # used to see working threads in debug mode
    sorted_list = num_list[start_index:end_index]  # creates a new list based on parameters
    sorted_list.sort()
    sorted_index = 0  # used to keep track of list numbers for later print statements
    for i in range(start_index, end_index):  # will put sorted values back into the original list
        num_list[i] = sorted_list[sorted_index]
        sorted_index += 1
    print("Sorted List #%d: %s" % (list_num, sorted_list))
    list_num += 1
    logging.debug("%s exiting..." % threading.currentThread().getName())


def merge_list():
    global final_list
    final_list = deepcopy(num_list)  # deepcopies the list to sort from
    print("\nUnsorted Merged List: %s" % final_list)
    final_list.sort()
    print("Sorted Merged List: %s" % final_list)

threads = []
for j in range(2):
    t = threading.Thread(target=sort_list, args=(5*j, 5 + 5*j))  # used for loop to separate in multiples of 5
    threads.append(t)
    t.start()
merge_list()
