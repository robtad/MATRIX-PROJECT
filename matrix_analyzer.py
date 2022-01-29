from dataclasses import replace
import linecache
import os
import re
from typing import OrderedDict


# read and process matrix from file

list = []


def matrix(file_name):
    with open(file_name, 'r') as f:
        num_lines = sum(1 for line in f)
        j = num_lines/4
        flag = 0
        # to skip the dotted line in the file
        # dotted line occurs in lines(4,8,12,16,20,24...)(arithmetic sequence)
        for i in range(1, num_lines+1):
            for k in range(int(j+1)):
                if i == (4*k):
                    flag = 1
                    index = i
                    break
            if(flag == 0):
                # used linecache to read specific line in the file( here it reads i^th line)
                content = (linecache.getline(file_name, i))
                # used 're' from regEx(regular expression) library to remove unwanted chars
                content = re.sub(r"[\n^[\]]*", "", content)
                # replaces multiple spaces with one space
                content = re.sub(' +', ' ', content)
                content += ' '
                content = content.replace(' ', '.')
                list.append(content)

            flag = 0
    just_numbers()


new_list = []
newer_list = []

# convert individual items in the list to pure numbers of power before writing
# them to different file


def just_numbers():
    for item in list:
        item = item.replace('1.', '0.')
        item = item.replace('x.', '1.')
        item = item.replace('x', '')
        item = item.lstrip('.')
        item = item.replace('.', ' ')
        new_list.append(item)
    # putting all exponents of elements of all rows of a matrix in a single string

    newer_item = ''
    num_row = 3
    i = 0
    for item in new_list:
        newer_item += item + '      '
        i += 1
        if i % num_row == 0:
            newer_item = newer_item.rstrip()
            newer_list.append(newer_item)
            newer_item = ''

# writing the new list(string) of exponents of matrix elements to new file
# f_exp--->f-file,exp-exponents


def write_list(file_name):
    file_name = 'e_list_' + file_name
    with open(file_name, 'w') as f_exp:
        for item in newer_list:
            f_exp.write(item)
            f_exp.write('\n')


sorted_list = []
new_sorted_list = []


def sort_list():
    for item in newer_list:
        item = re.sub(' +', ' ', item)
        item = item.split(' ')
        item = [int(i) for i in item]
        item.sort()
        sorted_list.append(item)
    # print(sorted_list)

    # preparing sorted string of matrix exponents
    # by converting the sorted list to sorted string of exponents

    for item in sorted_list:
        string_item = ' '.join(str(i) for i in item)
        new_sorted_list.append(string_item)


# writing a sorted list(string) of exponents of matrix elements to new file
# f_s_exp--->f-file,s-sorted,exp-exponents


def write_ordered_list(file_name):
    file_name = 'e_list_sorted_' + file_name
    sort_list()
    with open(file_name, 'w') as f_s_exp:
        for item in new_sorted_list:
            f_s_exp.write(item)
            f_s_exp.write('\n')

# unsorted string of exponents of a matrix ==> newer_list
# sorted string of exponents of a matrix ==> new_sorted_list


# fetching representative matrices.
rep_matrix = []  # new_sorted_list without duplicates


def write_rep_matrix(file_name):
    new_sorted_list.sort()
    # print(new_sorted_list)
    for item in new_sorted_list:
        if item not in rep_matrix:
            rep_matrix.append(item)

    # print(rep_matrix)

    # writing representative matrix to a file(f_r_matrix --->f-file,r-representative)
    file_name = 'rep_matrix_' + file_name
    with open(file_name, 'w') as f_r_matrix:
        for item in rep_matrix:
            f_r_matrix.write(item)
            f_r_matrix.write('\n')


# writing unique representative matrix(No zeros and no repeating elements)


def get_folder_name():
    path = os.getcwd()
    path = path.replace('\\', '/')
    folder_name = os.path.basename(path)
    return folder_name


new_rep_matrix = []

unique_rep_matrix = []
unique_rep_matrix2 = []  # unique_rep_matrix with no duplicates


def write_unique_rep_matrix(file_name):
    # convert list of strings to list of lists

    for item in rep_matrix:
        item_as_list = (item.split(' '))
        new_rep_matrix.append(item_as_list)

    for item in new_rep_matrix:
        new_item = set(item)  # to remove duplicates
        new_item = sorted(new_item, key=int)  # sorting by int value
        new_item = '  '.join(new_item)
        new_item = new_item.replace('0 ', '')
        new_item = new_item.lstrip(' ')
        new_item = re.sub(' +', ' ', new_item)
        unique_rep_matrix.append(new_item)
        new_item = ''
    # print(unique_rep_matrix)
# remove duplicates from unique_rep_matrix

    for item in unique_rep_matrix:
        if item not in unique_rep_matrix2:
            unique_rep_matrix2.append(item)
    # print(unique_rep_matrix2)

    # writing unique representative matrix to a file.
    # representative matrices of all matrices under one polinomial are in just one file
    name_of_file = 'unique_rep_matrix_' + get_folder_name() + '.txt'
    with open(name_of_file, 'a') as f_u_r_matrix:
        new_file_name = file_name.replace('matris.txt', 'unique_rep_matris')
        f_u_r_matrix.write('---------------------------------------------')
        f_u_r_matrix.write('\n')
        f_u_r_matrix.write(new_file_name)
        f_u_r_matrix.write('\n')
        f_u_r_matrix.write('---------------------------------------------')
        f_u_r_matrix.write('\n')
        for item in unique_rep_matrix2:
            f_u_r_matrix.write(item)
            f_u_r_matrix.write('\n')
