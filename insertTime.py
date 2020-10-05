# Author: Bryan DiStefano
# Date: 10/4/2020
# Description: Creates 8 arrays full of random numbers and times how long it takes to insertion_sort them.

import random
import time


def rand(start, end, num):
    random_array = []

    for each in range(num):
        random_array.append(random.randint(start, end))

    return random_array


def insertion_sort(insert_lists):
    # sorts a list by insertion sort
    for x in range(1, len(insert_lists)):
        current = insert_lists[x]
        while x > 0 and insert_lists[x - 1] < current:
            insert_lists[x] = insert_lists[x - 1]
            x = x - 1
        insert_lists[x] = current
    return insert_lists


def insert_timer(random_list):
    # multiplies the insertion sort of the random number array by the system clock
    start_time = time.perf_counter()
    insertion_sort(random_list)
    end_time = time.perf_counter()
    print(len(random_list), end_time - start_time)


def main():
    test1 = rand(0, 10000, 5000)
    test2 = rand(0, 10000, 5000)
    test3 = rand(0, 10000, 10000)
    test4 = rand(0, 10000, 10000)
    test5 = rand(0, 10000, 15000)
    test6 = rand(0, 10000, 15000)
    test7 = rand(0, 10000, 20000)
    test8 = rand(0, 10000, 20000)
    insert_timer(test1)
    insert_timer(test2)
    insert_timer(test3)
    insert_timer(test4)
    insert_timer(test5)
    insert_timer(test6)
    insert_timer(test7)
    insert_timer(test8)
    print("All Testing Complete!")


if __name__ == "__main__":
    main()
