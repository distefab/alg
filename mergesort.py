# Author: Bryan DiStefano
# Date: 10/4/2020
# Description: Takes in a text input as an array and uses mergesort to sort them.


def merge_lists(left_list, right_list):
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
    if len(input_list) <= 1:
        return input_list
    else:
        mid = int(len(input_list) / 2)
        left_list = merge_sort(input_list[:mid])
        right_list = merge_sort(input_list[mid:])
        return merge_lists(left_list, right_list)


def merge_data(input_lists):
    output_list = []
    for each in input_lists:
        output_list.append(merge_sort(each))
    return output_list


def get_list_from_file(filename):
    file = open(filename, "r")
    final_file_list = []

    for line in file:
        file_list = line.strip().split(" ")
        del file_list[0]
        sec_list = []
        for value in file_list:
            sec_list.append(int(value))
        final_file_list.append(sec_list)
    file.close()
    return final_file_list


def write_merged_list_to_file(filename, merged_list):
    file = open(filename, "w")
    for array in merged_list:
        for line in array:
            file.write((str(line)))
            file.write(" ")
        file.write("\n")
    file.close()


def main():
    file_to_sort = get_list_from_file("data.txt")
    sorted_list = merge_data(file_to_sort)
    write_merged_list_to_file("merge.out", sorted_list)


if __name__ == "__main__":
    main()

