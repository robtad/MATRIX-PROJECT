# To read all txt files in a folder
from fileinput import filelineno
import os
path = r"D:\MY PROJECTS\MATRIX PROJECT\Updated Codes"
print(path)
os.chdir(path)
file_list = []
# iterate through all file


def get_txt_files():
    file_list.clear()
    for file_name in os.listdir():
        if file_name.endswith('.txt'):
            file_list.append(file_name)

# deletes file with specific string in their file name


def remove_specific_file(list_of_files):
    for file in list_of_files:
        if ('list' in file) or ('rep' in file):
            os.remove(file)
# lists existing files in the directory


def list_existing_files(list):
    for file in list:
        print(file)


get_txt_files()
print('\nlisting files in the directory...\n')
list_existing_files(file_list)
remove_specific_file(file_list)
print('\n\nfile removal successful!')
print('\nlisting remaining file...\n')
get_txt_files()
list_existing_files(file_list)

# print(all_files)
# for file in all_files:
#   with open(file,'r') as f:
#     print(f.read())
