import os
os.chdir('/home/shrisharanyan/Desktop/nand2tetris/Assembler_In_Python/q2')
file_open = open('/home/shrisharanyan/Desktop/nand2tetris/Assembler_In_Python/q1/q1.asm','r')

list_file = file_open.readlines()

new_file = open('q2.asm','w')

for i in list_file:
    if i.startswith('('):
        new_file.write(i)
    if i.startswith('@'):
        if i[1].isnumeric():
            continue
        else:
            new_file.write(i)

