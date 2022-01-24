from matrix_analyzer import *

# change these
# without the extension (.txt) and the number at the beginning
general_file_name = 'GF3_0xb_3x3_matris'
i = 31  # the list start from
no_in_list = 47  # number doesn't exist in list

file_list = []
for x in range(18):
    if i != no_in_list:
        file_name = str(i) + general_file_name
        file_list.append(file_name)
    i += 1

for item in file_list:
    matrix(item)
    write_list(item)
    write_ordered_list(item)
    write_rep_matrix(item)
    write_unique_rep_matrix(item)
    # reset lists
    list.clear()
    new_list.clear()
    newer_list.clear()
    sorted_list.clear()
    new_sorted_list.clear()
    rep_matrix.clear()
    unique_rep_matrix.clear()

    # print(list);print(new_list);print(newer_list);print(sorted_list);print(new_sorted_list);print(rep_matrix)
