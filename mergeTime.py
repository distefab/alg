# Author: Bryan DiStefano
# Date: 10/4/2020
# Description: Creates 8 arrays full of random numbers and times how long it takes to mergesort them.

import random
import time


def rand(start, end, num):
    # simple function to create the random number array
    random_array = []
    for each in range(num):
        random_array.append(random.randint(start, end))
    return random_array


def merge_lists(left_list, right_list):
    # merges 2 sides of a list and sorts them in descending order
    x = 0
    i = 0
    merged = []
    while i < len(left_list) and x < len(right_list):
        if left_list[i] >= right_list[x]:
            merged.append(left_list[i])
            i += 1
        else:
            merged.append(right_list[x])
            x += 1
    merged += left_list[i:]
    merged += right_list[x:]
    return merged


def merge_sort(input_list):
    # returns the list if it is length 1, otherwise finds the midpoint and calls merge_sort on both sides
    if len(input_list) <= 1:
        return input_list
    else:
        mid = int(len(input_list) / 2)
        left_list = merge_sort(input_list[:mid])
        right_list = merge_sort(input_list[mid:])
        return merge_lists(left_list, right_list)


def merge_timer(random_list):
    # multiplies the merge sort of the random number array by the system clock
    start_time = time.perf_counter()
    merge_sort(random_list)
    end_time = time.perf_counter()
    # prints the length of the array and the time elapsed to console.
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
    merge_timer(test1)
    merge_timer(test2)
    merge_timer(test3)
    merge_timer(test4)
    merge_timer(test5)
    merge_timer(test6)
    merge_timer(test7)
    merge_timer(test8)
    print("All Testing Complete!")


if __name__ == "__main__":
    main()