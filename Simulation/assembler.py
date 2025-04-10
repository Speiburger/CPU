# Very simple and rough "assembler" to make writing test programs for the cpu less tedious

# Since the opcodes for each instruction are just counting up the list of instructions, the list index can be used to easily resolve instructions
# However, instructions with multiple kinds of arguments have to be handeled seperately and are included multiple times to not desync the list indices
INSTRUCTION_LIST = ["LDA", "LDA", "LDB", "LDB", "STA", "STB", "SWP", "ATC", "ATD", "JMP", "JMZ", "JMC", "JMN", "JSR", "RTS", "ADD", "SUB", "SHL", "NOT", "AND", "XOR", "OR", "PSH", "POP"]

import sys
sourcePath = sys.argv[1]

def parseInstruction(line):
    splitLine = str.split(line) # First version of this will only split at whitespace
    if splitLine[0] == "#":
        return -1
    for index, instruction in enumerate(INSTRUCTION_LIST):
        if splitLine[0] == instruction:
            return index
    return -1

