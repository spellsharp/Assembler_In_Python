import os
os.chdir('/home/shrisharanyan/Desktop/nand2tetris/Assembler_In_Python/q3')

symbol_table = {'R0':'0','R1':'1','R2':'2','R3':'3','R4':'4','R5':'5',
'R6':'6','R7':'7','R8':'8','R9':'9','R10':'10','R11':'11',
'R12':'12','R13':'13','R14':'14','R15':'15','SP':'0',
'LCL':'1','ARG':'2','THIS':'3','THAT':'4','SCREEN':'16384',
'KBD':'24576'}

symbol_list = []
label_list = []

for i in symbol_table.keys():
    symbol_list.append(i)

file_now = open('/home/shrisharanyan/Desktop/nand2tetris/Assembler_In_Python/q1/q1.asm','r')

lines_list = file_now.readlines()
# l = len(lines_list)
count = -1
variable_value = count + 16
for i in lines_list:
    count += 1
    
    #labels
    if i[0]=='(':
        label = i[1:-2]
        if label not in symbol_table and label not in symbol_list:
            label_list.append(label)
            symbol_table[label] = count
            count -= 1

    #variables
    if i[0]=='@' and not i[1].isnumeric():
        variable = i[1:-1]
        if (variable not in symbol_table) and (variable not in symbol_list) and (variable not in label_list):
            symbol_table[variable] = variable_value
            variable_value += 1

    #if a label is mistaken for a variable, remove it and delete it from dictionary and wait for it to be defined as a loop.
    if i[0]=='(' and i[1:-2] not in label_list:
        del symbol_table[i[1:-2]] 
        label_list.append(i[1:-2])
        symbol_table[i[1:-2]] = count

    #built-in
    if i[0]=='@' and (i[1:-1] in symbol_table) and (i[1:-1] in symbol_list) and (variable not in label_list):
        builtin = i[1:-1]
        continue

key_list = list(symbol_table.keys())
longest = key_list[0]
for i in key_list:
    if len(i) > len(longest):
        longest = i

# print()
# print(longest)
# print()
# print(symbol_table)

