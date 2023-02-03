import os
os.chdir('/home/shrisharanyan/Desktop/nand2tetris/Assembler_In_Python/q1')
old_file = open('/home/shrisharanyan/Desktop/nand2tetris/Assembler_In_Python/Rect.asm','r')

line_list = old_file.readlines()
print(line_list)

new_file = open('q1.asm','w')
new_list = []
for i in line_list:
    x = i.strip()
    if not x.startswith('//') and x!='':
        new_list.append(x)
        new_file.write(x + '\n')
    
print()
print(new_list)
