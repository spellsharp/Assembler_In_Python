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

binA_instructions = {}
a_instructions = []
c_instructions = []

with open('/home/shrisharanyan/Desktop/nand2tetris/Assembler_In_Python/symbolDict.txt', 'r') as symbolTable_file:
    symbol_table = eval(symbolTable_file.read())


with open('/home/shrisharanyan/Desktop/nand2tetris/Assembler_In_Python/q1/q1.asm', 'r') as file_now:
    lines = file_now.readlines()

    
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



def A_instruction(line):
    
    if isA_Instruction(line) and not line.startswith('('):
        line = cleanLines(line)
        # print(line)
        if line in symbol_table.keys():
            binline = binA_instructions[line]
        else:
            binline = format(int(line),'016b')
        print(binline)

    elif isC_Instructions(line):
        c_instructions.append(line.replace('\n',''))
        #in final program tell it to print c instructions.
# print(c_instructions)

with open('q1/q1.asm','r') as instructions:
    instruct = instructions.readlines()
    for line in instruct:
        A_instruction(line)

    