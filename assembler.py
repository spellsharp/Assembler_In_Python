symbol_table = {'R0':'0','R1':'1','R2':'2','R3':'3','R4':'4','R5':'5',
'R6':'6','R7':'7','R8':'8','R9':'9','R10':'10','R11':'11',
'R12':'12','R13':'13','R14':'14','R15':'15','SP':'0',
'LCL':'1','ARG':'2','THIS':'3','THAT':'4','SCREEN':'16384',
'KBD':'24576'}

comp_table = {
    0:{'0':'101010','1':'111111','-1':'111010','D':'001100','A':'110000','!D':'001101','!A':'110001','-D':'001111','-A':'110011','D+1':'011111','A+1':'110111','D-1':'001110','A-1':'110010','D+A':'000010','D-A':'010011','A-D':'000111','D&A':'000000','D|A':'010101'},
    1:{'M':'110000','!M':'110001','-M':'110011','M+1':'110111','M-1':'110010','D+M':'000010','D-M':'010011','M-D':'000111','D&M':'000000','D|M':'010101'}
    }

dest_table = {
    None:'000','M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':111
    }

jump_table = {
    None:'000','JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'
}

c_instruction = []



def isA_Instruction(string):
    if string.startswith('@') or string.startswith('('):
        return True
    return False

def isC_Instructions(string):
    if not isA_Instruction(string) and not string[1].isnumeric():
        return True
    return False

def cleanLines(line):
    line = line.replace('\n','').strip('@').strip('(').strip(')')
    return line

filename = input("Enter .asm file directory: \n")

old_file = open(filename, 'r')

line_list = old_file.readlines()

q1 = []

for i in line_list:
    x = i.strip()
    if not x.startswith('//') and x!='':
        q1.append(x)
    
print()

symbol_list = []
label_list = []

for i in symbol_table.keys():
    symbol_list.append(i)

lines_list = q1
print()

count = -1
variable_value = count + 16
for i in lines_list:
    count += 1
    
    #labels
    if i[0]=='(':
        label = i[1:-1]
        if label not in symbol_table and label not in symbol_list:
            label_list.append(label)
            symbol_table[label] = count
            count -= 1

    #variables
    if i[0]=='@' and not i[1].isnumeric():
        variable = i[1:]
        if (variable not in symbol_table) and (variable not in symbol_list) and (variable not in label_list):
            symbol_table[variable] = variable_value
            variable_value += 1

    #if a label is mistaken for a variable, remove it and delete it from dictionary and wait for it to be defined as a loop.
    if i[0]=='(' and i[1:-1] not in label_list:
        del symbol_table[i[1:-1]] 
        label_list.append(i[1:-1])
        symbol_table[i[1:-1]] = count

    #built-in
    if i[0]=='@' and (i[1:] in symbol_table) and (i[1:] in symbol_list) and (variable not in label_list):
        builtin = i[1:]
        continue

binA_instructions = {}
a_instructions = []
c_instructions = []

lines = q1


for line in lines:
    if isA_Instruction(line):
        line = cleanLines(line)
        a_instructions.append(line)

    else:
        continue

for a in a_instructions:

    if a in symbol_table.keys():
        binA = format(int(symbol_table[a]),'016b')
        binA_instructions[a] = binA

def C_instruction(instruct):
    instruct = cleanLines(instruct)
    comp = ''
    if '=' in instruct and not ';' in instruct:

        destIndex = instruct.index('=')
        dest = instruct[0:destIndex]
        jump = None
        if dest in dest_table:
            binaryDest = dest_table[dest]

        destIndex = instruct.index('=')
        compIndex = destIndex + 1
        comp = instruct[compIndex:]

    if ';' in instruct and not '=' in instruct:

        jumpIndex = instruct.index(';')
        jump = instruct[jumpIndex+1:]
        dest = None
        if jump in jump_table:
            binaryJump = jump_table[jump]
            jumpIndex = instruct.index(';')
            compIndex = jumpIndex
            comp = instruct[:compIndex]


    if ';' in instruct and '=' in instruct:


        jumpIndex = instruct.index(';')
        jump = instruct[jumpIndex+1:]
        binaryJump = jump_table[jump]

        destIndex = instruct.index('=')
        dest = instruct[:destIndex]
        binaryDest = dest_table[dest]

        comp = instruct[destIndex+1:jumpIndex]

    a_val = ''
    binaryComp = ''
    if comp in comp_table[0]:
        binaryComp = comp_table[0][comp]
        a_val = '0'

    elif comp in comp_table[1]:
        binaryComp = comp_table[1][comp]
        a_val = '1'
        
    binaryJump = jump_table[jump]
    binaryDest = dest_table[dest]

    binaryC_instruction = '111' + a_val + binaryComp + binaryDest + binaryJump
    return binaryC_instruction

def A_instruction(line):
    if not line.startswith('('):
        line = cleanLines(line)

        if line in symbol_table.keys():
            binline = binA_instructions[line]
        else:
            binline = format(int(line),'016b')

        return binline

output_file = open('Output.hack','w')
output = []
instruct = q1
for line in instruct:
    if isA_Instruction(line):
        if A_instruction(line) != None:
            output_file.write(str(A_instruction(line)))
            output_file.write('\n')
    elif isC_Instructions(line):
        output_file.write(str(C_instruction(line)))
        output_file.write('\n')
print("Successful!")
output_file.close()