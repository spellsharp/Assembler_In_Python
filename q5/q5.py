comp_table = {
    0:{'0':'101010','1':'111111','-1':'111010','D':'001100','A':'110000','!D':'001101','!A':'110001','-D':'001111','-A':'110011','D+1':'011111','A+1':'110111','D-1':'001110','A-1':'110010','D+A':'000010','D-A':'010011','A-D':'000111','D&A':'000000','D|A':'010101'},
    1:{'M':'110000','!M':'110001','-M':'110011','M+1':'110111','M-1':'110010','D+M':'000010','D-M':'010011','M-D':'000111','D&M':'000000','D|M':'010101'}
    }

dest_table = {
    None:'000','M':'001','D':'010','MD':'011','A':'100','AM':'101','AD':'110','AMD':111
    }

jump_table = {
    None:'000','JGT':'000','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'
}

c_instruction = []

def isA_Instruction(string):
    if string.startswith('@') or string.startswith('('):
        if not string[1].isnumeric():
            return True
    return False

def isC_Instructions(string):
    if not isA_Instruction(string) and not string[1].isnumeric():
        return True
    return False

def cleanLines(line):
    line = line.replace('\n','').strip('@').strip('(').strip(')')
    return line



def C_instruction(instruct):
    if '=' in instruct and not ';' in instruct:
        # print("Pure dest comp")
        destIndex = instruct.index('=')
        dest = instruct[0:destIndex]
        jump = None
        if dest in dest_table:
            binaryDest = dest_table[dest]

        destIndex = instruct.index('=')
        compIndex = destIndex + 1
        comp = instruct[compIndex:]
        # print(dest,end='')
        # print(comp,end='')
        # print(jump)
    if ';' in instruct and not '=' in instruct:
        # print("Pure jump comp")
        jumpIndex = instruct.index(';')
        jump = instruct[jumpIndex+1:]
        dest = None
        if jump in jump_table:
            binaryJump = jump_table[jump]
            jumpIndex = instruct.index(';')
            compIndex = jumpIndex
            comp = instruct[:compIndex]
        # print(dest,end='')
        # print(comp,end='')
        # print(jump)

    if ';' in instruct and '=' in instruct:
        # print("Both jump and comp")

        jumpIndex = instruct.index(';')
        jump = instruct[jumpIndex+1:]
        binaryJump = jump_table[jump]

        destIndex = instruct.index('=')
        dest = instruct[:destIndex]
        binaryDest = dest_table[dest]

        comp = instruct[destIndex+1:jumpIndex]
        # print(dest,end='')
        # print(comp,end='')
        # print(jump)

    if comp in comp_table[0]:
        binaryComp = comp_table[0][comp]
        a = '0'

    elif comp in comp_table[1]:
        binaryComp = comp_table[1][comp]
        a = '1'
        
    binaryJump = jump_table[jump]
    binaryDest = dest_table[dest]

    binaryC_instruction = '111' + a + binaryComp + binaryDest + binaryJump
    print(binaryC_instruction)

with open('q1.asm','r') as instructions:
    instruct = instructions.readlines()

    for line in instruct:
        if isC_Instructions(line):
            line = cleanLines(line)
            c_instruction.append(line)
        else:
            continue

    # print(c_instruction)

for instruct in c_instruction:
    C_instruction(instruct)