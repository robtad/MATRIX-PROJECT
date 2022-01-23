import linecache
import re

list = []

#read and process matrix from file
def matrix(file_name):
    file_name = file_name + '.txt'
    with open(file_name, 'r') as f:
        num_lines = sum(1 for line in f)
        j = num_lines/4
        flag = 0
        # to skip the dotted line in the file
        # dotted line occurs in lines(4,8,12,16,20,24...)
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
                content = re.sub(r"[\n\t\s^[\]]*", "", content)

                list.append(content)

            flag = 0
    just_numbers()

# convert individual items in the list to pure numbers of power before writing
# them to different file
new_list = []
newer_list = []

def just_numbers():
    for item in list:
        new_item = ''
        for i in range(len(item)-1):
            if item[i] == 'x' and item[i+1] == '1':
                new_item += '1 '
            elif item[i] == '1':
                new_item += '0 '
            elif (item[i] == 'x') and ((item[i+1] != 1) and (item[i+1] != 'x')):
                new_item += item[i+1] + ' '
                #item = item.replace(item[i+1], '')
            if item[i] == 'x' and item[i+1] == 'x':
                new_item += '1 '

        if item[len(item)-1] == '1':
            new_item += '0 '
        elif item[len(item)-1] == 'x':
            new_item += '1 '
        new_list.append(new_item + ' ')

    #putting all exponents of elements of all rows of a matrix in a single string
    
    newer_item = ''
    num_row = 3
    i = 0
    for item in new_list:
        newer_item += item 
        i += 1
        if i % num_row == 0:
            newer_list.append(newer_item)
            newer_item = ''

# writing the new list(string) of exponents of matrix elements to new file
#f_exp--->f-file,exp-exponents
def write_list(file_name):
    file_name = file_name + '_e_list.txt' 
    with open(file_name, 'w') as f_exp:
        for item in newer_list:
            f_exp.write(item)
            f_exp.write('\n')


sorted_list = []
new_sorted_list = []
def sort_list():
    for item in newer_list:
        item = str(item).replace(' ', '') 
        sorted_list.append(sorted(item))
    #print(sorted_list)

    #preparing sorted string of matrix exponents
    #by converting the sorted list to sorted string of exponents
    
    for item in sorted_list:
        n_item = ' '.join(item)
        new_sorted_list.append(n_item)
    #print(new_sorted_list)

# writing a sorted list(string) of exponents of matrix elements to new file
#f_s_exp--->f-file,s-sorted,exp-exponents
def write_ordered_list(file_name):
    file_name = file_name + '_e_list_sorted.txt'
    sort_list()
    with open(file_name, 'w') as f_s_exp:
        for item in new_sorted_list:
            f_s_exp.write(item)
            f_s_exp.write('\n')

#unsorted string of exponents of a matrix ==> newer_list
#sorted string of exponents of a matrix ==> new_sorted_list

#fetching representative matrices.
rep_matrix = []
def write_rep_matrix(file_name):
    new_sorted_list.sort()
    matrix = ''
    for item in new_sorted_list:
        if item == matrix:
            continue
        if item != matrix:
            matrix = item
            rep_matrix.append(matrix)
    #print(rep_matrix)

    #writing representative matrix to a file(f_r_matrix --->f-file,r-representative)
    file_name = file_name + '_rep_matrix.txt'
    with open(file_name, 'w') as f_r_matrix:
        for item in rep_matrix:
            f_r_matrix.write(item)
            f_r_matrix.write('\n')