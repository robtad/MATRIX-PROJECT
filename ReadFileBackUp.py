import linecache
import re

with open('31GF3_0xb_3x3_matris.txt', 'r') as f:
    list = []
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
            content = (linecache.getline('31GF3_0xb_3x3_matris.txt', i))
            # used 're' from regEx(regular expression) library to remove unwanted chars
            content = re.sub(r"[\n\t\s^[\]]*", "", content)

            list.append(content)

        flag = 0
print(list)
# convert individual items in the list to pure numbers of power before writing
# them to different file
new_list = []
for item in list:
    new_item = ''
    for i in range(len(item)-1):
        if item[i] == 'x' and item[i+1] == '1':
            new_item += '1'
        elif item[i] == '1':
            new_item += '0'
        elif (item[i] == 'x') and ((item[i+1] != 1) and (item[i+1] != 'x')):
            new_item += item[i+1]
            #item = item.replace(item[i+1], '')
        if item[i] == 'x' and item[i+1] == 'x':
            new_item += '1'

    if item[len(item)-1] == '1':
        new_item += '0'
    elif item[len(item)-1] == 'x':
        new_item += '1'
    new_list.append(new_item)


print(new_list)
# writing the new list of power of matrix elements to new file
with open('31GF3_0xb_3x3_matris_plist.txt', 'w') as af:
    num_row = 3
    i = 0
    for item in new_list:
        af.write(item)
        i += 1
        if i % num_row == 0:
            af.write('\n')
