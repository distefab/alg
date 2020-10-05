# Author: Bryan DiStefano
# Date: 10/4/2020
# Description: Takes in a text input (data.txt) as a list of lists and uses insertion_sort to sort them,
# then outputs them as insert.out.


def insertion_sort(insert_lists):
    # sorts a list by insertion sort
    for x in range(1, len(insert_lists)):
        current = insert_lists[x]
        while x > 0 and insert_lists[x - 1] < current:
            insert_lists[x] = insert_lists[x - 1]
            x = x - 1
        insert_lists[x] = current
    return insert_lists


def insert_sort_data(input_lists):
    # used to go through the list of lists output by the text file
    output_list = []
    for each in input_lists:
        output_list.append(insertion_sort(each))
    return output_list


def get_list_from_file(filename):
    # reads and separates a text file of numbers, converting them back into ints, getting rid
    # of the number showing the size of the list and putting them in a list
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


def write_insert_list_to_file(filename, insert_list):
    # writes the sorted merged_list to a test file, each list taking up a line
    file = open(filename, "w")
    for array in insert_list:
        for line in array:
            file.write((str(line)))
            file.write(" ")
        file.write("\n")
    file.close()


def main():
    file_to_sort = get_list_from_file("data.txt")
    sorted_list = insert_sort_data(file_to_sort)
    write_insert_list_to_file("insert.out", sorted_list)


if __name__ == "__main__":
    main()