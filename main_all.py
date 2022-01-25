from fileinput import filelineno
from matrix_analyzer import *
import os
# To read all txt files in a folder
# dont forget to update the belows path for the specific folder you're running this code in
path = r"D:\MY PROJECTS\MATRIX PROJECT\Updated Codes"
os.chdir(path)
# iterate through all file
file_list = []
def get_txt_files():
    file_list.clear()
    for file_name in os.listdir():
        if file_name.endswith('.txt'):
            file_list.append(file_name)
def remove_specific_file(list_of_files):
    for file in list_of_files:
        if ('list' in file) or ('rep' in file):
            os.remove(file)


get_txt_files()
remove_specific_file(file_list)
get_txt_files()


for file in file_list:
    matrix(file)
    write_list(file)
    write_ordered_list(file)
    write_rep_matrix(file)
    write_unique_rep_matrix(file)
    # reset lists
    list.clear()
    new_list.clear()
    newer_list.clear()
    sorted_list.clear()
    new_sorted_list.clear()
    rep_matrix.clear()
    unique_rep_matrix.clear()

    # print(list);print(new_list);print(newer_list);print(sorted_list);print(new_sorted_list);print(rep_matrix)
